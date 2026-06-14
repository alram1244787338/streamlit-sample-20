"""
check_consistency.py

Verifies that the page titles, key phrases, and structural elements defined
in run.py are accurately reflected in README.md (English) and README_ja.md
(Japanese).

Run with:
    python check_consistency.py

Exit code 0  -> all checks passed
Exit code 1  -> one or more checks failed (details printed to stdout)
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent

# ---------------------------------------------------------------------------
# 1. Extract expected strings from run.py
# ---------------------------------------------------------------------------
run_py = (ROOT / "run.py").read_text(encoding="utf-8")

# Title strings used in st.title() for each language
EXPECTED_TITLES = {
    "en": "Streamlit Sample App",
    "ja": "Streamlit サンプルアプリ",
}

# Status banner strings used in st.success() (without emoji prefix)
EXPECTED_STATUS = {
    "en": "The application is running successfully.",
    "ja": "アプリは正常に動作しています。",
}

# Intro keywords that signal a real welcome message (not a placeholder)
EXPECTED_INTRO_KEYWORDS = {
    "en": "Welcome",
    "ja": "ようこそ",
}

# "Next steps" header for each language
EXPECTED_NEXT_HEADERS = {
    "en": "What's next?",
    "ja": "次のステップ",
}

# Run command that should appear in both READMEs
EXPECTED_CMD = "streamlit run run.py"

# Stale placeholder text that must NOT appear anywhere in the app
STALE_PLACEHOLDERS = [
    "動作確認中",
    "Under construction",
    "TODO",
]

# ---------------------------------------------------------------------------
# 2. Load README files
# ---------------------------------------------------------------------------
readme_en = (ROOT / "README.md").read_text(encoding="utf-8")
readme_ja = (ROOT / "README_ja.md").read_text(encoding="utf-8")

# ---------------------------------------------------------------------------
# 3. Run checks
# ---------------------------------------------------------------------------
failures: list[str] = []


def check(condition: bool, message: str) -> None:
    if not condition:
        failures.append(message)


# 3a. Verify run.py itself contains the expected titles and status strings
for lang, title in EXPECTED_TITLES.items():
    check(
        title in run_py,
        f"[run.py] Expected title for '{lang}' not found: '{title}'",
    )

for lang, status in EXPECTED_STATUS.items():
    check(
        status in run_py,
        f"[run.py] Expected status text for '{lang}' not found: '{status}'",
    )

# 3b. Verify intro welcome keywords exist in run.py
for lang, keyword in EXPECTED_INTRO_KEYWORDS.items():
    check(
        keyword in run_py,
        f"[run.py] Intro welcome keyword for '{lang}' not found: '{keyword}'",
    )

# 3c. Verify "next steps" headers exist in run.py
for lang, header in EXPECTED_NEXT_HEADERS.items():
    check(
        header in run_py,
        f"[run.py] Next-steps header for '{lang}' not found: '{header}'",
    )

# 3d. No stale placeholder text in run.py
for placeholder in STALE_PLACEHOLDERS:
    check(
        placeholder not in run_py,
        f"[run.py] Stale placeholder text found: '{placeholder}'",
    )

# 3e. Sidebar language options must be present in run.py
check(
    "English" in run_py and "日本語" in run_py,
    "[run.py] Sidebar language options ('English', '日本語') not both present.",
)

# 3f. README.md must mention the English title and status phrase
check(
    EXPECTED_TITLES["en"] in readme_en,
    f"[README.md] English page title '{EXPECTED_TITLES['en']}' not mentioned.",
)
check(
    EXPECTED_STATUS["en"] in readme_en
    or "running successfully" in readme_en.lower(),
    "[README.md] Does not describe the expected success banner.",
)

# 3g. README_ja.md must mention the Japanese title and status phrase
check(
    EXPECTED_TITLES["ja"] in readme_ja,
    f"[README_ja.md] Japanese page title '{EXPECTED_TITLES['ja']}' not mentioned.",
)
check(
    EXPECTED_STATUS["ja"] in readme_ja
    or "正常に動作" in readme_ja,
    "[README_ja.md] Does not describe the expected success banner.",
)

# 3h. Both READMEs must reference the run command
check(
    EXPECTED_CMD in readme_en,
    f"[README.md] Run command '{EXPECTED_CMD}' not found.",
)
check(
    EXPECTED_CMD in readme_ja,
    f"[README_ja.md] Run command '{EXPECTED_CMD}' not found.",
)

# 3i. File-structure sections must list run.py (not stale app.py)
for name, text in [("README.md", readme_en), ("README_ja.md", readme_ja)]:
    check(
        "app.py" not in text,
        f"[{name}] File structure still references stale 'app.py'.",
    )
    check(
        "run.py" in text,
        f"[{name}] File structure does not list 'run.py'.",
    )

# 3j. Both READMEs must mention the default language behavior
check(
    "defaults to English" in readme_en or "default" in readme_en.lower(),
    "[README.md] Does not mention the default language.",
)
check(
    "デフォルト" in readme_ja,
    "[README_ja.md] Does not mention the default language (デフォルト).",
)

# 3k. Both READMEs must mention sidebar language switching
check(
    "sidebar" in readme_en.lower(),
    "[README.md] Does not mention the sidebar language switch.",
)
check(
    "サイドバー" in readme_ja,
    "[README_ja.md] Does not mention the sidebar language switch (サイドバー).",
)

# 3l. README descriptions should reference key page sections
check(
    "What's next" in readme_en or "next" in readme_en.lower(),
    "[README.md] Does not describe the 'What's next?' section.",
)
check(
    "次のステップ" in readme_ja or "ステップ" in readme_ja,
    "[README_ja.md] Does not describe the '次のステップ' section.",
)

# 3m. No stale placeholder text in either README
for placeholder in STALE_PLACEHOLDERS:
    for name, text in [("README.md", readme_en), ("README_ja.md", readme_ja)]:
        check(
            placeholder not in text,
            f"[{name}] Stale placeholder text found: '{placeholder}'",
        )

# ---------------------------------------------------------------------------
# 4. Report results
# ---------------------------------------------------------------------------
if failures:
    print("❌ Consistency check FAILED:\n")
    for msg in failures:
        print(f"  • {msg}")
    print(f"\n{len(failures)} issue(s) found. Please align the files above.")
    sys.exit(1)
else:
    print("✅ All consistency checks passed.")
    print(
        "   Page titles, status text, intro keywords, next-steps headers,\n"
        "   sidebar options, run command, default-language notes, and file\n"
        "   structure are aligned across run.py, README.md, and README_ja.md."
    )
    sys.exit(0)
