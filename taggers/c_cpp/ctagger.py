#! /usr/bin/env python


class CTagger():
    def __init__(self):
        pass

    def __repr__(self):
        return 'C/CPP Tagger'

    def getFileTypes(self):
        return ['c', 'h', 'cpp', 'hpp', 'cxx', 'hxx']

    def parseFiles(self, fileList):
        numFilesProcessed = 0
        if fileList is not None:
            pass
        return numFilesProcessed
