import pathlib, markdown

SRC = pathlib.Path("content")
DST = pathlib.Path("public")
DST.mkdir(parents=True, exist_ok=True)

for md in SRC.rglob("*.md"):
    rel = md.relative_to(SRC)
    out = (DST / rel).with_suffix(".html")
    out.parent.mkdir(parents=True, exist_ok=True)
    text = md.read_text(encoding="utf-8")
    body = markdown.markdown(text, extensions=["fenced_code", "tables"])
    html = f"""<!doctype html><meta charset="utf-8">
<title>SoftFrequency</title>
<link rel="stylesheet" href="/styles.css">
<main class="container">
{body}
</main>"""
    out.write_text(html, encoding="utf-8")
