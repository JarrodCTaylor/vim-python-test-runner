import os
import sys
import unittest

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import vim_python_test_runner as sut


class VimTestRunnerForDjangoTests(unittest.TestCase):

    def setUp(self):
        os.makedirs("/tmp/project_app_only/example_app1/tests/")
        os.makedirs("/tmp/project_app_name_and_env/example_app1/tests/")
        os.makedirs("/tmp/bad_project_no_files/example_app1/tests/")
        os.makedirs("/tmp/bad_project_no_config_file/example_app1/tests/")
        os.makedirs("/tmp/bad_project_no_app/example_app1/tests/")
        os.makedirs("/tmp/bad_project_no_path_to_tests/example_app1/tests/")
        os.makedirs("/tmp/project_multiple_apps/example_app1/tests/")
        os.makedirs("/tmp/bad_project_multiple_invalid_apps/example_app1/tests/")
        os.makedirs("/tmp/project_nested_test_dirs/example_app1/tests/nested1/")
        os.makedirs("/tmp/project_contains_app_name/app_name/tests/")
        os.makedirs("/tmp/project_failfast/example_app/tests/")
        os.makedirs("/tmp/bad_project_failfast/example_app/tests/")

        with open("/tmp/project_app_only/.vim-django", "w") as f:
            f.write('{"app_name": "example_app1"}')
        with open("/tmp/project_app_only/manage.py", "w") as f:
            f.write("#Place holder")

        with open("/tmp/project_app_name_and_env/.vim-django", "w") as f:
            f.write('{"app_name": "example_app1", "environment": "test"}')
        with open("/tmp/project_app_name_and_env/manage.py", "w") as f:
            f.write("#Place holder")

        with open("/tmp/bad_project_no_config_file/manage.py", "w") as f:
            f.write("#Place holder")

        with open("/tmp/bad_project_no_app/.vim-django", "w") as f:
            f.write('{"bad_field": "example_app1"}')
        with open("/tmp/bad_project_no_app/manage.py", "w") as f:
            f.write("#Place holder")

        with open("/tmp/bad_project_no_path_to_tests/.vim-django", "w") as f:
            f.write('{"app_name": "example_app1"}')
        with open("/tmp/bad_project_no_path_to_tests/manage.py", "w") as f:
            f.write("#Place holder")

        with open("/tmp/project_multiple_apps/.vim-django", "w") as f:
            f.write('{"app_name": "other_app, example_app1, example_app2"}')
        with open("/tmp/project_multiple_apps/manage.py", "w") as f:
            f.write("#Place holder")

        with open("/tmp/bad_project_multiple_invalid_apps/.vim-django", "w") as f:
            f.write('{"app_name": "other_app1, other_app2, other_app3"}')
        with open("/tmp/bad_project_multiple_invalid_apps/manage.py", "w") as f:
            f.write("#Place holder")

        with open("/tmp/project_nested_test_dirs/.vim-django", "w") as f:
            f.write('{"app_name": "example_app1, example_app2"}')
        with open("/tmp/project_nested_test_dirs/manage.py", "w") as f:
            f.write("#Place holder")

        with open("/tmp/project_contains_app_name/.vim-django", "w") as f:
            f.write('{"app_name": "example_app1, app_name"}')
        with open("/tmp/project_contains_app_name/manage.py", "w") as f:
            f.write("#Place holder")

        with open("/tmp/project_failfast/.vim-django", "w") as f:
            f.write('{"app_name": "example_app", "failfast": true}')
        with open("/tmp/project_failfast/manage.py", "w") as f:
            f.write("#Place holder")

        with open("/tmp/bad_project_failfast/.vim-django", "w") as f:
            f.write('{"app_name": "example_app", "failfast": false}')
        with open("/tmp/bad_project_failfast/manage.py", "w") as f:
            f.write("#Place holder")

    def tearDown(self):
        os.remove("/tmp/project_app_only/manage.py")
        os.remove("/tmp/project_app_only/.vim-django")

        os.remove("/tmp/project_app_name_and_env/.vim-django")
        os.remove("/tmp/project_app_name_and_env/manage.py")

        os.remove("/tmp/bad_project_no_config_file/manage.py")

        os.remove("/tmp/bad_project_no_app/.vim-django")
        os.remove("/tmp/bad_project_no_app/manage.py")

        os.remove("/tmp/bad_project_no_path_to_tests/.vim-django")
        os.remove("/tmp/bad_project_no_path_to_tests/manage.py")

        os.remove("/tmp/project_multiple_apps/.vim-django")
        os.remove("/tmp/project_multiple_apps/manage.py")

        os.remove("/tmp/bad_project_multiple_invalid_apps/.vim-django")
        os.remove("/tmp/bad_project_multiple_invalid_apps/manage.py")

        os.remove("/tmp/project_nested_test_dirs/.vim-django")
        os.remove("/tmp/project_nested_test_dirs/manage.py")

        os.remove("/tmp/project_contains_app_name/.vim-django")
        os.remove("/tmp/project_contains_app_name/manage.py")

        os.remove("/tmp/project_failfast/.vim-django")
        os.remove("/tmp/project_failfast/manage.py")

        os.remove("/tmp/bad_project_failfast/.vim-django")
        os.remove("/tmp/bad_project_failfast/manage.py")

        os.removedirs("/tmp/project_app_only/example_app1/tests/")
        os.removedirs("/tmp/project_app_name_and_env/example_app1/tests/")
        os.removedirs("/tmp/bad_project_no_files/example_app1/tests/")
        os.removedirs("/tmp/bad_project_no_config_file/example_app1/tests/")
        os.removedirs("/tmp/bad_project_no_app/example_app1/tests/")
        os.removedirs("/tmp/bad_project_no_path_to_tests/example_app1/tests/")
        os.removedirs("/tmp/project_multiple_apps/example_app1/tests/")
        os.removedirs("/tmp/bad_project_multiple_invalid_apps/example_app1/tests/")
        os.removedirs("/tmp/project_nested_test_dirs/example_app1/tests/nested1/")
        os.removedirs("/tmp/project_contains_app_name/app_name/tests/")
        os.removedirs("/tmp/project_failfast/example_app/tests/")
        os.removedirs("/tmp/bad_project_failfast/example_app/tests/")

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

    def build_buffer_helper(self):
        with open("dummy_test_file.py", "r") as f:
            current_buffer = []
            for line in f.readlines():
                current_buffer.append(line)
        return current_buffer

    def get_cached_command(self):
        with open("/tmp/vim_python_test_runner_cache", "r") as f:
            return f.read()
