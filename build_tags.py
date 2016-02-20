#! /usr/bin/env python

import collections
import imp
import os
import sys


def getTaggers():
    u""" Search through the tagger folder and get each tagger via its __init__.py """
    queue = collections.deque()
    base_tagger_path = os.path.abspath('./taggers')
    tagger_list = []

    if os.path.exists(base_tagger_path):
        queue.appendleft(base_tagger_path)
        while len(queue) > 0:
            current_dir = queue.pop()
            for tagger_dir in os.listdir(current_dir):
                # Search each directory for an __init__.py
                location = os.path.abspath(os.path.join(current_dir, tagger_dir))
                if '__init__.py' not in os.listdir(location):
                    if os.path.isdir(location):
                        queue.appendleft(location)
                    else:
                        continue
                else:
                    # Use python's module tools to get a handle to the module.
                    file_handle, pathname, descript = imp.find_module('__init__', [location])

                    if file_handle is not None:
                        try:
                            # Try and load the found module and access the tagger
                            module = imp.load_module(tagger_dir, file_handle, pathname, descript)
                            # Test to see if it has a getTagger function
                            if 'getTagger' in dir(module):
                                # Add the tagger to the tagger_list and add its path to sys.path
                                sys.path.append(os.path.abspath(os.path.split(pathname)[0]))
                                tagger_list.append(module.getTagger())
                            else:
                                print 'Found a module, but its not a tagger at: {0}'.format(pathname)
                        finally:
                            file_handle.close()

    return tagger_list

if __name__ == '__main__':
    print 'Welcome to pycodetagger'
    available_taggers = getTaggers()
    for tagger in available_taggers:
        print tagger
