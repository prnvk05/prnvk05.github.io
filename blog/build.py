"""Build the static engineering journal from content.json; no dependencies."""
from html import escape
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
CONTENT = json.loads((ROOT / "content.json").read_text(encoding="utf-8"))
ARTICLES = CONTENT["articles"]
LOGS = sorted(CONTENT["logs"], key=lambda item: item["date"], reverse=True)
BASE = "/blog/"
STINGRAY = BASE + "stingray/"

def e(value):
    return escape(str(value), quote=True)

def article_url(item):
    return BASE + "articles/" + item["slug"] + "/"

def log_url(item):
    return STINGRAY + item["slug"] + "/"

def layout(title, description, content, canonical, current="blog"):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} — Pranav Kanuparthi</title>
<meta name="description" content="{e(description)}">
<link rel="canonical" href="https://pranavkanuparthi.com{e(canonical)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&amp;family=Syne:wght@400;600;700;800&amp;family=DM+Sans:wght@400;500;600&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="/blog/assets/journal.css">
</head>
<body>
<nav aria-label="Main navigation"><div class="nav-inner"><a class="logo" href="/" aria-label="Pranav Kanuparthi home">PK_</a><div class="nav-links"><a href="/#projects">Projects</a><a href="/blog/"{' aria-current="page"' if current=="blog" else ""}>Blog</a><a href="/blog/stingray/"{' aria-current="page"' if current=="stingray" else ""}>Stingray</a></div></div></nav>
<main>{content}</main>
<footer><div class="wrap"><span>© 2026 Pranav Kanuparthi</span><span>Engineering · Experimentation · Making</span></div></footer>
</body>
</html>
"""

def hero(kicker, title, summary, extra=""):
    return f'<header class="hero"><div class="wrap"><p class="kicker">{e(kicker)}</p><h1>{e(title)}</h1><p class="intro">{e(summary)}</p>{extra}</div></header>'

def article_card(item):
    return f'<a class="card" href="{article_url(item)}"><div class="meta">{e(item["category"])}</div><h3>{e(item["title"])}</h3><p>{e(item["summary"])}</p><span class="link">Read article ↗</span></a>'

def log_row(item):
    kind = item["status"]
    css = "tag failed" if kind == "Failed" else "tag"
    return f'<a class="log-row" href="{log_url(item)}"><time class="log-date" datetime="{e(item["date"])}">{e(item["date"])}</time><div><div class="meta">{e(item["category"])}</div><h3>{e(item["title"])}</h3><p>{e(item["summary"])}</p></div><span class="{css}">{e(kind)}</span></a>'

def write(url, content):
    dest = ROOT / url.removeprefix(BASE) / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(content, encoding="utf-8")

def post(item, is_log=False):
    url = log_url(item) if is_log else article_url(item)
    crumbs = '<div class="crumbs"><a href="/blog/">Blog</a> / '
    crumbs += '<a href="/blog/stingray/">Stingray</a> / ' if is_log else ''
    crumbs += 'Entry</div>'
    kicker = (item["date"] + " · " + item["status"] + " · " if is_log else "Technical article · ") + item["category"]
    body = "".join(f"<h2>{e(heading)}</h2><p>{e(paragraph)}</p>" for heading, paragraph in item["sections"])
    if item.get("photos"):
        pictures = []
        for photo in item["photos"]:
            src = BASE + "assets/" + photo["file"]
            pictures.append(f'<figure><a href="{e(src)}"><img src="{e(src)}" loading="lazy" width="900" height="1200" alt="{e(photo["alt"])}"></a><figcaption>{e(photo["caption"])}</figcaption></figure>')
        body += '<h2>Photographic evidence</h2><div class="photos">' + "".join(pictures) + "</div>"
    return_link = STINGRAY if is_log else BASE
    return_text = "All development logs" if is_log else "All articles"
    content = hero(kicker, item["title"], item["summary"]) + f'<div class="wrap"><article class="article">{crumbs}{body}<div class="article-nav"><a class="link" href="{return_link}">← {return_text}</a></div></article></div>'
    write(url, layout(item["title"], item["summary"], content, url, "stingray" if is_log else "blog"))

def main():
    cards = "".join(article_card(item) for item in ARTICLES)
    latest = "".join(log_row(item) for item in LOGS[:3])
    home = hero("Notes from the workshop", "Technical blog.", "Experiments, design decisions, things that work, and things that don’t. An ongoing record of building across hardware and software.") + f'<div class="wrap"><section class="section"><p class="kicker">Project journal / 01</p><a class="project-card" href="{STINGRAY}"><div class="meta"><span class="tag">Active prototype</span> Underwater robotics</div><h2>Stingray</h2><p>A modular underwater robot for exploration and potential marine debris collection. Follow the engineering journey from CAD and fabrication to integration and testing.</p><span class="link">Explore the journal ↗</span></a></section><section class="section"><div class="heading-row"><h2>Technical articles</h2></div><div class="grid">{cards}</div></section><section class="section"><div class="heading-row"><h2>Latest development logs</h2><a class="link" href="{STINGRAY}">View all ↗</a></div><div class="archive">{latest}</div></section></div>'
    write(BASE, layout("Technical blog", "Technical articles and ongoing engineering journals.", home, BASE))
    stats = f'<div class="stats"><div><strong>{len(LOGS):02d}</strong><span class="mono">Activity logs</span></div><div><strong>01</strong><span class="mono">Active prototype</span></div><div><strong>R&amp;D</strong><span class="mono">Current stage</span></div></div>'
    journal = hero("Project journal / 01 · Underwater robotics", "Stingray.", "A modular, stingray-inspired remotely operated vehicle. The objective is to prototype an underwater robot for exploration and eventually marine cleanup. This journal records the engineering process, including failures.", stats) + f'<div class="wrap"><section class="section"><div class="heading-row"><h2>Development timeline</h2><span class="mono">Newest first</span></div><div class="note">Design and early prototyping. Underwater capability has not yet been validated. Retrospective entries are labelled; observations and hypotheses are kept separate.</div><div class="archive">{"".join(log_row(item) for item in LOGS)}</div></section><section class="section"><div class="heading-row"><h2>Technical deep dives</h2><a class="link" href="{BASE}">All articles ↗</a></div><div class="grid">{cards}</div></section></div>'
    write(STINGRAY, layout("Stingray development journal", "Dated engineering logs for the Stingray underwater robot prototype.", journal, STINGRAY, "stingray"))
    for item in ARTICLES:
        post(item)
    for item in LOGS:
        post(item, True)
    print(f"Built {len(ARTICLES)} technical articles and {len(LOGS)} development logs.")

if __name__ == "__main__":
    main()
