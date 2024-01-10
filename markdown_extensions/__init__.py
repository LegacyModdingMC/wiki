from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension
import re
import sys
from pathlib import Path

class LMMCWikiExtension(Extension):
   def extendMarkdown(self, md):
       md.preprocessors.register(FaviconLinks(), 'faviconlinks', 100)

class FaviconLinks(Preprocessor):
    def run(self, lines):
        short2long = {
            "gh": "github",
            "cb": "codeberg",
            "mr": "modrinth",
            "cf": "curseforge",
            "mcf": "minecraftforum",
            "bb": "bitbucket",
            "gl": "gitlab",
            "mujp": "minecraftuserjp",
        }
        
        # website ids containing '<' are skipped to make sure we don't parse
        # example strings like this one: {<website_id>:<url>}
        p = re.compile(r'{([^<]*?):(.*?)}')

        new_lines = []
        for line in lines:
            while True:
                m = p.search(line)
                if not m:
                    break
                
                site = m[1]
                
                siteLong = short2long.get(site) or site
                
                iconPath = Path() / "docs" / "img" / "favicon" / (siteLong + ".png")
                
                if not iconPath.exists():
                    sys.exit(f"Unknown site `{site}` in favicon link {m[0]} (couldn't find {iconPath.absolute()})")
                
                url = m[2]
                
                line = line[:m.start()] + f"[![icon-{siteLong}](img/favicon/{siteLong}.png)]({url})" + line[m.end():]
            
            new_lines.append(line)
        return new_lines
