import scripts.expand_favicon_links
import glob
from pathlib import Path

docsDir = Path("docs")

if not docsDir.is_dir():
    sys.exit("Couldn't find docs directory. Make sure you are running this script from the root directory of the repo.")

for template in glob.glob("docs-template/*.template.md"):
    print("Converting", template)
    templatePath = Path(template)
    outPath = templatePath.parent.parent / templatePath.parent.name.split("-")[0] / templatePath.name.replace(".template", "")
    scripts.expand_favicon_links.convert(template, outPath)

