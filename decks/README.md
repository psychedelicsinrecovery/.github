# <img src="../profile/assets/icons/presentation.svg" width="28" height="28" alt=""> PIR® decks

Walk-throughs for a call or a first look, each as **Marp markdown** (the source, for your helper), **HTML**
(download it and it opens in any browser, with working links) and **PDF** (for your eyes, easy to share). Nothing in this folder is private.

| Deck | For | Open |
|---|---|---|
| **Welcome to PIR®** (twelve slides, seven numbered stops, a Lucide icon beside each idea) | anyone new to service at PIR®, and the AI helper beside them: your first hour (SOP-COM-001), anonymity first, five words, proposals, procedures, the reading room and your helper, how a change travels, how to answer and ask for access | [PDF](welcome.marp.pdf) · [HTML](welcome.marp.html) (download, then open) · [markdown](welcome.marp.md) |

The deck wears PIR®'s purple (`5b2bb5`, `3b1f6e`, `7c3aed`, `ede9fe`) from
[TONES.md](https://github.com/drasticstatic/my-template/blob/main/proposals-template/TONES.md), and was made from
[my-template's decks-template](https://github.com/drasticstatic/my-template/tree/main/decks-template). Only welcome decks live here; members-only decks live in the [reading room](https://github.com/psychedelicsinrecovery/reading-room).

**To change it:** edit `welcome.marp.md`, then render both files from this folder and commit all three together,
after looking at the PDF pages:

```sh
export CHROME_PATH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
marp --no-stdin --html --allow-local-files welcome.marp.md -o welcome.marp.html
marp --no-stdin --html --allow-local-files welcome.marp.md --pdf -o welcome.marp.pdf
```

<sub>Started 2026-10-31; rebuilt 2026-11-01 from the redesigned template (the walkthrough deck's style). More: the [reading room](https://psychedelicsinrecovery.github.io/reading-room-public/) ·
the [public procedures](https://github.com/psychedelicsinrecovery/ops-standard-operating-procedures-public) ·
[ONBOARDING.md](../ONBOARDING.md).</sub>
