import os
import glob
import shutil
import unittest
from inspect import getfile, currentframe

import autoload.vim_python_test_runner as sut


class RunDockerInVimTests(unittest.TestCase):

    def setUp(self):
        dirs_to_make = [
            "/tmp/project_app_only/example_app1/tests/",
        ]

        contents_to_write = [
            ("/tmp/project_app_only/.vim-django", '{"app_name": "example_app1"}'),
            ("/tmp/project_app_only/manage.py", "#Place holder"),
        ]

        for directory in dirs_to_make:
            os.makedirs(directory)

        for needed_file in contents_to_write:
            with open(needed_file[0], "w") as f:
                f.write(needed_file[1])

    def tearDown(self):
        for a_dir in glob.glob("/tmp/*project_*"):
            shutil.rmtree(a_dir)

    def test_create_command_to_run_current_app_with_docker(self):
        current_dir = '/tmp/project_app_only/example_app1/tests/test_file.py'
        expected_return_value = "Dispatch docker compose run test example_app1"
        command_returned = sut.get_command_to_run_python_app_with_docker(current_dir)
        self.assertEqual(command_returned, expected_return_value)

    def test_create_command_to_run_current_file_with_docker(self):
        current_dir = '/tmp/project_app_only/example_app1/tests/test_file.py'
        expected_return_value = "Dispatch docker compose run test example_app1.tests.test_file"
        command_returned = sut.get_command_to_run_python_file_with_docker(current_dir)
        self.assertEqual(command_returned, expected_return_value)

    def test_create_command_to_run_current_class_with_docker(self):
        current_dir = '/tmp/project_app_only/example_app1/tests/test_file.py'
        current_line = 17
        current_buffer = self.build_buffer_helper()
        expected_return_value = "Dispatch docker compose run test example_app1.tests.test_file:Example1"
        self.assertEqual(expected_return_value, sut.get_command_to_run_python_class_with_docker(current_dir, current_line, current_buffer))

    def test_create_command_to_run_current_method(self):
        current_dir = '/tmp/project_app_only/example_app1/tests/test_file.py'
        current_line = 17
        current_buffer = self.build_buffer_helper()
        expected_return_value = "Dispatch docker compose run test example_app1.tests.test_file:Example1.dummy2"
        self.assertEqual(expected_return_value, sut.get_command_to_run_python_method_with_docker(current_dir, current_line, current_buffer))

    def build_buffer_helper(self):
        current_dir = os.path.dirname(os.path.abspath(getfile(currentframe())))
        with open("{}/dummy_test_file.py".format(current_dir), "r") as f:
            current_buffer = []
            for line in f.readlines():
                current_buffer.append(line)
        return current_buffer
