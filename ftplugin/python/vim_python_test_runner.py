#!/bin/env python
import os
import re
import json


def get_command_to_run_the_current_app(current_dir):
    path_to_manage = find_path_to_file(current_dir, "manage.py")
    if not path_to_manage:
        return "Not Django"

    app_name = get_app_name(current_dir)
    env_name = get_json_field_from_config_file(current_dir, "environment")

    if app_name and env_name:
        return ("{0} {1} test {2}".format(path_to_manage, env_name, app_name))
    elif app_name:
        return ("{0} test {1}".format(path_to_manage, app_name))
    else:
        return ".vim-django does not exist"


def get_command_to_run_the_current_file(current_dir):
    command_to_current_app = get_command_to_run_the_current_app(current_dir)
    path_to_tests = get_dot_notation_path_to_test(current_dir)
    file_name = get_file_name(current_dir)
    if "Not Django" in command_to_current_app:
        return "Not Django"
    elif ".vim-django does not exist" in command_to_current_app or not path_to_tests:
        return ".vim-django does not exist"
    else:
        return command_to_current_app + "." + path_to_tests + "." + file_name


def get_command_to_run_the_current_class(current_dir, current_line, current_buffer):
    class_name = get_current_class(current_line, current_buffer)
    command_to_current_file = get_command_to_run_the_current_app(current_dir)
    if "Not Django" in command_to_current_file:
        return command_to_current_file
    elif ".vim-django does not exist" in command_to_current_file:
        return ".vim-django does not exist"
    else:
        return get_command_to_run_the_current_file(current_dir) + ":" + class_name


def get_command_to_run_the_current_method(current_dir, current_line, current_buffer):
    method_name = get_current_method(current_line, current_buffer)
    command_to_current_class = get_command_to_run_the_current_class(current_dir, current_line, current_buffer)
    if "Not Django" in command_to_current_class:
        return command_to_current_class
    elif ".vim-django does not exist" in command_to_current_class:
        return ".vim-django does not exist"
    else:
        return command_to_current_class + "." + method_name


def get_command_to_run_current_file_with_nosetests(path_to_current_file):
    return ":!nosetests {0}".format(path_to_current_file)


def get_command_to_run_current_class_with_nosetests(path_to_current_file, current_line, current_buffer):
    run_file = get_command_to_run_current_file_with_nosetests(path_to_current_file)
    current_class = get_current_class(current_line, current_buffer)
    return run_file + ":" + current_class


def get_command_to_run_current_method_with_nosetests(path_to_current_file, current_line, current_buffer):
    run_class = get_command_to_run_current_class_with_nosetests(path_to_current_file, current_line, current_buffer)
    current_method = get_current_method(current_line, current_buffer)
    return run_class + "." + current_method


def find_path_to_file(current_dir, file_to_look_for):
    dir_list = [directory for directory in current_dir.split(os.path.sep) if directory]
    for x in range(len(dir_list) - 1, -1, -1):
        path_to_check = os.path.sep + os.path.sep.join(dir_list[:x])
        if file_to_look_for in os.listdir(path_to_check):
            return path_to_check + os.sep + file_to_look_for
    return False


def get_app_name(current_dir):
    apps = get_json_field_from_config_file(current_dir, "app_name")
    try:
        return [app.lstrip() for app in apps.split(",") if app.lstrip() in current_dir][0]
    except:
        return False
    return False


def get_dot_notation_path_to_test(current_dir):
    app_name = get_app_name(current_dir)
    if app_name:
        path_to_tests = current_dir.split(os.sep + app_name + os.sep)[1]
        return ".".join(path_to_tests.split("/")[:-1])
    return False


def get_file_name(current_dir):
    path_parts = current_dir.split(os.sep)
    return path_parts[-1].split(".")[0]


def get_current_class(current_line_index, current_buffer):
    class_regex = re.compile(r"^class (?P<class_name>.+)\(")
    for line in xrange(current_line_index - 1, -1, -1):
        if class_regex.search(current_buffer[line]) is not None:
            class_name = class_regex.search(current_buffer[line])
            return class_name.group(1)
    return False


def get_current_method(current_line_index, current_buffer):
    class_regex = re.compile(r"^class (?P<class_name>.+)\(")
    method_regex = re.compile(r"def (?P<method_name>.+)\(")
    for line in xrange(current_line_index - 1, -1, -1):
        if class_regex.search(current_buffer[line]) is not None:
            return False
        if method_regex.search(current_buffer[line]) is not None:
            method_name = method_regex.search(current_buffer[line])
            return method_name.group(1)
    return False


def get_json_field_from_config_file(current_dir, field_name):
    try:
        with open(find_path_to_file(current_dir, ".vim-django"), "r") as f:
            json_string = f.read()
        parsed_json = json.loads(json_string)
        return parsed_json[field_name]
    except Exception:
        return False
