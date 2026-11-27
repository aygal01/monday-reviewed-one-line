"""Monday, Reviewed in One Line.

Prints exactly one line: a funny one-line review of Monday.
Deterministic: no randomness, no wall-clock, no network, no file
access, no model calls. Standard library only.
"""

REVIEW = (
    "Monday: the weekend's free trial expired, the alarm clock filed "
    "for overtime, and my motivation is still buffering "
    "\u2014 1 star, would not recommend, see you again next week."
)


def review() -> str:
    """Return the one-line review of Monday."""
    return REVIEW


def main() -> None:
    line = review()
    # The contract is one line: no embedded newlines, no blank output.
    assert "\n" not in line and line.strip(), "review must be exactly one line"
    print(line)


if __name__ == "__main__":
    main()
