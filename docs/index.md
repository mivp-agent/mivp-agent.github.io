# MOOS-IvP Agent
## Overview

Model agnostic machine learning tooling for [MOOS-IvP](https://oceanai.mit.edu/moos-ivp/pmwiki/pmwiki.php). Inspired by [moos-ivp-pLearn](https://github.com/mnovitzky/moos-ivp-pLearn) this project was designed to allow for training of python ML agents for [Project Aquaticus](https://oceanai.mit.edu/aquaticus/pmwiki/pmwiki.php?n=Main.HomePage) while also providing generalized software to use with any MOOS-IvP project. 

!!! Note
    This project is still **very** young. As such feel free to any ask questions not answered by the documentation via a [github issues](https://github.com/mivp-agent/moos-ivp-agent/issues). There, you can also see the current backlog.

Bellow you can see an example MOOS-IvP mission [AgentAquaticus](moos_ivp/missions/agent_aquaticus.md) based on [Project Aquaticus](https://oceanai.mit.edu/aquaticus/pmwiki/pmwiki.php?n=Main.HomePage). The agents being trained are rewarded by successfully grabbing and returning a flag protected by robots which circle it. The agent's actions are being determined by [q-table](https://en.wikipedia.org/wiki/Q-learning) written in [NumPy](https://numpy.org/).

![Demo](assets/AgentAquaticusDemo.gif)

## Installation

This project currently supports both OSX and Linux operating systems. See the main README.

[README :fontawesome-brands-readme:](https://github.com/mivp-agent/moos-ivp-agent){ .md-button }

!!! Note "Pretty Please"
    **PLEASE** Raise a GitHub issue if there is ~any~ issue with these instructions.

## Getting Started

See the getting started page to start you on your ML path.

[Getting Started :fontawesome-solid-tachometer-alt:](getting_started.md){ .md-button .md-button--primary }
