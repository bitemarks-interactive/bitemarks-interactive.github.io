"""Builds privacy.html from a policy page in the game repo, in the site's look.

    python tools/wrap-policy.py ../TrashMob-git/docs/privacy-policy.html        # the current policy (0.9.x)
    python tools/wrap-policy.py ../TrashMob-git/docs/privacy-policy-m13.html    # when cloud saves ship

The game repo's docs/ copy stays the source; this only re-dresses its <main>. Placeholders
(SUPPORT_EMAIL, SITE_URL, EFFECTIVE_DATE) can be filled in with --set=KEY=value.
"""
import re
import sys
from pathlib import Path

args = [a for a in sys.argv[1:] if not a.startswith("--set")]
sets = dict(a.split("=", 1)[1].split("=", 1) for a in sys.argv[1:] if a.startswith("--set=")) if any(a.startswith("--set=") for a in sys.argv[1:]) else {}
if len(args) != 1:
    sys.exit(__doc__)
source = Path(args[0]).read_text(encoding="utf-8")
main = re.search(r"<main>(.*)</main>", source, re.S).group(1).strip()
main = re.sub(r"<!--.*?-->", "", main, flags=re.S)
for key, value in sets.items():
    main = main.replace(key, value)

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Trash Mob Privacy Policy · Bitemarks Interactive</title>
<meta name="description" content="What Trash Mob collects (nothing, for now), and how to reach us.">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Tiny5&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="./">Bitemarks <span>Interactive</span></a>
    <nav aria-label="Site">
      <ul>
        <li><a href="./">Trash Mob</a></li>
        <li><a href="support.html">Support</a></li>
        <li><a href="privacy.html" aria-current="page">Privacy</a></li>
        <li><a href="delete-account.html">Delete data</a></li>
      </ul>
    </nav>
  </div>
</header>

<main class="wrap legal">
{main}
</main>

<footer class="site-footer">
  <div class="wrap">
    <p>© 2026 Bitemarks Interactive · <a href="support.html">Support</a> · <a href="privacy.html">Privacy</a> · <a href="delete-account.html">Delete your data</a></p>
  </div>
</footer>
</body>
</html>
"""
out = Path(__file__).resolve().parent.parent / "privacy.html"
out.write_text(page, encoding="utf-8", newline="\n")
print(f"wrote {out}")
