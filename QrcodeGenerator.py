from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivy.uix.image import Image
import qrcode
import os

class QRCodeGenerator(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.text_field = MDTextField(
            hint_text="Enter text for QR code",
            helper_text_mode="on_focus"
        )
        self.generate_button = MDRaisedButton(
            text="Generate QR Code",
            on_release=self.generate_qr_code
        )
        self.qr_image = Image()

        self.add_widget(self.text_field)
        self.add_widget(self.generate_button)
        self.add_widget(self.qr_image)

    def generate_qr_code(self, *args):
        text = self.text_field.text
        if text:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=5,
            )
            qr.add_data(text)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(".qrcode.png")
            self.qr_image.source = ".qrcode.png"
            self.qr_image.reload()
class QRCodeApp(MDApp):
    def build(self):
        screen = MDScreen()
        screen.add_widget(QRCodeGenerator())
        return screen

if __name__ == "__main__":
    QRCodeApp().run()
    