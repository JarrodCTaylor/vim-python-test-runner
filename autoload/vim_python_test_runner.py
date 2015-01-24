#!/bin/env python
import os
import re
import json


class NotDjango(Exception):
    def __str__(self):
                return "Are you sure this is a Django project?"


class NoVimDjango(Exception):
    def __str__(self):
                return ".vim-django file does not exist or is improperly formated. ':help vim-python-test-runner.txt'"


def get_command_to_run_the_current_app(current_dir):
    path_to_manage = find_path_to_file(current_dir, "manage.py", NotDjango)
    app_name = get_app_name(current_dir)
    env_name = get_env_name_if_exists(current_dir)
    flags = get_flags(current_dir)
    command = "{0}{1}test {2}{3}".format(path_to_manage, env_name, flags, app_name)
    write_test_command_to_cache_file(command)
    return (command)


def get_command_to_run_the_current_file(current_dir):
    command_to_current_app = get_command_to_run_the_current_app(current_dir)
    path_to_tests = get_dot_notation_path_to_test(current_dir)
    file_name = get_file_name(current_dir)
    cmd = "{}.{}.{}".format(command_to_current_app, path_to_tests, file_name)
    write_test_command_to_cache_file(cmd)
    return cmd


def get_command_to_run_the_current_class(current_dir, current_line, current_buffer):
    class_name = get_current_method_and_class(current_line, current_buffer)[0]
    cmd = "{}:{}".format(get_command_to_run_the_current_file(current_dir), class_name)
    write_test_command_to_cache_file(cmd)
    return cmd


def get_command_to_run_the_current_method(current_dir, current_line, current_buffer):
    method_name = get_current_method_and_class(current_line, current_buffer)[1]
    command_to_current_class = get_command_to_run_the_current_class(current_dir, current_line, current_buffer)
    cmd = "{}.{}".format(command_to_current_class, method_name)
    write_test_command_to_cache_file(cmd)
    return cmd


def get_command_to_run_current_file_with_nosetests(path_to_current_file):
    command = ":!nosetests {0}".format(path_to_current_file)
    write_test_command_to_cache_file(command)
    return command


def get_command_to_run_current_class_with_nosetests(path_to_current_file, current_line, current_buffer):
    run_file = get_command_to_run_current_file_with_nosetests(path_to_current_file)
    current_class = get_current_method_and_class(current_line, current_buffer)[0]
    command = run_file + ":" + current_class
    write_test_command_to_cache_file(command)
    return command


def get_command_to_run_current_method_with_nosetests(path_to_current_file, current_line, current_buffer):
    run_class = get_command_to_run_current_class_with_nosetests(path_to_current_file, current_line, current_buffer)
    current_method = get_current_method_and_class(current_line, current_buffer)[1]
    command = run_class + "." + current_method
    write_test_command_to_cache_file(command)
    return command


def get_command_to_run_current_base_method_with_nosetests(path_to_current_file, current_line, current_buffer):
    run_file = get_command_to_run_current_file_with_nosetests(path_to_current_file)
    current_method = get_current_method_and_class(current_line, current_buffer)[1]
    command = run_file + ":" + current_method
    write_test_command_to_cache_file(command)
    return command


def get_command_to_rerun_last_tests():
    with open("/tmp/vim_python_test_runner_cache", "r") as f:
        return f.read()


def write_test_command_to_cache_file(command):
    with open("/tmp/vim_python_test_runner_cache", "w") as f:
        f.write(command)


def find_path_to_file(current_dir, file_to_look_for, raise_exception=False):
    dir_list = [directory for directory in current_dir.split(os.path.sep) if directory]
    for x in range(len(dir_list) - 1, -1, -1):
        path_to_check = os.path.sep + os.path.sep.join(dir_list[:x])
        if file_to_look_for in os.listdir(path_to_check):
            return path_to_check + os.sep + file_to_look_for
    raise raise_exception


def get_app_name(current_dir):
    apps = get_json_field_from_config_file(current_dir, "app_name")
    try:
        return [app.lstrip() for app in apps.split(",") if app.lstrip() in current_dir][0]
    except:
        raise NoVimDjango


def get_dot_notation_path_to_test(current_dir):
    app_name = get_app_name(current_dir)
    if app_name:
        path_to_tests = current_dir.split(os.sep + app_name + os.sep)[1]
        return ".".join(path_to_tests.split("/")[:-1])
    return False


def get_file_name(current_dir):
    path_parts = current_dir.split(os.sep)
    return path_parts[-1].split(".")[0]


def get_current_method_and_class(current_line_index, current_buffer):
    class_regex, class_name = re.compile(r"^class (?P<class_name>.+)\("), False
    method_regex, method_name = re.compile(r"def (?P<method_name>.+)\("), False
    for line in xrange(current_line_index - 1, -1, -1):
        if class_regex.search(current_buffer[line]) is not None and not class_name:
            class_name = class_regex.search(current_buffer[line])
            class_name = class_name.group(1)
        if method_regex.search(current_buffer[line]) is not None and not method_name and not class_name:
            method_name = method_regex.search(current_buffer[line])
            method_name = method_name.group(1)
    return (class_name, method_name)


def get_json_field_from_config_file(current_dir, field_name):
    try:
        with open(find_path_to_file(current_dir, ".vim-django"), "r") as f:
            json_string = f.read()
        parsed_json = json.loads(json_string)
        return parsed_json[field_name]
    except Exception:
        return False


def get_flags(current_dir):
    formatted_flags = ""
    user_flags = get_json_field_from_config_file(current_dir, "flags") or []
    for flag in user_flags:
        formatted_flags += "--{} ".format(flag)
    return formatted_flags


def get_env_name_if_exists(current_dir):
    env_name = get_json_field_from_config_file(current_dir, "environment")
    if env_name:
        return " {} ".format(env_name)
    return " "
