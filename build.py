def layout(title: str, inner: str, desc: str = "Ambient products. Natural tech. A future that breathes.", path: str = "/"):
    year = datetime.date.today().year
    BASE = "https://softfrequency.netlify.app"  # swap when custom domain is live
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
