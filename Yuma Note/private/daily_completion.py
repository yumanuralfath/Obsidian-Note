import re
from pathlib import Path

DAILY_ROOT = Path("../Daily")

TASK_PATTERN = re.compile(r"- \[( |x)\]")

DAILY_BLOCK_RE = re.compile(
    r"<!-- DAILY_COMPLETION_START -->(.*?)<!-- DAILY_COMPLETION_END -->", re.S
)

MONTHLY_BLOCK_RE = re.compile(
    r"<!-- MONTHLY_COMPLETION_START -->(.*?)<!-- MONTHLY_COMPLETION_END -->", re.S
)


def count_tasks(text):
    total = len(TASK_PATTERN.findall(text))
    done = len(re.findall(r"- \[x\]", text))
    return done, total


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
            text = md_file.read_text(encoding="utf-8")

            done, total = count_tasks(text)
            if total == 0:
                continue

            percent = round(done / total * 100, 1)
            monthly_summary[key][0] += done
            monthly_summary[key][1] += total
            monthly_summary[key][2].append(md_file)

            daily_block = f"""
<!-- DAILY_COMPLETION_START -->
### ✅ Daily Completion
**{percent}%** ({done}/{total})
<!-- DAILY_COMPLETION_END -->
""".strip()

            text = DAILY_BLOCK_RE.sub("", text).rstrip()

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

            md_file.write_text("\n".join(output), encoding="utf-8")


# ==========================
# MONTHLY COMPLETION
# ==========================
for month_key, (done, total, files) in monthly_summary.items():
    if total == 0:
        continue

    percent = round(done / total * 100, 1)
    bars = int(percent // 10)
    bar = "█" * bars + "░" * (10 - bars)

    monthly_block = f"""
<!-- MONTHLY_COMPLETION_START -->
### 📊 Monthly Completion ({month_key})
{bar} **{percent}%**
<!-- MONTHLY_COMPLETION_END -->
""".strip()

    for md_file in files:
        text = md_file.read_text(encoding="utf-8")
        text = MONTHLY_BLOCK_RE.sub("", text).rstrip()
        text += "\n\n" + monthly_block
        md_file.write_text(text, encoding="utf-8")

print("✅ Daily & Monthly completion updated (folder-based)")
