import unittest

import vim_python_test_runner as sut


class RunNosetestsInVimTests(unittest.TestCase):

    def test_create_command_to_run_current_file_with_nosetests(self):
        path_to_current_file = "/tmp/project/tests/aTestFile.py"
        command_to_run = sut.get_command_to_run_current_file_with_nosetests(path_to_current_file)
        self.assertEqual(":!nosetests /tmp/project/tests/aTestFile.py", command_to_run)

    def test_create_command_to_run_current_file_with_nosetests_writes_command_to_cache_file_when_successfully_called(self):
        path_to_current_file = "/tmp/project/tests/aTestFile.py"
        command_to_run = sut.get_command_to_run_current_file_with_nosetests(path_to_current_file)
        last_command = sut.get_command_to_rerun_last_tests()
        self.assertEqual(command_to_run, last_command)

    def test_create_command_to_run_current_class_with_nosetests(self):
        path_to_current_file = "/tmp/project/tests/aTestFile.py"
        current_line = 27
        current_buffer = self.build_buffer_helper()
        command_to_run = sut.get_command_to_run_current_class_with_nosetests(path_to_current_file, current_line, current_buffer)
        self.assertEqual(":!nosetests /tmp/project/tests/aTestFile.py:Example2", command_to_run)

    def test_create_command_to_run_current_class_with_nosetests_writes_command_to_cache_file_when_successfully_called(self):
        path_to_current_file = "/tmp/project/tests/aTestFile.py"
        current_line = 27
        current_buffer = self.build_buffer_helper()
        command_to_run = sut.get_command_to_run_current_class_with_nosetests(path_to_current_file, current_line, current_buffer)
        last_command = sut.get_command_to_rerun_last_tests()
        self.assertEqual(command_to_run, last_command)

    def test_create_command_to_run_current_method_with_nosetests(self):
        path_to_current_file = "/tmp/project/tests/aTestFile.py"
        current_line = 44
        current_buffer = self.build_buffer_helper()
        command_to_run = sut.get_command_to_run_current_method_with_nosetests(path_to_current_file, current_line, current_buffer)
        self.assertEqual(":!nosetests /tmp/project/tests/aTestFile.py:Example3.double_dummy1", command_to_run)

    def test_create_command_to_run_current_method_with_nosetests_writes_command_to_cache_file_when_successfully_called(self):
        path_to_current_file = "/tmp/project/tests/aTestFile.py"
        current_line = 44
        current_buffer = self.build_buffer_helper()
        command_to_run = sut.get_command_to_run_current_method_with_nosetests(path_to_current_file, current_line, current_buffer)
        last_command = sut.get_command_to_rerun_last_tests()
        self.assertEqual(command_to_run, last_command)

    def build_buffer_helper(self):
        with open("dummy_test_file.py", "r") as f:
            current_buffer = []
            for line in f.readlines():
                current_buffer.append(line)
        return current_buffer

    def get_cached_command(self):
        with open("/tmp/vim_python_test_runner_cache", "r") as f:
            return f.read()
