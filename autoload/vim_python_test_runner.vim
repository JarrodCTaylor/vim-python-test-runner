set makeprg=cat\ /tmp/test_results.txt
set efm+=%-G%.%#lib/python%.%#/site-package%.%#,%C\ %.%#,%A\ \ File\ \"%f\"\\,\ line\ %l%.%#,%Z%[%^\ ]%\\@=%m

if !has('python3')
    finish
endif

" -----------------------------
" Add our directory to the path
" -----------------------------
python3 import sys
python3 import vim
python3 sys.path.append(vim.eval('expand("<sfile>:h")'))

function! vim_python_test_runner#RunDesiredTests(command_to_run)
python3 << EndPython
import os
from vim_python_test_runner import *

def get_proper_command(desired_command, current_directory):
    current_line_index = vim.current.window.cursor[0]
    FUNCTIONS = {
        "django_app": lambda: get_command_to_run_the_current_app(current_directory),
        "django_file": lambda: get_command_to_run_the_current_file(current_directory),
        "django_class": lambda: get_command_to_run_the_current_class(current_directory, current_line_index, vim.current.buffer),
        "django_method": lambda: get_command_to_run_the_current_method(current_directory, current_line_index, vim.current.buffer),
        "nose_file": lambda: get_command_to_run_current_file_with_nosetests(vim.current.buffer.name),
        "nose_class": lambda: get_command_to_run_current_class_with_nosetests(vim.current.buffer.name, current_line_index, vim.current.buffer),
        "nose_method": lambda: get_command_to_run_current_method_with_nosetests(vim.current.buffer.name, current_line_index, vim.current.buffer),
        "nose_base_method": lambda: get_command_to_run_current_base_method_with_nosetests(vim.current.buffer.name, current_line_index, vim.current.buffer),
        "pytest_file": lambda: get_command_to_run_current_file_with_pytests(vim.current.buffer.name),
        "pytest_class": lambda: get_command_to_run_current_class_with_pytests(vim.current.buffer.name, current_line_index, vim.current.buffer),
        "pytest_method": lambda: get_command_to_run_current_method_with_pytests(vim.current.buffer.name, current_line_index, vim.current.buffer),
        "pytest_base_method": lambda: get_command_to_run_current_base_method_with_pytests(vim.current.buffer.name, current_line_index, vim.current.buffer),
        "rerun": lambda: get_command_to_rerun_last_tests()
    }
    return FUNCTIONS[desired_command]()

def run_desired_command_for_os(command_to_run):
    if "nose" in vim.eval("a:command_to_run") or "nose" in command_to_run:
        # Run nosetests for Python.
        vim.command("{0} 2>&1 | tee /tmp/test_results.txt".format(command_to_run))
    elif "pytest" in vim.eval("a:command_to_run") or "pytest" in command_to_run:
        # Run pytests for Python.
        vim.command("{0} 2>&1 | tee /tmp/test_results.txt".format(command_to_run))
    else:
        # Run manage.py test for Django.
        vim.command(":!python {0} 2>&1 | tee /tmp/test_results.txt".format(command_to_run))

def main():
    current_directory = os.sep.join([dir for dir in vim.current.buffer.name.split(os.sep) if dir])
    try:
        command_to_run = get_proper_command(vim.eval("a:command_to_run"), current_directory)
    except Exception as e:
        print(e)
    else:
        run_desired_command_for_os(command_to_run)
        vim.command('silent make! | cw')

vim.command('wall')
main()
EndPython
endfunction

