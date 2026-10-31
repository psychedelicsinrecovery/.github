# 🎞️ PIR® decks

Walk-throughs for a call or a first look, each as **Marp markdown** (the source, for your helper), **HTML**
(download it and it opens in any browser, with working links) and **PDF** (for your eyes, easy to share). Nothing in this folder is private.

| Deck | For | Open |
|---|---|---|
| **Welcome to PIR®** | anyone new to service at PIR®, and the AI helper beside them: where the proposals, procedures, decks and reading room live, how a change travels, how to ask for access | [PDF](welcome.marp.pdf) · [HTML](welcome.marp.html) (download, then open) · [markdown](welcome.marp.md) |

The deck wears PIR®'s purple (`5b2bb5`, `3b1f6e`, `7c3aed`, `ede9fe`) from
[TONES.md](https://github.com/drasticstatic/my-template/blob/main/proposals-template/TONES.md), and was made from
[my-template's decks-template](https://github.com/drasticstatic/my-template/tree/main/decks-template).

**To change it:** edit `welcome.marp.md`, then render both files from this folder and commit all three together,
after looking at the PDF pages:

```sh
export CHROME_PATH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
marp --no-stdin --html --allow-local-files welcome.marp.md -o welcome.marp.html
marp --no-stdin --html --allow-local-files welcome.marp.md --pdf -o welcome.marp.pdf
```

<sub>Started 2026-10-31. More: the [reading room](https://psychedelicsinrecovery.github.io/reading-room-public/) ·
the [public procedures](https://github.com/psychedelicsinrecovery/ops-standard-operating-procedures-public) ·
[ONBOARDING.md](../ONBOARDING.md).</sub>
