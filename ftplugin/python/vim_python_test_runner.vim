if !has('python')
    finish
endif

function! RunDesiredTests(command_to_run)
python << endPython
import os
import vim
import inspect
from sys import platform as _platform
# Add our python script to the path for importing
for path in vim.eval('&runtimepath').split(','):
    if 'vim-python' in path and "after" not in path:
        sys.path.append(os.path.join(path, 'ftplugin', 'python'))
from vim_python_test_runner import *

def get_proper_command(desired_command):
    current_directory = os.sep.join([dir for dir in vim.current.buffer.name.split(os.sep) if dir])
    current_line_index = vim.current.window.cursor[0]

    if desired_command == "django_app":
        return get_command_to_run_the_current_app(current_directory)
    elif desired_command == "django_file":
        return get_command_to_run_the_current_file(current_directory)
    elif desired_command == "django_class":
        return get_command_to_run_the_current_class(current_directory, current_line_index, vim.current.buffer)
    elif desired_command == "django_method":
        return get_command_to_run_the_current_method(current_directory, current_line_index, vim.current.buffer)
    elif desired_command == "nose_file":
        current_directory = vim.current.buffer.name
        return get_command_to_run_current_file_with_nosetests(current_directory)
    elif desired_command == "nose_class":
        current_directory = vim.current.buffer.name
        return get_command_to_run_current_class_with_nosetests(current_directory, current_line_index, vim.current.buffer)
    elif desired_command == "nose_method":
        current_directory = vim.current.buffer.name
        return get_command_to_run_current_method_with_nosetests(current_directory, current_line_index, vim.current.buffer)

def check_for_errors(command_to_run):
    if ".vim-django does not exist" == command_to_run:
        print(".vim-django file does not exist or is improperly formated. ':help run-django-tests'")
        return False
    elif "Not Django" == command_to_run:
        print("Are you sure this is a Django project?")
        return False
    return True

def run_desired_command(command_to_run):
    if "nose" in vim.eval("a:command_to_run"):
        vim.command(command_to_run)
    elif _platform == 'linux' or _platform == 'linux2':
        vim.command(":!python {0}".format(command_to_run))
    elif _platform == 'darwin':
        vim.command(":!sudo python {0}".format(command_to_run))

command_to_run = get_proper_command(vim.eval("a:command_to_run"))
proceede = check_for_errors(command_to_run)
if proceede:
    run_desired_command(command_to_run)

endPython
endfunction

command! DjangoTestApp call RunDesiredTests("django_app")
command! DjangoTestFile call RunDesiredTests("django_file")
command! DjangoTestClass call RunDesiredTests("django_class")
command! DjangoTestMethod call RunDesiredTests("django_method")
command! NosetestFile call RunDesiredTests("nose_file")
command! NosetestClass call RunDesiredTests("nose_class")
command! NosetestMethod call RunDesiredTests("nose_method")
