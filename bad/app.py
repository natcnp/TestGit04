def reduce_to_20_characters(original):
    substitution_table = {
        'aa': 'A', 'ab': 'B', 'ac': 'C', 'ad': 'D',
        'ba': 'E', 'bb': 'F', 'bc': 'G', 'bd': 'H',
        'ca': 'I', 'cb': 'J', 'cc': 'K', 'cd': 'L',
        'da': 'M', 'db': 'N', 'dc': 'O', 'dd': 'P'
    }
    reduced = ''

    for i in range(0, len(original), 2):
        pair = original[i:i + 2]
        if pair in substitution_table:
            reduced += substitution_table[pair]

    return reduced


def convert_to_original(reduced):
    substitution_table = {
        'A': 'aa', 'B': 'ab', 'C': 'ac', 'D': 'ad',
        'E': 'ba', 'F': 'bb', 'G': 'bc', 'H': 'bd',
        'I': 'ca', 'J': 'cb', 'K': 'cc', 'L': 'cd',
        'M': 'da', 'N': 'db', 'O': 'dc', 'P': 'dd'
    }
    original = ''

    for char in reduced:
        if char in substitution_table:
            original += substitution_table[char]

    return original


# Example:
def run():
    original_text = "ababdbdadbdbdbdbdbaaaa"
    reduced_text = reduce_to_20_characters(original_text)
    converted_text = convert_to_original(reduced_text)

    print("Original Text:", original_text)
    print("Reduced Text:", reduced_text)
    print("Converted Text:", converted_text)