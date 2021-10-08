# AgentAquaticus

AgentAquaticus is a fork of the Aquaticus mission which integrates the moos-ivp-agent project and provides for the ability to train multiple agents at once with one instance of a MOOS-IvP shoreside.

!!! Note
    You can download the original Aquaticus mission by a checkout of the moos-ivp-aquaticus repository: `svn co "https://oceanai.mit.edu/svn/moos-ivp-aquaticus-oai/trunk/" moos-ivp-aquaticus`.

## Usage

There are two main launch scripts associated with this mission. The [launch_heron.sh](https://github.com/CarterFendley/moos-ivp-agent/blob/main/missions/AgentAquaticus/heron/launch_heron.sh) script launches a vehicles while the [launch_shoreside.sh](https://github.com/CarterFendley/moos-ivp-agent/blob/main/missions/AgentAquaticus/shoreside/launch_shoreside.sh) script is used once per simulation to launch infrastructure associated with the Aquaticus mission.

Example simulation launch script can be seen [here](https://github.com/CarterFendley/moos-ivp-agent/blob/main/examples/QTable/scripts/sim_launch.sh).

### Launching vehicles

Vehicles take a number of **required** parameters to launch.

- `team`: Can take on the value of `red` or `blue`. This parameter, among other things, will determine the starting position of the vehicle.
- `role`: Can take on the value of `agent` or `drone`. Determines what if `BHV_Agent` will be spawned on the vehicle.
- `id`: Currently values 11-15 and 21-25 (inclusive) are supported for `agent`s and `drone`s respectively these, along with role, determine the `vname` of the vehicle. Vehicles will only be able to tag a vehicle with corresponding least significant digit (e.g. `drone_21` can tag `agent_11` and not `agent_12`)

!!! Note
    In coming updates the BHV_Agent behavior will be started on both `agent` and `drone` roles.

There are a number of helpful **optional** parameters some of which are highlighted below.

- `--log`: Enables the writing of MOOS-IvP log files. Useful during debugging.
- `--color=<my_color>`: Used to change the color of the vehicle when rendered via [pMarineViewer](https://oceanai.mit.edu/ivpman/pmwiki/pmwiki.php?n=IvPTools.PMViewer)
- `--behavior=<behavior_name>`: Used to set initial behavior for drones. Any value placed here will show up in the `ACTION` field in the [meta_heron.bhv](https://github.com/CarterFendley/moos-ivp-agent/blob/main/missions/AgentAquaticus/heron/meta_heron.bhv) file.
- [Time Warp](https://oceanai.mit.edu/ivpman/pmwiki/pmwiki.php?n=Lab.ClassHelmAutonomy#section5.1.3): A integer value with how many times the simulation should be speed up relative to real world time.

!!! Note
    The time warp of vehicles should correspond.

#### Example agent launch

```
./launch_heron.sh red agent 11 --color=orange 10
```

#### Example drone launch

```
./launch_heron.sh blue drone 21 --behavior=DEFEND --color=orange 10
```

### Launching shoreside

At least one shoreside is required as it acts as the bridge for vehicle communication and manages the flag capture / tagging.

Shore side takes only **optional** parameters.

- `--no_gui`: Used to disable the launch of `pMarineViewer` as it can slow the simulation.
- [Time Warp](https://oceanai.mit.edu/ivpman/pmwiki/pmwiki.php?n=Lab.ClassHelmAutonomy#section5.1.3): See vehicle launch section.

#### Example shoreside launch

```
./launch_shoreside.sh --no_gui 10
```

## Vehicle Overview

### Behaviors

MOOS-IvP behaviors are what should determine the actions of a robot. These can either be what are referred to as "hard coded behaviors" or those that are produced by [BHV_Agent](../bhv_agent.md). If extending the behavior file please use [this page](https://oceanai.mit.edu/ivpman/pmwiki/pmwiki.php?n=Helm.HelmAutonomy) as a reference.

!!! Note 
    Currently the `BHV_Agent` behavior is always running when the `MODE == ACTIVE`. This important as this contains the code which communicates with python.

For hard coded behaviors, the below config block shows that anytime the `ACTION != AGENT` (as set when `role` is set to `agent` in the launch script) and `MODE == ACTIVE` the vehicle will return to their flag when they either have the flag or are tagged.

```
set MODE     = RETURN_BASE {
  MODE       = ACTIVE
  (ACTION != AGENT) and ((HAS_FLAG = true) or (TAGGED = true))
} PLAY
```

Otherwise a number of `MODE`s can be selected depending on the `ACTION` value: `ATTACKING`, `ATTACK_LEFT`, `ATTACK_RIGHT`, `DEFENDING`, `STATIONING`

For more information see the current [meta_heron.bhv](https://github.com/CarterFendley/moos-ivp-agent/blob/main/missions/AgentAquaticus/heron/meta_heron.bhv) and reference the [IvP Helm wiki](https://oceanai.mit.edu/ivpman/pmwiki/pmwiki.php?n=Helm.Cover) page's left hand side bar.

### pEpisodeManager

The mission's [pEpisodeManager](../episode_manager.md) is configured in [this file](https://github.com/CarterFendley/moos-ivp-agent/blob/main/missions/AgentAquaticus/heron/plug_pEpisodeManager.moos) and currently looks for the `TAGGED == true` condition for failure and receives success signals by means of a `EPISODE_MGR_CTRL` post from `uFldFlagManagerAgent`

## Shoreside overview

The shoreside uses [uFldFlagManagerAgent](../flag_mgr_agent.md) and [uFldTagManagerAgent](../tag_mgr_agent.md) to allows for multi vehicle training.
