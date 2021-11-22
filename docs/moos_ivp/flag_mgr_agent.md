# uFldFlagManagerAgent

!!! Note
    There is a known [bug](https://github.com/mivp-agent/moos-ivp-agent/issues/3) in the rending of flags by pMarineViewer. Rest assured, the vehicle will still have a flag despite this rendering issue.

## Purpose of uFldFlagManagerAgent

To speed up the training of agents, it is helpful to have many agents train in the same simulation with without conflict. This application is a fork of Aquaticus' `uFldFlagManager` and is backwards compatible with the configuration options.

## Configuration

There is only one additional flag added by this fork: `infinite_flags`. This flag can be set to either `true` or `false` in the config block. This allows any vehicle to grab a red or blue flag without changing the availability of that flag to other grabbing vehicles. See a example config for the `uFldFlagManager` app (all of which is compatible with this app) by running the following command.

```
uFldFlagManager --example
```