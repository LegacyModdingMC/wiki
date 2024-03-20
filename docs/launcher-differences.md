# Launcher Differences

> This page is a work in progress.

Launchers have some subtle differences between them which can cause a lot of confusion for mod developers. This page tries to document these differences.

If a launcher has a (?) mark, that means I have not tested it firsthand and the information about it was derived from other users.

Forge's logging configuration is the following:
- On [1.7.10](https://github.com/MinecraftForge/MinecraftForge/blob/1.7.10/fml/src/main/resources/log4j2.xml): an all-level `fml-client-latest.log`, a not very useful `latest.log`, and a sometimes useful `fml-junk-earlystartup.log`
- On [1.12.2](https://github.com/MinecraftForge/MinecraftForge/blob/1.12.x/src/main/resources/log4j2.xml): a trace-level `debug.log`, and a not very useful `latest.log``

Tip: [NotEnoughVerbosity](https://github.com/LegacyModdingMC/NotEnoughVerbosity) can be used to force all launchers to use it.

## MultiMC/PolyMC/PrismLauncher

These three launchers are all based on the same codebase.

No issues known. This is the golden standard as far as launchers go.

### Logging

Uses Forge's logging configuration.

I have no idea how the GUI log works.

### Java runtime

User provided.

## Official Launcher

### Modern (2.x)

Versions are defined in `.minecraft/versions/<version>/<version>.json`. Mod loader installers define their own versions here.

#### Logging

For logging purposes the important fields are `inheritsFrom`, which lets a version inherit the settings of another version, and `logging`, which is where logger configs are defined.

The Forge 1.7.10 installer (and even Fabric 1.20.4) doesn't override the `logging` field, therefore [the vanilla logger config](https://launchermeta.mojang.com/mc/log_configs/client-1.7.xml/6605d632a2399010c0085d3e4da58974d62ccdfe/client-1.7.xml) is used.

I've found references ([1](https://bugs.mojang.com/browse/MC-123285), [2](https://wiki.vg/Debugging)) to a GUI option that allows changing the logging config, but it's nowhere to be found.

#### Java version

By default it uses the one defined by the Mojang API. For 1.7.10 this is 8u51. A custom one can be set on the "Edit installation" screen.

### Legacy (1.x)

Deletes extra items from the assets directory (`$launcherDir/assets`).

`$launcherDir/launcher_profiles.json` holds the verson of the launcher in `.launcher_version.name` (e.g. `1.6.61`.)

## CurseForge Launcher

It's just a frontend for the vanilla launcher. It has its own copy of it, and every time an instance is launched, it generates a launcher profile then launches it.

### Logging

It uses the vanilla config by default, but this can be changed by enabling "Enable Forge debug.log" in the settings. Despite what the name says, all this does is put `"logging": {},` in the generated launcher profile, which cancels out the logger profile inherited from the vanilla profile. This setting is permanent - instances launched while it was active will keep the "no logging" property set even after the option is disabled. (This is defined in `.baseModLoader.versionJson` in `minecraftinstance.json` in the instance directory).

### Java runtime

Uses the same version as vanilla by default. This can be overridden for Java 8 by using Java's [`-version` flag](http://web.archive.org/web/20090228125625/http://blogs.sun.com/ksrini/entry/java_launcher_tricks_with_multiple). For example, `-version:1.8+` will choose the newest `1.8` version installed on the system. Only versions of Java installed system-wide can be used this way, portable installs won't work (e.g. on Windows it checks the `Computer\HKEY_LOCAL_MACHINE\SOFTWARE\JavaSoft\Java Runtime Environment\1.8\JavaHome` registry string).

## Technic Launcher

Uses [LaunchWrapper's logger config](https://github.com/Mojang/LegacyLauncher/blob/a4801b70f8a0148c6e6279ec2e91527e8019e1c8/src/main/resources/log4j2.xml) (which is based on vanilla 1.7.2's) due to [seemingly incorrect classpath ordering](https://github.com/TechnicPack/LauncherV3/issues/350).

## ATLauncher

### Logging

Uses the vanilla log configuration.

In 1.7's case:

- On the disk, only a `latest.log` is created.
- The same log is shown in the GUI.
    - This log can be uploaded to `paste.atlauncher.com`.
    - It likes to eat the first line of stack traces.
    - But there are also messages that only appear in the GUI log.
    - It tries to remove sensitive information from the log, for example all occurrences of the launcher's path are replaced with `**USERSDIR**`.
    - There's an option to configure the verbosity in the settings, but it doesn't seem to do anything.

### Java runtime

Downloads 8u51 by default. A custom install can be provided.

## GDLauncher

It's a mystery. When I try to create an instance, it just keeps redownloading assets over and over again.

## TLauncher

(?)

Deletes extra items from the assets directory.

## HMCL

(?)

Logging: Uses [a custom log configuration](https://github.com/huanghongxun/HMCL/blob/c6afd53e73c5a2dc75afc7a1ab279c0b3918da82/HMCLCore/src/main/resources/assets/game/log4j2-1.7.xml) based on Vanilla's.

Can export crashes into a `minecraft-exported-crash-info-<TIMESTAMP>.zip` containing logs ([example](https://github.com/LegacyModdingMC/UniMixins/files/11413614/minecraft-exported-crash-info-2023-05-07T08-14-13.zip)).
