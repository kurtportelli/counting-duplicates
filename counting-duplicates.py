def duplicate_count(text):
    duplicates = 0
    text = text.lower()
    for c in set(text):
        if text.count(c) > 1:
            duplicates += 1
    return duplicates
