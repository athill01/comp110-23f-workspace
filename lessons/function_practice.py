"""Practicing Functions."""

def mimic(my_word: str, idx: int) -> str:
    """Outputs the character of my_words at index letter_idx."""
    if idx >= len(my_word):
        return "Index too high"
    else:
        return my_word[idx]