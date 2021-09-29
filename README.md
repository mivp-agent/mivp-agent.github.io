# mivp-agent website

## Environment Setup

### Install Conda

Follow the instructions [here](https://conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation) to install Anaconda or Miniconda.

Assure that your terminal prompt is now prefixed by the conda environment that is currently activated as bellow

```
(base) ~/src/mivp-agent.github.io $ 
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