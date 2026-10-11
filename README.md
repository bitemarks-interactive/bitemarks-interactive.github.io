# Bitemarks Interactive website

The public site for Bitemarks Interactive and Trash Mob: the game's home page, its privacy policy, support, and account deletion. Plain HTML and CSS, served by GitHub Pages straight from `main`, no build step. The game's code lives in a separate, private repo; this one is public because free GitHub Pages only serves public repos.

| Page | What it's for |
|---|---|
| `index.html` | Trash Mob: icon, feature graphic, description, six screenshots, the Play button |
| `privacy.html` | The privacy policy. **Generated, don't edit by hand** (see below). Play Console's privacy policy URL. |
| `support.html` | Contact and FAQ. Play's store listing website/contact. |
| `delete-account.html` | How to delete your data. Play Console's account deletion URL (needed once cloud saves ship). |
| `404.html` | GitHub Pages' not-found page |

The look is the game's: its palette, the Tiny5 pixel font (Google Fonts) for headings and buttons, notched panels, bevelled buttons (`assets/site.css`).

## Placeholders to fill in

| Placeholder | Where | Replace with |
|---|---|---|
| `PLAY_URL` | `index.html` | `https://play.google.com/store/apps/details?id=com.bitemarksinteractive.trashmob`, once the store page is public. Then change the button's text from "Coming soon to Google Play" to "Get it on Google Play" and remove `aria-disabled`. |
| `EFFECTIVE_DATE` | Only in the M13 policy | The date the M13 policy takes effect |

The support email (support@bitemarksinteractive.com) and the site address are already filled in, in the game repo's policies too.

## The privacy policy

The source is in the game repo: `TrashMob-git/docs/privacy-policy.html` (current) and `docs/privacy-policy-m13.html` (cloud saves and purchases, not published yet). `tools/wrap-policy.py` takes a policy's `<main>`, drops its comments, fills in placeholders and wraps it in this site's header and footer as `privacy.html`. Change the policy in the game repo first, then rebuild:

```bash
python tools/wrap-policy.py ../TrashMob-git/docs/privacy-policy.html
```

When M13 ships (cloud saves, Google account linking, purchases):

```bash
python tools/wrap-policy.py ../TrashMob-git/docs/privacy-policy-m13.html --set=EFFECTIVE_DATE="1 March 2027"
```

Then on `delete-account.html`, remove the "Takes effect when cloud saves ship" badge and replace the "Right now" panel. The game repo's `docs/play-console-answers.md` lists everything else to change in Play Console at M13.

## Preview locally

```bash
python -m http.server 5180
```

Then open http://localhost:5180. Check at 360 px wide (a phone) and at desktop width.

## Setup (owner only, once)

These steps need your GitHub login, so only you can do them.

1. **Where the site lives.** Either:
   - **A GitHub organization (recommended):** github.com → your avatar → **Your organizations → New organization** → the **Free** plan → name it e.g. `bitemarks-interactive` (that becomes the address). The site is then `https://bitemarksinteractive.com`, and the game repo can move there later if you want.
   - **Your personal account:** the site is `https://dkmagnificent.github.io`. Simpler, but the address carries your username.
2. **Create the repo:** in the organization (or your account) → **New repository** → name it exactly `<name>.github.io` (e.g. `bitemarks-interactive.github.io`) → **Public** → don't add a README, licence or .gitignore → **Create repository**.
3. **Push this folder.** Tell Claude the repo's URL and it can push for you, or run:
   ```bash
   git remote add origin https://github.com/bitemarks-interactive/bitemarks-interactive.github.io.git
   git push -u origin main
   ```
4. **Turn on Pages:** the repo → **Settings → Pages** → Source **Deploy from a branch** → Branch `main`, folder `/ (root)` → **Save**. A minute later the site is live at `https://<name>.github.io`. Tick **Enforce HTTPS** if it isn't already.
5. **Support email.** Pick an address you'll actually check, since Play shows it publicly and players will write to it. Options: a free Gmail just for this (e.g. `bitemarks.support@gmail.com`), or an address on your own domain (step 6) forwarded to your inbox. (Done: support@bitemarksinteractive.com.)
6. **Custom domain (optional).** If you buy one (e.g. `bitemarks.games`): **Settings → Pages → Custom domain**, enter it, and at your registrar add the DNS records GitHub shows (four `A` records for the apex, or a `CNAME` to `<name>.github.io` for `www`). Verify the domain under your organization's **Settings → Pages** so nobody else can claim it. Wait for the certificate, then tick **Enforce HTTPS**. The Play Console URLs then use the new domain.
7. **Play Console:** paste the URLs:
   - **Store settings → Store listing contact details:** Email `support@bitemarksinteractive.com`, Website `https://bitemarksinteractive.com`.
   - **App content → Privacy policy:** `https://bitemarksinteractive.com/privacy.html`.
   - **App content → Data safety → Delete account URL** (only once cloud saves ship): `https://bitemarksinteractive.com/delete-account.html`.

## Moving to Bitemarks Interactive's own domain

Done 2026-10-11: the site is at https://bitemarksinteractive.com (it was `bitemarks-interactive.github.io`), the studio's own domain, so AdMob's `app-ads.txt` (M13's rewarded ads, `TrashMob-git/docs/m13-ads.md`) can sit at the domain's root. The repo and GitHub Pages stay as they are; only the address changes. GitHub keeps redirecting the old github.io address to the new one, so links already handed out keep working.

1. **Point the domain at GitHub Pages** (owner, at the registrar):
   - Apex (`bitemarks.example`): four `A` records to `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`, and four `AAAA` records to `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`. Add a `CNAME` for `www` → `bitemarks-interactive.github.io` so both work.
   - Check GitHub's current list first: [Managing a custom domain for your GitHub Pages site](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site).
2. **Verify the domain** (owner): the organization → **Settings → Pages → Add a domain**, then the `TXT` record GitHub shows, so nobody else's Pages site can claim it.
3. **Switch the site** (Claude can do this once you send the domain): `python tools/set-domain.py bitemarks.example` writes `CNAME` and changes every `https://bitemarksinteractive.com` to the new address, here and in the game repo's docs. Commit and push both repos.
4. **HTTPS** (owner): the repo → **Settings → Pages**: wait for the certificate (minutes to a day), then tick **Enforce HTTPS**.
5. **Play Console** (owner): update the store listing's **Website** and the **Privacy policy** URL (and at M13 the **Delete account URL**) to the new domain.
6. **At M13:** add `app-ads.txt` at the site root with the AdMob line (`google.com, pub-…, DIRECT, f08c47fec0942fa0`). The store listing's Website must already be the new domain when AdMob crawls; check its app-ads.txt status after the first crawl.

## Updating screenshots

The six screenshots in `assets/screenshots/` are the store ones halved to 540×960. When the 1.0 store screenshots are retaken (the game repo's `docs/play-release.md` launch checklist), copy them here too, halved with nearest-neighbour scaling so the pixels stay sharp.
