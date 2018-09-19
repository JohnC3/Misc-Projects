import unittest
import logging
import os


current_dir = [i for i in os.listdir(os.path.curdir) if i != 'test_code.py']

print('searching sub folders of current_dir for merge and quicksort implementations to test')
print('current dir contains', current_dir)
# for sub_folders in
