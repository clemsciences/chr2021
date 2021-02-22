

PUNCTUATION = [".", ":", ";", ",", "?", "!", "<", ">"]


def remove_punctuation(text: str):
    for punctuation in PUNCTUATION:
        text = text.replace(punctuation, "")
    return text
