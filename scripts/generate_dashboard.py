"""
Builds the dashboard cards shown at the top of README.md from progress.json.

    python scripts/generate_dashboard.py

Writes light and dark SVGs to assets/dashboard/. generate_questions_log.py calls this
automatically, so the cards stay in step with the spreadsheet.
"""
import datetime
import json
from collections import Counter
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROGRESS_JSON = ROOT / "progress.json"
OUT_DIR = ROOT / "assets" / "dashboard"

W = 880
PAD = 48
FONT = ('-apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", '
        '"Segoe UI Variable Display", "Segoe UI", system-ui, Roboto, Helvetica, Arial, sans-serif')

TOPIC_NAMES = {
    "arrays-hashing": "Arrays & Hashing",
    "pattern-printing": "Pattern Printing",
    "binary-search": "Binary Search",
    "math-geometry": "Math",
    "two-pointers": "Two Pointers",
    "recursion": "Recursion",
    "sliding-window": "Sliding Window",
    "matrix": "Matrix",
    "intervals": "Intervals",
    "strings": "Strings",
}

THEMES = {
    "light": dict(card="#F5F5F7", border="rgba(0,0,0,0.07)", primary="#1D1D1F", secondary="#6E6E73",
                  track="rgba(0,0,0,0.07)", a1="#007AFF", a2="#5AC8FA",
                  easy="#34C759", medium="#FF9F0A", hard="#FF3B30"),
    "dark": dict(card="#1C1C1E", border="rgba(255,255,255,0.10)", primary="#F5F5F7", secondary="#A1A1A6",
                 track="rgba(255,255,255,0.11)", a1="#0A84FF", a2="#64D2FF",
                 easy="#30D158", medium="#FF9F0A", hard="#FF453A"),
}

STYLE = """
text { font-family: %s; }
.num { font-variant-numeric: tabular-nums; }
@keyframes grow { from { transform: scaleX(0); } to { transform: scaleX(1); } }
@keyframes rise { from { transform: scaleY(0); } to { transform: scaleY(1); } }
@keyframes pop { from { opacity: 0; transform: scale(.92); } to { opacity: 1; transform: scale(1); } }
@keyframes fade { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }
.grow { transform-box: fill-box; transform-origin: 0%% 50%%; animation: grow .8s cubic-bezier(.22,1,.36,1) both; }
.rise { transform-box: fill-box; transform-origin: 50%% 100%%; animation: rise .8s cubic-bezier(.22,1,.36,1) both; }
.pop { transform-box: fill-box; transform-origin: 50%% 50%%; animation: pop .8s cubic-bezier(.22,1,.36,1) both; }
.fade { animation: fade .7s cubic-bezier(.22,1,.36,1) both; }
@media (prefers-reduced-motion: reduce) { .grow, .rise, .pop { transform-box: fill-box; transform-origin: 50%% 50%%; animation: pop .8s cubic-bezier(.22,1,.36,1) both; }
.fade { animation: none; } }
""" % FONT


def load():
    data = json.loads(PROGRESS_JSON.read_text(encoding="utf-8"))
    rows = [q for q in data["questions"] if q.get("status") in ("solved", "struggled") and q.get("first_attempted")]
    for q in rows:
        q["_date"] = datetime.date.fromisoformat(q["first_attempted"])
    return rows


def stats(rows):
    topics = Counter(q["topic"] for q in rows)
    difficulty = Counter(q["difficulty"] for q in rows)
    days = {q["_date"] for q in rows}
    first = min(days)
    week0 = first - datetime.timedelta(days=first.weekday())
    weekly = Counter((q["_date"] - week0).days // 7 for q in rows)
    n_weeks = max(weekly) + 1
    first_batch = Counter(q["topic"] for q in rows if q["_date"] == first).most_common(1)[0]
    return dict(
        total=len(rows),
        topics=topics,
        difficulty=difficulty,
        active_days=len(days),
        in_review=sum(1 for q in rows if q["status"] == "struggled"),
        week0=week0,
        weekly=[weekly.get(i, 0) for i in range(n_weeks)],
        first_batch=first_batch,
    )


def open_svg(h, title, desc, t):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}" role="img" '
        f'aria-labelledby="t d">\n<title id="t">{escape(title)}</title>\n<desc id="d">{escape(desc)}</desc>\n'
        f'<defs>\n<style>{STYLE}</style>\n'
        f'<linearGradient id="acc" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{t["a1"]}"/>'
        f'<stop offset="1" stop-color="{t["a2"]}"/></linearGradient>\n'
        f'<linearGradient id="accv" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="{t["a1"]}"/>'
        f'<stop offset="1" stop-color="{t["a2"]}"/></linearGradient>\n</defs>\n'
        f'<rect x="0.5" y="0.5" width="{W - 1}" height="{h - 1}" rx="28" fill="{t["card"]}" stroke="{t["border"]}"/>\n'
    )


def text(x, y, s, size, weight, fill, anchor="start", tracking=0.0, cls="", delay=None, extra=""):
    style = f' style="animation-delay:{delay}ms"' if delay is not None else ""
    klass = f' class="{cls}"' if cls else ""
    return (f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}" letter-spacing="{tracking}em"{klass}{style}{extra}>{escape(str(s))}</text>\n')


def donut(cx, cy, r, sw, parts, gap=8):
    """Segmented ring with rounded caps. parts = [(share, colour), ...]; shares sum to 1."""
    c = 2 * 3.141592653589793 * r
    cut = sw + gap
    out = '<g class="pop" style="animation-delay:80ms">\n'
    pos = 0.0
    for share, colour in parts:
        arc = c * share
        dash = arc - cut
        if dash > 0.5:
            out += (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{colour}" stroke-width="{sw}" '
                    f'stroke-linecap="round" stroke-dasharray="{dash:.2f} {c:.2f}" '
                    f'stroke-dashoffset="{-(pos + cut / 2):.2f}" transform="rotate(-90 {cx} {cy})"/>\n')
        pos += arc
    return out + '</g>\n'


def hero(s, t):
    h = 376
    desc = (f'{s["total"]} problems logged across {len(s["topics"])} topics on {s["active_days"]} days; '
            f'{s["difficulty"].get("Easy", 0)} easy, {s["difficulty"].get("Medium", 0)} medium, '
            f'{s["difficulty"].get("Hard", 0)} hard; {s["in_review"]} in review.')
    out = open_svg(h, "Practice dashboard", desc, t)

    # left column: headline and key numbers
    out += text(PAD, 68, "DSA PRACTICE  ·  PYTHON", 13, 600, t["secondary"], tracking=0.1)
    out += text(PAD, 128, "Data structures", 38, 700, t["primary"], tracking=-0.025, cls="fade", delay=0)
    out += text(PAD, 172, "and algorithms.", 38, 700, t["primary"], tracking=-0.025, cls="fade", delay=40)
    out += text(PAD, 206, "Tested against brute force,", 16, 500, t["secondary"], tracking=0.005, cls="fade", delay=80)
    out += text(PAD, 230, "with the traps written down.", 16, 500, t["secondary"], tracking=0.005, cls="fade", delay=100)
    metrics = [(len(s["topics"]), "topics"), (s["active_days"], "active days"), (s["in_review"], "in review")]
    for i, (v, label) in enumerate(metrics):
        x = PAD + i * 128
        out += text(x, 300, v, 36, 650, t["primary"], tracking=-0.03, cls="num fade", delay=140 + i * 60)
        out += text(x, 326, label, 13, 500, t["secondary"], tracking=0.01, cls="fade", delay=160 + i * 60)

    # right column: difficulty ring with the total in the middle
    cx, cy = 686, 174
    diffs = [("Easy", t["easy"]), ("Medium", t["medium"]), ("Hard", t["hard"])]
    total = sum(s["difficulty"].get(n, 0) for n, _ in diffs) or 1
    out += donut(cx, cy, 84, 22, [(s["difficulty"].get(n, 0) / total, colour) for n, colour in diffs])
    out += text(cx, cy + 14, s["total"], 54, 700, t["primary"], anchor="middle", tracking=-0.04, cls="num fade", delay=0)
    out += text(cx, cy + 40, "problems", 14, 500, t["secondary"], anchor="middle", tracking=0.01, cls="fade", delay=60)

    lx = [548, 646, 752]
    for (n, colour), x in zip(diffs, lx):
        c = s["difficulty"].get(n, 0)
        out += f'<circle cx="{x + 5}" cy="{cy + 128}" r="5" fill="{colour}"/>\n'
        out += text(x + 16, cy + 133, n, 14, 500, t["secondary"], tracking=0.01)
        out += text(x + 16 + len(n) * 8.2 + 7, cy + 133, c, 14, 650, t["primary"], cls="num")
    return out + "</svg>\n"


def topics_card(s, t):
    rows = s["topics"].most_common()
    n = len(rows)
    h = 132 + n * 44 + 20
    desc = "Problems per topic: " + ", ".join(f"{TOPIC_NAMES.get(k, k)} {v}" for k, v in rows) + "."
    out = open_svg(h, "Problems per topic", desc, t)
    out += text(PAD, 70, "Topics", 28, 700, t["primary"], tracking=-0.02)
    out += text(PAD, 98, "Problems per topic", 15, 500, t["secondary"], tracking=0.01)
    track_x, track_w = 236, 560
    peak = rows[0][1]
    for i, (topic, count) in enumerate(rows):
        cy = 146 + i * 44
        name = TOPIC_NAMES.get(topic, topic.replace("-", " ").title())
        out += text(PAD, cy + 5, name, 15, 500, t["primary"], tracking=0.0)
        out += f'<rect x="{track_x}" y="{cy - 5}" width="{track_w}" height="10" rx="5" fill="{t["track"]}"/>\n'
        fill_w = max(10, track_w * count / peak)
        out += (f'<rect class="grow" style="animation-delay:{i * 60}ms" x="{track_x}" y="{cy - 5}" '
                f'width="{fill_w:.1f}" height="10" rx="5" fill="url(#acc)"/>\n')
        out += text(W - PAD, cy + 5, count, 15, 650, t["primary"], anchor="end", cls="num")
    return out + "</svg>\n"


def activity_card(s, t):
    h = 336
    weekly = s["weekly"]
    n = len(weekly)
    desc = f"Problems logged per week over {n} weeks: " + ", ".join(str(v) for v in weekly) + "."
    out = open_svg(h, "Problems logged per week", desc, t)
    out += text(PAD, 70, "Activity", 28, 700, t["primary"], tracking=-0.02)
    out += text(PAD, 98, "Problems logged per week", 15, 500, t["secondary"], tracking=0.01)

    chart_x, chart_w = PAD, W - 2 * PAD
    base_y, chart_h = 252, 112
    slot = chart_w / n
    bar_w = min(44, slot * 0.56)
    peak = max(weekly) or 1
    out += f'<line x1="{chart_x}" y1="{base_y + 0.5}" x2="{chart_x + chart_w}" y2="{base_y + 0.5}" stroke="{t["track"]}"/>\n'
    for i, v in enumerate(weekly):
        cx = chart_x + slot * (i + 0.5)
        bh = max(4, chart_h * v / peak) if v else 4
        fill = "url(#accv)" if v else t["track"]
        out += (f'<rect class="rise" style="animation-delay:{i * 50}ms" x="{cx - bar_w / 2:.1f}" y="{base_y - bh:.1f}" '
                f'width="{bar_w:.1f}" height="{bh:.1f}" rx="6" fill="{fill}"/>\n')
        if v:
            out += text(f"{cx:.1f}", f"{base_y - bh - 10:.1f}", v, 13, 650, t["primary"], anchor="middle", cls="num")
        d = s["week0"] + datetime.timedelta(days=7 * i)
        out += text(f"{cx:.1f}", base_y + 26, f"{d.strftime('%b')} {d.day}", 12, 500, t["secondary"],
                    anchor="middle", tracking=0.01)
    topic, count = s["first_batch"]
    if count >= 5:
        out += text(PAD, h - 26, f"The first week includes {count} {topic} problems that were logged together.",
                    12, 500, t["secondary"], tracking=0.01)
    return out + "</svg>\n"


def main():
    rows = load()
    s = stats(rows)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for name, t in THEMES.items():
        (OUT_DIR / f"hero-{name}.svg").write_text(hero(s, t), encoding="utf-8")
        (OUT_DIR / f"topics-{name}.svg").write_text(topics_card(s, t), encoding="utf-8")
        (OUT_DIR / f"activity-{name}.svg").write_text(activity_card(s, t), encoding="utf-8")
    print(f"Wrote dashboard cards for {s['total']} problems to {OUT_DIR}")


if __name__ == "__main__":
    main()
