# mivp-agent website

[![Deploy GitHub Pages](https://github.com/mivp-agent/mivp-agent.github.io/actions/workflows/deploy.yml/badge.svg)](https://github.com/mivp-agent/mivp-agent.github.io/actions/workflows/deploy.yml)

## Environment Setup

### Install Conda

Follow the instructions [here](https://conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation) to install Anaconda or Miniconda.

Assure that your terminal prompt is now prefixed by the conda environment that is currently activated as bellow

```
(base) $ 
```

If you don't see the `(base)` text (indicating you are in the "base" conda environment), it is suggested that you follow [this](https://github.com/conda/conda/blob/master/CHANGELOG.md#440-2017-12-20) practice

### Initialize the conda environment

If this is your first time setting up the repository you should use the following command to create the website's environment from file.

```
conda env create -f environment.yml
```

You should see a number of packages install using both conda and pip.

### Activating the environment

To activate, or enter, the newly created environment, you can use the following command.

**NOTE:** This will need to be each time you wish serve the documentation and open a new terminal.

```
conda activate mivp-agent-web
```

You should see this change in your environment in the conda's terminal prompt prefix.

### Updating the environment

If new dependencies are added to the `environment.yml` you can update your local environment by the use of the following command.

**IMPORTANT NOTE:** This should be run **ONLY** when the `(mivp-agent-web)` environment is activated.

```
conda env update -f environment.yml
```

### Setting up mivp-agent

Because the mivp-agent package is not currently on PyPI or other indexes, we can not directly include it in the `environment.yml` file. To allow [mkdocstrings](https://mkdocstrings.github.io/) to import the package and read the doc strings, we must install it in the `mivp-agent-web` conda environment. Navigating to the `moos-ivp-agent/src/python_module` directory (wherever that is on your system) and running the following command.

```
pip3 install -e .
```

Secondly, mkdocstrings needs a directory to watch for updates to know when to regenerate documentation. The plugin is configured to watch a `mivp_agent` directory in the root of this repository. All you need to do is link that directory to the `moos-ivp-agent/src/python_module/src/mivp_agent` in the main repository (wherever you put that). For example **on my system** I run the following command

```
ln -s /Users/carter/src/moos-ivp-agent/src/python_module/src/mivp_agent /Users/carter/src/mivp-agent.github.io/mivp_agent
```

**NOTE:** You will still need to *refresh* the browser to view updates to the python documentation 


### Serving the website locally

A local version of the documentation can be served through the following command in the root directory.

```
mkdocs serve
```

### Building a static site

A static site can be build with the following command.

```
mkdocs build
```

## References

- General
  - [MkDocs](https://www.mkdocs.org/)
  - [MkDocs Material Theme](https://squidfunk.github.io/mkdocs-material/)
    - [Emoji Lookup](https://emojipedia.org)
    - [Fontawesome](https://fontawesome.com/v5.15/icons?d=gallery&p=2)
- Python API
  - [mkdocstrings](https://mkdocstrings.github.io/)
  - [Google Docstrings Example](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
