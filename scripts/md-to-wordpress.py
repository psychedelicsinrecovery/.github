#!/usr/bin/env python3
"""📝 Markdown → WordPress HTML, for PIR® docs that live canonically on GitHub.

Converts the subset of Markdown our docs use (headings, paragraphs, nested lists, tables,
blockquotes, links, bold/italic/code, <a id> anchors, horizontal rules) into clean HTML for a
WordPress page's content, then appends a footer pointing back to the GitHub source.

Usage:
  python3 scripts/md-to-wordpress.py privacy-policy.md > /tmp/privacy.html
  python3 scripts/md-to-wordpress.py privacy-policy.md --source-url https://github.com/... > out.html

Then paste the HTML into the page (Code editor), or have an agent push it via EMCP .
The first "# Title" line is dropped because WordPress supplies the page title.
Used for: the privacy policy (main site page ID 3) — re-run whenever privacy-policy.md changes.
"""
import argparse, re, sys, html
def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![\w*])\*([^*\n]+)\*(?!\w)', r'<em>\1</em>', t)
    t = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', r'<a href="\2">\1</a>', t)
    return t
def convert(md):
    lines = md.split('\n'); out=[]; i=0
    while i < len(lines):
        l = lines[i]
        if not l.strip(): i+=1; continue
        m = re.match(r'<a id="([^"]+)"></a>', l.strip())
        if m: out.append(f'<a id="{m.group(1)}"></a>'); i+=1; continue
        if l.strip()=='---': out.append('<hr />'); i+=1; continue
        m = re.match(r'(#{1,6})\s+(.*)', l)
        if m: n=len(m.group(1)); out.append(f'<h{n}>{inline(m.group(2))}</h{n}>'); i+=1; continue
        if l.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].startswith('|'): rows.append(lines[i]); i+=1
            cells=lambda r:[c.strip() for c in r.strip().strip('|').split('|')]
            h=cells(rows[0]); body=[cells(r) for r in rows[2:]]
            t='<table><thead><tr>'+''.join(f'<th>{inline(c)}</th>' for c in h)+'</tr></thead><tbody>'
            t+=''.join('<tr>'+''.join(f'<td>{inline(c)}</td>' for c in r)+'</tr>' for r in body)+'</tbody></table>'
            out.append(t); continue
        if l.startswith('>'):
            buf=[]
            while i<len(lines) and lines[i].startswith('>'): buf.append(lines[i][1:].strip()); i+=1
            out.append('<blockquote><p>'+inline(' '.join(buf))+'</p></blockquote>'); continue
        if re.match(r'\s*([-*]|\d+\.)\s', l):
            # collect list block including continuation lines
            items=[]
            while i<len(lines) and lines[i].strip() and (re.match(r'\s*([-*]|\d+\.)\s', lines[i]) or lines[i].startswith('  ')):
                ln=lines[i]; mm=re.match(r'(\s*)([-*]|\d+\.)\s+(.*)', ln)
                if mm: items.append([len(mm.group(1)), mm.group(2)[0].isdigit(), mm.group(3)])
                else: items[-1][2]+=' '+ln.strip()
                i+=1
            def render(items, start, depth):
                ordered=items[start][1]; tag='ol' if ordered else 'ul'; s=f'<{tag}>'; j=start
                while j<len(items) and items[j][0]>=depth:
                    if items[j][0]>depth: sub,j=render(items,j,items[j][0]); s=s[:-5]+sub+'</li>'; continue
                    s+=f'<li>{inline(items[j][2])}</li>'; j+=1
                return s+f'</{tag}>', j
            h,_=render(items,0,items[0][0]); out.append(h); continue
        buf=[]
        while i<len(lines) and lines[i].strip() and not re.match(r'(#|\||>|\s*([-*]|\d+\.)\s|---$|<a id)', lines[i]): buf.append(lines[i].strip()); i+=1
        if buf[0].startswith('**Psychedelics In Recovery'):
            joined=inline(buf[0])
            for b in buf[1:]: joined+=('<br />' if b.startswith('**') else ' ')+inline(b)
        else:
            joined=inline(' '.join(buf))
        out.append('<p>'+joined+'</p>')
    return '\n'.join(out)
src=open(sys.argv[1]).read()
src=re.sub(r'^# .*\n','',src,count=1)  # page title comes from WP
print(convert(src))
