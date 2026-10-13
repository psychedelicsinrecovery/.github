# 🔄 Social previews: refresh guide + share-image ledger

When a link to one of PIR®'s GitHub Pages sites is pasted into a chat app, the app shows a
preview card (title, description and a share image) that it fetched **once** and then **cached**.
After a share image or title changes, old previews keep showing until each app is told to look again.
This file lists how to do that for each app, and which pages have their own tailored share image.

*Generated 2026-10-13 by the arrival kit's `social/social-previews.mjs` (canonical copy in
[my-template](https://github.com/drasticstatic/my-template/tree/main/changelog-template/arrival/social)).
Re-run it after deploys that add pages or change share images.*

## 🧰 How to refresh each app

| App | How to make it re-fetch | Notes |
|---|---|---|
| ✈️ **Telegram** | Message [@WebpageBot](https://t.me/WebpageBot) the link (you can send several links, one per line) | The bot replies with the fresh preview; new shares use it right away |
| 💼 **LinkedIn** | Paste the link into [Post Inspector](https://www.linkedin.com/post-inspector/) | Inspecting re-scrapes the page |
| 📘 **Facebook / Messenger** | Paste into the [Sharing Debugger](https://developers.facebook.com/tools/debug/) and press **Scrape Again** | Also accepts a batch of links |
| 💬 **Discord** | No refresh tool. Share the link with a harmless suffix such as `?v=2` | Discord caches per exact URL, so a new suffix gets a new preview |
| 🟪 **Slack** | No refresh tool. Use the `?v=2` suffix trick | Old messages keep their old unfurl |
| 🐦 **X (Twitter)** | No public validator any more. Use the `?v=2` suffix, or wait (cards refresh on their own, roughly a week) | |
| 🟢 **WhatsApp** | No refresh tool. Use the `?v=2` suffix | WhatsApp caches aggressively |
| 🦋 **Bluesky** / 🐘 **Mastodon** | Fetched when a post is written; nothing to clear | Each Mastodon server fetches its own copy |
| 💬 **iMessage** | Fetched on the sender's phone at send time | Nothing to clear |

**Rule of thumb:** after changing a share image, refresh Telegram (@WebpageBot), LinkedIn and
Facebook for the pages listed below. Use the `?v=2` suffix anywhere else.

## 🖼️ Share-image ledger

31 pages checked: **24 tailored**, 7 using the default card,
0 with no share image.

### ✨ Pages with their own tailored share image

| Page | Title | Share image |
|---|---|---|
| [psychedelicsinrecovery.github.io/changelog-astro-public/ledger](https://psychedelicsinrecovery.github.io/changelog-astro-public/ledger) | Ledger: every public change — PIR® AstroLog | [image](https://psychedelicsinrecovery.github.io/changelog-astro-public/og/ledger.jpg) |
| [psychedelicsinrecovery.github.io/changelog-astro-public/changelog/brand-assets/2026-10-12-the-ledger-reading-mode-whats-new](https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog/brand-assets/2026-10-12-the-ledger-reading-mode-whats-new) | The ledger: every public change in plain words, plus reading mode and what's new since your last visit — Changelog | [image](https://psychedelicsinrecovery.github.io/changelog-astro-public/og/changelog/brand-assets/2026-10-12-the-ledger-reading-mode-whats-new.jpg) |
| [psychedelicsinrecovery.github.io/changelog-astro-public/changelog/wordpress/2026-10-12-main-site-moves-onto-wpx-cdn](https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog/wordpress/2026-10-12-main-site-moves-onto-wpx-cdn) | The main site moves onto WPX's CDN, plus three wasted requests per page removed — Changelog | [image](https://psychedelicsinrecovery.github.io/changelog-astro-public/og/changelog/wordpress/2026-10-12-main-site-moves-onto-wpx-cdn.jpg) |
| [psychedelicsinrecovery.github.io/changelog-astro-public/changelog/brand-assets/2026-10-12-choose-how-you-arrive](https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog/brand-assets/2026-10-12-choose-how-you-arrive) | Choose how you arrive: a welcome guide, one search for everything, and a preview card for every entry — Changelog | [image](https://psychedelicsinrecovery.github.io/changelog-astro-public/og/changelog/brand-assets/2026-10-12-choose-how-you-arrive.jpg) |
| [psychedelicsinrecovery.github.io/changelog-astro-public/changelog/wordpress/2026-10-11-publicrelations-site-launched-calendar-root-cause-found](https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog/wordpress/2026-10-11-publicrelations-site-launched-calendar-root-cause-found) | A fifth PIR site launches, and the events calendar's real root cause gets found — Changelog | [image](https://psychedelicsinrecovery.github.io/changelog-astro-public/og/changelog/wordpress/2026-10-11-publicrelations-site-launched-calendar-root-cause-found.jpg) |
| [psychedelicsinrecovery.github.io/changelog-astro-public/changelog/brand-assets/2026-10-11-astrolog-joins-the-alex-family-look](https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog/brand-assets/2026-10-11-astrolog-joins-the-alex-family-look) | The AstroLog gets a new look, a star chart of everything shipped, and an RSS feed — Changelog | [image](https://psychedelicsinrecovery.github.io/changelog-astro-public/og/changelog/brand-assets/2026-10-11-astrolog-joins-the-alex-family-look.jpg) |
| [psychedelicsinrecovery.github.io/changelog-astro-public/changelog/wordpress/2026-10-10-live-stream-hub-v5-color-coded-zones](https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog/wordpress/2026-10-10-live-stream-hub-v5-color-coded-zones) | Live Stream Hub v5: color-coded time zones, one-click day cards, and a new schedule poster — Changelog | [image](https://psychedelicsinrecovery.github.io/changelog-astro-public/og/changelog/wordpress/2026-10-10-live-stream-hub-v5-color-coded-zones.jpg) |
| [psychedelicsinrecovery.github.io/changelog-astro-public/changelog/wordpress/2026-10-04-new-helpdesk-email-and-our-email-history](https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog/wordpress/2026-10-04-new-helpdesk-email-and-our-email-history) | A new helpdesk@ address, checkout follow-ups, and a look back at PIR's email — Changelog | [image](https://psychedelicsinrecovery.github.io/changelog-astro-public/og/changelog/wordpress/2026-10-04-new-helpdesk-email-and-our-email-history.jpg) |
| [psychedelicsinrecovery.github.io/changelog-astro-public/changelog/alex-desk/2026-10-04-meet-alex-helpdesks-in-the-works](https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog/alex-desk/2026-10-04-meet-alex-helpdesks-in-the-works) | Meet A.L.E.X. — a Discord helper and real helpdesks are on the way — Changelog | [image](https://psychedelicsinrecovery.github.io/changelog-astro-public/og/changelog/alex-desk/2026-10-04-meet-alex-helpdesks-in-the-works.jpg) |
| [psychedelicsinrecovery.github.io/changelog-astro-public/changelog/brand-assets/2026-10-04-github-home-for-pir-brand-and-literature](https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog/brand-assets/2026-10-04-github-home-for-pir-brand-and-literature) | PIR's logos now have an official home on GitHub — Changelog | [image](https://psychedelicsinrecovery.github.io/changelog-astro-public/og/changelog/brand-assets/2026-10-04-github-home-for-pir-brand-and-literature.jpg) |
| [psychedelicsinrecovery.github.io/changelog-astro-public/changelog/wordpress/2026-09-24-mobile-menu-now-scrolls-properly](https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog/wordpress/2026-09-24-mobile-menu-now-scrolls-properly) | The mobile menu now scrolls properly to reach every page — Changelog | [image](https://psychedelicsinrecovery.github.io/changelog-astro-public/og/changelog/wordpress/2026-09-24-mobile-menu-now-scrolls-properly.jpg) |
| [psychedelicsinrecovery.github.io/changelog-astro-public/changelog/wordpress/2026-09-23-mobile-menu-button-now-reliable](https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog/wordpress/2026-09-23-mobile-menu-button-now-reliable) | The mobile menu button now works reliably on phones — including iPhone — Changelog | [image](https://psychedelicsinrecovery.github.io/changelog-astro-public/og/changelog/wordpress/2026-09-23-mobile-menu-button-now-reliable.jpg) |
| [psychedelicsinrecovery.github.io/changelog-astro-public/changelog/wordpress/2026-09-23-header-stays-out-of-your-way](https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog/wordpress/2026-09-23-header-stays-out-of-your-way) | The site header now stays out of your way while you scroll — and comes right back when you need it — Changelog | [image](https://psychedelicsinrecovery.github.io/changelog-astro-public/og/changelog/wordpress/2026-09-23-header-stays-out-of-your-way.jpg) |
| [psychedelicsinrecovery.github.io/changelog-astro-public/changelog/wordpress/2026-09-22-footer-icons-centered-on-mobile](https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog/wordpress/2026-09-22-footer-icons-centered-on-mobile) | Footer social icons now properly centered on mobile — Changelog | [image](https://psychedelicsinrecovery.github.io/changelog-astro-public/og/changelog/wordpress/2026-09-22-footer-icons-centered-on-mobile.jpg) |
| [psychedelicsinrecovery.github.io/changelog-astro-public/library/capabilities-astra](https://psychedelicsinrecovery.github.io/changelog-astro-public/library/capabilities-astra) | Astra theme MCP capabilities — Library | [image](https://psychedelicsinrecovery.github.io/changelog-astro-public/og/library/capabilities-astra.jpg) |
| [psychedelicsinrecovery.github.io/changelog-astro-public/library/capabilities-emcp-tools](https://psychedelicsinrecovery.github.io/changelog-astro-public/library/capabilities-emcp-tools) | Elementor MCP (emcp) tool capabilities — Library | [image](https://psychedelicsinrecovery.github.io/changelog-astro-public/og/library/capabilities-emcp-tools.jpg) |
| [psychedelicsinrecovery.github.io/changelog-astro-public/library/footer-reconnaissance](https://psychedelicsinrecovery.github.io/changelog-astro-public/library/footer-reconnaissance) | Footer reconnaissance: Astra footer internals — Library | [image](https://psychedelicsinrecovery.github.io/changelog-astro-public/og/library/footer-reconnaissance.jpg) |
| [psychedelicsinrecovery.github.io/changelog-astro-public/library/how-alex-works](https://psychedelicsinrecovery.github.io/changelog-astro-public/library/how-alex-works) | How A.L.E.X. works (and why it's built this way) — Library | [image](https://psychedelicsinrecovery.github.io/changelog-astro-public/og/library/how-alex-works.jpg) |
| [psychedelicsinrecovery.github.io/changelog-astro-public/library/how-to-reconnect-mcp](https://psychedelicsinrecovery.github.io/changelog-astro-public/library/how-to-reconnect-mcp) | How to reconnect the MCP tools — Library | [image](https://psychedelicsinrecovery.github.io/changelog-astro-public/og/library/how-to-reconnect-mcp.jpg) |
| [psychedelicsinrecovery.github.io/changelog-astro-public/library/email-and-domain-basics](https://psychedelicsinrecovery.github.io/changelog-astro-public/library/email-and-domain-basics) | PIR's email setup, explained for volunteers — Library | [image](https://psychedelicsinrecovery.github.io/changelog-astro-public/og/library/email-and-domain-basics.jpg) |
| [psychedelicsinrecovery.github.io/changelog-astro-public/library/site-health-and-plugins](https://psychedelicsinrecovery.github.io/changelog-astro-public/library/site-health-and-plugins) | Site health, caching layers, and plugin inventory — Library | [image](https://psychedelicsinrecovery.github.io/changelog-astro-public/og/library/site-health-and-plugins.jpg) |
| [psychedelicsinrecovery.github.io/changelog-astro-public/library/header-sticky-scroll-and-mobile-nav](https://psychedelicsinrecovery.github.io/changelog-astro-public/library/header-sticky-scroll-and-mobile-nav) | The header saga: sticky scroll-reveal + mobile pill nav — Library | [image](https://psychedelicsinrecovery.github.io/changelog-astro-public/og/library/header-sticky-scroll-and-mobile-nav.jpg) |
| [psychedelicsinrecovery.github.io/changelog-astro-public/library/search-widget-mobile-fix](https://psychedelicsinrecovery.github.io/changelog-astro-public/library/search-widget-mobile-fix) | The search widget's mobile horizontal-scroll saga — Library | [image](https://psychedelicsinrecovery.github.io/changelog-astro-public/og/library/search-widget-mobile-fix.jpg) |
| [psychedelicsinrecovery.github.io/changelog-astro-public/library/why-the-site-was-slow-and-it-wasnt-ai](https://psychedelicsinrecovery.github.io/changelog-astro-public/library/why-the-site-was-slow-and-it-wasnt-ai) | Why the site got slow (and why it wasn't Claude, Littlebird, or AI) — Library | [image](https://psychedelicsinrecovery.github.io/changelog-astro-public/og/library/why-the-site-was-slow-and-it-wasnt-ai.jpg) |

### 🪪 Pages using the default card

- [psychedelicsinrecovery.github.io/](https://psychedelicsinrecovery.github.io/)
- [psychedelicsinrecovery.github.io/changelog-astro-public/](https://psychedelicsinrecovery.github.io/changelog-astro-public/)
- [psychedelicsinrecovery.github.io/changelog-astro-public/changelog](https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog)
- [psychedelicsinrecovery.github.io/changelog-astro-public/library](https://psychedelicsinrecovery.github.io/changelog-astro-public/library)
- [psychedelicsinrecovery.github.io/changelog-astro-public/changelog/wordpress](https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog/wordpress)
- [psychedelicsinrecovery.github.io/changelog-astro-public/changelog/alex-desk](https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog/alex-desk)
- [psychedelicsinrecovery.github.io/changelog-astro-public/changelog/brand-assets](https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog/brand-assets)

## 📋 Copy-paste list for @WebpageBot

```
https://psychedelicsinrecovery.github.io/
https://psychedelicsinrecovery.github.io/changelog-astro-public/
https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog
https://psychedelicsinrecovery.github.io/changelog-astro-public/library
https://psychedelicsinrecovery.github.io/changelog-astro-public/ledger
https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog/wordpress
https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog/alex-desk
https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog/brand-assets
https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog/brand-assets/2026-10-12-the-ledger-reading-mode-whats-new
https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog/wordpress/2026-10-12-main-site-moves-onto-wpx-cdn
https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog/brand-assets/2026-10-12-choose-how-you-arrive
https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog/wordpress/2026-10-11-publicrelations-site-launched-calendar-root-cause-found
https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog/brand-assets/2026-10-11-astrolog-joins-the-alex-family-look
https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog/wordpress/2026-10-10-live-stream-hub-v5-color-coded-zones
https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog/wordpress/2026-10-04-new-helpdesk-email-and-our-email-history
https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog/alex-desk/2026-10-04-meet-alex-helpdesks-in-the-works
https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog/brand-assets/2026-10-04-github-home-for-pir-brand-and-literature
https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog/wordpress/2026-09-24-mobile-menu-now-scrolls-properly
https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog/wordpress/2026-09-23-mobile-menu-button-now-reliable
https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog/wordpress/2026-09-23-header-stays-out-of-your-way
https://psychedelicsinrecovery.github.io/changelog-astro-public/changelog/wordpress/2026-09-22-footer-icons-centered-on-mobile
https://psychedelicsinrecovery.github.io/changelog-astro-public/library/capabilities-astra
https://psychedelicsinrecovery.github.io/changelog-astro-public/library/capabilities-emcp-tools
https://psychedelicsinrecovery.github.io/changelog-astro-public/library/footer-reconnaissance
https://psychedelicsinrecovery.github.io/changelog-astro-public/library/how-alex-works
https://psychedelicsinrecovery.github.io/changelog-astro-public/library/how-to-reconnect-mcp
https://psychedelicsinrecovery.github.io/changelog-astro-public/library/email-and-domain-basics
https://psychedelicsinrecovery.github.io/changelog-astro-public/library/site-health-and-plugins
https://psychedelicsinrecovery.github.io/changelog-astro-public/library/header-sticky-scroll-and-mobile-nav
https://psychedelicsinrecovery.github.io/changelog-astro-public/library/search-widget-mobile-fix
https://psychedelicsinrecovery.github.io/changelog-astro-public/library/why-the-site-was-slow-and-it-wasnt-ai
```
