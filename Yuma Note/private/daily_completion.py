import re
from pathlib import Path
from datetime import date

BASE_DIR = Path(__file__).resolve().parent
DAILY_ROOT = BASE_DIR.parent / "Daily"

TASK_PATTERN = re.compile(r"- \[( |x)\]")
DAILY_BLOCK_RE = re.compile(
    r"\n?<!-- DAILY_COMPLETION_START -->.*?<!-- DAILY_COMPLETION_END -->\n?",
    re.S,
)
MONTHLY_BLOCK_RE = re.compile(
    r"\n?<!-- MONTHLY_COMPLETION_START -->.*?<!-- MONTHLY_COMPLETION_END -->\n?",
    re.S,
)


def count_tasks(text: str):
    total = len(TASK_PATTERN.findall(text))
    done = len(re.findall(r"- \[x\]", text))
    return done, total


def is_today_file(md_file: Path) -> bool:
    today = date.today()
    expected_prefix = today.strftime("%d.%m.%y")
    return md_file.stem.startswith(expected_prefix)


# ==========================
# DAILY COMPLETION
# ==========================
monthly_summary = {}

for year_dir in DAILY_ROOT.iterdir():
    if not year_dir.is_dir():
        continue

    for month_dir in year_dir.iterdir():
        if not month_dir.is_dir():
            continue

        key = f"{year_dir.name} {month_dir.name}"
        monthly_summary.setdefault(key, [0, 0, []])

        for md_file in month_dir.glob("*.md"):
            original_text = md_file.read_text(encoding="utf-8")

            done, total = count_tasks(original_text)
            if total == 0:
                continue

            percent = round(done / total * 100, 1)

            monthly_summary[key][0] += done
            monthly_summary[key][1] += total
            monthly_summary[key][2].append(md_file)

            daily_block = (
                "<!-- DAILY_COMPLETION_START -->\n"
                "### ✅ Daily Completion\n"
                f"**{percent}%** ({done}/{total})\n"
                "<!-- DAILY_COMPLETION_END -->"
            )

            # Hapus block lama
            text = DAILY_BLOCK_RE.sub("", original_text).rstrip()

            lines = text.splitlines()
            output = []
            inserted = False

            for line in lines:
                output.append(line)
                if "Week" in line and not inserted:
                    output.append("")
                    output.append(daily_block)
                    inserted = True

            if not inserted:
                output.append("")
                output.append(daily_block)

            new_text = "\n".join(output).rstrip() + "\n"

            # 🔒 WRITE HANYA JIKA BERUBAH
            if new_text != original_text:
                md_file.write_text(new_text, encoding="utf-8")


# ==========================
# MONTHLY COMPLETION
# ==========================
for month_key, (done, total, files) in monthly_summary.items():
    if total == 0:
        continue

    percent = round(done / total * 100, 1)
    bars = int(percent // 10)
    bar = "█" * bars + "░" * (10 - bars)

    monthly_block = (
        "<!-- MONTHLY_COMPLETION_START -->\n"
        f"### 📊 Monthly Completion ({month_key})\n"
        f"{bar} **{percent}%**\n"
        "<!-- MONTHLY_COMPLETION_END -->"
    )

    for md_file in files:
        if not is_today_file(md_file):
            continue

        original_text = md_file.read_text(encoding="utf-8")

        text = MONTHLY_BLOCK_RE.sub("", original_text).rstrip()
        new_text = text + "\n\n" + monthly_block + "\n"

        if new_text != original_text:
            md_file.write_text(new_text, encoding="utf-8")


print("✅ Daily & Monthly completion updated (idempotent)")
