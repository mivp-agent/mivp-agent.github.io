# `BHV_Agent`

!!! Note
    `BHV_Agent` has only been tested in scenarios where: 

    1. It has the maximum `pwt` out of all behaviors in the mission it is used
    2. Has `perpetual = true` set in it's configuration block

## Okay fine, a little MOOS-IvP primer

Behaviors, are the "IvP" part of MOOS-IvP which take in "MOOS" variables and produce "IvP Functions" which dictate how the robots running MOOS-IvP should behavior. For a good primer see these [2.680 Lecture Slides (2021)](https://oceanai.mit.edu/2.680/docs/2.680-08-ivphelm_behaviors_2021.pdf).

## Purpose of BHV_Agent

In the case of moos-ivp-agent, `BHV_Agent` is forwarding all "MOOS state" to the python `ModelBridgeServer` (wrapped by `MissionManager`). The python ML models then make decisions on what action a robot running MOOS-IvP and `BHV_Agent` should take by providing a `course` and `speed` and optionally mutate the "MOOS State" of the robot by making `posts`.

## Configuration

!!! Note
    See the general [Helm Autonomy reference](https://oceanai.mit.edu/ivpman/pmwiki/pmwiki.php?n=Helm.HelmAutonomy) for information about configuring behaviors in general.

`BHV_Agent` exports three types of state from MOOS-IvP to python

- **(Automatic):** The position of the robot
    - As defined by the `NAV_X` and `NAV_Y` moos vars.
- **(Upon subscription):** The position of *other* robots.
    - As supplied by the `NODE_REPORT_<VNAME>` and `pNodeParse` (aquaticus)
- **(Upon subscription):** Any specified MOOS var

### Subscribing to vehicle positions

The `sub_vehicle` configuration key is used to subscribe to vehicles based on their name. The following `BHV_Agent` config block shows a subscription to two vehicles with names `evan` and `felix`.

```
Behavior = BHV_Agent
{
  name = agent
  pwt  = 100
  perpetual = true

  condition = MODE == ACTIVE

  sub_vehicle = evan
  sub_vehicle = felix
}
```

### Subscribing to MOOS vars

The `sub_var` configuration key is used to subscribe to MOOS vars based on their state. The following `BHV_Agent` config block shows a subscription to two vars with names `TAGGED` and `HAS_FLAG`.

!!! Note
    As some MOOS-IvP apps have startup delays or do not post vars initially, you cannot assume that vars subscribed to will be **immediately** available on the python side. You are responsible for checking before you access.

```
Behavior = BHV_Agent
{
  name = agent
  pwt  = 100
  perpetual = true

  condition = MODE == ACTIVE

  sub_var = TAGGED
  sub_var = HAS_FLAG
}
```

## What does state look like in Python

Once the state is outputted from `MissionManager`, it will be in a python dictionary with the following form. All values will be translated into python's string, float, or boolean types (With the exception of the node report dictionaries).

```
>>> msg = mgr.get_message()
>>> print(msg.state)
{
  'NAV_X': 30.5,
  'NAV_Y': -75.2,
  'TAGGED': False,
  'HAS_FLAG': True,
  'NODE_REPORTS': {
    'evan': {
      'NAV_X': -60.3
      'NAV_Y': 35.2
    },
    'felix': {
      'NAV_X': -12.3
      'NAV_Y': -54.0
    }
  }
}
```

## BHV_Agent and pEpisodeManager

`BHV_Agent` will automatically collect data from `pEpisodeManager` if it is present and forward that data to the python model. See the (MissionMessage)[api_pages/mission_message.md] for information on how to access this.