# Comparison of IDEs

For writing mods, you will want a Java IDE. There are several available, and they each have their own strengths and weaknesses. This document compares the most common choices in the context of Minecraft mod development.

## IntelliJ

Currently the most popular choice, IntelliJ is packed with helpful features, but suffers from poor performance and interface customizability.

Pros:

- First-class Gradle support.
- Excellent debugger that can debug even without source code available.
- The MinecraftDev plugin makes Mixin development much more convenient, with autocompletion and support for placing breakpoints in mixins.

Cons:

- Compiler is much slower than Eclipse's.
    - This makes refactoring more time consuming, as you don't find out about all compilation errors immediately, triggering a slow compile is needed.
    - Hot swapping is also miserably slow, with waits of 10 seconds to hot swap a single method not being uncommon. (And this is with the [fast hot swap plugin](https://plugins.jetbrains.com/plugin/14832-single-hotswap).)
- The ability to customize the layout of the user interface is limited.
- Fairly resource intensive. Consumes twice as much RAM and 12 times as much disk space as Eclipse on this user's machine.

## Eclipse

Eclipse is less feature-packed than IntelliJ, but it also gets in your way less. It has a very fast compiler, but less convenience features than IntelliJ.

Pros:

- Blazing fast incremental compiler which lets you hotswap code instantly and immediately see any errors that pop up in the entire project as you edit code.
- Layout is very customizable.

Cons:

- Poor Gradle support.
    - Doesn't differentiate between compile-only and runtime dependency scopes, so compile-only dependencies will go on the class path when launching a mod using a native run configuration. This adds overhead, and causes some mods to outright fail to launch.
        - Can be worked around using [EclipseGradleDependencyScope](https://github.com/makamys/EclipseGradleDependencyScope).
    - Treated as a second class citizen by Gradle plugins. Importing RetroFuturaGradle projects requires some non-obvious extra steps, for example.
- Debugger is more barebones than IntelliJ's. The ability to debug code without source is crucially lacking.
- No IDE support for Mixin.
- Doesn't auto-detect indentation style, has to be set manually for each project.

## Visual Studio Code

I never actually tried the Java plugin of this one, but it's good as a code viewer for just quickly opening projects and searching their code without having to wait for an IDE to slowly import it.

It apparently shows errors in all classes automatically with the plugin.
