#NOTE
Currently the plugin appears to work with Linux however I cannot get it to function 
on a Mac. I am working to resole this issue and will remove this notice when the 
plugin is functioning properly on OS X.

vim-python-test-runner.vim
==========
A simple way of running tests for your python files from within VIM.

This plugin was created to allow running Django tests with django-nose that 
require database interaction from within Vim. Thus avoiding the need to toggle 
between your vim session and the shell for longer periods of time. It will 
also run your regular python unit tests with nosetests as well when not 
working on a Django project.

INSTALLATION
============

The recommended installation method is vundle <https://github.com/gmarik/vundle>
however installation should also work via pathogen <https://github.com/tpope/vim-pathogen>

REQUIREMENTS
============

You need a VIM version that was compiled with python support, which is typical 
for most distributions on Linux/Mac.  You can check this by running 
``vim --version | grep +python``
if you get a hit you are in business.

Tests are ran with either django-nose or nosetest so these will need to be 
pip installed in order for the plugin to function properly. 

Usage
=====

The plugin provides seven commands:

    DjangoTestApp
    DjangoTestFile
    DjangoTestClass
    DjangoTestMethod
    NosetestFile
    NosetestClass
    NosetestMethod

All arguments can be tab-completed. Ensure that your cursor is within a 
file, class or method as appropriate for the command being called.

For ease of usage you can map the above actions to a shortcut. For example, 
if you wanted leader mappings you could set something like the following in 
your vimrc:

    nnoremap<Leader>da :DjangoTestApp<CR>
    nnoremap<Leader>df :DjangoTestFile<CR>
    nnoremap<Leader>dc :DjangoTestClass<CR>
    nnoremap<Leader>dm :DjangoTestMethod<CR>
    nnoremap<Leader>nf :NosetestFile<CR>
    nnoremap<Leader>nc :NosetestClass<CR>
    nnoremap<Leader>nm :NosetestMethod<CR>

Required Configuration File for Django Tests
--------------------------------------------
To make use of the plugin for Django projects you will need to create a small 
config file named ``.vim-django`` in your project that defines some information
about the app you would like to run tests for. Assuming a basic folder 
structure the config file would be saved in the following location if we are 
testing app2.
```
── Project Root
   ├── manage.py
   ├── app1
   └── app2
       ├── .vim-django
       └── tests
          ├── tests1.py
          └── tests2.py
```

Config file contents
------------------
The contents of the file are minimal. You must define an app_name and 
a dot separated path to the test folder from within your app. Optionally if you
have your project configured for different environments you may specify that also 

Using the example above we would set the app name to "app2" and the path_to_tests
will be equal to "tests" since we are using the basic common folder structure of 
having our tests directory saved in the root of our app. If it is nested you would
need something like "parent.tests". The environment field is optional. If you don't
know what it should be then you don't need to use it. 

```
{"app_name": "app2",
 "path_to_tests": "tests",
 "environment": "OptionalNameOfEnv"}
```
*NOTE* be sure to use double quotes in the config file as it is parsed as json

Outside of Django
-----------------
Nothing other than nose is required to use this plugin for tests that are 
outside of a Django application.

