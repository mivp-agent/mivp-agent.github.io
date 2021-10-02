# Getting Started

!!! Note
    This  page is currently under construction 

Currently the best way of getting started is to:

1. Look at the examples from the main repository
    - See bellow for suggestions on **which** examples to focus on depending on your background
2. While going through examples, reference the following two pages
    - Python API for building models
    - MOOS-IvP Reference for configuring new missions

[Python API :fontawesome-brands-python:](../python){ .md-button .md-button--primary }
[MOOS-IvP Reference :fontawesome-solid-robot:](../moos_ivp){ .md-button .md-button--primary }

## If you are coming from MOOS-IvP

I would recommend looking at the "ManagerExample" and look at the configuration blocks for the `BHV_Agent`. This behavior is one that does the actual connection to python land through a TCP socket.

[ManagerExample :fontawesome-brands-readme:](https://github.com/CarterFendley/moos-ivp-agent/tree/main/examples/ManagerExample){ .md-button }

Then, focus on the python side of the more complex "QTable" mission bellow.

## If you said "What is MOOS-IvP"

Look at the "QTable" example. This implements a reinforcement learning [q-table](https://en.wikipedia.org/wiki/Q-learning). This example is trained on the [Project Aquaticus](https://oceanai.mit.edu/aquaticus/pmwiki/pmwiki.php?n=Main.HomePage) scenario. It's goal is to grab a flag in virtual game of capture flag. 

[QTable :fontawesome-brands-readme:](https://github.com/CarterFendley/moos-ivp-agent/tree/main/examples/QTable){ .md-button }

!!! Note "If you came from the MOOS-IvP section:"
    The associated MOOS-IvP mission files which are in that directory are based on the moos-ivp-agent's [AgentAquaticus](https://github.com/CarterFendley/moos-ivp-agent/tree/main/missions/AgentAquaticus) which allows for spawning of multiple vehicles in one MOOS-IvP simulation during training time. A good config block to look at is that for `pEpisodeManager` which manages the resetting of vehicles to form episodes of training.

## Hi Joe :wave:

