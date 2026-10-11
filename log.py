"""Add a dated entry to LOG.md, commit it, and push.

Usage:
    python log.py "Read 1.1-1.3, did exercises 1.1-1.5"
    python log.py --local "..."    # commit but don't push
"""
import argparse
import datetime
import pathlib
import subprocess
import sys

LOG = pathlib.Path(__file__).parent / "LOG.md"


def git(*args):
    return subprocess.run(["git", *args], cwd=LOG.parent).returncode


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("entry", help="what you did")
    parser.add_argument("--local", action="store_true", help="commit but don't push")
    args = parser.parse_args()

    entry = args.entry.strip().replace("|", "/").replace("\n", " ")
    if not entry:
        sys.exit("Entry is empty.")

    today = datetime.date.today().isoformat()
    text = LOG.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        text += "\n"
    LOG.write_text(text + f"| {today} | {entry} |\n", encoding="utf-8")
    print(f"Logged: {today} | {entry}")

    if git("add", "-A") or git("commit", "-q", "-m", f"Log {today}: {entry}"):
        sys.exit("Logged, but the git commit failed. Commit by hand.")
    if not args.local and git("push", "-q"):
        sys.exit("Committed, but the push failed. Run `git push` when you're online.")


if __name__ == "__main__":
    main()
