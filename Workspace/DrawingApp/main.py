from kivy.uix.widget import Widget
from kivy.graphics import Line, Color
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.uix.scrollview import ScrollView

class DrawingPad(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.colors = [(1, 0, 0), (0.5, 1, 0.5), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1), (0.8, 0.8, 0.8), (0, 0, 0), (0.5, 0.25, 0), (1, 0.75, 0.5), (0.9, 0.65, 0.4), (1, 0, 0.5), (0.6, 0.4, 0.8), (0.5, 0.7, 1), (.8, 0, 0), (0.8, 1, 0.8), (1, 0.4, 0.4), (1, 0.6, 1), (0.2, 0.4, 0.6), (1, 0.6, 0), (0, 0.5, 0), (0, .8, .8),(0,0.9,0.8),(0.6,1,1),(.99, .99, .99)]
        self.current_color_index = 0
        self.line_thickness = 25

    def on_touch_down(self, touch):
        with self.canvas:
            Color(*self.colors[self.current_color_index])
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=self.line_thickness)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

    def change_color(self, index):
        self.current_color_index = index

class DrawingApp(MDApp):
    def build(self):
        self.drawing_pad = DrawingPad()

        clear_btn = MDIconButton(icon="delete")
        clear_btn.bind(on_release=lambda btn: self.clear_canvas())

        erase_btn = MDIconButton(icon="eraser",on_press=self.change_color_callback(24))

        color_buttons_layout = BoxLayout(orientation='horizontal', size_hint=(3, 1))
        for i, color in enumerate(self.drawing_pad.colors[:-1]):
            btn = Button(background_color=color, on_press=self.change_color_callback(i))
            color_buttons_layout.add_widget(btn)

        layout = BoxLayout(orientation='vertical')
        self.scroll_view = ScrollView(size_hint_y=0.1, do_scroll_y=False)
        layout.add_widget(clear_btn)
        layout.add_widget(erase_btn)
        layout.add_widget(self.drawing_pad)
        layout.add_widget(self.scroll_view)
        self.scroll_view.add_widget(color_buttons_layout)
        return layout

    def change_color_callback(self, index):
        return lambda btn: self.drawing_pad.change_color(index)

    def clear_canvas(self):
        self.drawing_pad.canvas.clear()

if __name__ == '__main__':
    Window.clearcolor = (1, 1, 1, 1)
    DrawingApp().run()
