from others import my_files
# maximum chars per message is 43.
# my signature is 19 characters. So message can be till 24 chars long.

DICTIONARY = dict(
    TXT_CANNED_MESSAGE_List_Okay_STR_M="OK",                                        # OK.
    TXT_CANNED_MESSAGE_Prompt_Okay_STR_M="OK",                                      # OK.
    TXT_CANNED_MESSAGE_List_Yes_STR_M="Ano",                                        # Ano
    TXT_CANNED_MESSAGE_Prompt_Yes_STR_M="Ano",                                      # Ano
    TXT_CANNED_MESSAGE_List_No_STR_M="Ne",                                          # Ne
    TXT_CANNED_MESSAGE_Prompt_No_STR_M="Ne",                                        # Ne
    TXT_CANNED_MESSAGE_List_Out_Riding_STR_M="Jsem na kole. Ozvu se.",              # Jezdím.
    TXT_CANNED_MESSAGE_Prompt_Out_Riding_STR_M="Jsem na kole. Ozvu se.",            # Jezdím.
    TXT_CANNED_MESSAGE_List_Be_Home_Soon_STR_M="Brzy budu doma.",                   # Brzy budu doma.
    TXT_CANNED_MESSAGE_Prompt_Be_Home_Soon_STR_M="Brzy budu doma.",                 # Brzy budu doma.
    TXT_CANNED_MESSAGE_List_Cant_Talk_Now_STR_M="Teď nemůžu. Ozvu se.",             # Teď nemůžu mluvit.
    TXT_CANNED_MESSAGE_Prompt_Cant_Talk_Now_STR_M="Teď nemůžu. Ozvu se.",           # Teď nemůžu mluvit.
    TXT_CANNED_MESSAGE_List_Busy_At_The_Moment_STR_M="Můžu psát jen ANO/NE.",       # Teď nemůžu.
    TXT_CANNED_MESSAGE_Prompt_Busy_At_The_Moment_STR_M="Můžu psát jen ANO/NE.",     # Teď nemůžu.
    TXT_CANNED_MESSAGE_List_Running_Late_STR_M="Mám menší zpoždění.",               # Se zpožděním.
    TXT_CANNED_MESSAGE_Prompt_Running_Late_STR_M="Mám menší zpoždění.",             # Se zpožděním.
    TXT_CANNED_MESSAGE_List_Almost_There_STR_M="Za chvíli jsem tam!",               # Téměř u cíle.
    TXT_CANNED_MESSAGE_Prompt_Almost_There_STR_M="Za chvíli jsem tam!",             # Téměř u cíle.
    TXT_CANNED_MESSAGE_List_Halfway_STR_M="Dorazím do půl hodiny.",                 # Jste v polovině.
    TXT_CANNED_MESSAGE_Prompt_Halfway_STR_M="Dorazím do půl hodiny.",               # Jste v polovině.

    TXT_CANNED_MESSAGE_Signature_STR_M="Odesláno z Garminu",                        # Odesláno z mého zařízení Garmin
)


JSON_FILE_NAME = "config.json"
LANG_EXTENSION = "gtt"
LANG_FILE = "E:\\Garmin\\Text\\Czech.gtt"

def json_exist() -> bool:
    return my_files.exist_file(JSON_FILE_NAME)

def get_lang_file_name() -> str:
    # return predefined file if exist
    if my_files.exist_file(LANG_FILE):
        return LANG_FILE
    # otherwise return first occurrence of *.gtt file
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


if __name__ == "__main__":
    print("writing JSON")
    my_files._write_json(JSON_FILE_NAME, DICTIONARY)
