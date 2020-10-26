from others import my_files

DICTIONARY = dict(
    TXT_CANNED_MESSAGE_List_Okay_STR_M="OK",                                        # OK.
    TXT_CANNED_MESSAGE_Prompt_Okay_STR_M="OK",                                      # OK.
    TXT_CANNED_MESSAGE_List_Yes_STR_M="Ano",                                        # Ano
    TXT_CANNED_MESSAGE_Prompt_Yes_STR_M="Ano",                                      # Ano
    TXT_CANNED_MESSAGE_List_No_STR_M="Ne",                                          # Ne
    TXT_CANNED_MESSAGE_Prompt_No_STR_M="Ne",                                        # Ne
    TXT_CANNED_MESSAGE_List_Out_Riding_STR_M="Jsem na kole. Ozvu se později.",      # Jezdím.
    TXT_CANNED_MESSAGE_Prompt_Out_Riding_STR_M="Jsem na kole. Ozvu se později.",    # Jezdím.
    TXT_CANNED_MESSAGE_List_Be_Home_Soon_STR_M="Brzy budu doma.",                   # Brzy budu doma.
    TXT_CANNED_MESSAGE_Prompt_Be_Home_Soon_STR_M="Brzy budu doma.",                  # Brzy budu doma.
    TXT_CANNED_MESSAGE_List_Cant_Talk_Now_STR_M="Teď nemůžu mluvit. Ozvu se.",      # Teď nemůžu mluvit.
    TXT_CANNED_MESSAGE_Prompt_Cant_Talk_Now_STR_M="Teď nemůžu mluvit. Ozvu se.",    # Teď nemůžu mluvit.
    TXT_CANNED_MESSAGE_List_Busy_At_The_Moment_STR_M="Za chvíli jsem tam!",         # Teď nemůžu.
    TXT_CANNED_MESSAGE_Prompt_Busy_At_The_Moment_STR_M="Za chvíli jsem tam!",       # Teď nemůžu.
    TXT_CANNED_MESSAGE_List_Running_Late_STR_M="Budu mít zpoždění.",                # Se zpožděním.
    TXT_CANNED_MESSAGE_Prompt_Running_Late_STR_M="Budu mít zpoždění.",              # Se zpožděním.
    TXT_CANNED_MESSAGE_List_Almost_There_STR_M="Dorazím za 20 minut.",              # Téměř u cíle.
    TXT_CANNED_MESSAGE_Prompt_Almost_There_STR_M="Dorazím za 20 minut.",            # Téměř u cíle.
    TXT_CANNED_MESSAGE_List_Halfway_STR_M="Dorazím za 30 minut.",                   # Jste v polovině.
    TXT_CANNED_MESSAGE_Prompt_Halfway_STR_M="Dorazím za 30 minut.",                 # Jste v polovině.

    TXT_CANNED_MESSAGE_Signature_STR_M="Odesláno ze zařízení Garmin",               # Odesláno z mého zařízení Garmin
)


JSON_FILE_NAME = "config.json"
LANG_EXTENSION = "gtt"

def json_exist() -> bool:
    return my_files.exist_file(JSON_FILE_NAME)

def get_lang_file_name() -> str:
    files = my_files.get_files_with_extension(LANG_EXTENSION)
    if files:
        return my_files.get_abs_path(str(files[0]))
    else:
        return ""

def replace(text: str) -> str:
    json_data = my_files._read_json(JSON_FILE_NAME)
    DICTIONARY = dict(json_data)

    for tag, txt in DICTIONARY.items():
        if text.count(tag) != 1:
            raise ValueError("TAG occurred more times or was not found: " + tag)
        tag_pos = text.index(tag)
        start = text.index("<txt>", tag_pos)
        end = text.index("</txt>", tag_pos)
        text = text[:start+5] + str(txt) + text[end:]

    # Check if the last char is ENTER. If that you should remove it,
    # because the row count must be the same like before
    if text.endswith("\n"):
        text = text[:-1]

    return text


#if __name__ == "__main__":
#    my_files._write_json(JSON_FILE_NAME, DICTIONARY)


'''
#  Original messages are:
"""OK."""
"""Ano"""
"""Ne"""
"""Jezdím."""
"""Brzy budu doma."""
"""Teď nemůžu mluvit."""
"""Teď nemůžu."""
"""Se zpožděním."""
"""Téměř u cíle."""
"""Jste v polovině."""

# First column are original texts, second column are replaced texts
CHANGE_LIST = [
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
EXCEPTION_LIST = \
    ['Odesláno z mého zařízení Garmin']
    
FILE_NAME = 'Czech.gtt'
    
def replace_old(text: str) -> str:
for i in range(len(CHANGE_LIST)):
    orig_item = CHANGE_LIST[i][0]
    replace_item = CHANGE_LIST[i][1]
    count = text.count(orig_item)

    if count != 2:
        if not (orig_item in EXCEPTION_LIST) or count != 1:
            raise ValueError("Can not be find text - " + str(i + 1) + ". " + orig_item)
    text = text.replace(orig_item, replace_item)

# Check if the last char is ENTER. If that you should remove it,
# because the row count must be the same like before
last_char = text[len(text) - 1:len(text)]
if last_char == '\n':
    text = text[0:len(text) - 1]

return text

'''






