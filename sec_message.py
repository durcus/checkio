"""
 Дан кусок текста. Соберите все заглавные буквы в одно слово в том порядке как они встречаются в куске текста.
Например: текст = "How are you? Eh, ok. Low or Lower? Ohhh.", если мы соберем все заглавные буквы, то получим сообщение "HELLO".
"""


def sec_mes(text):
    message = ''
    for i in text:
        if i.isupper():
            message += i
    return message


print(sec_mes("How are you? Eh, ok. Low or Lower? Ohhh."))
print(sec_mes("hello world!"))
