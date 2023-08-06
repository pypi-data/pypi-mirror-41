atelParser
==========

[![Documentation Status](https://readthedocs.org/projects/atelParser/badge/)](http://atelParser.readthedocs.io/en/latest/?badge)

[![Coverage Status](https://cdn.rawgit.com/thespacedoctor/atelParser/master/coverage.svg)](https://cdn.rawgit.com/thespacedoctor/atelParser/master/htmlcov/index.html)

*A python package and command-line tools for Download Astronomers’ Telegrams and parse them to find transient names and coordinates*.

Command-Line Usage
==================

``` sourceCode
Documentation for atelParser can be found here: http://atelParser.readthedocs.org/en/stable

Usage:
    atel init
    atel count [-s <pathToSettingsFile>]
    atel download [-s <pathToSettingsFile>]
    atel [-r] parse [-s <pathToSettingsFile>]

Options:
    init                  setup the atelParser settings file for the first time
    count                 report the total number of atels reported so far
    download              download new and remaining ATel to the atel-directory stated in settings file
    parse                 add the new ATel contents to database and parse for names and coordinates


    -h, --help            show this help message
    -v, --version         show version
    -s, --settings        the settings file
    -r, --reparse         re-parse all ATel for names and coordinates
```

Installation
============

The easiest way to install atelParser is to use `pip`:

``` sourceCode
pip install atelParser
```

Or you can clone the [github repo](https://github.com/thespacedoctor/atelParser) and install from a local version of the code:

``` sourceCode
git clone git@github.com:thespacedoctor/atelParser.git
cd atelParser
python setup.py install
```

To upgrade to the latest version of atelParser use the command:

``` sourceCode
pip install atelParser --upgrade
```

Documentation
=============

Documentation for atelParser is hosted by [Read the Docs](http://atelParser.readthedocs.org/en/stable/) (last [stable version](http://atelParser.readthedocs.org/en/stable/) and [latest version](http://atelParser.readthedocs.org/en/latest/)).

Command-Line Tutorial
=====================

Before you begin using atelParser you will need to populate some custom settings within the atelParser settings file.

To setup the default settings file at `~/.config/atelParser/atelParser.yaml` run the command:

``` sourceCode
> atel init
```

This should create and open the settings file; follow the instructions in the file to populate the missing settings values (usually given an `XXX` placeholder).

Report the Latest ATel Count
----------------------------

To report the latest ATel count run the command:

``` sourceCode
> atel count
11994 ATels have been reported as of 2018/08/29 13:31:02s
```

Downloading all new ATels
-------------------------

Once you have an `atel-directory` parameter added to your settings file you can download all missign ATels to this directory.

``` sourceCode
atel-directory: /home/user/atel-archive/html 
```

To kick off the download run the command:

``` sourceCode
atel download
```

This will download the HTML pages for all new/missing ATels to your `atel-directory`.

Parsing Names and Coordiantes from ATels
----------------------------------------

To read new contents from the `atel_fullcontent` table from the database and parse out all transient names and coordinates into two separate database tables (`atel_names` & `atel_coordinates`), run the command:

``` sourceCode
atel parse
```

Or to re-parse *ALL* content from the `atel_fullcontent` table run:

``` sourceCode
atel -r parse
```
