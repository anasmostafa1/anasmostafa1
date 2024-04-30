from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton, MDIconButton
from kivymd.uix.boxlayout import MDBoxLayout
from pytube import YouTube
class YouTubeDownloaderApp(MDApp):
    def build(self):
        self.title = "YouTube Downloader"
        self.theme_cls.theme_style = "Dark"
        screen = Screen()

        title = MDLabel(
            text="YouTube Downloader",
            halign="center",
            theme_text_color="Primary",
            font_style="H5",
            pos_hint={"center_x": 0.5, "center_y": 0.9},
        )
        screen.add_widget(title)

        self.url_input = MDTextField(
            hint_text="Enter YouTube video URL",
            helper_text="e.g. https://www.youtube.com/watch?v=......",
            helper_text_mode="on_focus",
            pos_hint={"center_x": 0.5, "center_y": 0.625},
            size_hint_x=None,
            width=700,
        )
        screen.add_widget(self.url_input)

        self.download_button = MDRectangleFlatButton(
            text="Download",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            on_release=self.download_video,
        )
        screen.add_widget(self.download_button)

        self.info_label = MDLabel(
            text="",
            halign="center",
            theme_text_color="Primary",
            font_style="Body1",
            pos_hint={"center_x": 0.5, "center_y": 0.4},
        )
        screen.add_widget(self.info_label)

        # Light mode button
        self.light_mode_button = MDIconButton(
            icon="theme-light-dark",
            pos_hint={"center_x": 0.5, "center_y": 0.05},
            on_release=self.toggle_theme
        )
        screen.add_widget(self.light_mode_button)

        return screen

    def toggle_theme(self, *args):
        if self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"
        else:
            self.theme_cls.theme_style = "Dark"

    def download_video(self, *args):
        url = self.url_input.text
        try:
            yt = YouTube(url)
            self.info_label.text = f"Downloading {yt.title}..."
            video_stream = yt.streams.get_highest_resolution()
            video_stream.download("./Videos")
            self.info_label.text = "Video downloaded successfully"
        except Exception as e:
            self.info_label.text = "Invalid Url..."

if __name__ == "__main__":
    YouTubeDownloaderApp().run()