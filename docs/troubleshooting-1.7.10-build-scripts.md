# Troubleshooting 1.7.10 Build Scripts

So you want to compile an old 1.7.10 mod, but Gradle is throwing some cryptic errors at you?

1.7.10 was released [over 8 years ago](https://howoldisminecraft1710.today/) and has stopped receiving official support, so many old build scripts no longer work.

This guide will show you how to revitalize the build script using a fork of [ForgeGradle](gradle-plugins.md#forgegradle), which has a critical issue fixed. We will be building the [GalaxyOdyssey fork of EnviroMine](https://gitgud.io/AstroTibs/enviromine-for-galaxy-odyssey) as the example mod, as it showcases various issues you can run into. Naturally, you can also use any other mod.

# Introduction

## What you need
- You need to have Java 8 installed on your machine.
- It is recommended to have Git installed
- It is recommended to have Gradle 4.4.1 installed
- The steps below are written using Bash as the shell. On Windows you can easily get a Bash installation by installing [Git for Windows](https://git-scm.com/download/win).

> If you're insistent on using cmd, you will have to replace `./gradlew` with `gradlew` in the commands. As for PowerShell, the commands should work unless otherwise noted.

## Get the source code

The recommended way is to use Git to clone the entire repo:
```
git clone https://gitgud.io/AstroTibs/enviromine-for-galaxy-odyssey
```
This will get you all branches and the entire history of the mod, which lets you switch between commits and is good for preservation.

**Alternatively**: Look for a download button and click it. This will only download the latest commit.

### Switching branches

Some mods have the 1.7.10 source on a different branch than the default one. To find the right branch, choose the one that mentions 1.7.10 in its `build.gradle` or `gradle.properties`.

If you cloned the repo, you can switch branches using `git checkout` (for example, `git checkout 1.7.10` will switch to the branch named `1.7.10`.)

## Build the mod and see what happens

Run `./gradlew build` and see what happens. If you're lucky, everything will work fine, and the mod will be built in `build/libs/<mod_name>.jar`. But if you're reading this, it's probably not that simple.

# Troubleshooting

## Make sure `build.gradle` exists

If you're especially unlucky, the mod doesn't even come with a build script. With some luck, there might already be a fork of the mod that has a build script added. If there isn't, you'll have to do it yourself. Grab the Forge MDK or a [template project](forge-workspace-setup.md#template-projects) (such as [GTNewHorizons/ExampleMod](https://github.com/GTNewHorizons/ExampleMod1.7.10)), and transplant the mod's source code into it. If you have a pre-existing build of the mod at hand, compare the jar you produce to the existing one, and make adjustments to the build script until the two match up. Pay special attention to `META-INF/MANIFEST.MF` and `mcmod.info`.

## Make sure `gradlew` exists

**Symptom:** `bash: ./gradlew: No such file or directory` 

Building the mod using the Gradle wrapper (`gradlew`) is the most reliable way, and it's what we will be focusing on in this guide. If you can't find a file called `gradlew` in the same directory as `build.gradle`, you need to put it there.

- If you have Gradle installed system-wide, you can simply run `gradle wrapper --gradle-version 4.4.1` to generate it. (4.4.1 is the version recommended for best compatibility, see [below](#use-gradle-441) for more details.)
- If you don't have Gradle installed, you can copy it from a mod that has it. For example, [GTNewHorizons/ExampleMod1.7.10@a159153](https://github.com/GTNewHorizons/ExampleMod1.7.10/tree/a15915363a5a46dc609d3de46c069bcb8b4db527). Copy `gradlew`, `gradlew.bat`, and the `gradle` directory.

**Alternatively,** you can use the system-wide installation of Gradle instead of the Gradle wrapper, but you have to make sure it's the right version. I have 4.4.1 installed this way for convenience. In this case, you can run `gradle <command>` instead of `./gradlew <command>`.

## Make sure you're running with Java 8

**Symptom:**
```
FAILURE: Build failed with an exception.

* What went wrong:
Could not determine java version from '16.0.1'.
```
1.7.10 mods need to be built using Java 8. You can tell the Gradle wrapper to use a specific Java distribution by setting the `JAVA_HOME` environmental variable to the desired directory. In Bash, you can do this by prefixing the command with `JAVA_HOME=/path/to/java_home`.

For example: `JAVA_HOME=/opt/jdk/jdk-1.8 ./gradlew build`

> If you're using cmd, run `export JAVA_HOME=C:\path\to\jdk-1.8` on its own to set the environmental variable.
> If you're using PowerShell, run `$env:JAVA_HOME='C:\path\to\jdk-1.8'` on its own to set the environmental variable.

**Alternatively**, you can change your `JAVA_HOME` environmental variable permanently. This is left as an exercise to the reader.

## Use Gradle 4.4.1

**Symptom (Gradle version 2.0, too low):**
```
FAILURE: Build failed with an exception.

* What went wrong:
A problem occurred configuring root project 'forge-1.7.10-10.13.4.1614-1.7.10-src'.
> Could not resolve all dependencies for configuration ':classpath'.
   > Could not resolve net.minecraftforge.gradle:ForgeGradle:1.2-SNAPSHOT.
     Required by:
         :forge-1.7.10-10.13.4.1614-1.7.10-src:unspecified
      > Unable to load Maven meta-data from http://repo1.maven.org/maven2/net/minecraftforge/gradle/ForgeGradle/1.2-SNAPSHOT/maven-metadata.xml.
         > Could not GET 'http://repo1.maven.org/maven2/net/minecraftforge/gradle/ForgeGradle/1.2-SNAPSHOT/maven-metadata.xml'. Received status code 501 from server: HTTPS Required
      > Could not HEAD 'http://files.minecraftforge.net/maven/net/minecraftforge/gradle/ForgeGradle/1.2-SNAPSHOT/ForgeGradle-1.2-20211118.175523-305.pom'. Received status code 308 from server: Permanent Redirect
```

Gradle 4.4.1 is the highest version of Gradle that should work with all mods (it's the [highest version supported by the upstream fork of ForgeGradle](https://github.com/MinecraftModDevelopment/Modding-Resources/blob/master/version_info.md)). Gradle 2.0 will no longer work, as it doesn't support HTTPS.

If your build script uses a lower version than 4.4.1, or didn't come with a Gradle wrapper, try switching to it.

To do so, edit `gradle/wrapper/gradle-wrapper.properties` like this:

```patch
-distributionUrl=https\://services.gradle.org/distributions/gradle-2.0-bin.zip
+distributionUrl=https\://services.gradle.org/distributions/gradle-4.4.1-bin.zip
```

## Switch to a fork of ForgeGradle

**Symptom:**
```
:downloadClient FAILED

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':downloadClient'.
> java.io.IOException: Server returned HTTP response code: 403 for URL: http://s3.amazonaws.com/Minecraft.Download/versions/1.7.10/1.7.10.jar
```

ForgeGradle is the Gradle plugin used by 1.7.10 Forge mods. It stopped working in 2022 due to a Mojang API it's hardcoded to use going down. This was fixed in the GTNH fork of ForgeGradle (version 1.2.11), so let's change the build script to use it.

To do this, add jitpack as a build script repository, and replace the ForgeGradle version with GTNH.

In `build.gradle`:

> `+` means add that line, `-` means remove it.

```patch
buildscript {
    repositories {
        mavenCentral()
        maven {
            name = "forge"
            url = "http://files.minecraftforge.net/maven"
        }
        maven {
            name = "sonatype"
            url = "https://oss.sonatype.org/content/repositories/snapshots/"
        }
+       maven {
+           url = "https://jitpack.io"
+       }
    }
    dependencies {
-       classpath 'net.minecraftforge.gradle:ForgeGradle:1.2-SNAPSHOT'
+       classpath 'com.github.GTNewHorizons:ForgeGradle:1.2.11'
    }
}
```

**Alternatively,** you can use [any other active ForgeGradle fork](gradle-plugins.md#forgegradle) that also has the issue fixed.

**Alternatively,** you don't have to do this step at all if you have already successfully run `./gradlew setupDecompWorkspace` in a mod with a working build script (such as [GTNewHorizons/ExampleMod](https://github.com/GTNewHorizons/ExampleMod1.7.10)). In this case your Gradle cache has been filled with the necessary files, and a mod using the upstream version of ForgeGradle will manage to build.

# Further reading
- [https://gtnh.miraheze.org/wiki/Development#Getting_started](https://gtnh.miraheze.org/wiki/Development#Getting_started)
