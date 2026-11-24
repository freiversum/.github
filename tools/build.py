#!/usr/bin/env python3
"""Build the assets of the freiversum organization profile.

Writes
  assets/header-light.svg, assets/header-dark.svg  constellation + wordmark + motto, text as paths
  assets/icons/<slug>.png                          64 px app icons from the app repositories
  assets/shots/<slug>.webp                         screenshots, 900x600 (desktop) or 450x900 (phone)
  assets/mark.svg                                  constellation mark, copied from the brand kit

Sources are the local clones next to this checkout (05_Projekte/apps) and the brand kit
(web/linuxundich/social-media/dachmarke-2026-11/marke). Fonts are only used here and are not
committed. Needs: python3-fonttools (+brotli), rsvg-convert, magick, ffmpeg.

Run: python3 tools/build.py
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

HERE = Path(__file__).resolve().parent.parent
ROOT = HERE.parents[2]  # 05_Projekte
APPS = ROOT / "apps"
BRAND = ROOT / "web/linuxundich/social-media/dachmarke-2026-11/marke/fonts"
SITE_FONTS = ROOT / "web/freiversum.de/public/fonts"
ASSETS = HERE / "assets"

ICONS = {
    "gnomos": APPS / "gnomos/data/icons/hicolor/scalable/apps/de.linuxundich.Gnomos.svg",
    "parkett": APPS / "parkett/data/icons/hicolor/scalable/apps/de.linuxundich.Parkett.svg",
    "dandelion": APPS / "dandelion/data/icons/hicolor/scalable/apps/de.linuxundich.Dandelion.svg",
    "screenforge": APPS / "screenforge/app/data/icons/hicolor/scalable/apps/de.christophlangner.ScreenForge.svg",
    "tretlager": APPS / "tretlager/tretlager/data/icons/de.linuxundich.Tretlager.svg",
    "pulsgeber": APPS / "pulsgeber/extension/icons/hicolor/scalable/apps/de.linuxundich.Pulsgeber.svg",
    "planetfoss-android": APPS / "planetfoss-android/fastlane/metadata/android/en-US/images/icon.png",
    "hausmusik": APPS / "hausmusik/fastlane/metadata/android/en-US/images/icon.png",
    "commentator": APPS / "commentator/store/play/icon-512.png",
}

# (slug, source, kind, gravity) – kind "desk" = 900x600, "phone" = 450x900
SHOTS = [
    ("gnomos", APPS / "gnomos/screenshots/gnomos-albums.webp", "desk", "center"),
    ("screenforge", APPS / "screenforge/docs/screenshots/main-window.png", "desk", "center"),
    ("tretlager", APPS / "tretlager/docs/screenshots/tretlager-ready.webp", "desk", "center"),
    ("pulsgeber", APPS / "pulsgeber/docs/screenshots/quick-settings.webp", "desk", "center"),
    ("planetfoss-android", APPS / "planetfoss-android/docs/screenshots/radar.webp", "phone", "north"),
    ("hausmusik", APPS / "hausmusik/fastlane/metadata/android/en-US/images/phoneScreenshots/1_stage.png", "phone", "north"),
]
# Commentator has only German screenshots; take the phone from the English demo video.
COMMENTATOR_VIDEO = ROOT / "media/app-demo-video/videos/commentator-0.3-en/demo_raw.mp4"
COMMENTATOR_CROP = "382x764+1439+117"  # phone window at 8 s, 1920x1080

STAR = "M0,-11Q1.76,-1.76 11,0Q1.76,1.76 0,11Q-1.76,1.76 -11,0Q-1.76,-1.76 0,-11Z"
THEMES = {
    "light": {"line": "#8b90ab", "star4": "#59636e", "t1": "#1f2328", "t2": "#59636e"},
    "dark": {"line": "#5b6080", "star4": "#eef2f8", "t1": "#f0f6fc", "t2": "#9198a1"},
}
MOTTO = "Linux, open source and tech you run yourself"


class Face:
    """Glyph runs without kerning (for the monospaced motto)."""

    def __init__(self, font: TTFont):
        self.f = font
        self.cmap = font.getBestCmap()
        self.gs = font.getGlyphSet()
        self.upm = font["head"].unitsPerEm

    def run(self, text: str, size: float, x: float, y: float, tracking: float = 0.0) -> tuple[str, float]:
        s = size / self.upm
        out = []
        for ch in text:
            g = self.cmap[ord(ch)]
            pen = SVGPathPen(self.gs, ntos=lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
            self.gs[g].draw(TransformPen(pen, (s, 0, 0, -s, x, y)))
            out.append(pen.getCommands())
            x += self.f["hmtx"][g][0] * s + tracking * size
        return " ".join(p for p in out if p), x


def header() -> None:
    sys.path.insert(0, str(BRAND.parent))
    from wortmarke import Face as KernFace  # same wordmark code as the brand kit, with GPOS kerning

    bold = KernFace(str(BRAND / "ox700.ttf"))
    medium = KernFace(str(BRAND / "ox500.ttf"))
    mono_var = TTFont(SITE_FONTS / "atkinson-hyperlegible-mono-variable.woff2")
    mono = Face(instancer.instantiateVariableFont(mono_var, {"wght": 400}))

    d_frei, x = bold.run("frei", 76, 250, 128, -0.012)
    d_versum, x_end = medium.run("versum", 76, x, 128, -0.012)
    d_motto, x_motto = mono.run(MOTTO, 29, 254, 180)
    width = round(max(x_end, x_motto) + 24)

    for name, c in THEMES.items():
        svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} 210" width="{width // 2}" height="105" role="img" aria-label="freiversum – {MOTTO}">
<polyline points="40,150 92,90 148,126 196,60" fill="none" stroke="{c['line']}" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
<path d="{STAR}" transform="translate(40 150) scale(1.9)" fill="#ff6600"/>
<path d="{STAR}" transform="translate(92 90) scale(1.5)" fill="#8370EE"/>
<path d="{STAR}" transform="translate(148 126) scale(1.5)" fill="#ffbc00"/>
<path d="{STAR}" transform="translate(196 60) scale(1.5)" fill="{c['star4']}"/>
<path d="{d_frei}" fill="{c['t1']}"/>
<path d="{d_versum}" fill="{c['t2']}"/>
<path d="{d_motto}" fill="{c['t2']}"/>
</svg>
"""
        (ASSETS / f"header-{name}.svg").write_text(svg)
    print(f"header: {width}x210")


def mark() -> None:
    src = BRAND.parent / "out/zeichen-l.svg"
    (ASSETS / "mark.svg").write_text(src.read_text())
    print("mark: ok")


def run(*cmd: str) -> None:
    subprocess.run(cmd, check=True)


def icons() -> None:
    out = ASSETS / "icons"
    out.mkdir(parents=True, exist_ok=True)
    for slug, src in ICONS.items():
        dst = out / f"{slug}.png"
        if src.suffix == ".svg":
            run("rsvg-convert", "-w", "64", "-h", "64", "-o", str(dst), str(src))
        else:
            run("magick", str(src), "-resize", "64x64", "-strip", str(dst))
    print(f"icons: {len(ICONS)}")


def shots() -> None:
    out = ASSETS / "shots"
    out.mkdir(parents=True, exist_ok=True)
    for slug, src, kind, grav in SHOTS:
        size = "900x600" if kind == "desk" else "450x900"
        run("magick", str(src), "-resize", f"{size}^", "-gravity", grav, "-extent", size,
            "-strip", "-quality", "82", str(out / f"{slug}.webp"))
    with tempfile.TemporaryDirectory() as tmp:
        frame = Path(tmp) / "frame.png"
        run("ffmpeg", "-v", "error", "-y", "-ss", "8", "-i", str(COMMENTATOR_VIDEO), "-frames:v", "1", str(frame))
        run("magick", str(frame), "-crop", COMMENTATOR_CROP, "+repage", "-resize", "450x900",
            "-strip", "-quality", "82", str(out / "commentator.webp"))
    print(f"shots: {len(SHOTS) + 1}")


if __name__ == "__main__":
    steps = sys.argv[1:] or ["header", "mark", "icons", "shots"]
    for step in steps:
        {"header": header, "mark": mark, "icons": icons, "shots": shots}[step]()
