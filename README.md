# vim-python-test-runner.vim

A simple way of running tests for your python files from within VIM.

This plugin was created to allow running Django tests with django-nose that
require database interaction from within Vim. Thus avoiding the need to toggle
between your vim session and the shell for longer periods of time. It will
also run your regular python unit tests with nosetests as well when not
working on a Django project.

## Demo
![django_test_run](https://f.cloud.github.com/assets/4416952/2181329/c3107922-974b-11e3-88a8-c40f27061658.gif)

## Installation

Use your plugin manager of choice.

- [Pathogen](https://github.com/tpope/vim-pathogen)
  - `git clone https://github.com/JarrodCTaylor/vim-python-test-runner ~/.vim/bundle/vim-python-test-runner`
- [Vundle](https://github.com/gmarik/vundle)
  - Add `Plugin 'JarrodCTaylor/vim-python-test-runner'` to .vimrc
  - Run `:PluginInstall`
- [NeoBundle](https://github.com/Shougo/neobundle.vim)
  - Add `NeoBundle 'https://github.com/JarrodCTaylor/vim-python-test-runner'` to .vimrc
  - Run `:NeoBundleInstall`
- [vim-plug](https://github.com/junegunn/vim-plug)
  - Add `Plug 'https://github.com/JarrodCTaylor/vim-python-test-runner'` to .vimrc
  - Run `:PlugInstall`

## Requirements

You need a VIM version that was compiled with python support, which is typical
for most distributions on Linux/Mac.  You can check this by running
``vim --version | grep +python``
if you get a hit you are in business.

Tests are ran with either django-nose or nosetest so these will need to be
pip installed in order for the plugin to function properly.

## Usage

The plugin provides eight commands:

```
    DjangoTestApp
    DjangoTestFile
    DjangoTestClass
    DjangoTestMethod
    NosetestFile
    NosetestClass
    NosetestMethod
    RerunLastTests
```

All arguments can be tab-completed. Ensure that your cursor is within a
file, class or method as appropriate for the command being called.

For ease of usage you can map the above actions to a shortcut. For example,
if you wanted leader mappings you could set something like the following in
your vimrc:

```
    nnoremap<Leader>da :DjangoTestApp<CR>
    nnoremap<Leader>df :DjangoTestFile<CR>
    nnoremap<Leader>dc :DjangoTestClass<CR>
    nnoremap<Leader>dm :DjangoTestMethod<CR>
    nnoremap<Leader>nf :NosetestFile<CR>
    nnoremap<Leader>nc :NosetestClass<CR>
    nnoremap<Leader>nm :NosetestMethod<CR>
    nnoremap<Leader>rr :RerunLastTests<CR>
```

### Quickfix Results

Your tests results will be available in the quickfix window after they finish
running and you return to your Vim buffer. Open quickfix with `:copen` and
you can jump to failing tests by placing your cursor on the desired test and
pressing enter.

### NOTE to OS X users

The django commands need to be ran from vim with sudo on OS X so the first
time you run one of the Django test commands you will be asked by the shell
for your password. You should only have to enter it once then you will be able
to run subsequent commands in that buffer without reentering your password.

### Required Configuration File for Django Tests

To make use of the plugin for Django projects you will need to create a small
config file named ``.vim-django`` in the root of your project that defines some
information about the apps you would like to run tests for. Assuming a basic
folder structure the config file would be saved in the following location.
```
── Project Root
   ├── .vim-django
   ├── manage.py
   ├── app1
   │   └── tests
   │       └── testsa1.py
   └── app2
       └── tests
           ├── testsb1.py
           └── testsb2.py
```

### Config file contents

#### Required fields

The only required field is a list of the app names that you will be running
tests for.
`"app_name": "app1, app2"`

#### Optional fields

Optional fields that can be set in the vim-django config file are as follows:
- `environment`: If you have modifyed your manage.py file to accept an environment argument
                 then you may use the environment flag to specify which one to run tests for.
                 Example `"environment": "dev"` If you haven't modifyed your manage.py file
                 then you don't need to use this.

- `failfast`:    Enable the django-nose builtin failfast option by specifying
                 failfast to be true. Example `"failfast": true`

- `nocapture`:   Enable the django-nose builtin nocapture option by specifiying
                 nocapture to be true. Example `"nocapture": true`

#### vim-django config file example

Using the example project above we would set the app name to "app1, app2"
The environment field is optional.  We are also saying that we want the test to use
the fail fast option.

```
{"app_name": "app1, app2",
 "environment": "OptionalNameOfEnv",
 "failfast": true}
```
*NOTE* be sure to use double quotes in the config file as it is parsed as json

### Outside of Django

Nothing other than nose is required to use this plugin for tests that are
outside of a Django application.
