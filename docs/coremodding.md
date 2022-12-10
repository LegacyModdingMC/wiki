# Coremodding

Coremodding is the act of modifying the game's code from a mod, as opposed to purely using the hooks provided by the modding API. If done poorly, it can cause compatibility issues that are very tricky to resolve. It is therefore recommended to use it with great caution.

A single modification to the game's code is referred to as a *patch*.

## Access Transformers

An Access Transformer lets you change the visibility of a field or method.

## ASM

Bytecode transformers (commonly referred to as ASM after [the library which handles most of the work](https://asm.ow2.io/)) are the most powerful tools available for modifying game code.

## Mixins

Mixin is a library that acts as a frontend to ASM. It allows creating patches in a much easier and significantly more readable way than ASM. However, it comes with some limitations.
