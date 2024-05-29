from kivy.lang import Builder
from kivy.properties import DictProperty
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
import webbrowser as web

KV = '''
MDScreen:
    MDFloatingActionButtonSpeedDial:
        id: speed_dial
        data: app.data
    MDTextField:
        id: search_bar
        hint_text: "Search"
        on_text_validate: app.search_website(self.text)
        pos_hint: {'center_y':.7,'center_x':.5}
        size_hint_x: None
        width: 750
'''

class Browser(MDApp):
    data = DictProperty()

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.data = {
            'Twitter':[
                'twitter',
                "on_press", lambda x: web.open("https://www.twitter.com")
            ],
            'Facebook': [
                'facebook',
                "on_press", lambda x: web.open("https://www.facebook.com") ,
            ],
            'Instagram': [
                'instagram',
                "on_press", lambda x: web.open("https://www.instagram.com") ,
            ],
            'Youtube': [
                'youtube',
                "on_press", lambda x: web.open("https://www.youtube.com") ,
            ],
            'Spotify': [
                'spotify',
                "on_press", lambda x: web.open("https://www.spotify.com") ,
            ],
            'Google': [
                'google',
                "on_press", lambda x: web.open("https://app.google.com") ,
            ],
            'Maps': [
                'google-maps',
                "on_press", lambda x: web.open("https://www.google.com") ,
            ],
            'Bing': [
                'microsoft-bing',
                "on_press", lambda x: web.open("https://www.bing.com") ,
            ],
        }
        return Builder.load_string(KV)

    def search_website(self, query):
        # Handle the search query here (e.g., open a search engine with the query)
        web.open(f"https://www.google.com/search?q={query}")

if __name__ == "__main__":
    Browser().run()
