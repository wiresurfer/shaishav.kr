---
title: Tech Tip - Make Neovim Python LSP play nice with pyenv
description:
    Modern python development relies on some form of virtual environment
    management. pyenv + virtialenv is a goto toolkit for managing both python
    versions and isolated package environments. For people using Neovim as their
    editor, setting up Neovim's LSP to play nice with pyenv requires a trick.
    This post covers the interplay of tools to make this work.
categories:
    - Engineering
tags:
    - topic/engineering
    - topic/python
    - topic/neovim
    - topic/devtools
topic:
    - engineering
public: true
date: 2024-07-26
created: 2024-07-26 06:49
coverImage: https://opengraph.githubassets.com/4c338d32f782385335706e884a4e72a5119003b7fa4ba9e3286202031dbeaefa/alefpereira/pyenv-pyright
---

# Tech Tip - Make Neovim Python LSP play nice with pyenv

Modern python development relies on some form of virtual environment management.
pyenv + virtialenv is a goto toolkit for managing both python versions and
isolated package environments.

<!-- more -->

For people using Neovim as their editor, setting up Neovim's LSP to play nice
with pyenv requires a trick. This post covers the interplay of tools to make
this work.

## What's the problem?

Lets say you have the following folder structure.

```
src\
  python-project\
    main.py
    .python-version
```

1. You have setup a local python version using say, `pyenv local 3.11`
2. You have also created a virtualenv using `pyenv virtualenv 3.11 demoenv`
3. You activate your virtualenv `pyenv virtualenv activate demoenv`
4. Install a package say `python -m pip install python-dotenv`
5. And finally write the following in `main.py`

```python
from dotenv import load_dotenv

load_dotenv()

```

So far so good. We have setup a barebones environment with its own package and a
minimal main.py

Test this by running `python main.py` and it should run without any error, and
ironically without any output.

The problem happens if you have neovim setup with some sane LSP config and open
`main.py` To follow along, I recommend you start with
[LunarVim](https://www.lunarvim.org/) to keep things simple. Lunarvim has a
known working python LSP setup using ruff and pyright.

If you open main.py in lunarvim you would notice the import statement would be
marked in squiglies. And you would also notice all your LSP superpowers like
autocomplete and hints are gone. kaput. zilch.

Thats an uncomfortable place to be in, if you want to be a productive
programmer. So what's going on here?

## I. Trying to deactivate/activate the virtualenv and launching lvim.

tl;dr. This wont work.

My first hunch when I had this issue was that I launched lunarvim without the
right python paths. Maybe a simple deactive and then activate should do the
trick. So I quit neovim, deactivated the env, closed the terminal for good
measure and meticulously redid the environment activation.

And the same squigly lines reappeared. Ah well, it was worth a shot.

## II. Debugger Hat On: Looking at LSP logs

I remembered Neovim gives the `:LspInfo` and `:LspLog` command which opens up a
buffer with logs.

A quick look at how the LSP was launching pyright raised a few red flags. It
seems pyright wasn't aware of pyenv path or pyenv environment at all.

And this looked awfully familiar.

A few months ago, I had a similar issue with CMake c++ projects and not being
able to resolve library and include files.

The solution in the CMake case was a directive in the CMakeList.txt which output
the compile parameters into a json file in the project root director.

```
#File: CMakeList.txt
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
```

or

```bash
cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=1 ...rest of cmake arguments...
```

## III. Final Solution

Just like Cmake outputs a json file when run with CMAKE_EXPORT_COMPILE_COMMANDS
option, it seems pyright also looks for a json file to infer a few path/root
related settings.

The file is named
[`pyrightconfig.json`](https://github.com/microsoft/pyright/blob/main/docs/configuration.md)
Its pretty well documented and has a bunch of config options, but the one's we
are interested in are

-   venvPath : [path, optional]: Path to a directory containing one or more subdirectories,
    each of which contains a virtual environment. When used in conjunction with a
    venv setting (see below), pyright will search for imports in the virtual environment’s
    site-packages directory rather than the paths specified by the default Python
    interpreter. If you are working on a project with other developers, it is best
    not to specify this setting in the config file, since this path will typically
    differ for each developer. Instead, it can be specified on the command line or
    in a per-user setting. For more details, refer to the import resolution documentation.
-   venv : [string, optional]: Used in conjunction with the venvPath, specifies the
    virtual environment to use. For more details, refer to the import resolution
    documentation.

This
[stackoverflow answer](https://stackoverflow.com/questions/65847159/how-to-set-python-interpreter-in-neovim-for-python-language-server-depending-on)
was what led me to this solution, after wasting about 20mins.

To make your project work properly you have one of two options.

1. Manually place a pyrightconfig.json file in the root of your project.

```pyrightconfig.json

{
    "venvPath": "/home/USERNAME/.pyenv/versions/",
    "venv": "MY-VENV"
}

```

1. Or you can use
   [this pyenv plugin called "pyenv-pyright"](https://github.com/alefpereira/pyenv-pyright)
   which automatically sets up the pyrightconfig.json file as per your current
   active environment.

```sh
#install pyenv-pyright plugin
git clone https://github.com/alefpereira/pyenv-pyright.git $(pyenv root)/plugins/pyenv-pyright

#generate the pyrightconfig.json file.
pyenv pyright

#lunarvim main.py  should work flawlessly now.
```

Once the pyrightconfig.json is setup using either method 1, or 2, starting
neovim should load the LSP and also detect packages in your virtualenv properly.

A small summary of why this problem happens in the first place

-   Microsoft pyright doesnt infer pyenv from the shell variables.
-   Even though you ran `pyenv activate demoenv`, this only sets up the python
    path and shims for library paths.
-   pyright will only detect venvs when a pyrightconfig file is present.
-   doing pyenv activate doesn't generate this file automatically.
-   hence we need to either roll out our own file, or use the plugin mentioned
    above to do it for us.

Anyways, 20mins to fix LSP, 20 mins to write this. I guess I should do something
more than `load_dotenv()` now.

Ciao. ~ wiresurfer
