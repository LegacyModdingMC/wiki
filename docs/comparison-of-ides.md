# Comparison of IDEs

There are several IDEs available for Java development, and they each have their own pros and cons. This document compares the most common choices in the context of Minecraft mod development.

## IntelliJ

### Pros

* First-class Gradle support.
* Excellent debugger that can debug without source code.
* Auto-detects indentation style.
* The MinecraftDev plugin simplifies the process of writing mixins.
* The most popular choice, so support from the community is readily available.

### Cons

* Everyone builds projects via Gradle, which can result in very slow hot swapping (and compilation times).
	* *Can you build mods without Gradle? I couldn't figure it out.*
* Only shows errors in opened source files. Seeing all errors requires running a build or a (slow) code inspection task.
* Fairly resource intensive. Consumes twice as much RAM and 12 times as much disk space as Eclipse on this user's machine.
* The layout of the interface is not very customizable.

## Eclipse

### Pros

* You can build projects without Gradle, which guarantees nearly instantaneous hot swapping.
* Shows errors in all classes automatically.
* Layout is very customizable.

### Cons

* Poor Gradle support. It may be necessary to launch mods using the clunky and slow `runClient` Gradle task (which cannot(?) be launched with a debugger with a single button press).
	* Doesn't differentiate between compile-only and runtime dependency scopes, so compile-only dependencies will go on the class path when launching a mod using a native run configuration. This adds overhead, and causes some mods to fail to launch.
		* Can be worked around using [EclipseGradleDependencyScope](https://github.com/makamys/EclipseGradleDependencyScope).
	* Build scripts that rely on Gradle to launch the mod must be launched using `runClient`.
* Doesn't auto-detect indentation style, has to be set manually for each project.
* No IDE support for Mixin.

## Visual Studio Code

### Pros

* Can be used to quickly open projects and browse their code without analysis.
* Shows errors in all classes automatically.
* ?

### Cons

* ?
