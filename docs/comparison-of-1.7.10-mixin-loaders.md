# Comparison of 1.7.10 Mixin Loaders

|   | [SpongeMixins](https://github.com/GTNewHorizons/SpongeMixins) | [Grimoire](https://github.com/Aizistral-Studios/Grimoire) | [MBL](https://github.com/tox1cozZ/mixin-booter-legacy) | [GasStation](https://github.com/FalsePattern/GasStation) | [GTNHMixins](https://github.com/GTNewHorizons/GTNHMixins) | [GTNHMixinsLite](https://github.com/makamys/GTNHMixinsLite) | [UniMixins](https://github.com/LegacyModdingMC/UniMixins) |
| -- | -- | -- | -- | -- | -- | -- | -- |
| Mixin 0.7 | ✅ (0.7.11/0.7.12) | ✅ (0.7.11) | | ✴️ (Partial compat) | | | ✴️ (Partial compat) |
| Mixin 0.8 | | | ✅ (0.8.2) | ✅ (0.8.5-GasMix) | ✅ (0.8.5-GTNH) | | ✅ (0.8.5-UniMix) |
| ASM <sup>[ASM]</sup><br><span style="opacity: 0.6;font-size: 0.8em;">(org.spongepowered&#8203;.asm.lib)</span> | ✅ (5.2) | ✅ (5.2) | | ✅ (5.2) | | | ✅ (9.4) |
| ASM <sup>[ASM]</sup><br><span style="opacity: 0.6;font-size: 0.8em;">(org.spongepowered&#8203;.libraries&#8203;.org.objectweb.asm)</span> | | | ✅ (5.2) | | ✅ (9.4) | | ✴️ (Emulated) |
| SpongeMixins extras <sup>[1]</sup> | ✅ | | | ✅ | ✅ | | ✅ |
| Grimoire extras <sup>[2]</sup> | | ✅ | | | | |
| MixinBooterLegacy extras <sup>[3]</sup> | | | ✅ | ✅ | | | ✅ |
| GasStation extras <sup>[4]</sup> <sup>[NOP]</sup> | | | | ✅ | | | ✅ |
| MixinExtras <br><span style="opacity: 0.6;font-size: 0.8em;">(com.llamalad7.mixinextras)</span> | | | | ✅ | | | ✅ |
| MixinExtras <br><span style="opacity: 0.6;font-size: 0.8em;">(io.github.tox1cozz.mixinextras)</span> | | | ✅ | | | | ✅ |
| MixinExtras <br><span style="opacity: 0.6;font-size: 0.8em;">(com.gtnewhorizon.mixinextras)</span> | | | | | ✅ | ✅ | ✅ |
| GTNHMixins extras <sup>[5]</sup> | | | | | ✅ | ✅ | ✅ |
| Mixingasm <sup>[6]</sup> <sup>[SEP]</sup> | | | | ✅ | | | ✅ |

### Legend

* [ASM] Referenced by mods in mixin config plugins. FalsePatternLib and Unimixins:Compat automatically remap config plugins to use the existing package name. 
* [NOP] Not actually functional (as of 2023-01-31.) <sup>[[issue]](https://github.com/FalsePattern/GasStation/issues/15)</sup>
* [SEP] Available separately.

### Packages

* [1] `ru.timeconqueror.spongemixins`
* [2] `io.github.crucible`
* [3] `io.github.tox1cozz.mixinbooterlegacy`
* [4] `com.falsepattern.gasstation`
* [5] `com.gtnewhorizon.gtnhmixins`
* [6] `makamys.mixingasm`

## See also

* [List of "Essential" 1.7.10 Mods ≫ Mixin mods](https://gist.github.com/makamys/7cb74cd71d93a4332d2891db2624e17c#mixin-mods)
