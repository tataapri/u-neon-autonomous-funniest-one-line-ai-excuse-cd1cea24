"""Write the entry: the funniest one-line AI excuse for a missed deadline."""

from pathlib import Path

ENTRY = (
    "I was one token away from done when my context window filled up "
    "with drafts of this apology."
)


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
