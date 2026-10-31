---
marp: true
theme: default
paginate: true
size: 16:9
title: Welcome to PIR® — Psychedelics In Recovery™
description: A first walk for people in service at PIR® (and the AI helper beside them): where the proposals, procedures, decks and reading room live, how a change travels, and how to ask for access.
style: |
  /* Tone: the four shades of the organisation's family, from my-template/proposals-template/TONES.md (bare hex, no #).
     The ground is the DEEP shade mixed into near-black, headings are the TINT with a PRIMARY rule, so every family
     reads on the dark ground, purple included. Do not hand-edit colours below; change the four placeholders. */
  section { background: color-mix(in srgb, #3b1f6e 32%, #0b0d12); color: #eef0f3; font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 25px; padding: 52px 64px 56px; border-left: 10px solid #5b2bb5; }
  section::after { color: color-mix(in srgb, #ede9fe 60%, #6b7280); font-size: 0.6em; }
  section h1 { color: #ede9fe !important; border-bottom: 3px solid #5b2bb5; padding-bottom: 8px; font-size: 1.45em; margin-bottom: 0.45em; }
  section h2 { color: color-mix(in srgb, #5b2bb5 45%, white) !important; font-size: 1.1em; margin: 0.2em 0 0.4em; }
  strong { color: #ede9fe; }
  a { color: color-mix(in srgb, #5b2bb5 40%, white); text-decoration: underline; text-decoration-color: #7c3aed; }
  code { background: color-mix(in srgb, #3b1f6e 70%, #1f2937); color: #ede9fe; padding: 1px 6px; border-radius: 4px; font-size: 0.82em; }
  pre { background: color-mix(in srgb, #3b1f6e 45%, #111318); color: #ede9fe; border: 1px solid #7c3aed; border-radius: 8px; padding: 12px 16px; font-size: 0.68em; line-height: 1.35; }
  pre code { background: transparent; color: inherit; padding: 0; font-size: 1em; }
  table { border-collapse: collapse; width: 100%; font-size: 0.74em; }
  section table th { background: #3b1f6e; color: #ede9fe; padding: 6px 10px; text-align: left; border: 1px solid #7c3aed; }
  section table td { background: color-mix(in srgb, #3b1f6e 22%, #14161c); color: #eef0f3; padding: 5px 10px; border: 1px solid color-mix(in srgb, #7c3aed 45%, #14161c); }
  blockquote { border-left: 4px solid #5b2bb5; background: color-mix(in srgb, #3b1f6e 40%, #111318); color: #eef0f3; padding: 8px 16px; margin: 0.6em 0; font-style: normal; }
  li { margin: 0.18em 0; }
  .small { font-size: 0.66em; color: color-mix(in srgb, #ede9fe 55%, #6b7280); }
  .fill { color: #0b0d12; background: #ede9fe; padding: 0 6px; border-radius: 3px; }
  .shades { display: flex; height: 14px; margin: 18px 0 0; border-radius: 3px; overflow: hidden; }
  .shades span { flex: 1; }
  .s1 { background: #3b1f6e } .s2 { background: #7c3aed } .s3 { background: #5b2bb5 } .s4 { background: #ede9fe }
  section.lead { border-left: none; background: linear-gradient(135deg, #3b1f6e 0%, color-mix(in srgb, #3b1f6e 30%, #0b0d12) 75%); justify-content: center; }
  section.lead h1 { border: none; font-size: 2.3em; color: #ffffff !important; margin-bottom: 0.1em; }
  section.lead h2 { color: #ede9fe !important; font-weight: 400; font-size: 1.15em; }
  section.lead .kicker { color: #ede9fe; letter-spacing: 0.25em; font-size: 0.6em; font-weight: 700; opacity: .85; }
---

<!--
  PIR®'s newcomer deck, instantiated 2026-10-31 from my-template/decks-template/welcome.marp.md in PIR® purple
  (5b2bb5 / 3b1f6e / 7c3aed / ede9fe, my-template/proposals-template/TONES.md). Public: nothing here is private.
  Render (from this folder):
    export CHROME_PATH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    marp --no-stdin --html --allow-local-files welcome.marp.md -o welcome.marp.html
    marp --no-stdin --html --allow-local-files welcome.marp.md --pdf -o welcome.marp.pdf
  Commit the three files together, and look at the PDF pages first.
-->

<!-- _class: lead -->
<!-- _paginate: false -->

<span class="kicker">WELCOME</span>

# Welcome to PIR®

## Psychedelics In Recovery™: where the proposals, the procedures and the decks live, how a change travels, and how to answer

<span class="small">A first walk for anyone in service, and for the AI helper beside them. Every slide points at a real page; the deck only shows the order to open them in. Members: your helper's own welcome is [WELCOME-FOR-YOUR-HELPER.md](https://github.com/psychedelicsinrecovery/.github-private/blob/main/WELCOME-FOR-YOUR-HELPER.md) in the members' home (it opens only for signed-in members).</span>

<div class="shades"><span class="s1"></span><span class="s2"></span><span class="s3"></span><span class="s4"></span></div>

---

# What you will find here

| Kind | What it is | Where |
|---|---|---|
| **Reading room** | one front door: what anyone may read, and the way into the members' room | [psychedelicsinrecovery.github.io/reading-room-public](https://psychedelicsinrecovery.github.io/reading-room-public/) |
| **Proposals** | *should we?* One folder, one page, a PDF beside it; members only | [psychedelicsinrecovery/proposals](https://github.com/psychedelicsinrecovery/proposals) |
| **Procedures** (SOPs) | *this is how we do it now*; the pages marked public | [ops-standard-operating-procedures-public](https://github.com/psychedelicsinrecovery/ops-standard-operating-procedures-public) |
| **Decks** | walk-throughs like this one, for a call or a first look | [.github/decks](https://github.com/psychedelicsinrecovery/.github/tree/main/decks) |

> Everything PIR® writes for its service work wears the same purple, these four shades, so you can tell whose page it is before you read a word.

<div class="shades"><span class="s1"></span><span class="s2"></span><span class="s3"></span><span class="s4"></span></div>

---

# Anonymity first

- Never connect a person's **name, face, voice or handle** to recovery, to a meeting, or to this fellowship, unless they have chosen to share it publicly themselves.
- People appear by **first name and last initial**, and only those in visible service.
- Never put anyone's recovery, sponsor relationship, private messages, or personal, medical or legal history into a repository, a proposal or a chat with a helper that writes to one.
- **No secrets, ever.** No password or key in a chat or a file; the secret scan stops one that slips through.

> If you are not sure whether something may be shared, it may not, yet. Ask first.

---

# Five words, and you can find your way

| Word | Means |
|---|---|
| **Repository** | a folder that remembers every change and who made it |
| **`preview` and `main`** | the rehearsal copy and the live copy of the same folder |
| **Promote** | the pull request that moves rehearsal to live; a person with the role merges it |
| **Public twin** | a public copy that carries only the pages marked public; nobody edits it by hand |
| **Issue** | a conversation thread: the easiest way to ask or answer |

<span class="small">You never need to type a branch command. You read, you comment, and you say yes or no.</span>

---

# How a proposal reads

1. **TL;DR**: five lines, the only part you have to read.
2. **What is offered**: how things are today, beside what is proposed.
3. **Decisions log**: what was chosen, when, and by whom. Yours stay blank until you choose.
4. **Asks**: usually none, sometimes one.
5. **Sources, and what could not be confirmed**: folded away, never hidden.

Every proposal comes as a **PDF for your eyes** and the **markdown it was made from** for your helper's. Org-wide proposals live in [psychedelicsinrecovery/proposals](https://github.com/psychedelicsinrecovery/proposals) on their way to the Board's inbox (`board-of-directors/proposals/`); each committee keeps its own. Start with **000 Start here**.

---

# Procedures: how we do it now

- A procedure is named `SOP-<Department>-<ID>-<name>`: `SOP-OPS-001` is the first operations procedure.
- It is a **draft** until the officers tag an approved version; the tag is the approval.
- Each one opens with a badge row: the number in **PIR® purple**, its status, the date it last changed, and **For** in the slate every organisation shares.
- Every procedure is also a PDF, rendered on each push.

> Read **SOP-OPS-001 "How a change travels"** first, then **SOP-IT-002**, the reading room and helper access. **SOP-GOV-001** says how a Board member joins the Board's reading.

<span class="small">The procedures visitors may read: [ops-standard-operating-procedures-public](https://github.com/psychedelicsinrecovery/ops-standard-operating-procedures-public). Members read all of them, drafts included, in [ops-standard-operating-procedures](https://github.com/psychedelicsinrecovery/ops-standard-operating-procedures).</span>

---

# The reading room, and your helper

- **Open to everyone:** [psychedelicsinrecovery.github.io/reading-room-public](https://psychedelicsinrecovery.github.io/reading-room-public/), the pages marked public, in a browser, no GitHub account needed.
- **For members:** the private room, [psychedelicsinrecovery/reading-room](https://github.com/psychedelicsinrecovery/reading-room), gathers proposals, procedures and decks, each as a page and a PDF. Open it signed in; a **404** means signed out or not yet in the **readers** team.
- **Your helper** (Claude, ChatGPT, Codex, Littlebird, any of them) reads the same pages once connected with your permission, never more than you can. Point it at the markdown, and first at [WELCOME-FOR-YOUR-HELPER.md](https://github.com/psychedelicsinrecovery/.github-private/blob/main/WELCOME-FOR-YOUR-HELPER.md) (members only).

> A good first question for your helper: *"Read 000 Start here and tell me what is waiting for my answer."*

---

# The road a change travels

```
  an edit  ──→  preview  (the rehearsal: read it here, comment here)
                   │
                   │  "Promote: <what>"  pull request, preview into main
                   │  a person with the role merges it
                   ▼
                  main  (the live copy)
                   │
                   │  automatic sync: only pages marked public
                   ▼
            the public twin  (what visitors see)
```

- If a link to `main` still shows old words while someone says the change is done, it is on `preview`: the Promote has not been merged yet.
- A page that is not marked public never leaves the private repository, on any branch.

---

# How to answer

| You want to… | Do this |
|---|---|
| say yes, no, or "not yet" to a proposal | open an **issue** titled with its number, or ask a committee chair to note it in the decisions log |
| comment on a change before it goes live | comment on the **Promote** pull request |
| ask a question about a procedure | open an issue in the procedures repository, naming the SOP |
| ask your helper to answer for you | let it draft; **you** read it and post it under your name |
| get access, or more of it | ask the Tech Committee (next slide) |

> There is no wrong door. A question in the wrong place gets moved, not lost.

---

# How to ask for access

**The Tech Committee** looks after PIR®'s GitHub and who can read what.

1. Type **`/github`** in [PIR®'s Discord](https://discord.gg/MyprTq8w95), or use the [web helpdesk](https://psychedelicsinrecovery.github.io/alex-desk-public/portal.html), and name your service role: *"reading room, please"*.
2. Accept GitHub's invitation, then turn on **two-factor login**: [ONBOARDING.md](https://github.com/psychedelicsinrecovery/.github/blob/main/ONBOARDING.md) shows how, and how to connect a helper.
3. An owner adds you to the team your service needs (**readers** for the reading room).

<span class="small">Ask too when a link shows 404, a page looks out of date, or you are not sure where an answer belongs. Where to start next: the [reading room](https://psychedelicsinrecovery.github.io/reading-room-public/), **000 Start here** in [proposals](https://github.com/psychedelicsinrecovery/proposals), then **SOP-OPS-001**.</span>

<div class="shades"><span class="s1"></span><span class="s2"></span><span class="s3"></span><span class="s4"></span></div>
