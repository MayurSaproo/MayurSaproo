from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel

class LoginApp(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Teal"

        # Username Input
        self.username = MDTextField(
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            size_hint=(0.8, 0.1),
            hint_text="Username",
            mode="rectangle",
            icon_right="account-circle"
        )
        screen.add_widget(self.username)

        # Password Input
        self.password = MDTextField(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(0.8, 0.1),
            hint_text="Password",
            password=True,
            mode="rectangle",
            icon_right="lock-off"
        )
        screen.add_widget(self.password)

        # Login Button
        login_button = MDFillRoundFlatButton(
            text="Login",
            pos_hint={'center_x': 0.5, 'center_y': 0.4},
            on_release=self.login
        )
        screen.add_widget(login_button)

        # Message Label
        self.message = MDLabel(
            text="Hello python language",
            halign="center",
            pos_hint={'center_x': 0.5, 'center_y': 0.3}
        )
        screen.add_widget(self.message)

        return screen

    def login(self, instance):
        username = self.username.text
        password = self.password.text

        # Here you would typically check against a database or API
        if username == "h" and password == "h":
            self.message.text = "Login Successful!"
        else:
            self.message.text = "Invalid Credentials"

if __name__ == "__main__":
    LoginApp().run()