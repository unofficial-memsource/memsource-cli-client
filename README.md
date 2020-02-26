# Unofficial Memsource CLI client

![GitHub](https://img.shields.io/github/license/unofficial-memsource/memsource-cli-client)
[![Coverage Status](https://coveralls.io/repos/github/unofficial-memsource/memsource-cli-client/badge.svg?branch=master)](https://coveralls.io/github/unofficial-memsource/memsource-cli-client?branch=master)
[![Build Status](https://travis-ci.com/unofficial-memsource/memsource-cli-client.svg?branch=master)](https://travis-ci.com/unofficial-memsource/memsource-cli-client)
[![PyPI version](https://badge.fury.io/py/memsource-cli.svg)](https://badge.fury.io/py/memsource-cli)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/unofficial-memsource/memsource-cli-client)
<a href="https://t.me/Unofficial_MemsourceCLI"><img src="https://img.shields.io/badge/Telegram-Unofficial Memsource CLI Telegram Group-blue?logo=telegram" alt="Unofficial Memsource CLI Telegram Group"></a>
[![Google group : Unofficial Memsource CLI Forum](https://img.shields.io/badge/Google%20Group-Unofficial%20Memsource%20CLI%20Forum-blue.svg)](https://groups.google.com/forum/#!forum/unofficial-memsource-cli)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=unofficial-memsource_memsource-cli-client&metric=alert_status)](https://sonarcloud.io/dashboard?id=unofficial-memsource_memsource-cli-client)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ddaee7e9ca2f429cb2474cdf441ef166)](https://www.codacy.com/manual/zerodayz/memsource-cli-client?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=unofficial-memsource/memsource-cli-client&amp;utm_campaign=Badge_Grade)

<img src="docs/Cloudy_shell.png" border=0 align="right">

**Table of contents**
<!-- TOC depthFrom:1 insertAnchor:true orderedList:true -->

- [Introduction](#introduction)
- [Releases](#releases)
- [Highlights](#highlights)
- [What's new](#whatsnew)
- [How does it looks like?](#how-does-it-looks-like)
- [Collaborate](#collaborate)
- [Usage](#usage)
- [Getting Started](#getting-started)
- [Install from PyPI](#pip-install)
- [Install from Github](#github-install)
- [Configuration](#configuration)
- [Contact us!](#contact-us)

<!-- /TOC -->


<a id="markdown-introduction" name="introduction"></a>
## Introduction

Memsource CLI is a framework to help with automation of Memsource related tasks. This empowers you to automate repetitive tasks such as project, job creation, analysis runs and others. The framework is cabable to talk to Memsource API using REST client and show you the results of the execution on the screen.

Please if you have any idea on any improvements please do not hesitate to open an issue.

<a id="markdown-releases" name="releases"></a>
## Releases
- For the latest and greatest bits, please follow guide [Install from Github](#github-install)
- For latest released version, please follow guide [Install from PyPI](#pip-install)

<a id="markdown-highlights" name="highlights"></a>
## Highlights
- Extensions are written in Python
- Allows you to use formatter `-f` to choose one of many different formats: csv,json,table,value,yaml
- You can sort by any individual columns or multiple columns using `--sort-column`
- Specify the columns that you are interested in using `-c`

Framework will download additional packages:

- cliff
- certifi>=2017.4.17
- python-dateutil>=2.1
- six>=1.10
- urllib3>=1.23

<a id="markdown-whatsnew" name="whatsnew"></a>
## What's new

Version 0.3.3

Fixed #20 [BUG] memsource job create --debug displays empty output  
Fixed #23 [BUG] memsource job download didn't display help  

Version 0.3.2

[0.3.2] Fixed user.py syntax error for python2

Version 0.3.1

Fixed #19 [BUG] List users  
Fixed #12 [BUG] Assign jobs to poviders  
Fixed #15 [BUG] 'charmap' error on bilingual download  
[0.3.1] Add new command 'memsource use list'  
[0.3.1] Add new command 'memsource job edit'  
[0.3.1] memsource job download can work on multiple job_uids  
[0.3.1] force directory creation with --output-dir on job download  
[0.3.1] Add Memsource custom base url

Added new features such as
- [Job edit](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Jobs#job-edit)
- [User list](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-User#user-list)
- [Job file download (multiple job_uids)](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Jobs#job-download-multiple-job_uids)
- [Job file download (all job_uids within project)](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Jobs#job-download-all-job_uids-within-project)

Option to use custom URL:

````
  --ms-auth-url <auth-url>
                        Authentication URL (Env: MEMSOURCE_URL)
````
or add to your `memsourcerc` file:
````
export MEMSOURCE_URL="https://cloud.memsource.com/web"
````

Version 0.3

[0.3] Adding feature project template list  
[0.3] Move memsource `project template create` to `project create --template-id`  

- [Template list](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Template#template-list)  


Version 0.2.10

[0.2.10] Adding feature template show  

Added new features such as

- [Template show](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Template#template-show)


Version 0.2.9

[0.2.9] Adding feature job translations delete all  
[0.2.9] Job download renamed  
[0.2.9] Add Translation pre-translate option  
[0.2.9] Customized output directory for file downloads  
[0.2.9] Fix to datetime JSON serialization  
[0.2.9] Minor fix: invalid JSON in references in memsource project list  

Added features such as

- [Job Translation pre-translate](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Translation)
- [Job Translations delete](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Jobs#job-translations-delete)

Version 0.2.8

Fixed #6 [BUG] A CLI returns invalid JSON with single-quotes bug low triaged

Version 0.2.6 contains features such as:

- [Job file download (bilingual MXLF)](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Jobs#job-download-bilingual-mxlf)
- [Job file download (bilingual XLIFF)](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Jobs#job-download-bilingual-xliff)
- [Job file download (bilingual DOCX)](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Jobs#job-download-bilingual-docx)
- [Job file download (target)](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Jobs#job-download-target)
- [Job file download (original)](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Jobs#job-download-original)

Version 0.2.5 contains features such as:

- [Create analysis](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Analysis#analyse-create)
- [Delete analysis](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Analysis#analyse-delete)
- [Create analyses by languages](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Analysis#analyse-language-create)
- [List analyses by project](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Analysis#analyse-project-list)
- [Get Analysis](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Analysis#analyse-show)
- [Login](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Auth#login)
- [Who Am I](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Auth#whoami)
- [Creates job in project](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Jobs#job-create)
- [Delete job](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Jobs#job-delete)
- [List jobs in project](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Jobs#job-list)
- [Get job](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Jobs#job-show)
- [Create new project](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Project#project-create)
- [Deletes a project](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Project#project-delete)
- [List projects](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Project#project-list)
- [Get project](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Project#project-show)
- [Create new project from template](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Project#project-template-create)
- [Create user](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-User#user-create)
- [Get user](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-User#user-get)

For more information see [CHANGELOG.md](CHANGELOG.md)
<a id="markdown-how-does-it-looks-like" name="how-does-it-looks-like"></a>
## How does it looks like?
Check how does it look in an execution at:
[![asciicast](https://asciinema.org/a/270610.png)](https://asciinema.org/a/270610)

<a id="markdown-collaborate" name="collaborate"></a>
## Collaborate

- Open issues/feature requests, etc at <https://github.com/unofficial-memsource/memsource-cli-client/issues>


<a id="markdown-usage" name="usage"></a>
## Usage

```
$ memsource --help
usage: memsource [--version] [-v | -q] [--log-file LOG_FILE] [-h] [--debug]
                 [--ms-username <auth-username>]
                 [--ms-password <auth-password>] [--ms-token <auth-token>]
                 [--ms-auth-url <auth-url>]

Unofficial Memsource CLI client

optional arguments:
  --version             show program's version number and exit
  -v, --verbose         Increase verbosity of output. Can be repeated.
  -q, --quiet           Suppress output except warnings and errors.
  --log-file LOG_FILE   Specify a file to log output. Disabled by default.
  -h, --help            Show help message and exit.
  --debug               Show tracebacks on errors.
  --ms-username <auth-username>
                        Authentication username (Env: MEMSOURCE_USERNAME)
  --ms-password <auth-password>
                        Authentication password (Env: MEMSOURCE_PASSWORD)
  --ms-token <auth-token>
                        Authentication token (Env: MEMSOURCE_TOKEN)
  --ms-auth-url <auth-url>
                        Authentication URL (Env: MEMSOURCE_URL)

Commands:
  analyse create  Create analysis
  analyse delete  Delete analysis
  analyse language create  Create analyses by languages
  analyse project list  List analyses by project
  analyse show   Get Analysis
  auth login     Login
  auth whoami    Who am I
  complete       print bash completion command (cliff)
  help           print detailed help for another command (cliff)
  job create     Creates job in project
  job delete     Delete jobs
  job download   Download job file
  job edit       Edit job
  job list       List jobs in project
  job show       Get job
  job translations delete  Delete translations
  project create  Create new project
  project delete  Deletes a project
  project list   List projects
  project show   Get project
  template list  List templates
  template show  Show template
  translation pre-translate  Pre-translate job
  user create    Create user
  user get       Get user
  user list      List users

```

<a id="markdown-getting-started" name="getting-started"></a>
## Getting Started
Requirements for python2 environments:
- package `python-virtualenv`

<a id="markdown-pip-install" name="pip-install"></a>
### Install from PyPI

```
DIRECTORY="${HOME}/git/memsource-cli-client/"
if [[ ! -d ${DIRECTORY} ]]; then
  mkdir -p ${DIRECTORY}
fi
cd $DIRECTORY

if [[ -f $(which python3) ]];
then
  python3 -m venv --system-site-packages .memsource
else
  if [[ ! -f $(which virtualenv) ]];
  then
    sudo yum -y install python-virtualenv
  fi
  virtualenv --system-site-packages .memsource
fi

source .memsource/bin/activate
pip install -U pip
pip install -U setuptools
pip install memsource-cli

clear
memsource --help
```

<a id="markdown-github-install" name="github-install"></a>
### Install from Github
```
DIRECTORY="$HOME/git/"

if [[ ! -d ${DIRECTORY} ]]; then
  mkdir ${DIRECTORY}
fi
cd ${DIRECTORY}
if [[ ! -d ${DIRECTORY}/memsource-cli-client ]]; then
  git clone https://github.com/unofficial-memsource/memsource-cli-client.git
  cd memsource-cli-client/
  if [[ -f $(which python3) ]];
  then
    python3 -m venv --system-site-packages .memsource
  else
    if [[ ! -f $(which virtualenv) ]];
    then
      sudo yum -y install python-virtualenv
    fi
    virtualenv --system-site-packages .memsource
    for py in $(find memsource_cli -name "*.py"); do sed -i -e 's#/usr/bin/env python3#/usr/bin/env python#' $py; done
  fi
  source .memsource/bin/activate
  pip install -U pip
  pip install -U setuptools
  pip install -e .
  deactivate
else
  cd memsource-cli-client/
  rm -Rf .memsource
  if [[ -f $(which python3) ]];
  then
    python3 -m venv --system-site-packages .memsource
  else
    if [[ ! -f $(which virtualenv) ]];
    then
      sudo yum -y install python-virtualenv
    fi
    virtualenv --system-site-packages .memsource
    for py in $(find memsource_cli -name "*.py"); do sed -i -e 's#/usr/bin/env python3#/usr/bin/env python#' $py; done
  fi
  source .memsource/bin/activate
  git checkout master
  git reset --hard
  git pull
  if [[ ! -f $(which python3) ]];
  then
    for py in $(find memsource_cli -name "*.py"); do sed -i -e 's#/usr/bin/env python3#/usr/bin/env python#' $py; done
  fi
  source .memsource/bin/activate
  pip install -e .
  deactivate
fi
source ${DIRECTORY}/memsource-cli-client/.memsource/bin/activate
clear
memsource --help
```
And that's it!

<a id="markdown-configuration" name="configuration"></a>
## Configuration
This way you can configure your username/password and set up memsource token for faster authentication:

```
source ${HOME}/git/memsource-cli-client/.memsource/bin/activate
export MEMSOURCE_URL="https://cloud.memsource.com/web"
export MEMSOURCE_USERNAME=<username>
export MEMSOURCE_PASSWORD=<password>
export MEMSOURCE_TOKEN=$(memsource auth login --user-name $MEMSOURCE_USERNAME --password "${MEMSOURCE_PASSWORD}" -c token -f value)
```

Or you can create a file:

Edit file with `vi ~/.memsourcerc` and paste following content:
```
source ${HOME}/git/memsource-cli-client/.memsource/bin/activate
export MEMSOURCE_URL="https://cloud.memsource.com/web"
export MEMSOURCE_USERNAME=<username>
export MEMSOURCE_PASSWORD=<password>
export MEMSOURCE_TOKEN=$(memsource auth login --user-name $MEMSOURCE_USERNAME --password "${MEMSOURCE_PASSWORD}" -c token -f value)
```

Then only source that file to start using memsource-cli:

```
source ~/.memsourcerc
```

Requirements:
- `jq`

## Autocompletion
To add autocompletion to your shell so you can type:

`mem[tab] pr[tab] cr[tab]` which will translate to:

`memsource project create`
```
memsource complete | sudo tee /etc/bash_completion.d/memsource > /dev/null
. /etc/bash_completion.d/memsource
```

Now you should be fine to use `memsource`

<a id="markdown-contact" name="contact-us"></a>
## Contact us!

This project is maintained on Github.
- Please contact us by submitting [issue](#collaborate)
- Feel free to join our [Unofficial Memsource CLI Telegram Group](https://t.me/Unofficial_MemsourceCLI)
- Check out our [wiki](https://github.com/unofficial-memsource/memsource-cli-client/wiki/) !


