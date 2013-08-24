import os
import sys
import unittest
import os.path

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import vim_python_test_runner as sut


class RunBasicDjangoTestsInVimTests(unittest.TestCase):

    def setUp(self):
        os.makedirs("/tmp/project_apps_only/Level1/Level2/tests/")
        os.makedirs("/tmp/project_app_names_and_env/Level1/Level2/tests/")
        os.makedirs("/tmp/bad_project_no_files/Level1/Level2/tests/")
        os.makedirs("/tmp/bad_project_no_config_file/Level1/Level2/tests/")
        os.makedirs("/tmp/bad_project_no_apps/Level1/Level2/tests/")
        os.makedirs("/tmp/bad_project_no_path_to_tests/Level1/Level2/tests")

        with open("/tmp/project_apps_only/Level1/.vim-django", "w") as f:
            f.write('{"app_name": {"example_app1", "example_app2"}, "path_to_tests": "tests"}')
        with open("/tmp/project_apps_only/manage.py", "w") as f:
            f.write("#Place holder")

        with open("/tmp/project_app_names_and_env/Level1/.vim-django", "w") as f:
            f.write('{"app_name": "example_app", "environment": "test", "path_to_tests": "tests"}')
        with open("/tmp/project_app_names_and_env/manage.py", "w") as f:
            f.write("#Place holder")
        with open("/tmp/bad_project_no_config_file/manage.py", "w") as f:
            f.write("#Place holder")

        with open("/tmp/bad_project_no_apps/Level1/.vim-django", "w") as f:
            f.write('{"bad_field": "example_app"}')
        with open("/tmp/bad_project_no_apps/manage.py", "w") as f:
            f.write("#Place holder")

        with open("/tmp/bad_project_no_path_to_tests/Level1/.vim-django", "w") as f:
            f.write('{"app_name": "example_app"}')
        with open("/tmp/bad_project_no_path_to_tests/manage.py", "w") as f:
            f.write("#Place holder")

    def tearDown(self):
        os.remove("/tmp/project_apps_only/manage.py")
        os.remove("/tmp/project_apps_only/Level1/.vim-django")

        os.remove("/tmp/project_app_names_and_env/Level1/.vim-django")
        os.remove("/tmp/project_app_names_and_env/manage.py")

        os.remove("/tmp/bad_project_no_config_file/manage.py")

        os.remove("/tmp/bad_project_no_apps/Level1/.vim-django")
        os.remove("/tmp/bad_project_no_apps/manage.py")

        os.remove("/tmp/bad_project_no_path_to_tests/Level1/.vim-django")
        os.remove("/tmp/bad_project_no_path_to_tests/manage.py")

        os.removedirs("/tmp/project_apps_only/Level1/Level2/tests/")
        os.removedirs("/tmp/project_app_names_and_env/Level1/Level2/tests/")
        os.removedirs("/tmp/bad_project_no_files/Level1/Level2/tests/")
        os.removedirs("/tmp/bad_project_no_config_file/Level1/Level2/tests/")
        os.removedirs("/tmp/bad_project_no_apps/Level1/Level2/tests/")
        os.removedirs("/tmp/bad_project_no_path_to_tests/Level1/Level2/tests")

    def test_find_vim_django_file(self):
        return_value = sut.find_path_to_file("/tmp/project_apps_only/Level1/Level2/tests", ".vim-django")
        self.assertEqual(return_value, "/tmp/project_apps_only/Level1/.vim-django")

    def test_can_not_find_vim_django_file(self):
        return_value = sut.find_path_to_file("/tmp/bad_project_no_files/Level1/Level2/tests", ".vim-django")
        self.assertEqual(return_value, False)

    def test_find_manage_py(self):
        return_value = sut.find_path_to_file("/tmp/project_apps_only/Level1/Level2/tests", "manage.py")
        self.assertEqual(return_value, "/tmp/project_apps_only/manage.py")

    def test_can_not_find_manage_py(self):
        return_value = sut.find_path_to_file("/tmp/bad_project_no_files/Level1/Level2/tests", "manage.py")
        self.assertEqual(return_value, False)

    def test_get_valid_class_name(self):
        current_line1 = "        print('This is a testD')\n"
        current_line2 = "        print('This is a test4b')\n"
        current_buffer = self.build_buffer_helper()
        self.assertEqual("Example1", sut.get_current_class(current_line1, current_buffer))
        self.assertEqual("Example2", sut.get_current_class(current_line2, current_buffer))

    def test_get_not_in_class_message(self):
        current_buffer = self.build_buffer_helper()
        self.assertEqual("You don't appear to be in a class", sut.get_current_class("Bad line", current_buffer))

    def test_get_valid_method_name(self):
        should_return_dummy2 = "        print('This is a testD')\n"
        should_return_dummy1b = "        print('This is a test4b')\n"
        current_buffer = self.build_buffer_helper()
        self.assertEqual("dummy2", sut.get_current_method(should_return_dummy2, current_buffer))
        self.assertEqual("dummy1b", sut.get_current_method(should_return_dummy1b, current_buffer))

    def test_get_not_in_method_message(self):
        current_buffer = self.build_buffer_helper()
        self.assertEqual("You don't appear to be in a method", sut.get_current_method("Bad line", current_buffer))

    def test_get_app_name(self):
        app_name = sut.get_json_field_from_config_file("/tmp/project_apps_only/Level1/Level2/tests", "app_name")
        self.assertEqual("example_app", app_name)

    def test_get_env_name_when_present(self):
        app_name = sut.get_json_field_from_config_file("/tmp/project_app_names_and_env/Level1/Level2/tests", "environment")
        self.assertEqual("test", app_name)

    def test_get_env_name_returns_false_when_not_provided(self):
        app_name = sut.get_json_field_from_config_file("/tmp/project_apps_only/Level1/Level2/tests", "environment")
        self.assertEqual(False, app_name)

    def test_get_command_to_run_the_current_app_when_manage_py_found_and_app_name_provided_and_no_env_specified(self):
        current_dir = '/tmp/project_apps_only/Level1/Level2/tests/test_file.py'
        command_to_run = sut.get_command_to_run_the_current_app(current_dir)
        self.assertEqual("/tmp/project_apps_only/manage.py test example_app", command_to_run)

    def test_get_command_to_run_the_current_app_when_manage_py_found_and_app_name_and_env_specified(self):
        current_dir = '/tmp/project_app_names_and_env/Level1/Level2/tests/test_file.py'
        command_to_run = sut.get_command_to_run_the_current_app(current_dir)
        self.assertEqual("/tmp/project_app_names_and_env/manage.py test test example_app", command_to_run)

    def test_get_command_to_run_the_current_app_when_config_file_not_properly_formated(self):
        current_dir = '/tmp/bad_project_no_apps/Level1/Level2/tests/test_file.py'
        command_to_run = sut.get_command_to_run_the_current_app(current_dir)
        self.assertEqual(".vim-django file does not exist or is improperly formated. ':help vim-python-test-runner'", command_to_run)

    def test_get_command_to_run_the_current_app_when_config_file_not_present(self):
        current_dir = '/tmp/bad_project_no_config_file/Level1/Level2/tests/test_file.py'
        command_to_run = sut.get_command_to_run_the_current_app(current_dir)
        self.assertEqual(".vim-django file does not exist or is improperly formated. ':help vim-python-test-runner'", command_to_run)

    def test_get_command_to_run_the_current_app_when_manage_py_not_found(self):
        current_dir = '/tmp/bad_project_no_files/Level1/Level2/tests/test_file.py'
        command_to_run = sut.get_command_to_run_the_current_app(current_dir)
        self.assertEqual("Are you sure this is a Django project?", command_to_run)

    def test_get_command_to_run_the_current_class_with_manage_py_app_name_but_no_env_specified(self):
        current_dir = '/tmp/project_apps_only/Level1/Level2/tests/test_file.py'
        current_line = "        print('This is a testD')\n"
        current_buffer = self.build_buffer_helper()
        self.assertEqual("/tmp/project_apps_only/manage.py test example_app.tests.test_file:Example1", sut.get_command_to_run_the_current_class(current_dir, current_line, current_buffer))

    def test_get_command_to_run_the_current_class_with_manage_py_app_name_and_env_specified(self):
        current_dir = '/tmp/project_app_names_and_env/Level1/Level2/tests/test_file.py'
        current_line = "        print('This is a testD')\n"
        current_buffer = self.build_buffer_helper()
        self.assertEqual("/tmp/project_app_names_and_env/manage.py test test example_app.tests.test_file:Example1", sut.get_command_to_run_the_current_class(current_dir, current_line, current_buffer))

    def test_get_command_to_run_the_current_class_when_config_not_properly_formated_no_app_name(self):
        current_dir = '/tmp/bad_project_no_apps/Level1/Level2/tests/test_file.py'
        current_line = "        print('This is a testD')\n"
        current_buffer = self.build_buffer_helper()
        self.assertEqual(".vim-django file does not exist or is improperly formated. ':help vim-python-test-runner'", sut.get_command_to_run_the_current_class(current_dir, current_line, current_buffer))

    def test_get_command_to_run_the_current_class_when_config_not_properly_formated_no_path_to_tests(self):
        current_dir = '/tmp/bad_project_no_path_to_tests/Level1/Level2/tests/test_file.py'
        current_line = "        print('This is a testD')\n"
        current_buffer = self.build_buffer_helper()
        self.assertEqual(".vim-django file does not exist or is improperly formated. ':help vim-python-test-runner'", sut.get_command_to_run_the_current_class(current_dir, current_line, current_buffer))

    def test_get_command_to_run_the_current_class_when_config_not_present(self):
        current_dir = '/tmp/bad_project_no_apps/Level1/Level2/tests/test_file.py'
        current_line = "        print('This is a testD')\n"
        current_buffer = self.build_buffer_helper()
        self.assertEqual(".vim-django file does not exist or is improperly formated. ':help vim-python-test-runner'", sut.get_command_to_run_the_current_class(current_dir, current_line, current_buffer))

    def test_get_command_to_run_the_current_class_when_manage_py_not_found(self):
        current_dir = '/tmp/bad_project_no_files/Level1/Level2/tests/test_file.py'
        current_line = "        print('This is a testD')\n"
        current_buffer = self.build_buffer_helper()
        self.assertEqual("Are you sure this is a Django project?", sut.get_command_to_run_the_current_class(current_dir, current_line, current_buffer))

    def test_get_command_to_run_the_current_method_with_manage_py_app_name_but_no_env_specified(self):
        current_dir = '/tmp/project_apps_only/Level1/Level2/tests/test_file.py'
        current_line = "        print('This is a testD')\n"
        current_buffer = self.build_buffer_helper()
        self.assertEqual("/tmp/project_apps_only/manage.py test example_app.tests.test_file:Example1.dummy2", sut.get_command_to_run_the_current_method(current_dir, current_line, current_buffer))

    def test_get_command_to_run_the_current_method_with_manage_py_app_name_and_env_specified(self):
        current_dir = '/tmp/project_app_names_and_env/Level1/Level2/tests/test_file.py'
        current_line = "        print('This is a testD')\n"
        current_buffer = self.build_buffer_helper()
        expected_return_value = "/tmp/project_app_names_and_env/manage.py test test example_app.tests.test_file:Example1.dummy2"
        self.assertEqual(expected_return_value, sut.get_command_to_run_the_current_method(current_dir, current_line, current_buffer))

    def test_get_command_to_run_the_current_method_when_config_not_properly_formated(self):
        current_dir = '/tmp/bad_project_no_apps/Level1/Level2/tests/test_file.py'
        current_line = "        print('This is a testD')\n"
        current_buffer = self.build_buffer_helper()
        expected_return_value = ".vim-django file does not exist or is improperly formated. ':help vim-python-test-runner'"
        self.assertEqual(expected_return_value, sut.get_command_to_run_the_current_method(current_dir, current_line, current_buffer))

    def test_get_command_to_run_the_current_method_when_config_not_present(self):
        current_dir = '/tmp/bad_project_no_apps/Level1/Level2/tests/test_file.py'
        current_line = "        print('This is a testD')\n"
        current_buffer = self.build_buffer_helper()
        expected_return_value = ".vim-django file does not exist or is improperly formated. ':help vim-python-test-runner'"
        self.assertEqual(expected_return_value, sut.get_command_to_run_the_current_method(current_dir, current_line, current_buffer))

    def test_get_command_to_run_the_current_method_when_manage_py_not_found(self):
        current_dir = '/tmp/bad_project_no_files/Level1/Level2/tests/test_file.py'
        current_line = "        print('This is a testD')\n"
        current_buffer = self.build_buffer_helper()
        expected_return_value = "Are you sure this is a Django project?"
        self.assertEqual(expected_return_value, sut.get_command_to_run_the_current_method(current_dir, current_line, current_buffer))

    def test_get_command_to_run_the_django_test_for_the_current_file(self):
        current_dir = '/tmp/project_apps_only/Level1/Level2/tests/test_file.py'
        expected_return_value = "/tmp/project_apps_only/manage.py test example_app.tests.test_file"
        command_returned = sut.get_command_to_run_the_current_file(current_dir)
        self.assertEqual(command_returned, expected_return_value)

    def build_buffer_helper(self):
        with open("dummy_test_file.py", "r") as f:
            current_buffer = []
            for line in f.readlines():
                current_buffer.append(line)
        return current_buffer


class RunNestedDjangoTestsInVimTests(unittest.TestCase):

    def setUp(self):
        os.makedirs("/tmp/project_apps_only/Level1/Level2/tests/")
        os.makedirs("/tmp/project_app_names_and_env/Level1/Level2/tests/")
        os.makedirs("/tmp/bad_project_no_files/Level1/Level2/tests/")
        os.makedirs("/tmp/bad_project_no_config_file/Level1/Level2/tests/")
        os.makedirs("/tmp/bad_project_no_apps/Level1/Level2/tests/")
        os.makedirs("/tmp/bad_project_no_path_to_tests/Level1/Level2/tests")

        with open("/tmp/project_apps_only/Level1/.vim-django", "w") as f:
            f.write('{"app_name": "example_app", "path_to_tests": "tests"}')
        with open("/tmp/project_apps_only/manage.py", "w") as f:
            f.write("#Place holder")

        with open("/tmp/project_app_names_and_env/Level1/.vim-django", "w") as f:
            f.write('{"app_name": "example_app", "environment": "test", "path_to_tests": "tests"}')
        with open("/tmp/project_app_names_and_env/manage.py", "w") as f:
            f.write("#Place holder")
        with open("/tmp/bad_project_no_config_file/manage.py", "w") as f:
            f.write("#Place holder")

        with open("/tmp/bad_project_no_apps/Level1/.vim-django", "w") as f:
            f.write('{"bad_field": "example_app"}')
        with open("/tmp/bad_project_no_apps/manage.py", "w") as f:
            f.write("#Place holder")

        with open("/tmp/bad_project_no_path_to_tests/Level1/.vim-django", "w") as f:
            f.write('{"app_name": "example_app"}')
        with open("/tmp/bad_project_no_path_to_tests/manage.py", "w") as f:
            f.write("#Place holder")

    def tearDown(self):
        os.remove("/tmp/project_apps_only/manage.py")
        os.remove("/tmp/project_apps_only/Level1/.vim-django")

        os.remove("/tmp/project_app_names_and_env/Level1/.vim-django")
        os.remove("/tmp/project_app_names_and_env/manage.py")

        os.remove("/tmp/bad_project_no_config_file/manage.py")

        os.remove("/tmp/bad_project_no_apps/Level1/.vim-django")
        os.remove("/tmp/bad_project_no_apps/manage.py")

        os.remove("/tmp/bad_project_no_path_to_tests/Level1/.vim-django")
        os.remove("/tmp/bad_project_no_path_to_tests/manage.py")

        os.removedirs("/tmp/project_apps_only/Level1/Level2/tests/")
        os.removedirs("/tmp/project_app_names_and_env/Level1/Level2/tests/")
        os.removedirs("/tmp/bad_project_no_files/Level1/Level2/tests/")
        os.removedirs("/tmp/bad_project_no_config_file/Level1/Level2/tests/")
        os.removedirs("/tmp/bad_project_no_apps/Level1/Level2/tests/")
        os.removedirs("/tmp/bad_project_no_path_to_tests/Level1/Level2/tests")

    def test_find_vim_django_file(self):
        return_value = sut.find_path_to_file("/tmp/project_apps_only/Level1/Level2/tests", ".vim-django")
        self.assertEqual(return_value, "/tmp/project_apps_only/Level1/.vim-django")
