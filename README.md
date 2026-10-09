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
| `SUPPORT_EMAIL` | `support.html`, `delete-account.html`, `privacy.html` (via the policy) | The monitored support address |
| `PLAY_URL` | `index.html` | `https://play.google.com/store/apps/details?id=com.bitemarksinteractive.trashmob`, once the store page is public. Then change the button's text from "Coming soon to Google Play" to "Get it on Google Play" and remove `aria-disabled`. |
| `SITE_URL` | Only in the M13 policy | This site's address, e.g. `https://bitemarks-interactive.github.io` |
| `EFFECTIVE_DATE` | Only in the M13 policy | The date the M13 policy takes effect |

For the email in `support.html` and `delete-account.html`, a find-and-replace of `SUPPORT_EMAIL` is enough. For the policy, rebuild it with `--set` (next section).

## The privacy policy

The source is in the game repo: `TrashMob-git/docs/privacy-policy.html` (current) and `docs/privacy-policy-m13.html` (cloud saves and purchases, not published yet). `tools/wrap-policy.py` takes a policy's `<main>`, drops its comments, fills in placeholders and wraps it in this site's header and footer as `privacy.html`. Change the policy in the game repo first, then rebuild:

```bash
python tools/wrap-policy.py ../TrashMob-git/docs/privacy-policy.html --set=SUPPORT_EMAIL=you@example.com
```

When M13 ships (cloud saves, Google account linking, purchases):

```bash
python tools/wrap-policy.py ../TrashMob-git/docs/privacy-policy-m13.html --set=EFFECTIVE_DATE="1 March 2027" --set=SUPPORT_EMAIL=you@example.com --set=SITE_URL=https://bitemarks-interactive.github.io
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
   - **A GitHub organization (recommended):** github.com → your avatar → **Your organizations → New organization** → the **Free** plan → name it e.g. `bitemarks-interactive` (that becomes the address). The site is then `https://bitemarks-interactive.github.io`, and the game repo can move there later if you want.
   - **Your personal account:** the site is `https://dkmagnificent.github.io`. Simpler, but the address carries your username.
2. **Create the repo:** in the organization (or your account) → **New repository** → name it exactly `<name>.github.io` (e.g. `bitemarks-interactive.github.io`) → **Public** → don't add a README, licence or .gitignore → **Create repository**.
3. **Push this folder.** Tell Claude the repo's URL and it can push for you, or run:
   ```bash
   git remote add origin https://github.com/bitemarks-interactive/bitemarks-interactive.github.io.git
   git push -u origin main
   ```
4. **Turn on Pages:** the repo → **Settings → Pages** → Source **Deploy from a branch** → Branch `main`, folder `/ (root)` → **Save**. A minute later the site is live at `https://<name>.github.io`. Tick **Enforce HTTPS** if it isn't already.
5. **Support email.** Pick an address you'll actually check, since Play shows it publicly and players will write to it. Options: a free Gmail just for this (e.g. `bitemarks.support@gmail.com`), or an address on your own domain (step 6) forwarded to your inbox. Then fill in `SUPPORT_EMAIL` (above) and push.
6. **Custom domain (optional).** If you buy one (e.g. `bitemarks.games`): **Settings → Pages → Custom domain**, enter it, and at your registrar add the DNS records GitHub shows (four `A` records for the apex, or a `CNAME` to `<name>.github.io` for `www`). Verify the domain under your organization's **Settings → Pages** so nobody else can claim it. Wait for the certificate, then tick **Enforce HTTPS**. The Play Console URLs then use the new domain.
7. **Play Console:** paste the URLs:
   - **Store settings → Store listing contact details:** Email `SUPPORT_EMAIL`, Website `SITE_URL`.
   - **App content → Privacy policy:** `SITE_URL/privacy.html`.
   - **App content → Data safety → Delete account URL** (only once cloud saves ship): `SITE_URL/delete-account.html`.

## Updating screenshots

The six screenshots in `assets/screenshots/` are the store ones halved to 540×960. When the 1.0 store screenshots are retaken (the game repo's `docs/play-release.md` launch checklist), copy them here too, halved with nearest-neighbour scaling so the pixels stay sharp.
