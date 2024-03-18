# Launcher Differences

Launchers have some subtle differences between them which can cause a lot of confusion for mod developers. This page tries to document these differences.

This page is written from a 1.7 Forge mod developer's perspective.

If a launcher has a (?) mark, that means I have not tested it firsthand and the information about it was derived from other users.

Tip: [NotEnoughVerbosity](https://github.com/LegacyModdingMC/NotEnoughVerbosity) can be used to force some launchers to use the standard logging configuration, with a trace-level `fml-client-latest.log`.

> This page is a work in progress.

## MultiMC/PolyMC/PrismLauncher

These three launchers are all based on the same codebase.

No issues known.

Logging: Uses [the standard logging configuration](https://github.com/MinecraftForge/MinecraftForge/blob/9274e4fe435cb415099a8216c1b42235f185443e/fml/src/main/resources/log4j2.xml) (with a trace level `fml-client-latest.log`, a not very useful `latest.log`, and a sometimes useful `fml-junk-earlystartup.log`). I have no idea how the GUI log works.

Java runtime: User provided

## ATLauncher

Logging: Uses a custom log configuration ([example from a 1.7 Forge instance](https://github.com/LegacyModdingMC/wiki/blob/master/references/launchers/atlauncher/client-1.7.xml)).

- On the disk, only a `latest.log` is created.
- The same log is shown in the GUI.
    - This log can be uploaded to `paste.atlauncher.com`.
    - It likes to eat the first line of stack traces.
    - But there are also messages that only appear in the GUI log.
    - It tries to remove sensitive information from the log, for example all occurrences of the launcher's path are replaced with `**USERSDIR**`.
    - There's an option to configure the verbosity in the settings, but it doesn't seem to do anything.

Java runtime: Downloads 8u51 by default. A custom install can be provided.

## Technic Launcher

Uses [LaunchWrapper's logger config](https://github.com/Mojang/LegacyLauncher/blob/a4801b70f8a0148c6e6279ec2e91527e8019e1c8/src/main/resources/log4j2.xml) (which is based on vanilla 1.7.2's) due to incorrect classpath ordering.

## CurseForge Launcher

(?)

Java runtime: Downloads 8u51. A different version can be forced if a mystery CF-specific flag is set<sup>[[*](https://github.com/GTNewHorizons/Angelica/issues/82#issuecomment-1871629459)]</sup>. (The flag in question seems to be `-version:1.8+`.)<sup>[[*](https://old.reddit.com/r/feedthebeast/comments/4kq9ks/how_do_i_change_the_default_version_of_java_that/d3hiod2/)]</sup>

## Official Launcher (1.x)

Uses [the vanilla launcher config](https://launchermeta.mojang.com/mc/log_configs/client-1.7.xml/6605d632a2399010c0085d3e4da58974d62ccdfe/client-1.7.xml) even in modded instances.

Deletes extra items from the assets directory (`$launcherDir/assets`).

`$launcherDir/launcher_profiles.json` holds the verson of the launcher in `.launcher_version.name` (e.g. `1.6.61`.)

## TLauncher

(?)

Deletes extra items from the assets directory.

## HMCL

(?)

Logging: Uses [a custom log configuration](https://github.com/huanghongxun/HMCL/blob/c6afd53e73c5a2dc75afc7a1ab279c0b3918da82/HMCLCore/src/main/resources/assets/game/log4j2-1.7.xml) based on Vanilla's.

Can export crashes into a `minecraft-exported-crash-info-<TIMESTAMP>.zip` containing logs ([example](https://github.com/LegacyModdingMC/UniMixins/files/11413614/minecraft-exported-crash-info-2023-05-07T08-14-13.zip)).
