# freiversum/.github

Organization profile for [github.com/freiversum](https://github.com/freiversum).

- `profile/README.md` – the page shown on the organization's overview
- `assets/` – header (light and dark, text as paths), constellation mark, app icons and screenshots
- `tools/build.py` – rebuilds `assets/` from the local app repositories and the freiversum brand kit

## Rebuilding the assets

```
python3 tools/build.py            # everything
python3 tools/build.py header     # only the header
```

The script expects the app repositories and the brand kit next to this checkout (see the paths at the top of
`tools/build.py`) and needs fontTools with brotli, `rsvg-convert`, ImageMagick and ffmpeg. Fonts are only read
from the brand kit and are not part of this repository.

## Adding a project

1. Add its icon (and, if it should appear in a strip, a screenshot) to `ICONS` / `SHOTS` in `tools/build.py`.
2. Run the script and add a row to the matching table in `profile/README.md`.
3. Pin it on the organization page if it should be among the six pinned repositories.

## License

Text and images: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). App icons and screenshots belong to the
respective projects and are under their licenses.
