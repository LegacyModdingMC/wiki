# Gradle Plugins

## ForgeGradle

ForgeGradle is the official Gradle plugin used to build [Minecraft Forge](minecraft-forge.md) mods.

Minecraft 1.7.10 is only supported by version 1.2.

* Official repo: [https://github.com/MinecraftForge/ForgeGradle/tree/FG_1.2](https://github.com/MinecraftForge/ForgeGradle/tree/FG_1.2)
    * No longer maintained.
    * Asset downloading is no longer functional.
    * Supports Gradle up to 4.4.1

### Forks

Notable forks of FG 1.2:

* GTNH fork: [https://github.com/GTNewHorizons/ForgeGradle](https://github.com/GTNewHorizons/ForgeGradle)
    * Supports Gradle 6.9.1
* anatawa fork: [https://github.com/anatawa12/ForgeGradle](https://github.com/anatawa12/ForgeGradle)
    * Supports Gradle 7.4.2
* juanmuscaria fork: [https://github.com/juanmuscaria/ForgeGradle](https://github.com/juanmuscaria/ForgeGradle)
    * Supports Gradle 5.6.4

## RetroFuturaGradle

A backwards-compatible rewrite of ForgeGradle for use in 1.7.10 mod development. It complements [lwjgl3ify](https://github.com/GTNewHorizons/lwjgl3ify) by allowing the use of LWJGL 3 and modern Java versions, and has a task for running the mod in an obfuscated environment. [<sup>[*]</sup>](https://discord.com/channels/181078474394566657/603348502637969419/1076168257326829639)

Used by [GTNH](https://github.com/GTNewHorizons/ExampleMod1.7.10).

* [https://github.com/GTNewHorizons/RetroFuturaGradle](https://github.com/GTNewHorizons/RetroFuturaGradle)

## unimined

Unimined is a Gradle plugin that lets you build mods for legacy versions using modern tooling, all the way down to alpha versions of the game. It was created as a replacement for Architectury Loom, and is used by [CraftPresence](https://gitlab.com/CDAGaming/CraftPresence). [<sup>[*]</sup>](https://discord.com/channels/181078474394566657/603348502637969419/1076145769591095369)

* [https://github.com/WagYourOrg/unimined](https://github.com/WagYourOrg/unimined)
