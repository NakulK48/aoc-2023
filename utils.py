from pathlib import Path


def get_lines(problem: int) -> list[str]:
    raw = Path(f"problem_{problem:02}.txt").read_text()
    return raw.strip().splitlines()


def get_sections(problem: int) -> list[str]:
    raw = Path(f"problem_{problem:02}.txt").read_text()
    return raw.strip().split("\n\n")
