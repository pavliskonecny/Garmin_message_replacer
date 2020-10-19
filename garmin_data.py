#  Original messages are:
"""OK."""
"""ANO"""
"""NE"""
"""Jezdím."""
"""Brzy budu doma."""
"""Teď nemůžu mluvit."""
"""Teď nemůžu."""
"""Se zpožděním."""
"""Téměř u cíle."""
"""Jste v polovině."""


# First column are original texts, second column are replaced texts
change_list = [
    ['OK.', 'OK'],  # ...it can be not safety, because it can be many times inside the file.
    ['Jezdím.', 'Jsem na kole. Ozvu se později.'],
    ['Teď nemůžu mluvit.', 'Teď nemůžu mluvit. Ozvu se.'],
    ['Teď nemůžu.', 'Za chvíli jsem tam!'],
    ['Se zpožděním.', 'Budu mít zpoždění.'],
    ['Téměř u cíle.', 'Dorazím za 20 minut.'],
    ['Jste v polovině.', 'Dorazím za 30 minut.'],
    ['Odesláno z mého zařízení Garmin', 'Odesláno ze zařízení Garmin']
]

# List of texts what don't have to be 2 times in the language file
exception_list = \
    ['Odesláno z mého zařízení Garmin']

file_name = 'Czech.gtt'


def replace(text: str):
    for i in range(len(change_list)):
        orig_item = change_list[i][0]
        replace_item = change_list[i][1]
        count = text.count(orig_item)

        if count != 2:
            if not (orig_item in exception_list) or count != 1:
                raise ValueError("Can not be find text - " + str(i + 1) + ". " + orig_item)
        text = text.replace(orig_item, replace_item)

    # Check if the last char is ENTER. If that you should remove it,
    # because the row count must be the same like before
    last_char = text[len(text) - 1:len(text)]
    if last_char == '\n':
        text = text[0:len(text) - 1]

    return text


