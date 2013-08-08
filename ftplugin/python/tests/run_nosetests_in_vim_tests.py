import os
import sys
import unittest

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import vim_python_test_runner as sut


class RunNosetestsInVimTests(unittest.TestCase):

    def test_create_command_to_run_current_file_with_nosetests(self):
        path_to_current_file = "/tmp/project/tests/aTestFile.py"
        command_to_run = sut.get_command_to_run_current_file_with_nosetests(path_to_current_file)
        self.assertEqual(":!nosetests /tmp/project/tests/aTestFile.py", command_to_run)

    def test_create_command_to_run_current_class_with_nosetests(self):
        path_to_current_file = "/tmp/project/tests/aTestFile.py"
        current_line = "        print('This is a test4b')\n"
        current_buffer = self.build_buffer_helper()
        command_to_run = sut.get_command_to_run_current_class_with_nosetests(path_to_current_file, current_line, current_buffer)
        self.assertEqual(":!nosetests /tmp/project/tests/aTestFile.py:Example2", command_to_run)

    def test_create_command_to_run_current_method_with_nosetests(self):
        path_to_current_file = "/tmp/project/tests/aTestFile.py"
        current_line = "        print('This is a test4b')\n"
        current_buffer = self.build_buffer_helper()
        command_to_run = sut.get_command_to_run_current_method_with_nosetests(path_to_current_file, current_line, current_buffer)
        self.assertEqual(":!nosetests /tmp/project/tests/aTestFile.py:Example2.dummy1b", command_to_run)

    def build_buffer_helper(self):
        with open("dummy_test_file.py", "r") as f:
            current_buffer = []
            for line in f.readlines():
                current_buffer.append(line)
        return current_buffer
