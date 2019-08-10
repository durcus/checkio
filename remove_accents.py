"""
Assuming you are developing a user based system like facebook, you will want to provide the functionality to search for other members regardless of the presence of accents in a username. Without using 3rd party collation library, you will need to remove the accents from username before comparison.
é - letter with accent; e - letter without accent; ̀ and ́ - stand alone accents;
Input: A phrase as a string (unicode)
Output: An accent free Unicode string.
"""

import unicodedata


def checkio(in_string):
    if len(in_string) == 0 or unicodedata.east_asian_width(in_string[0]) == 'W':
        return in_string
    else:
        nfkd_form = unicodedata.normalize('NFKD', in_string)
        only_ascii = nfkd_form.encode('ASCII', 'ignore')
        result = only_ascii.decode("utf-8")
        return result


print(checkio(u"préfèrent") == u"preferent")
print(checkio(u"loài trăn lớn") == u"loai tran lon")
print(checkio("完好無缺") == "完好無缺")



