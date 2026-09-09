#!/usr/bin/env python3
"""Footer-overlap check für Marp-Decks.

Prüft pro Folie, ob Inhalt in die Fußzeile ragt. Dependency-frei:
injiziert Mess-JS in das gerenderte HTML und lässt Headless-Chromium
die Geometrie messen (--dump-dom).

Usage:   python3 tests/check_footer.py docs/presentations/<deck>.html
Exit 0 = keine Überlappung, 1 = Überlappungen gefunden, 2 = technischer Fehler.
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

TOLERANCE_PX = 2

MEASURE_JS = """
<script>
(function () {
  var finish = function () {
    var out = [];
    var sections = document.querySelectorAll('section');
  for (var i = 0; i < sections.length; i++) {
    var sec = sections[i];
    var footer = sec.querySelector('footer');
    if (!footer) continue;
    var f = footer.getBoundingClientRect();
    var h1 = sec.querySelector('h1, h2');
    var title = h1 ? h1.textContent.trim() : '(ohne Titel)';
    var worst = null;
    var all = sec.querySelectorAll('*');
    for (var j = 0; j < all.length; j++) {
      var el = all[j];
      var tag = el.tagName;
      if (el === footer || footer.contains(el) || el.contains(footer)) continue;
      if (tag === 'SCRIPT' || tag === 'STYLE' || tag === 'HEAD') continue;
      var r = el.getBoundingClientRect();
      if (r.height === 0 || r.width === 0) continue;
      var overlap = r.bottom - f.top;
      if (overlap <= %TOLERANCE%) continue;
      if (r.right <= f.left || r.left >= f.right) continue;
      // tiefstes Element gewinnen: nur Blätter/Exits melden
      var childOverlaps = false;
      var kids = el.children;
      for (var k = 0; k < kids.length; k++) {
        var kr = kids[k].getBoundingClientRect();
        if (kr.height > 0 && kr.bottom - f.top > %TOLERANCE%) { childOverlaps = true; break; }
      }
      if (childOverlaps) continue;
      var rec = {
        tag: tag,
        overlapPx: Math.round(overlap),
        text: (el.textContent || '').replace(/\\s+/g, ' ').trim().slice(0, 60)
      };
      if (!worst || rec.overlapPx > worst.overlapPx) worst = rec;
    }
    if (worst) out.push({ slide: i + 1, title: title.slice(0, 50), worst: worst });
  }
  var d = document.createElement('div');
  d.id = 'footer-check-result';
  d.textContent = '###RESULT###' + JSON.stringify(out);
  document.body.appendChild(d);
  };
  var imgs = document.querySelectorAll('img');
  var pending = imgs.length;
  var done = function () { if (--pending <= 0) { setTimeout(finish, 50); } };
  if (pending === 0) { done(); return; }
  for (var p = 0; p < imgs.length; p++) {
    var im = imgs[p];
    if (im.complete) { done(); }
    else { im.addEventListener('load', done); im.addEventListener('error', done); }
  }
})();
</script>
""".replace("%TOLERANCE%", str(TOLERANCE_PX))


def find_chromium():
    for name in ("chromium", "chromium-browser", "google-chrome", "google-chrome-stable"):
        path = shutil.which(name)
        if path:
            return path
    sys.exit("kein Chromium/Chrome gefunden")


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    deck = Path(sys.argv[1])
    if not deck.exists():
        sys.exit(f"nicht gefunden: {deck}")
    html = deck.read_text()
    if "</body>" not in html:
        sys.exit("kein gültiges HTML")
    injected = html.replace("</body>", MEASURE_JS + "\n</body>")

    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as tmp:
        tmp.write(injected)
        tmp_path = tmp.name

    chromium = find_chromium()
    proc = subprocess.run(
        [
            chromium,
            "--headless",
            "--no-sandbox",
            "--disable-gpu",
            "--window-size=1280,800",
            "--virtual-time-budget=5000",
            "--dump-dom",
            f"file://{tmp_path}",
        ],
        capture_output=True,
        text=True,
        timeout=120,
    )
    Path(tmp_path).unlink(missing_ok=True)

    match = re.search(r"###RESULT###(\[.*?\])</div>", proc.stdout, re.S)
    if not match:
        print(proc.stdout[-2000:], file=sys.stderr)
        sys.exit("Konnte Messergebnis nicht extrahieren (Exit 2)")

    violations = json.loads(match.group(1))
    if not violations:
        print(f"PASS ✅  {len(re.findall('<section', html))} Folien, keine Überlappung mit der Fußzeile (Toleranz {TOLERANCE_PX}px)")
        return

    print(f"FAIL ❌  {len(violations)} Folie(n) überlappen die Fußzeile:\n")
    for v in violations:
        w = v["worst"]
        print(f"  Folie {v['slide']:>2}: +{w['overlapPx']}px  {w['tag']}  „{w['text']}”  [{v['title']}]")
    sys.exit(1)


if __name__ == "__main__":
    main()
