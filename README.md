vim-python-test-runner.vim
==========
A simple way of running tests for your python files from within VIM.

This plugin was created to allow running Django unit tests that require
database interaction from within Vim. Thus avoiding the need to toggle 
between your vim session and the shell for longer periods of time. It will 
also run your regular python unit tests with nosetests as well when not 
working on a Django project.

INSTALLATION
============

The recommended installation method is vundle <https://github.com/gmarik/vundle>
however installation should also work via pathogen <https://github.com/tpope/vim-pathogen>

REQUIREMENTS
============

You need a VIM version that was compiled with
``+python``, which is typical for most distributions on Linux/Mac. 
You can check this by running ``vim --version | grep +python``
if you get a hit you are in business.

Also if you plan to run unit tests outside of a Django app you will
need to have nose testrunner installed.

Usage
=====

The plugin provides six commands::

    DjangoTestApp
    DjangoTestClass
    DjangoTestMethod
    NosetestFile
    NosetestClass
    NosetestMethod

All arguments can be tab-completed. Ensure that your cursor is within a 
file, class, method as appropriate for the command being called.

For ease of usage you can map the above actions to a shortcut. For example, 
if you wanted leader mappings you could set something like the following in 
your vimrc:

    nnoremap<Leader>da :DjangoTestApp<CR>
    nnoremap<Leader>dc :DjangoTestClass<CR>
    nnoremap<Leader>dm :DjangoTestMethod<CR>
    nnoremap<Leader>nf :NosetestFile<CR>
    nnoremap<Leader>nc :NosetestClass<CR>
    nnoremap<Leader>nm :NosetestMethod<CR>

Required Configuration File for Django Tests
--------------------------------------------
To make use of the plugin for Django projects you will need to create a small 
config file named ``.vim-django`` in your project that defines what application you 
would like to run tests for. Assuming a basic folder structure the config file 
would be saved in the following location if we are testing app2.
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
optionally if you have your project configured for different environments 
you may specify that as well. 
```
{'app_name': 'nameOfMyApp', 'environment': 'OptionalNameOfEnv'}
```

Outside of Django
-----------------
Nothing other than nose is required to use this plugin for tests that are 
outside of a Django application.

