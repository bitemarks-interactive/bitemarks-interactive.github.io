"""Moves the site's address to Bitemarks Interactive's own domain.

    python tools/set-domain.py bitemarks.example          # the apex domain
    python tools/set-domain.py www.bitemarks.example      # or a subdomain

Writes CNAME (GitHub Pages' custom domain file) and replaces the old address
(https://bitemarks-interactive.github.io, or whatever CNAME held before) with
https://<domain> in this site and in the game repo's docs next to it
(../TrashMob-git/docs and CLAUDE.md). Commit and push both repos afterwards.
"""
import re
import sys
from pathlib import Path

if len(sys.argv) != 2 or not re.fullmatch(r"[a-z0-9.-]+\.[a-z]{2,}", sys.argv[1]):
    sys.exit(__doc__)
domain = sys.argv[1]
site = Path(__file__).resolve().parent.parent
cname = site / "CNAME"
old = [f"https://{cname.read_text().strip()}"] if cname.exists() else []
old.append("https://bitemarks-interactive.github.io")
new = f"https://{domain}"

game = site.parent / "TrashMob-git"
files = [*site.glob("*.html"), site / "README.md",
         *game.glob("docs/*.html"), *game.glob("docs/*.md"), game / "CLAUDE.md"]
for f in files:
    if not f.exists():
        continue
    text = f.read_text(encoding="utf-8")
    changed = text
    for o in old:
        if o != new:
            changed = changed.replace(o, new)
    if changed != text:
        f.write_text(changed, encoding="utf-8", newline="\n")
        print(f"updated {f}")
cname.write_text(domain + "\n", encoding="utf-8", newline="\n")
print(f"wrote {cname} ({domain})")
