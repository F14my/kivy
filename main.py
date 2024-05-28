from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.utils import get_color_from_hex

Window.size = (360, 640)

KV = '''
ScreenManager:
    RegistrationScreen:

<RegistrationScreen>:
    name: 'registration'

    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20), dp(20), dp(20), dp(20)
        md_bg_color: get_color_from_hex('#5228f5')

        MDCard:
            orientation: 'vertical'
            spacing: dp(20)
            padding: dp(20), dp(20), dp(20), dp(20)
            size_hint: 1, 1
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            radius: [30, 30, 30, 30]
            md_bg_color: 1, 1, 1, 1

            MDLabel:
                text: 'Регистрация'
                halign: 'center'
                font_style: 'H4'
                theme_text_color: 'Primary'
                size_hint_y: None
                height: self.texture_size[1] - dp(10)

            MDLabel:
                text: 'Уже есть аккаунт? Войти'
                halign: 'center'
                theme_text_color: 'Primary'
                size_hint_y: None
                height: self.texture_size[1] + dp(10)

            MDTextField:
                id: first_name
                hint_text: 'Имя'
                size_hint_x: None
                width: root.width * 0.8
                pos_hint: {'center_x': 0.5}

            MDTextField:
                id: last_name
                hint_text: 'Фамилия'
                size_hint_x: None
                width: root.width * 0.8
                pos_hint: {'center_x': 0.5}

            MDTextField:
                id: email
                hint_text: 'Почта'
                size_hint_x: None
                width: root.width * 0.8
                pos_hint: {'center_x': 0.5}

            MDTextField:
                id: password
                hint_text: 'Пароль'
                password: True
                size_hint_x: None
                width: root.width * 0.8
                pos_hint: {'center_x': 0.5}

            MDTextField:
                id: confirm_password
                hint_text: 'Повторите пароль'
                password: True
                size_hint_x: None
                width: root.width * 0.8
                pos_hint: {'center_x': 0.5}

            MDRaisedButton:
                text: 'Зарегистрироваться'
                size_hint_x: None
                width: root.width * 0.8
                pos_hint: {'center_x': 0.5}
                on_release: app.register()

            MDBoxLayout:
                orientation: 'horizontal'
                size_hint_x: None
                width: root.width * 0.8
                pos_hint: {'center_x': 0.5}

                MDCheckbox:
                    id: checkbox
                    size_hint: None, None
                    size: dp(48), dp(48)

                MDLabel:
                    text: 'Я принимаю политику конфиденциальности'
                    size_hint_x: None
                    width: root.width * 0.7
'''


class RegistrationScreen(Screen):
    pass


class RegistrationApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

    def register(self):
        first_name = self.root.get_screen('registration').ids.first_name.text
        last_name = self.root.get_screen('registration').ids.last_name.text
        email = self.root.get_screen('registration').ids.email.text
        password = self.root.get_screen('registration').ids.password.text
        confirm_password = self.root.get_screen('registration').ids.confirm_password.text
        accept_policy = self.root.get_screen('registration').ids.checkbox.active

        if password != confirm_password:
            print("Пароли не совпадают")
            return

        if not accept_policy:
            print("Необходимо принять политику конфиденциальности")
            return

        # Здесь можно добавить логику для регистрации пользователя
        print(f"Регистрация успешна: {first_name} {last_name} {email}")


if __name__ == '__main__':
    RegistrationApp().run()
