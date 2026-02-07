import re
import uuid
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from datetime import date

BASE_DIR = Path(__file__).resolve().parent
DAILY_ROOT = BASE_DIR.parent / "Daily"
TAGS_ROOT = BASE_DIR.parent / "tags"

TASK_PATTERN = re.compile(r"- \[( |x)\]")
DAILY_BLOCK_RE = re.compile(
    r"\n?<!-- DAILY_COMPLETION_START -->.*?<!-- DAILY_COMPLETION_END -->\n?",
    re.S,
)
MONTHLY_BLOCK_RE = re.compile(
    r"\n?<!-- MONTHLY_COMPLETION_START -->.*?<!-- MONTHLY_COMPLETION_END -->\n?",
    re.S,
)

TAGS_BLOCK_RE = re.compile(
    r"(## Tags\s+Tags Worth Exploring\s+- .*?)(\n\n|$)",
    re.S,
)


def count_tasks(text: str):
    total = len(TASK_PATTERN.findall(text))
    done = len(re.findall(r"- \[x\]", text))
    return done, total


def get_tag_names(tags_root: Path) -> list[str]:
    tags = []
    for tag_file in tags_root.glob("*.md"):
        tags.append(tag_file.stem)
    return sorted(tags)


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


# ==========================
# TAGS INDEX UPDATE
# ==========================
index_file = BASE_DIR.parent / "index.md"

if index_file.exists():
    original_text = index_file.read_text(encoding="utf-8")

    # Tags dari folder
    folder_tags = get_tag_names(TAGS_ROOT)
    folder_tags_set = {f"#{t}" for t in folder_tags}

    match = TAGS_BLOCK_RE.search(original_text)

    if match:
        block = match.group(1)

        # Ambil tags yang sudah ada
        existing_tags = set(re.findall(r"#\w+", block))

        # Gabungkan (skip yang sudah ada)
        all_tags = sorted(existing_tags | folder_tags_set, key=str.lower)

        new_block = "## Tags \nTags Worth Exploring\n- " + " ".join(all_tags)

        new_text = TAGS_BLOCK_RE.sub(new_block + "\n\n", original_text)

    else:
        # Jika section Tags belum ada sama sekali
        tag_line = "- " + " ".join(f"#{t}" for t in folder_tags)
        new_block = f"\n## Tags \nTags Worth Exploring\n{tag_line}\n\n"
        new_text = original_text.rstrip() + new_block

    if new_text != original_text:
        index_file.write_text(new_text, encoding="utf-8")

# ==========================
# PRIORITY → GOOGLE CALENDAR EXPORT
# ==========================

PRIORITY_SECTION_RE = re.compile(r"# ⚡ Priority(.*?)(\n# |\Z)", re.S)
TIME_TASK_RE = re.compile(r"- \[( |x)\] (\d{2}:\d{2}) - (\d{2}:\d{2}) (.+)")

ICS_OUTPUT_DIR = BASE_DIR / "generated_ics"
ICS_OUTPUT_DIR.mkdir(exist_ok=True)


def parse_date_from_filename(md_file: Path):
    match = re.match(r"^(\d{2}\.\d{2}\.\d{2})", md_file.stem)
    if not match:
        return None
    return datetime.strptime(match.group(1), "%d.%m.%y").date()


def generate_ics_event(date_obj, start_time, end_time, title):
    start_dt = datetime.strptime(f"{date_obj} {start_time}", "%Y-%m-%d %H:%M")
    end_dt = datetime.strptime(f"{date_obj} {end_time}", "%Y-%m-%d %H:%M")
    uid = str(uuid.uuid4())
    return f"""BEGIN:VEVENT
UID:{uid}
DTSTAMP:{datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")}
DTSTART:{start_dt.strftime("%Y%m%dT%H%M%S")}
DTEND:{end_dt.strftime("%Y%m%dT%H%M%S")}
SUMMARY:{title}
BEGIN:VALARM
ACTION:DISPLAY
DESCRIPTION:Reminder: {title}
TRIGGER:-PT1M
END:VALARM
END:VEVENT
"""


today_date = date.today()

for year_dir in DAILY_ROOT.iterdir():
    if not year_dir.is_dir():
        continue

    for month_dir in year_dir.iterdir():
        if not month_dir.is_dir():
            continue

        for md_file in month_dir.glob("*.md"):
            date_obj = parse_date_from_filename(md_file)
            if not date_obj:
                continue

            ics_filename = ICS_OUTPUT_DIR / f"{md_file.stem}.ics"

            # 🛡️ LOGIK DUPLIKASI:
            # Jika file .ics sudah ada, asumsikan sudah pernah di-import.
            if ics_filename.exists():
                # Hapus file lama (bukan hari ini) untuk pembersihan berkala
                if date_obj < today_date:
                    ics_filename.unlink()
                    print(f"🗑️ Deleted old marker: {ics_filename.name}")
                continue

            text = md_file.read_text(encoding="utf-8")
            match = PRIORITY_SECTION_RE.search(text)
            if not match:
                continue

            section = match.group(1)
            tasks = TIME_TASK_RE.findall(section)
            if not tasks:
                continue

            events = []
            for status, start, end, title in tasks:
                title = title.strip().replace("*", "")
                events.append(generate_ics_event(date_obj, start, end, title))

            if not events:
                continue

            # Buat konten ICS
            ics_content = "BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//Daily Planner//EN\n"
            ics_content += "".join(events)
            ics_content += "END:VCALENDAR"

            ics_filename.write_text(ics_content, encoding="utf-8")

            # Import ke Google Calendar
            try:
                subprocess.run(
                    [
                        "gcalcli",
                        "import",
                        "--calendar",
                        "yumanuralfath1@gmail.com",
                        str(ics_filename),
                    ],
                    check=True,
                    capture_output=True,
                    text=True,
                )
                print(f"✅ Imported to Calendar: {md_file.stem}")

                # 🔒 RETENTION POLICY:
                # Jika bukan hari ini, hapus setelah import.
                # Jika hari ini, BIARKAN file tetap ada sebagai marker agar tidak re-import.
                if date_obj != today_date:
                    ics_filename.unlink()
                    print(f"🗑️ Temporary ICS deleted: {ics_filename.name}")
                else:
                    print("📌 Today's marker kept to prevent duplicates.")

            except subprocess.CalledProcessError as e:
                print(f"❌ Failed to import {ics_filename.name}: {e.stderr}")


print("✅ Priority events exported & imported to Google Calendar")
print("✅ Daily & Monthly completion updated")
print("✅ Tags Update")
