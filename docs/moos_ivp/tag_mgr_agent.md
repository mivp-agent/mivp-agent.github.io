# uFldTagManagerAgent

## Purpose of uFldTagManagerAgent

To speed up the training of agents, it is helpful to have many agents train in the same simulation with without conflict. This application is a fork of Aquaticus' `uFldTagManager` and is backwards compatible with the configuration options.

## Configuration

There are two components to configuring a instance of uFldTagManagerAgent.

- Enabling / disabling restricted tagging
- Specifying which vehicles can tag each other

All other options can be seen by running the following command to see an example config from uFldTagManager.

```
uFldTagManager --example
```

### Restricted tagging

To enable restricted tagging you would add `restrict_tagging = true` to the configuration block of uFldTagManagerAgent (default it `false`). When enabled, all vehicles will not be able to tag each other by default and you will need to go to the next configuration component.

### Can tag rules

To specify that a vehicle can tag another you must provide a `can_tag` config line. For example, the below config lines will restrict tagging and allow the vehicle `drone_21` to tag `agent_11` and for `drone_22` to tag `agent_12`

```
  restrict_tagging = true
  can_tag = drone_21=agent_11
  can_tag = drone_22=agent_12
```

!!! Note
    This is not a two way street! With the above config, `agent_11` will not be able to tag `drone_21`.

