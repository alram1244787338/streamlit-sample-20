"""Basic consistency checks between the app page and the documentation.

This is intentionally dependency-free (standard library only) so it can be run
without installing Streamlit:

    python test_consistency.py

It is also pytest-compatible (``pytest test_consistency.py``).

The checks prove that the page text in ``run.py`` and the README files do not
drift apart, which is the kind of mismatch that makes a sample repo look like a
half-finished project.
"""

import ast
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent
RUN_PY = ROOT / "run.py"
README = ROOT / "README.md"
README_JA = ROOT / "README_ja.md"


def _string_constants(source_path: pathlib.Path) -> dict:
    """Return top-level ``NAME = "string"`` assignments from a Python file."""
    tree = ast.parse(source_path.read_text(encoding="utf-8"))
    constants = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            target = node.targets[0]
            value = node.value
            if (
                isinstance(target, ast.Name)
                and isinstance(value, ast.Constant)
                and isinstance(value.value, str)
            ):
                constants[target.id] = value.value
    return constants


def _first_h1(markdown_text: str):
    for line in markdown_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None


def test_page_title_matches_readme_heading():
    constants = _string_constants(RUN_PY)
    assert "APP_TITLE" in constants, "run.py must define APP_TITLE"
    heading = _first_h1(README.read_text(encoding="utf-8"))
    assert heading == constants["APP_TITLE"], (
        f"Page title {constants['APP_TITLE']!r} does not match "
        f"README.md heading {heading!r}"
    )


def test_description_is_shared_between_page_and_readme():
    constants = _string_constants(RUN_PY)
    assert "APP_DESCRIPTION" in constants, "run.py must define APP_DESCRIPTION"
    readme = README.read_text(encoding="utf-8")
    assert constants["APP_DESCRIPTION"] in readme, (
        "README.md should contain the same description sentence shown on the "
        f"page: {constants['APP_DESCRIPTION']!r}"
    )


def test_no_placeholder_text_in_app():
    source = RUN_PY.read_text(encoding="utf-8")
    assert "動作確認中" not in source, (
        "run.py still contains the placeholder text '動作確認中'"
    )


def test_readmes_reference_correct_entry_point():
    for path in (README, README_JA):
        text = path.read_text(encoding="utf-8")
        assert "streamlit run run.py" in text, (
            f"{path.name} must document how to run the app (streamlit run run.py)"
        )
        assert "app.py" not in text, (
            f"{path.name} still mentions app.py, but the entry point is run.py"
        )


def main() -> int:
    checks = [
        value
        for name, value in sorted(globals().items())
        if name.startswith("test_") and callable(value)
    ]
    failures = 0
    for check in checks:
        try:
            check()
        except AssertionError as error:
            failures += 1
            print(f"FAIL  {check.__name__}: {error}")
        else:
            print(f"PASS  {check.__name__}")

    if failures:
        print(f"\n{failures} of {len(checks)} consistency check(s) failed.")
        return 1
    print(f"\nAll {len(checks)} consistency checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
