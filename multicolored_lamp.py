"""
Реализовать класс Lamp() (лампочка) и метод light(), который будет заставлять лампочку загораться очередным цветом в последовательности (‘Green’, ‘Red’, ‘Blue’, ‘Yellow’) при каждом включении. Если в данный момент цвет лампочки - Yellow, то при следующем включении она загорится зеленым (Green) и так далее. В этой миссии вам может помочь такой шаблон проектирования, как State. Он полезен в ситуациях, когда объект должен менять свое поведение в зависмости от внутреннего состояния.
"""


class Lamp():
    def __init__(self, c=-1):
        self.c = c

    def light(self):
        self.res = ('Green', 'Red', 'Blue', 'Yellow')[self._counter(self.c)]
        return self.res

    def _counter(self, c):
        self.c = c + 1
        if self.c == 4:
            self.c = 0
        return self.c


lamp_1 = Lamp()
lamp_2 = Lamp()
lamp_1.light()  # Green
lamp_1.light()  # Red
lamp_2.light()  # Green
print(lamp_1.light() == "Blue")
print(lamp_1.light() == "Yellow")
print(lamp_1.light() == "Green")
print(lamp_2.light() == "Red")
print(lamp_2.light() == "Blue")

