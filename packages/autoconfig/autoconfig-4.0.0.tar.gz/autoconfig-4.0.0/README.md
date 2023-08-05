
# autoconfig

- [Overview](#overview)
- [Simple Example](#simple-example)
- [Signature](#signature)
- [Environment Variables](#environment-variables)
    - [System Path](#system-path)
    - [relpath](#relpath)
- [Locating The Config File](#locating-the-config-file)
- [Multiple Config Files](#multiple-config-files)


## Overview

A module to easily configure a Python program from a configuration file:

    import autoconfig
    autoconfig.init()

With these simple lines before other imports, you can:

- add environment variables
- add directories to the Python module search path

I decided to create this for a project that had lots of programs that all needed the same
configuration and used the same set of shared libraries in the same repository.  (That is,
directories in the same repository, not external modules.)

The [12 Factor App](http://12factor.net) recommends keeping configuration in environment
variables, but unless you are using [Heroku](http://heroku.com) that usually means storing them
in a file and loading them into the environment.  Instead of requiring another utility to
configure the environment and then launch my Python apps, I decided to make this library which
does the same thing from within the app.

## Simple Example

If no parameters are passed, the library searches for a file named ".config", starting from the
current directory (os.getcwd) and searching upwards.

The file uses the INI file format read by Python's
[ConfigParser](https://docs.python.org/3.6/library/configparser.html):

    [env]
    DATABASE_URL=postgresql://localhost/test?client_encoding=utf8
    PYTHONPATH=lib:/var/helpers

The two entries from the [env] section, DATABASE_URL and PYTHONPATH, are put into
[os.environ](https://docs.python.org/3.6/library/os.html#os.environ), making them easily
available to the rest of your application.

The PYTHONPATH entry is also prepended to
[sys.path](https://docs.python.org/3.6/library/sys.html?highlight=sys.path#sys.path).  Any
entries that are relative, such as "lib" in the example, are first made relative to the
location of the configuration file.


## Signature

The `init` function supports customization through a few parameters:

    def init(filename='.config', searchfrom=None, env='env', relpath=None, otherfiles=None) --> None


## Environment Variables

The `env` parameter is the name of a section or a list of section names in the file.  All items
in those sections are copied into [os.environ](https://docs.python.org/3.6/library/os.html#os.environ).

    autoconfig.init()                      # copy from env, which is the default
    autoconfig.init(env='other')           # copy from other
    autoconfig.init(env=['env', 'other'])  # copy from env and other

If your OS supports putenv, this will modify the program's environment and that received by
subprocesses when they are created.

To delete an environment variable that may already exist, use the variable name with no value.
In this example, the EDITOR environment variable is removed from `os.environ`.

    [env]
    EDITOR


### System Path

All PYTHONPATH items in any of the sections copied to environment variables are also prepended
to the `sys.path` to emulate Python's handling of PYTHONPATH.

Each entry is examined and any that are not absolute paths are made relative to the directory
the configuration file is in.

    [env]
    PYTHONPATH = lib:/var/project/libs


### relpath

Additionally, paths relative to the module that called init can be added to the Python path
using the `relpath` parameter.  This is useful for "monolithic repositories" that contain
multiple projects.  Usually major projects and shared libraries are at the top level, but you
may want private packages under each projects' directory.  Each project with private package
directories can pass them to init.

For example, a project with this layout:

    /usr/local/prj
     +- .config
     +- deploy       <-- project root
        +- project1
        |  +- project1.py
        +- project2
        |  +- project2.py
        |  +- privatelib
        |     +- __init__.py
        +- lib
           +- sharedlibrary
              +- __init__.py


With this kind of repository, you may deploy the entire project and put the .config in the
directory *above* the deployment directory.  This ensures the .config file is not checked in
and is not disturbed when code is redeployed.

To allow both project1 and project2 to automatically import packages from the `lib`
directory, your .config file would include:

    [env]
    PYTHONPATH = deploy/lib

Remember that relative paths are relative to the directory of the configuration file,
`/usr/local/prj` in this case, which is why the `deploy` directory must be included in this
example.

Additionally, if you wanted project2 to be able to import from `privatelib`, you could use
this in project2.py:

    autoconfig.init(relpath='.')

In addition to any PYTHONPATH entries defined in [env], this adds `/usr/local/prj/project2` to
the system path, which is '.' relative to project2.py.

## Locating The Config File

The default behavior is to look for a file named ".config", starting in the [current working
directory](https://docs.python.org/3.6/library/os.html#os.getcwd) and searching upwards.  If a
file is not found, a FileNotFound exception is raised.

The `init` function accepts two keywords to customize this:

- filename

  Pass just a filename, such as "project.ini" to search for a different filename.

  Pass an absolute path name, such as "/etc/project.ini", to disable searching and use the
  filename as given.

- searchfrom

  An optional directory to begin the search from.  If not provided, the default is the current
  working directory as provided by `os.getcwd()`.

  To simplify configuration, a path to a file can also be passed and the search will begin in
  the same directory as the file.  This is particularly handy for starting a search from the
  directory where the calling module is located:

      autoconfig.init(searchfrom=__file__)

  This parameter is ignored if `filename` is an absolute path since no search is performed.

## Multiple Config Files

The `otherfiles` parameter can be a filename or a list of filenames that should also be read.
The environment sections, "[env]" and those specified by the `env` parameter, are added to the
environment and the Python path is updated if a PYTHONPATH entry is found.

Like the main config file, each of these can be a fully qualified path or will be searched for
individually.  They do not all have to be in the same path.  (This is useful if you have a
config file outside of your project for machine specific settings and a config file in your
project.)
