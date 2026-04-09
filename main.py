import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class GuessGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 40
        self.spacing = 20

        self.secret_number = random.randint(1, 100)
        
        self.label = Label(text="Вгадай число від 1 до 100", font_size='20sp')
        self.add_widget(self.label)

        self.user_input = TextInput(multiline=False, input_filter='int', font_size='30sp', halign='center')
        self.add_widget(self.user_input)

        self.btn = Button(text="Перевірити", background_color=(0, 0.7, 0.9, 1), font_size='20sp')
        self.btn.bind(on_press=self.check_guess)
        self.add_widget(self.btn)

    def check_guess(self, instance):
        try:
            guess = int(self.user_input.text)
            if guess < self.secret_number:
                self.label.text = "Мало! Спробуй більше."
            elif guess > self.secret_number:
                self.label.text = "Багато! Спробуй менше."
            else:
                self.label.text = f"Перемога! Це було {self.secret_number}"
        except ValueError:
            self.label.text = "Введи число!"

class MyApp(App):
    def build(self):
        return GuessGame()

if __name__ == '__main__':
    MyApp().run()
