#!/usr/bin/env python3
"""Folienverzeichnis aus dem gerenderten Deck: Nummer, Referent, Titel."""
import re
import sys
from pathlib import Path

for i, sec in enumerate(re.split(r"<section", Path(sys.argv[1]).read_text())[1:], 1):
    m = re.search(r"<h[12][^>]*>(.*?)</h[12]>", sec, re.S)
    title = re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else "(ohne Titel)"
    who = "C" if 'class="speaker speaker-christian"' in sec else (
          "T" if 'class="speaker speaker-tobias"' in sec else " ")
    print(f"{i:>3} {who}  {title[:64]}")
