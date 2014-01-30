import os
import unittest

import vim_python_test_runner as sut


class VimTestRunnerForDjangoTests(unittest.TestCase):

    def setUp(self):
        dirs_to_make = [
            "/tmp/project_app_only/example_app1/tests/", "/tmp/project_app_name_and_env/example_app1/tests/",
            "/tmp/bad_project_no_files/example_app1/tests/", "/tmp/bad_project_no_config_file/example_app1/tests/",
            "/tmp/bad_project_no_app/example_app1/tests/", "/tmp/bad_project_no_path_to_tests/example_app1/tests/",
            "/tmp/project_multiple_apps/example_app1/tests/", "/tmp/bad_project_multiple_invalid_apps/example_app1/tests/",
            "/tmp/project_nested_test_dirs/example_app1/tests/nested1/", "/tmp/project_contains_app_name/app_name/tests/",
            "/tmp/project_failfast/example_app/tests/", "/tmp/bad_project_failfast/example_app/tests/",
            "/tmp/project_nocapture/example_app/tests/", "/tmp/bad_project_nocapture/example_app/tests/",
            "/tmp/project_with_dots/example.app.something/tests/"
        ]

        contents_to_write = [
            ("/tmp/project_app_only/.vim-django", '{"app_name": "example_app1"}'),
            ("/tmp/project_app_only/manage.py", "#Place holder"),
            ("/tmp/project_app_name_and_env/.vim-django", '{"app_name": "example_app1", "environment": "test"}'),
            ("/tmp/project_app_name_and_env/manage.py", "#Place holder"),
            ("/tmp/bad_project_no_config_file/manage.py", "#Place holder"),
            ("/tmp/bad_project_no_app/.vim-django", '{"bad_field": "example_app1"}'),
            ("/tmp/bad_project_no_app/manage.py", "#Place holder"),
            ("/tmp/bad_project_no_path_to_tests/.vim-django", '{"app_name": "example_app1"}'),
            ("/tmp/bad_project_no_path_to_tests/manage.py", "#Place holder"),
            ("/tmp/project_multiple_apps/.vim-django", '{"app_name": "other_app, example_app1, example_app2"}'),
            ("/tmp/project_multiple_apps/manage.py", "#Place holder"),
            ("/tmp/bad_project_multiple_invalid_apps/.vim-django", '{"app_name": "other_app1, other_app2, other_app3"}'),
            ("/tmp/bad_project_multiple_invalid_apps/manage.py", "#Place holder"),
            ("/tmp/project_nested_test_dirs/.vim-django", '{"app_name": "example_app1, example_app2"}'),
            ("/tmp/project_nested_test_dirs/manage.py", "#Place holder"),
            ("/tmp/project_contains_app_name/.vim-django", '{"app_name": "example_app1, app_name"}'),
            ("/tmp/project_contains_app_name/manage.py", "#Place holder"),
            ("/tmp/project_failfast/.vim-django", '{"app_name": "example_app", "failfast": true}'),
            ("/tmp/project_failfast/manage.py", "#Place holder"),
            ("/tmp/bad_project_failfast/.vim-django", '{"app_name": "example_app", "failfast": false}'),
            ("/tmp/bad_project_failfast/manage.py", "#Place holder"),
            ("/tmp/project_nocapture/.vim-django", '{"app_name": "example_app", "nocapture": true}'),
            ("/tmp/project_nocapture/manage.py", "#Place holder"),
            ("/tmp/bad_project_nocapture/.vim-django", '{"app_name": "example_app", "nocapture": false}'),
            ("/tmp/bad_project_nocapture/manage.py", "#Place holder"),
            ("/tmp/project_with_dots/.vim-django", '{"app_name": "example.app.something"}'),
            ("/tmp/project_with_dots/manage.py", "#Place holder")
        ]

        for directory in dirs_to_make:
            os.makedirs(directory)

        for needed_file in contents_to_write:
            with open(needed_file[0], "w") as f:
                f.write(needed_file[1])

    def tearDown(self):
        files_to_del = [
            "/tmp/project_app_only/manage.py", "/tmp/project_app_only/.vim-django",
            "/tmp/project_app_name_and_env/.vim-django", "/tmp/project_app_name_and_env/manage.py",
            "/tmp/bad_project_no_config_file/manage.py", "/tmp/bad_project_no_app/.vim-django",
            "/tmp/bad_project_no_app/manage.py", "/tmp/bad_project_no_path_to_tests/.vim-django",
            "/tmp/bad_project_no_path_to_tests/manage.py", "/tmp/project_multiple_apps/.vim-django",
            "/tmp/project_multiple_apps/manage.py", "/tmp/bad_project_multiple_invalid_apps/.vim-django",
            "/tmp/bad_project_multiple_invalid_apps/manage.py", "/tmp/project_nested_test_dirs/.vim-django",
            "/tmp/project_nested_test_dirs/manage.py", "/tmp/project_contains_app_name/.vim-django",
            "/tmp/project_contains_app_name/manage.py", "/tmp/project_failfast/.vim-django",
            "/tmp/project_failfast/manage.py", "/tmp/bad_project_failfast/.vim-django",
            "/tmp/bad_project_failfast/manage.py", "/tmp/project_nocapture/.vim-django",
            "/tmp/project_nocapture/manage.py", "/tmp/bad_project_nocapture/.vim-django",
            "/tmp/bad_project_nocapture/manage.py", "/tmp/project_with_dots/.vim-django",
            "/tmp/project_with_dots/manage.py"
        ]

        dirs_to_del = [
            "/tmp/project_app_only/example_app1/tests/", "/tmp/project_app_name_and_env/example_app1/tests/",
            "/tmp/bad_project_no_files/example_app1/tests/", "/tmp/bad_project_no_config_file/example_app1/tests/",
            "/tmp/bad_project_no_app/example_app1/tests/", "/tmp/bad_project_no_path_to_tests/example_app1/tests/",
            "/tmp/project_multiple_apps/example_app1/tests/", "/tmp/bad_project_multiple_invalid_apps/example_app1/tests/",
            "/tmp/project_nested_test_dirs/example_app1/tests/nested1/", "/tmp/project_contains_app_name/app_name/tests/",
            "/tmp/project_failfast/example_app/tests/", "/tmp/bad_project_failfast/example_app/tests/",
            "/tmp/project_nocapture/example_app/tests/", "/tmp/bad_project_nocapture/example_app/tests/",
            "/tmp/project_with_dots/example.app.something/tests/"
        ]

        for a_file in files_to_del:
            os.remove(a_file)

        for directory in dirs_to_del:
            os.removedirs(directory)

    def test_find_vim_django_file(self):
        return_value = sut.find_path_to_file("/tmp/project_app_only/example_app1/tests", ".vim-django")
        self.assertEqual(return_value, "/tmp/project_app_only/.vim-django")

    def test_can_not_find_vim_django_file(self):
        return_value = sut.find_path_to_file("/tmp/bad_project_no_files/example_app1/tests", ".vim-django")
        self.assertEqual(return_value, False)

    def test_find_manage_py(self):
        return_value = sut.find_path_to_file("/tmp/project_app_only/example_app1/tests", "manage.py")
        self.assertEqual(return_value, "/tmp/project_app_only/manage.py")

    def test_can_not_find_manage_py(self):
        return_value = sut.find_path_to_file("/tmp/bad_project_no_files/example_app1/tests", "manage.py")
        self.assertEqual(return_value, False)

    def test_get_valid_class_name(self):
        current_line1 = 17
        current_line2 = 24
        current_buffer = self.build_buffer_helper()
        self.assertEqual("Example1", sut.get_current_class(current_line1, current_buffer))
        self.assertEqual("Example2", sut.get_current_class(current_line2, current_buffer))

    def test_get_current_class_returns_false_when_not_in_class(self):
        current_buffer = self.build_buffer_helper()
        self.assertEqual(False, sut.get_current_class(2, current_buffer))

    def test_get_valid_method_name(self):
        should_return_dummy2 = 15
        should_return_dummy1b = 27
        current_buffer = self.build_buffer_helper()
        self.assertEqual("dummy2", sut.get_current_method(should_return_dummy2, current_buffer))
        self.assertEqual("dummy1b", sut.get_current_method(should_return_dummy1b, current_buffer))

    def test_get_current_method_returns_false_when_not_in_method_message(self):
        current_buffer = self.build_buffer_helper()
        self.assertEqual(False, sut.get_current_method(25, current_buffer))

    def test_get_app_name(self):
        app_name = sut.get_json_field_from_config_file("/tmp/project_app_only/example_app1/tests", "app_name")
        self.assertEqual("example_app1", app_name)

    def test_get_env_name_when_present(self):
        app_name = sut.get_json_field_from_config_file("/tmp/project_app_name_and_env/example_app1/tests", "environment")
        self.assertEqual("test", app_name)

    def test_get_env_name_returns_false_when_not_provided(self):
        app_name = sut.get_json_field_from_config_file("/tmp/project_app_only/example_app1/tests", "environment")
        self.assertEqual(False, app_name)

    def test_get_command_to_run_the_current_app_when_manage_py_found_and_app_name_provided_and_no_env_specified(self):
        current_dir = '/tmp/project_app_only/example_app1/tests/test_file.py'
        command_to_run = sut.get_command_to_run_the_current_app(current_dir)
        self.assertEqual("/tmp/project_app_only/manage.py test example_app1", command_to_run)

    def test_get_command_to_run_the_current_app_when_manage_py_found_and_app_name_and_env_specified(self):
        current_dir = '/tmp/project_app_name_and_env/example_app1/tests/test_file.py'
        command_to_run = sut.get_command_to_run_the_current_app(current_dir)
        self.assertEqual("/tmp/project_app_name_and_env/manage.py test test example_app1", command_to_run)

    def test_get_command_to_run_the_current_app_when_config_file_not_properly_formated(self):
        current_dir = '/tmp/bad_project_no_app/example_app1/tests/test_file.py'
        command_to_run = sut.get_command_to_run_the_current_app(current_dir)
        expected_return_value = ".vim-django does not exist"
        self.assertEqual(expected_return_value, command_to_run)

    def test_get_command_to_run_the_current_app_when_config_file_not_present(self):
        current_dir = '/tmp/bad_project_no_config_file/example_app1/tests/test_file.py'
        command_to_run = sut.get_command_to_run_the_current_app(current_dir)
        expected_return_value = ".vim-django does not exist"
        self.assertEqual(expected_return_value, command_to_run)

    def test_get_command_to_run_the_current_app_when_manage_py_not_found(self):
        current_dir = '/tmp/bad_project_no_files/example_app1/tests/test_file.py'
        command_to_run = sut.get_command_to_run_the_current_app(current_dir)
        self.assertEqual("Not Django", command_to_run)

    def test_get_command_to_run_the_current_file_when_manage_py_found_and_app_name_provided_and_no_env_specified(self):
        current_dir = '/tmp/project_app_only/example_app1/tests/test_file.py'
        expected_return_value = "/tmp/project_app_only/manage.py test example_app1.tests.test_file"
        command_returned = sut.get_command_to_run_the_current_file(current_dir)
        self.assertEqual(command_returned, expected_return_value)

    def test_get_command_to_run_the_current_file_when_manage_py_found_and_app_name_and_env_specified(self):
        current_dir = '/tmp/project_app_name_and_env/example_app1/tests/test_file.py'
        command_to_run = sut.get_command_to_run_the_current_file(current_dir)
        self.assertEqual("/tmp/project_app_name_and_env/manage.py test test example_app1.tests.test_file", command_to_run)
        pass

    def test_get_command_to_run_the_current_file_when_config_file_not_properly_formated(self):
        current_dir = '/tmp/bad_project_no_app/example_app1/tests/test_file.py'
        command_to_run = sut.get_command_to_run_the_current_file(current_dir)
        expected_return_value = ".vim-django does not exist"
        self.assertEqual(expected_return_value, command_to_run)

    def test_get_command_to_run_the_current_file_when_config_file_not_present(self):
        current_dir = '/tmp/bad_project_no_config_file/example_app1/tests/test_file.py'
        command_to_run = sut.get_command_to_run_the_current_file(current_dir)
        expected_return_value = ".vim-django does not exist"
        self.assertEqual(expected_return_value, command_to_run)

    def test_get_command_to_run_the_current_file_when_manage_py_not_found(self):
        current_dir = '/tmp/bad_project_no_files/example_app1/tests/test_file.py'
        command_to_run = sut.get_command_to_run_the_current_file(current_dir)
        self.assertEqual("Not Django", command_to_run)

    def test_get_command_to_run_the_current_class_with_manage_py_app_name_but_no_env_specified(self):
        current_dir = '/tmp/project_app_only/example_app1/tests/test_file.py'
        current_line = 17
        current_buffer = self.build_buffer_helper()
        expected_return_value = "/tmp/project_app_only/manage.py test example_app1.tests.test_file:Example1"
        self.assertEqual(expected_return_value, sut.get_command_to_run_the_current_class(current_dir, current_line, current_buffer))

    def test_get_command_to_run_the_current_class_with_manage_py_app_name_and_env_specified(self):
        current_dir = '/tmp/project_app_name_and_env/example_app1/tests/test_file.py'
        current_line = 17
        current_buffer = self.build_buffer_helper()
        expected_return_value = "/tmp/project_app_name_and_env/manage.py test test example_app1.tests.test_file:Example1"
        self.assertEqual(expected_return_value, sut.get_command_to_run_the_current_class(current_dir, current_line, current_buffer))

    def test_get_command_to_run_the_current_class_when_config_not_properly_formated_no_app_name(self):
        current_dir = '/tmp/bad_project_no_app/example_app1/tests/test_file.py'
        current_line = 17
        current_buffer = self.build_buffer_helper()
        expected_return_value = ".vim-django does not exist"
        self.assertEqual(expected_return_value, sut.get_command_to_run_the_current_class(current_dir, current_line, current_buffer))

    def test_get_command_to_run_the_current_class_when_config_not_present(self):
        current_dir = '/tmp/bad_project_no_app/example_app1/tests/test_file.py'
        current_line = 17
        current_buffer = self.build_buffer_helper()
        expected_return_value = ".vim-django does not exist"
        self.assertEqual(expected_return_value, sut.get_command_to_run_the_current_class(current_dir, current_line, current_buffer))

    def test_get_command_to_run_the_current_class_when_manage_py_not_found(self):
        current_dir = '/tmp/bad_project_no_files/example_app1/tests/test_file.py'
        current_line = 17
        current_buffer = self.build_buffer_helper()
        self.assertEqual("Not Django", sut.get_command_to_run_the_current_class(current_dir, current_line, current_buffer))

    def test_get_command_to_run_the_current_method_with_manage_py_app_name_but_no_env_specified(self):
        current_dir = '/tmp/project_app_only/example_app1/tests/test_file.py'
        current_line = 17
        current_buffer = self.build_buffer_helper()
        expected_return_value = "/tmp/project_app_only/manage.py test example_app1.tests.test_file:Example1.dummy2"
        self.assertEqual(expected_return_value, sut.get_command_to_run_the_current_method(current_dir, current_line, current_buffer))

    def test_get_command_to_run_the_current_method_with_manage_py_app_name_and_env_specified(self):
        current_dir = '/tmp/project_app_name_and_env/example_app1/tests/test_file.py'
        current_line = 17
        current_buffer = self.build_buffer_helper()
        expected_return_value = "/tmp/project_app_name_and_env/manage.py test test example_app1.tests.test_file:Example1.dummy2"
        self.assertEqual(expected_return_value, sut.get_command_to_run_the_current_method(current_dir, current_line, current_buffer))

    def test_get_command_to_run_the_current_method_when_config_not_properly_formated(self):
        current_dir = '/tmp/bad_project_no_app/example_app1/tests/test_file.py'
        current_line = 17
        current_buffer = self.build_buffer_helper()
        expected_return_value = ".vim-django does not exist"
        self.assertEqual(expected_return_value, sut.get_command_to_run_the_current_method(current_dir, current_line, current_buffer))

    def test_get_command_to_run_the_current_method_when_config_not_present(self):
        current_dir = '/tmp/bad_project_no_app/example_app1/tests/test_file.py'
        current_line = 17
        current_buffer = self.build_buffer_helper()
        expected_return_value = ".vim-django does not exist"
        self.assertEqual(expected_return_value, sut.get_command_to_run_the_current_method(current_dir, current_line, current_buffer))

    def test_get_command_to_run_the_current_method_when_manage_py_not_found(self):
        current_dir = '/tmp/bad_project_no_files/example_app1/tests/test_file.py'
        current_line = 17
        current_buffer = self.build_buffer_helper()
        expected_return_value = "Not Django"
        self.assertEqual(expected_return_value, sut.get_command_to_run_the_current_method(current_dir, current_line, current_buffer))

    def test_get_command_to_run_the_current_app_when_multiple_apps_are_listed_and_a_valid_app_name_is_in_config_file(self):
        current_dir = "/tmp/project_multiple_apps/example_app1/tests/test_file.py"
        expected_return_value = "/tmp/project_multiple_apps/manage.py test example_app1"
        command_returned = sut.get_command_to_run_the_current_app(current_dir)
        self.assertEqual(command_returned, expected_return_value)

    def test_get_command_to_run_the_current_file_when_multiple_apps_are_listed_and_a_valid_app_name_is_in_config_file(self):
        current_dir = "/tmp/project_multiple_apps/example_app1/tests/test_file.py"
        expected_return_value = "/tmp/project_multiple_apps/manage.py test example_app1.tests.test_file"
        command_returned = sut.get_command_to_run_the_current_file(current_dir)
        self.assertEqual(command_returned, expected_return_value)

    def test_get_command_to_run_the_current_class_when_multiple_apps_are_listed_and_a_valid_app_name_is_in_config_file(self):
        current_dir = "/tmp/project_multiple_apps/example_app1/tests/test_file.py"
        current_line = 17
        current_buffer = self.build_buffer_helper()
        expected_return_value = "/tmp/project_multiple_apps/manage.py test example_app1.tests.test_file:Example1"
        command_returned = sut.get_command_to_run_the_current_class(current_dir, current_line, current_buffer)
        self.assertEqual(command_returned, expected_return_value)

    def test_get_command_to_run_the_current_method_when_multiple_apps_are_listed_and_a_valid_app_name_is_in_config_file(self):
        current_dir = "/tmp/project_multiple_apps/example_app1/tests/test_file.py"
        current_line = 17
        current_buffer = self.build_buffer_helper()
        expected_return_value = "/tmp/project_multiple_apps/manage.py test example_app1.tests.test_file:Example1.dummy2"
        command_returned = sut.get_command_to_run_the_current_method(current_dir, current_line, current_buffer)
        self.assertEqual(command_returned, expected_return_value)

    def test_get_command_to_run_the_current_app_when_multiple_apps_are_listed_and_a_valid_app_name_is_not_in_config_file(self):
        current_dir = "/tmp/bad_project_multiple_invalid_apps/example_app1/tests/test_file.py"
        expected_return_value = ".vim-django does not exist"
        command_returned = sut.get_command_to_run_the_current_app(current_dir)
        self.assertEqual(command_returned, expected_return_value)

    def test_get_command_to_run_the_current_file_when_multiple_apps_are_listed_and_a_valid_app_name_is_not_in_config_file(self):
        current_dir = "/tmp/bad_project_multiple_invalid_apps/example_app1/tests/test_file.py"
        expected_return_value = ".vim-django does not exist"
        command_returned = sut.get_command_to_run_the_current_file(current_dir)
        self.assertEqual(command_returned, expected_return_value)

    def test_get_command_to_run_the_current_class_when_multiple_apps_are_listed_and_a_valid_app_name_is_not_in_config_file(self):
        current_dir = "/tmp/bad_project_multiple_invalid_apps/example_app1/tests/test_file.py"
        current_line = 17
        current_buffer = self.build_buffer_helper()
        expected_return_value = ".vim-django does not exist"
        command_returned = sut.get_command_to_run_the_current_class(current_dir, current_line, current_buffer)
        self.assertEqual(command_returned, expected_return_value)

    def test_get_command_to_run_the_current_method_when_multiple_apps_are_listed_and_a_valid_app_name_is_not_in_config_file(self):
        current_dir = "/tmp/bad_project_multiple_invalid_apps/example_app1/tests/test_file.py"
        current_line = 17
        current_buffer = self.build_buffer_helper()
        expected_return_value = ".vim-django does not exist"
        command_returned = sut.get_command_to_run_the_current_method(current_dir, current_line, current_buffer)
        self.assertEqual(command_returned, expected_return_value)

    def test_get_command_to_run_current_app_when_tests_are_in_a_nested_directory(self):
        current_dir = "/tmp/project_nested_test_dirs/example_app1/tests/nested1/test_nested_file.py"
        expected_return_value = "/tmp/project_nested_test_dirs/manage.py test example_app1"
        command_returned = sut.get_command_to_run_the_current_app(current_dir)
        self.assertEqual(command_returned, expected_return_value)

    def test_get_command_to_run_current_file_when_tests_are_in_a_nested_directory(self):
        current_dir = "/tmp/project_nested_test_dirs/example_app1/tests/nested1/test_nested_file.py"
        expected_return_value = "/tmp/project_nested_test_dirs/manage.py test example_app1.tests.nested1.test_nested_file"
        command_returned = sut.get_command_to_run_the_current_file(current_dir)
        self.assertEqual(command_returned, expected_return_value)

    def test_get_command_to_run_current_class_when_tests_are_in_a_nested_directory(self):
        current_dir = "/tmp/project_nested_test_dirs/example_app1/tests/nested1/test_nested_file.py"
        current_line = 17
        current_buffer = self.build_buffer_helper()
        expected_return_value = "/tmp/project_nested_test_dirs/manage.py test example_app1.tests.nested1.test_nested_file:Example1"
        command_returned = sut.get_command_to_run_the_current_class(current_dir, current_line, current_buffer)
        self.assertEqual(command_returned, expected_return_value)

    def test_get_command_to_run_current_method_when_tests_are_in_a_nested_directory(self):
        current_dir = "/tmp/project_nested_test_dirs/example_app1/tests/nested1/test_nested_file.py"
        current_line = 17
        current_buffer = self.build_buffer_helper()
        expected_return_value = "/tmp/project_nested_test_dirs/manage.py test example_app1.tests.nested1.test_nested_file:Example1.dummy2"
        command_returned = sut.get_command_to_run_the_current_method(current_dir, current_line, current_buffer)
        self.assertEqual(command_returned, expected_return_value)

    def test_get_command_to_run_current_class_when_current_line_occurs_in_file_more_than_once(self):
        current_dir = '/tmp/project_app_only/example_app1/tests/test_file.py'
        current_line = 42
        current_buffer = self.build_buffer_helper()
        expected_return_value = "/tmp/project_app_only/manage.py test example_app1.tests.test_file:Example3"
        self.assertEqual(expected_return_value, sut.get_command_to_run_the_current_class(current_dir, current_line, current_buffer))

    def test_get_command_to_run_current_method_when_current_line_occurs_in_file_more_than_once(self):
        current_dir = '/tmp/project_app_name_and_env/example_app1/tests/test_file.py'
        current_line = 50
        current_buffer = self.build_buffer_helper()
        expected_return_value = "/tmp/project_app_name_and_env/manage.py test test example_app1.tests.test_file:Example3.double_dummy"
        self.assertEqual(expected_return_value, sut.get_command_to_run_the_current_method(current_dir, current_line, current_buffer))

    def test_get_command_to_run_the_current_class_when_project_name_contains_the_app_name(self):
        current_dir = "/tmp/project_contains_app_name/app_name/tests/test_file.py"
        current_line = 17
        current_buffer = self.build_buffer_helper()
        expected_return_value = "/tmp/project_contains_app_name/manage.py test app_name.tests.test_file:Example1"
        command_returned = sut.get_command_to_run_the_current_class(current_dir, current_line, current_buffer)
        self.assertEqual(command_returned, expected_return_value)

    def test_get_command_to_run_the_current_app_when_failfast_is_set_to_true_in_config_file(self):
        current_dir = '/tmp/project_failfast/example_app/tests/test_file.py'
        command_to_run = sut.get_command_to_run_the_current_app(current_dir)
        self.assertEqual("/tmp/project_failfast/manage.py test --failfast example_app", command_to_run)

    def test_get_command_to_run_the_current_app_when_failfast_is_set_to_a_bad_value_in_config_file(self):
        current_dir = '/tmp/bad_project_failfast/example_app/tests/test_file.py'
        command_to_run = sut.get_command_to_run_the_current_app(current_dir)
        self.assertEqual("/tmp/bad_project_failfast/manage.py test example_app", command_to_run)

    def test_get_command_to_run_the_current_app_when_nocapture_is_set_to_true_in_config_file(self):
        current_dir = '/tmp/project_nocapture/example_app/tests/test_file.py'
        command_to_run = sut.get_command_to_run_the_current_app(current_dir)
        self.assertEqual("/tmp/project_nocapture/manage.py test --nocapture example_app", command_to_run)

    def test_get_command_to_run_the_current_app_when_nocapture_is_set_to_a_bad_value_in_config_file(self):
        current_dir = '/tmp/bad_project_nocapture/example_app/tests/test_file.py'
        command_to_run = sut.get_command_to_run_the_current_app(current_dir)
        self.assertEqual("/tmp/bad_project_nocapture/manage.py test example_app", command_to_run)

    def test_get_command_to_run_current_app_writes_command_to_cache_file_when_successfully_called(self):
        current_dir = '/tmp/project_app_only/example_app1/tests/test_file.py'
        command_to_run = sut.get_command_to_run_the_current_app(current_dir)
        last_command = self.get_cached_command()
        self.assertEqual(command_to_run, last_command)

    def test_get_command_to_run_current_file_writes_command_to_cache_file_when_successfully_called(self):
        current_dir = '/tmp/project_app_only/example_app1/tests/test_file.py'
        command_to_run = sut.get_command_to_run_the_current_file(current_dir)
        last_command = self.get_cached_command()
        self.assertEqual(command_to_run, last_command)

    def test_get_command_to_run_current_class_writes_command_to_cache_file_when_successfully_called(self):
        current_dir = '/tmp/project_app_only/example_app1/tests/test_file.py'
        current_line = 17
        current_buffer = self.build_buffer_helper()
        command_to_run = sut.get_command_to_run_the_current_class(current_dir, current_line, current_buffer)
        last_command = self.get_cached_command()
        self.assertEqual(command_to_run, last_command)

    def test_get_command_to_run_current_method_writes_command_to_cache_file_when_successfully_called(self):
        current_dir = '/tmp/project_app_only/example_app1/tests/test_file.py'
        current_line = 17
        current_buffer = self.build_buffer_helper()
        command_to_run = sut.get_command_to_run_the_current_method(current_dir, current_line, current_buffer)
        last_command = self.get_cached_command()
        self.assertEqual(command_to_run, last_command)

    def test_get_command_to_rerun_last_tests_returns_the_command_last_used_to_run_tests(self):
        current_dir = '/tmp/project_app_only/example_app1/tests/test_file.py'
        command_to_run = sut.get_command_to_run_the_current_app(current_dir)
        last_command = sut.get_command_to_rerun_last_tests()
        self.assertEqual(command_to_run, last_command)

    def test_get_command_to_run_current_method_when_app_name_has_dots(self):
        current_dir = "/tmp/project_with_dots/example.app.something/tests/test_dot_file.py"
        current_line = 17
        current_buffer = self.build_buffer_helper()
        expected_return_value = "/tmp/project_with_dots/manage.py test example.app.something.tests.test_dot_file:Example1.dummy2"
        command_returned = sut.get_command_to_run_the_current_method(current_dir, current_line, current_buffer)
        self.assertEqual(command_returned, expected_return_value)

    def build_buffer_helper(self):
        with open("dummy_test_file.py", "r") as f:
            current_buffer = []
            for line in f.readlines():
                current_buffer.append(line)
        return current_buffer

    def get_cached_command(self):
        with open("/tmp/vim_python_test_runner_cache", "r") as f:
            return f.read()
