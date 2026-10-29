"""
build.py
Build the donate page:  src/ (small html/css/js)  ->  docs/index.html (ONE file)

Usage:
    pip install jinja2
    python3 build.py

Preview:
    python3 -m http.server -d docs 8000
"""

from pathlib import Path
import shutil


from jinja2 import Environment, FileSystemLoader, select_autoescape
import rcssmin  # type: ignore


import config

#


ROOT = Path(__file__).parent
SRC = ROOT / "src"
OUT = ROOT / "docs"  # GitHub Pages serves this folder

CSS_ORDER = ["base", "hero", "sections", "free", "donate"]  # concatenated in this order
JS_ORDER = ["copy", "main"]


def read_parts(folder: str, names: list[str], ext: str) -> str:
    return "\n".join((SRC / folder / f"{n}.{ext}").read_text("utf-8") for n in names)


def minify_css(css: str) -> str:
    return rcssmin.cssmin(css)  # type: ignore


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()

    # Copy images to docs/static/image/
    image_src = ROOT / "static" / "image"
    image_out = OUT / "static" / "image"

    shutil.copytree(
        image_src,
        image_out,
    )

    env = Environment(
        loader=FileSystemLoader(SRC), autoescape=select_autoescape(["html"])
    )
    html = env.get_template("index.html").render(
        site=config.SITE,
        links=config.LINKS,
        upi=config.UPI,
        bank=config.BANK,
        projects=config.PROJECTS,
        goal=config.GOAL,
        photo=config.IMAGES.photo,
        upi_qr=config.IMAGES.upi_qr,
        style_tag=f"<style>{minify_css(read_parts('css', CSS_ORDER, 'css'))}</style>",
        script_tag=f"<script>{read_parts('js', JS_ORDER, 'js')}</script>",
    )
    (OUT / "index.html").write_text(html, encoding="utf-8")
    (OUT / "CNAME").write_text("donate.rana49.online\n")
    (OUT / ".nojekyll").touch()
    print(f"Built {OUT / 'index.html'}  ({len(html) / 1024:.1f} KB, single file)")


if __name__ == "__main__":
    main()
