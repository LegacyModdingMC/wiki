We use a custom Markdown extension which adds a compact syntax for favicon links:
```
{<website_id>:<url>}
```

Where `website_id` is the id of the site, and url is the url of the link.

These will be replaced with an image of the website's favicon which links to the url.

## Available websites

| Icon | ID | URL |
| -- | -- | -- |
| ![](../docs/img/favicon/bitbucket.png) | bb | bitbucket.org |
| ![](../docs/img/favicon/codeberg.png) | cb | codeberg.org |
| ![](../docs/img/favicon/curseforge.png) | cf | curseforge.com |
| ![](../docs/img/favicon/electricalage.png) | electricalage | electrical-age.net |
| ![](../docs/img/favicon/flansmod.png) | flansmod | flansmod.com |
| ![](../docs/img/favicon/github.png) | gh | github.com |
| ![](../docs/img/favicon/gitlab.png) | gl | gitlab.com |
| ![](../docs/img/favicon/gregtech.png) | gregtech | gregtech.overminddl1.com |
| ![](../docs/img/favicon/minecraftforum.png) | mcf | minecraftforum.net |
| ![](../docs/img/favicon/modrinth.png) | mr | modrinth.com |
| ![](../docs/img/favicon/minecraftuserjp.png) | mujp | forum.minecraftuser.jp |

## Example

```
Cool Mod {gh:https://github.com/coolguy/CoolMod} {cf:https://legacy.curseforge.com/minecraft/mc-mods/coolmod} {mr:https://modrinth.com/mod/coolmod}
```

Gets turned into:

> Cool Mod [![icon-github](../docs/img/favicon/github.png)](https://github.com/coolguy/CoolMod) [![icon-curseforge](../docs/img/favicon/curseforge.png)](https://legacy.curseforge.com/minecraft/mc-mods/coolmod) [![icon-modrinth](../docs/img/favicon/modrinth.png)](https://modrinth.com/mod/coolmod)