"""
переконвертировать время из 12-часового формата в 24-часовой, используя следующие правила:
- выходной формат должен быть 'чч:мм'
- если часы меньше 10 - допишите '0' перед ними. Например: '09:05'
"""


def time_converter(time):
    time = time.split()
    if time[1] == 'p.m.':
        if time[0][:2] == '12':
            return time[0]
        else:
            result = time[0].split(":")
            result[0] = str(int(result[0]) + 12)
            result = ':'.join(result)
            return result
    else:
        result = time[0].split(":")
        if int(result[0]) < 10:
            result[0] = '0' + result[0]
            result = ':'.join(result)
            return result
        elif int(result[0]) == 12:
            result[0] = '00'
            result = ':'.join(result)
            return result
        else:
            result = ':'.join(result)
            return result


print(time_converter('12:30 p.m.') == '12:30')
print(time_converter('9:00 a.m.') == '09:00')
print(time_converter('11:15 p.m.') == '23:15')
print(time_converter('12:00 a.m.') == '00:00')
