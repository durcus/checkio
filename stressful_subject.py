"""
 Функция должна распознавать является ли тема письма стрессовой. Стрессовая тема определяется тем, что все буквы в верхнем регистре, и / или заканчиваются как минимум тремя восклицательными знаками, и / или содержат по крайней мере одно из следующих слов-маркеров: "help", "asap", "urgent". Любое из этих слов-маркеров может быть написано по-разному: «HELP», «help», «HeLp», «H! E! L! P!», «H-E-L-P», и даже очень непринужденно «HHHEEEEEEEEELLP».
Входные данные: Тема письма в виде строки.
Выходные данные: Boolean.
"""


def is_stressful(subj):
    if subj.isupper():
        return True
    if subj[-3:] == '!!!':
        return True
    subj = subj.lower()
    if 'h' in subj and 'e' in subj and 'l' in subj and 'p' in subj:
        result = 'h'
        for i in subj[subj.find('h') + 1:]:
            if i != result[-1] and i.isalpha():
                result += i
        if 'help' in result:
            return True
    if 'a' in subj and 's' in subj and 'p' in subj:
        result = 'a'
        for i in subj[subj.find('a') + 1:]:
            if i != result[-1] and i.isalpha():
                result += i
        if 'asap' in result:
            return True
    if 'u' in subj and 'r' in subj and 'g' in subj and 'e' in subj\
       and 'n' in subj and 't' in subj:
        result = 'u'
        for i in subj[subj.find('u') + 1:]:
            if i != result[-1] and i.isalpha():
                result += i
        if 'urgent' in result:
            return True
    return False


print(is_stressful("Hi") == False)
print(is_stressful("Hi!!!") == True)
print(is_stressful("I neeed HELP") == True)
print(is_stressful("something is gona happen") == False)
print(is_stressful("He loves peace") == False)
