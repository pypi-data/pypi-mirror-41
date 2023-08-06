# coding=utf-8
from __future__ import print_function

import argparse
import os
import re

import cv2
import numpy as np

from suanpan import path, utils
from suanpan.arguments import *  # pylint: disable-msg=w0614
from suanpan.components import Result
from suanpan.datawarehouse import dw
from suanpan.io import storage


class Table(Arg):
    def __init__(self, key, table, partition):
        super(HiveTable, self).__init__(key)
        self.table = String(key=table, required=True)
        self.partition = String(key=partition)

    @property
    def isSet(self):
        return True

    def addParserArguments(self, parser):
        self.table.addParserArguments(parser)
        self.partition.addParserArguments(parser)

    def load(self, args):
        self.table.load(args)
        self.partition.load(args)
        self.value = dict(table=self.table.value, partition=self.partition.value)

    def format(self, context):
        self.value = dw.readTable(self.table.value, self.partition.value)
        return self.value

    def save(self, context, result):
        data = result.value
        dw.writeTable(self.table.value, data)
        return self.value


HiveTable = Table


class SeriesRules(ListOfString):
    OPERATORS = {
        ">": np.greater,
        ">=": np.greater_equal,
        "<": np.less,
        "<=": np.less_equal,
    }

    @classmethod
    def transform(cls, item):
        key, operate, value = re.match(r"^(\w+)\s*([<>]=?)\s*(\d+)$", item).groups()
        return {"key": key, "operate": cls.getOperator(operate), "value": float(value)}

    @classmethod
    def getOperator(cls, name):
        return cls.OPERATORS[name]


class LogicalOperator(String):
    LOGICAL_OPERATORS = {
        "and": np.logical_and,
        "or": np.logical_or,
        "xor": np.logical_xor,
        "not": np.logical_not,
    }

    def format(self, context):
        try:
            self.value = self.getLogicalOperator(self.value)
            return self.value
        except:
            argparse.ArgumentTypeError(
                "Unknown logical operator: {}, should in {}".format(
                    self.value, self.LOGICAL_OPERATORS
                )
            )

    @classmethod
    def getLogicalOperator(cls, name):
        return cls.LOGICAL_OPERATORS[name]


class File(String):
    FILENAME = "file"
    FILETYPE = None

    def __init__(self, key, **kwargs):
        fileName = kwargs.pop("name", self.FILENAME)
        fileType = kwargs.pop("type", self.FILETYPE)
        self.fileName = (
            "{}.{}".format(fileName, fileType.lower()) if fileType else fileName
        )
        super(File, self).__init__(key, **kwargs)

    def load(self, args):
        self.objectPrefix = super(File, self).load(args)
        self.objectName = (
            storage.pathJoin(self.objectPrefix, self.fileName)
            if self.objectPrefix
            else None
        )
        self.filePath = (
            storage.getPathInTempStore(self.objectName) if self.objectName else None
        )
        if self.filePath:
            path.safeMkdirsForFile(self.filePath)
        self.value = self.filePath
        return self.filePath

    def format(self, context):
        if self.filePath:
            storage.download(self.objectName, self.filePath)
        return self.filePath

    def save(self, context, result):
        filePath = result.value
        storage.upload(self.objectName, filePath)
        return self.objectPrefix


class Folder(String):
    def load(self, args):
        self.folderName = super(Folder, self).load(args)
        self.folderPath = (
            storage.getPathInTempStore(self.folderName) if self.folderName else None
        )
        if self.folderPath:
            path.safeMkdirs(self.folderPath)
        self.value = self.folderPath
        return self.folderPath

    def format(self, context):
        if self.folderPath:
            storage.download(self.folderName, self.folderPath)
        return self.folderPath

    def clean(self, context):
        if self.folderPath:
            path.empty(self.folderPath)
        return self.folderPath

    def save(self, context, result):
        folderPath = result.value
        storage.upload(self.folderName, folderPath)
        return self.folderName


class Data(File):
    FILENAME = "data"


class Csv(Data):
    FILETYPE = "csv"

    def format(self, context):
        super(Csv, self).format(context)
        self.value = utils.loadFromCsv(self.filePath)
        return self.value

    def save(self, context, result):
        utils.saveAsCsv(self.filePath, result.value)
        return super(Csv, self).save(context, Result(self.filePath))


class Npy(Data):
    FILETYPE = "npy"

    def format(self, context):
        super(Npy, self).format(context)
        self.value = utils.loadFromNpy(self.filePath)
        return self.value

    def save(self, context, result):
        utils.saveAsNpy(self.filePath, result.value)
        return super(Npy, self).save(context, Result(self.filePath))


class Model(File):
    FILENAME = "model"


class H5Model(Model):
    FILETYPE = "h5"


class Checkpoint(Model):
    FILETYPE = "ckpt"


class JsonModel(Model):
    FILETYPE = "json"


class Image(File):
    FILENAME = "image"
    FILETYPE = "png"

    def format(self, context):
        filepath = super(Image, self).format(context)
        self.value = cv2.imread(filepath)  # pylint: disable-msg=e1101
        return self.value

    def save(self, context, result):
        img = result.value
        filepath = storage.getPathInTempStore(self.objectName)
        path.safeMkdirsForFile(filepath)
        cv2.imwrite(filepath, img)  # pylint: disable-msg=e1101
        return super(Image, self).save(context, Result(self.filePath))
