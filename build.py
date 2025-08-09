import pathlib, markdown, datetime, html

# --- Paths ---
ROOT = pathlib.Path(".").resolve()
SRC = ROOT / "content"
DST = ROOT / "public"
DST.mkdir(parents=True, exist_ok=True)

# --- Site base (swap when custom domain is live) ---
BASE = "https://softfrequency.netlify.app"

# --- Page frame ---
def layout(
    title: str,
    inner: str,
    desc: str = "Ambient products. Natural tech. A future that breathes.",
    path: str = "/",
) -> str:
    year = datetime.date.today().year
    url = BASE.rstrip("/") + path
    ogimg = "/assets/og-default.jpg"
    return f"""<!doctype html><meta charset="utf-8">
<title>{title} – SoftFrequency</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title} – SoftFrequency">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{ogimg}">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="/styles.css">
<div class="container">
  <nav class="nav">
    <a href="/">Home</a>
    <a href="/blog/">Blog</a>
    <a href="/about.html">About</a>
    <a href="/contact.html">Contact</a>
  </nav>
  {inner}
  <footer>© {year} SoftFrequency</footer>
</div>"""

def render_md(md_path: pathlib.Path):
    text = md_path.read_text(encoding="utf-8")
    html_body = markdown.markdown(text, extensions=["fenced_code", "tables"])
    # title = first h1 or fallback to filename
    title = md_path.stem.replace("-", " ")
    for line in text.splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
            break
    return title, html_body

# --- Build blog posts ---
posts = []
if (SRC / "blog").exists():
    mds = sorted((SRC / "blog").rglob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True)
    for md in mds:
        title, body = render_md(md)
        rel = md.relative_to(SRC / "blog").with_suffix(".html")
        out = (DST / "blog" / rel)
        out.parent.mkdir(parents=True, exist_ok=True)
        path = f"/blog/{rel.as_posix()}"
        out.write_text(layout(title, f"<article>{body}</article>", path=path), encoding="utf-8")
        dt = datetime.datetime.fromtimestamp(md.stat().st_mtime, tz=datetime.timezone.utc)
        posts.append({"title": title, "href": path, "date": dt})

# --- Blog index ---
if posts:
    items = "\n".join(
        f'<li><a href="{p["href"]}">{html.escape(p["title"])}</a> '
        f'<time datetime="{p["date"].isoformat()}">{p["date"].date()}</time></li>'
        for p in posts
import pathlib, markdown, datetime, html

# --- Paths ---
ROOT = pathlib.Path(".").resolve()
SRC = ROOT / "content"
DST = ROOT / "public"
DST.mkdir(parents=True, exist_ok=True)

# --- Site base (swap when custom domain is live) ---
BASE = "https://softfrequency.netlify.app"

# --- Page frame ---
def layout(
    title: str,
    inner: str,
    desc: str = "Ambient products. Natural tech. A future that breathes.",
    path: str = "/",
) -> str:
    year = datetime.date.today().year
    url = BASE.rstrip("/") + path
    ogimg = "/assets/og-default.jpg"
    return f"""<!doctype html><meta charset="utf-8">
<title>{title} – SoftFrequency</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title} – SoftFrequency">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{ogimg}">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="/styles.css">
<div class="container">
  <nav class="nav">
    <a href="/">Home</a>
    <a href="/blog/">Blog</a>
    <a href="/about.html">About</a>
    <a href="/contact.html">Contact</a>
  </nav>
  {inner}
  <footer>© {year} SoftFrequency</footer>
</div>"""

def render_md(md_path: pathlib.Path):
    text = md_path.read_text(encoding="utf-8")
    html_body = markdown.markdown(text, extensions=["fenced_code", "tables"])
    # title = first h1 or fallback to filename
    title = md_path.stem.replace("-", " ")
    for line in text.splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
            break
    return title, html_body

# --- Build blog posts ---
posts = []
if (SRC / "blog").exists():
    mds = sorted((SRC / "blog").rglob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True)
    for md in mds:
        title, body = render_md(md)
        rel = md.relative_to(SRC / "blog").with_suffix(".html")
        out = (DST / "blog" / rel)
        out.parent.mkdir(parents=True, exist_ok=True)
        path = f"/blog/{rel.as_posix()}"
        out.write_text(layout(title, f"<article>{body}</article>", path=path), encoding="utf-8")
        dt = datetime.datetime.fromtimestamp(md.stat().st_mtime, tz=datetime.timezone.utc)
        posts.append({"title": title, "href": path, "date": dt})

# --- Blog index ---
if posts:
    items = "\n".join(
        f'<li><a href="{p["href"]}">{html.escape(p["title"])}</a> '
        f'<time datetime="{p["date"].isoformat()}">{p["date"].date()}</time></li>'
        for p in posts
    )
    (DST / "blog").mkdir(parents=True, exist_ok=True)
    (DST / "blog" / "index.html").write_text(
        layout("Blog", f"<h1>Blog</h1><ul>{items}</ul>", path="/blog/"),
        encoding="utf-8",
    )

# --- Optional pages (about, contact, home, etc.) ---
if (SRC / "pages").exists():
    for md in (SRC / "pages").glob("*.md"):
        title, body = render_md(md)
        (DST / f"{md.stem}.html").write_text(
            layout(title, body, path=f"/{md.stem}.html"),
            encoding="utf-8",
        )

# --- Assets (publish under /assets/ ...) ---
ASSETS = ROOT / "assets"
if ASSETS.exists():
    for p in ASSETS.rglob("*"):
        if p.is_file():
            target = DST / "assets" / p.relative_to(ASSETS)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(p.read_bytes())

# --- Stylesheet ---
root_css = ROOT / "styles.css"
if root_css.exists():
    (DST / "styles.css").write_text(root_css.read_text(encoding="utf-8"), encoding="utf-8")

# --- Global fallback index (only if no real homepage) ---
if not (SRC / "pages" / "index.md").exists():
    items = []
    for html_file in DST.rglob("*.html"):
        if html_file.name == "index.html":
            continue
        rel = html_file.relative_to(DST).as_posix()
        label = rel.replace(".html", "")
        items.append((label, "/" + rel))
    items.sort()
    links = "\n".join(f'<li><a href="{href}">{label}</a></li>' for label, href in items)
    index_html = f"""<!doctype html><meta charset="utf-8">
<title>SoftFrequency</title>
<link rel="stylesheet" href="/styles.css">
<main class="container">
  <h1>SoftFrequency</h1>
  <p>Welcome. Browse pages:</p>
  <ul>
    {links}
  </ul>
</main>"""
    (DST / "index.html").write_text(index_html, encoding="utf-8")

# --- Sitemap + robots + _headers copy ---
# collect URLs (dedup with a set)
url_set = {"/", "/blog/"} | {p["href"] for p in posts}
for html_file in DST.rglob("*.html"):
    rel = "/" + html_file.relative_to(DST).as_posix()
    url_set.add(rel)

today = datetime.date.today().isoformat()
sitemap_xml = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
]
for path in sorted(url_set):
    loc = BASE.rstrip("/") + path
    sitemap_xml.append(f"<url><loc>{loc}</loc><lastmod>{today}</lastmod></url>")
sitemap_xml.append("</urlset>")
(DST / "sitemap.xml").write_text("\n".join(sitemap_xml), encoding="utf-8")

(DST / "robots.txt").write_text(
    f"User-agent: *\nAllow: /\nSitemap: {BASE.rstrip('/')}/sitemap.xml\n",
    encoding="utf-8",
)

# publish Netlify _headers into /public
headers_src = ROOT / "_headers"
if headers_src.exists():
    (DST / "_headers").write_text(headers_src.read_text(encoding="utf-8"), encoding="utf-8")
