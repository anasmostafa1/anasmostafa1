import tkinter as tk
from customtkinter import CTk, CTkButton, CTkLabel, CTkFrame, CTkCanvas
from PIL import ImageGrab, ImageTk, Image
from tkinter import filedialog, colorchooser

class DrawingApp:
    def __init__(self, root):
        self.width = 1000
        self.height = 600
        self.root = root
        self.root.title("Drawing App")
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.configure(bg="#F0F0F0")
        self.right_frame = CTkFrame(self.root)
        self.right_frame.pack(side="top", fill="x")
        self.drawing_area = CTkCanvas(self.root, width=self.width, height=550, bg="#FFFFFF", highlightthickness=0)
        self.drawing_area.pack(padx=10, pady=15)
        self.setup()
        self.last_x, self.last_y = 0, 0
        self.drawing_area.bind('<1>', self.start_drawing)
        self.drawing_area.bind('<B1-Motion>', self.draw_line)
        self.old_x = None
        self.old_y = None
        self.line_width = 5
        self.color = '#000000'
        self.cpallete()
        self.undo_stack = []
        self.root.bind('<Control-z>', self.undo)
        self.root.bind('<Control-s>', self.save_drawing_dialog)
        self.root.bind('<Control-o>', self.open_drawing_dialog)
        self.root.bind('<Delete>', self.clear_drawing)
    def setup(self):
        self.clear_button = CTkButton(self.right_frame, text="Clear", command=self.clear_drawing, width=50, height=30, corner_radius=5)
        self.clear_button.pack(side="left", padx=10)
        self.save_button = CTkButton(self.right_frame, text="Save", command=self.save_drawing_dialog, width=50, height=30, corner_radius=5)
        self.save_button.pack(side="left", padx=10)
        self.open_button = CTkButton(self.right_frame, text="Open", command=self.open_drawing_dialog, width=50, height=30, corner_radius=5)
        self.open_button.pack(side="left", padx=10)
        self.undo_button = CTkButton(self.right_frame, text="Undo", command=self.undo, width=50, height=30, corner_radius=5)
        self.undo_button.pack(side="left", padx=10)
    def start_drawing(self, event):
        self.old_x = event.x
        self.old_y = event.y

    def draw_line(self, event):
        if self.old_x and self.old_y:
            line = self.drawing_area.create_line(self.old_x, self.old_y, event.x, event.y, 
                                          width=self.line_width, fill=self.color,
                                          capstyle=tk.ROUND, smooth=True, splinesteps=36)
            self.undo_stack.append(line)
        self.old_x = event.x
        self.old_y = event.y

    def clear_drawing(self,obj=None):
        self.drawing_area.delete("all")

    def save_drawing_dialog(self,obj=None):
        file = filedialog.asksaveasfile(mode='w', defaultextension=".png")
        if file is None:
            return
        self.save_drawing(file.name)

    def save_drawing(self, filename):
        x = self.root.winfo_rootx() + self.drawing_area.winfo_x()
        y = self.root.winfo_rooty() + self.drawing_area.winfo_y()
        x1 = x + self.drawing_area.winfo_width()
        y1 = y + self.drawing_area.winfo_height()
        ImageGrab.grab().crop((x,y,x1,y1)).save(filename)
        
    def open_drawing_dialog(self,obj=None):
        filename = filedialog.askopenfilename(title="Open Image", filetypes=[("PNG images", "*.png"), ("JPEG images", "*.jpg;*.jpeg"), ("All files", "*.*")])
        if filename:
            self.open_drawing(filename)

    def open_drawing(self, filename):
        self.clear_drawing()
        image = Image.open(filename)
        image.thumbnail((self.width, 550))  # Resize the image to fit the canvas
        photo = ImageTk.PhotoImage(image)
        self.drawing_area.create_image(0, 0, image=photo, anchor="nw")
        self.drawing_area.image = photo  # Keep a reference to prevent garbage collection
    def cpallete(self):
        self.cpallete_frame = CTkFrame(self.right_frame)
        self.cpallete_frame.pack(side="top")
        colors = ["#000000", "#ffffff", "#FF0000", "#0000FF", "#008000", "#FFFF00", "#FF00FF", "#800000", "#008080", "#808000"]
        for i, color in enumerate(colors):
            button = CTkButton(self.cpallete_frame, text="", fg_color=color, width=30, height=30, hover_color=color, corner_radius=50, command=lambda c=color: self.change_color(c))
            button.grid(row=0, column=i, padx=5, pady=5)

        self.color_picker_button = CTkButton(self.cpallete_frame, text="Pick Color", command=self.pick_color, width=100, height=30, corner_radius=5)
        self.color_picker_button.grid(row=1, column=0, columnspan=len(colors), padx=5, pady=5)

        self.size_frame = tk.Frame(self.right_frame, bg="#F0F0F0")
        self.size_frame.pack(side="top", padx=10, pady=10)
        self.size_label = CTkLabel(self.size_frame, text="Size:", bg_color="#F0F0F0")
        self.size_slider = tk.Scale(self.size_frame, from_=1, to=50, orient="horizontal", command=self.change_size)
        self.size_slider.pack(side="left", padx=5, pady=5)

    def change_color(self, color):
        self.color = color

    def pick_color(self):
        color = colorchooser.askcolor()[1]
        self.color = color

    def change_size(self, size):
        self.line_width = size

    def undo(self,obj=None):
        try:
            if self.undo_stack:
                for x in range(20):
                    line = self.undo_stack.pop()
                    self.drawing_area.delete(line)
        except:
            pass

if __name__ == "__main__":
    root = CTk()
    app = DrawingApp(root)
    root.mainloop()