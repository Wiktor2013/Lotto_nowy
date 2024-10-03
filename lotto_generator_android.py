import random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class LottoApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.input_label = Label(text="Podaj liczbę losowań")
        self.layout.add_widget(self.input_label)

        self.input_field = TextInput(multiline=False, input_filter='int')
        self.layout.add_widget(self.input_field)

        self.button = Button(text="Losuj", on_press=self.on_button_press)
        self.layout.add_widget(self.button)

        self.result_label = Label(text="")
        self.layout.add_widget(self.result_label)

        return self.layout

    def lotto_generator(self, x, y):
        liczby = []
        i = 0
        while i < x:
            liczba = random.randint(1, y)
            if liczby.count(liczba) == 0:
                liczby.append(liczba)
                i += 1
        return liczby

    def on_button_press(self, instance):
        try:
            ilosc_losowan = int(self.input_field.text)
            result = ""
            for i in range(1, ilosc_losowan + 1):
                result += f'Typuję 6 z 49 liczb, Losuję {i} raz\n'
                result += str(self.lotto_generator(6, 49)) + "\n\n"
            self.result_label.text = result
        except ValueError:
            self.result_label.text = "Wprowadź poprawną liczbę losowań"


if __name__ == '__main__':
    LottoApp().run()