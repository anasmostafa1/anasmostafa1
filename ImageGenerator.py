from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivy.uix.image import AsyncImage
import random

class ImageGeneratorApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        
        screen = Screen()
        
        self.image_url = "https://picsum.photos/800/600/?"
        self.async_image = AsyncImage(source=self.image_url)

        refresh_button = MDIconButton(icon="refresh", on_release=self.refresh_image, pos_hint={"center_x": .1, "center_y": .9})

        label = MDLabel(text="Random Image Generator", pos_hint={"center_x": .5, "center_y": .9}, halign="center", font_style="Subtitle1")
        
        screen.add_widget(self.async_image)
        screen.add_widget(refresh_button)
        screen.add_widget(label)
        
        return screen

    def refresh_image(self, instance):
        self.image_url = f"https://picsum.photos/800/600/?{random.randint(1, 1000000)}"
        self.async_image.source = self.image_url

if __name__ == "__main__":
    ImageGeneratorApp().run()