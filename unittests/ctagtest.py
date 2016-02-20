#! /usr/bin/env python

import unittest
import os
import sys

sys.path.append(os.path.abspath('../taggers/c_cpp'))

import ctagger


class TestGetFileTypes(unittest.TestCase):

    def test_file_types_is_not_none(self):
        tagger = ctagger.CTagger()
        self.assertIsNotNone(tagger.getFileTypes())

    def test_return_type_is_list(self):
        tagger = ctagger.CTagger()
        self.assertEqual(type(list()), type(tagger.getFileTypes()))

    def test_list_is_not_empty(self):
        tagger = ctagger.CTagger()
        data = tagger.getFileTypes()
        self.assertNotEqual(0, len(data))


class TestParseFiles(unittest.TestCase):

    def test_none_argument_no_throw(self):
        tagger = ctagger.CTagger()
        self.assertEqual(0, tagger.parseFiles(None))

if __name__ == '__main__':
    unittest.main()
