# pEpisodeManager

!!! Note
    This page will not explain **anything** about the basics of MOOS-IvP. If you are new and looking for resources on this checkout [their homepage](https://oceanai.mit.edu/moos-ivp/pmwiki/pmwiki.php). Consider completing the labs associated with [MIT 2.680](https://oceanai.mit.edu/2.680/pmwiki/pmwiki.php) if you are really serious in your goal to learn MOOS-IvP.

## Purpose of pEpisodeManager

In training of ML agents it is often desirable to split training experience into episodes that end in either success or failure. pEpisodeManager provides the capability to reset vehicles when some conditions are meet. This prevents the need to shutdown the vehicle between episodes (a expensive process).

The demo below shows pEpisodeManager running during training of an agent in the [AgentAquaticus](https://github.com/mivp-agent/moos-ivp-agent/tree/main/missions/AgentAquaticus) mission. This mission is configured to reset agents to their home flag when they successfully capture the flag **OR** when they go out of bounds.

![pEpisodeManager](../assets/QTableDemo.gif)

---

## Configuration

There are four *main* components to configuring a instance of pEpisodeManager.

- Reset position
- Configuring success conditions
- Configuring failure conditions

### Reset position

!!! Note
    Currently, the only supported reset `depth` is 0. MOOS-IvP Agent is not currently compatible with submersible missions.

For the basic functionality of pEpisodeManager to work, you must tell the manager where to reset the vehicle when. The following config block shows the proper usage of the `reset_pos` config variable where `x=50`, `y=-24`, and `heading=240`.

```
ProcessConfig = pEpisodeManager
{
  AppTick   = 4
  CommsTick = 4

  reset_pos = 50,-24,240
}
```

If the following pEpisodeManager was started it **would not** reset the vehicle as it does not know *when* to do so. See bellow for configuration of success and failure conditions.

### Success & failure conditions

For the manager to know when it should reset the vehicle (or equivalently when episodes *should* end), we need to do one of two things.

- Specify configuration variables for success & failure conditions.
- Trigger reset directly via a post to the `EPISODE_MGR_CTRL` moos var.

This section will follow the configuration method. See below for the usage of `EPISODE_MGR_CTRL.`

!!! Note "Reminder"
    For pEpisodeManager to have access to a MOOS var it must either originate from an app also running on that vehicle or be forwarded from another vehicle. Forwarding is usually done via [uFldNodeBroker](https://oceanai.mit.edu/ivpman/pmwiki/pmwiki.php?n=IvPTools.UFldNodeBroker) or [uFldShoreBroker](https://oceanai.mit.edu/ivpman/pmwiki/pmwiki.php?n=IvPTools.UFldShoreBroker).

The following configuration block is made for [Project Aquaticus](https://oceanai.mit.edu/aquaticus/pmwiki/pmwiki.php?n=Main.HomePage) and shows proper usage of the `end_success_condition` and `end_failure_condition`. The resulting behavior will be for the vehicle to reset when either tagged or in possession of the virtual flag.

```
ProcessConfig = pEpisodeManager
{
  AppTick   = 4
  CommsTick = 4

  end_success_condition = (HAS_FLAG = true)
  end_failure_condition = (TAGGED = true)

  reset_pos = 50,-24,240
}
```

More complex conditions can be specified using [this format](https://github.com/moos-ivp/svn-mirror/blob/master/ivp/src/lib_logic/manpage.txt). If multiple `end_success_condition` or `end_failure_condition` lines are specified then pEpisodeManager will treat the relationship between them as an **AND** clause.

### State Transition Posts

There are three [state transitions](episode_manager.md#state-transitions) which can be configured to post specified MOOS vars. The following config block shows the correct usage of the configuration variables. 

```
ProcessConfig = pEpisodeManager
{
  AppTick   = 4
  CommsTick = 4

  end_success_condition = (HAS_FLAG = true)
  end_failure_condition = (TAGGED = true)

  reset_pos = 50,-24,240

  start_post = var=MY_VAR,val=now_starting

  reset_post = var=UNTAG_REQUEST,val=vname=$(VNAME)
  reset_post = var=MY_VAR,val=now_resetting

  pause_post = var=MY_VAR,val=now_pausing
}
```

TODO: Explain

### TODO: Max duration

---

## State & Transitions

### Overview

There are four states which pEpisodeManager can be in. These states will be posted to the `EPISODE_MGR_STATE` MOOS var 

#### - `RUNNING`

This is the main state, where MOOS variables are consumed to check if either `end_success_condition`s or `end_failure_conditions`s are satisfied at which point a state transition to `STOPPING_HELM` is triggered. 

Alternatively the vehicle can be reset through the `EPISODE_MGR_STATE` or by reaching the `max_duration` specified in the config. 

#### - `STOPPING_HELM`

This state is used to wait for the `IVPHELM_STATE` MOOS var to enter the `PARK` state indicating that the vehicle will not be attempting to navigate during which is useful for the next state `RESETING`.

#### - `RESETING` (working on the spelling)

This state is used to wait for the vehicles `NAV_X` and `NAV_Y` to be in some tolerance of the configured `reset_pos`. After this condition is meet pEpisodeManager will check if a pause has been requested by use of `EPISODE_MGR_STATE` [see here](episode_manager.md#using-episode_mgr_ctrl). If a pause has been requested the next state will be `PAUSED` and otherwise it will continue to the `RUNNING` state.

#### - `PAUSED`

Used to stop keep vehicles stopped until a `EPISODE_MGR_CTRL` post is made indicating that it should be started and transition to the `RUNNING` state.


## Using EPISODE_MGR_CTRL

It can be useful to manually trigger state change in pEpisodeManager via a MOOS var post. For this reason pEpisodeManager listens on the `EPISODE_MGR_CTRL` variable. There are three  "actions" which can be triggered via this method.

- `start`: Used when pEpisodeManager is in the `PAUSED` state to transition to `RUNNING`.
- `hardstop`: Immediately stop the current episode and enter the `PAUSED` state after resetting. Will report the episode as a failure in the episode report.
- `reset`: Immediately end the current episode. The state of success / failure can be set in the `EPISODE_MGR_CTRL` post.
- `pause`: After the current episode ends, enter the `PAUSED` state.

These actions can be triggered by making a post where `type=` is followed by one of these action's names. For example, the following command uses the [uPokeDB](https://oceanai.mit.edu/ivpman/pmwiki/pmwiki.php?n=IvPTools.UPokeDB) utility to make post causing the pEpisodeManager to come to a paused state after the current episode.

```
uPokeDB alpha.moos EPISODE_MGR_CTRL=type=pause
```

The `reset` can take an additional argument which specifies what value should be reported for the success state.

```
uPokeDB alpha.moos EPISODE_MGR_CTRL=type=pause,success=true
```

The [MissionMessage](../python/mission_message.md) python wrapper provides a pythonic way of trigging these posts.

## Episode Reports

To report of the success / failure of each episode pEpisodeManager will post to the `EPISODE_MGR_REPORT` a comma separated key/value pairs. This are also helpful for debugging. The below is an example of one such report.

```
NUM=8,SUCCESS=true,DURATION=122.0297,WILL_PAUSE=false
```

These reports are automatically forwarded by [BHV_Agent](bhv_agent.md) without any need for further configuration. In python [MissionMessage](../python/mission_message.md) will parse these into easily accessible variables.

## How it works

TODO
- Logic Conditions
- USIM reset