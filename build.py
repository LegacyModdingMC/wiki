import scripts.expand_favicon_links
import glob
from pathlib import Path

docsDir = Path("docs")

if not docsDir.is_dir():
    sys.exit("Couldn't find docs directory. Make sure you are running this script from the root directory of the repo.")

for template in glob.glob("docs/*.template.md"):
    print("Converting", template)
    scripts.expand_favicon_links.convert(template, template.replace(".template", ""))

