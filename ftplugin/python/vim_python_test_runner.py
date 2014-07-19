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
    failfast = get_json_field_from_config_file(current_dir, "failfast")
    failfast = set_flag("failfast", failfast)
    nocapture = get_json_field_from_config_file(current_dir, "nocapture")
    nocapture = set_flag("nocapture", nocapture)
    if app_name and env_name:
        command = "{0} {1} test {2}{3}{4}".format(path_to_manage, env_name, failfast, nocapture, app_name)
        write_test_command_to_cache_file(command)
        return (command)
    elif app_name:
        command = "{0} test {1}{2}{3}".format(path_to_manage, failfast, nocapture, app_name)
        write_test_command_to_cache_file(command)
        return (command)
    else:
        return ".vim-django does not exist"


def command(command_to_run, cmd, path=True):
    if "Not Django" in command_to_run:
        return "Not Django"
    elif ".vim-django does not exist" in command_to_run or not path:
        return ".vim-django does not exist"
    else:
        command = cmd
        write_test_command_to_cache_file(command)
        return command


def get_command_to_run_the_current_file(current_dir):
    command_to_current_app = get_command_to_run_the_current_app(current_dir)
    path_to_tests = get_dot_notation_path_to_test(current_dir)
    file_name = get_file_name(current_dir)
    cmd = "{}.{}.{}".format(command_to_current_app, path_to_tests, file_name)
    return command(command_to_current_app, cmd, path_to_tests)


def get_command_to_run_the_current_class(current_dir, current_line, current_buffer):
    class_name = get_current_class(current_line, current_buffer)
    command_to_current_file = get_command_to_run_the_current_app(current_dir)
    cmd = "{}:{}".format(get_command_to_run_the_current_file(current_dir), class_name)
    return command(command_to_current_file, cmd)


def get_command_to_run_the_current_method(current_dir, current_line, current_buffer):
    method_name = get_current_method(current_line, current_buffer)
    command_to_current_class = get_command_to_run_the_current_class(current_dir, current_line, current_buffer)
    cmd = "{}.{}".format(command_to_current_class, method_name)
    return command(command_to_current_class, cmd)


def get_command_to_run_current_file_with_nosetests(path_to_current_file):
    command = ":!nosetests {0}".format(path_to_current_file)
    write_test_command_to_cache_file(command)
    return command


def get_command_to_run_current_class_with_nosetests(path_to_current_file, current_line, current_buffer):
    run_file = get_command_to_run_current_file_with_nosetests(path_to_current_file)
    current_class = get_current_class(current_line, current_buffer)
    command = run_file + ":" + current_class
    write_test_command_to_cache_file(command)
    return command


def get_command_to_run_current_method_with_nosetests(path_to_current_file, current_line, current_buffer):
    run_class = get_command_to_run_current_class_with_nosetests(path_to_current_file, current_line, current_buffer)
    current_method = get_current_method(current_line, current_buffer)
    command = run_class + "." + current_method
    write_test_command_to_cache_file(command)
    return command


def get_command_to_rerun_last_tests():
    with open("/tmp/vim_python_test_runner_cache", "r") as f:
        return f.read()


def write_test_command_to_cache_file(command):
    with open("/tmp/vim_python_test_runner_cache", "w") as f:
        f.write(command)


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


def set_flag(flag, value):
    if value:
        return "--{0} ".format(flag)
    else:
        return ""
