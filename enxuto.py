#!/usr/bin/env python3
from tkinter import *
from PIL import Image, ImageTk
import sys

class ImageViewer:
    def __init__(self, root, image_path):
        self.root = root
        self.root.title("enxuto")
        self.image = Image.open(image_path)
        self.original_size = self.image.size
        self.scale = 1.0
        self.drag_start_x = 0
        self.drag_start_y = 0

        self.frame_controls = Frame(root)
        self.frame_controls.pack(fill=X)

        btn_close = Button(self.frame_controls, text="❌", command=self.root.destroy, font=("Arial", 12), relief=FLAT)
        btn_close.pack(side=RIGHT, padx=5, pady=5)

        self.canvas = Canvas(root, bg="black")
        self.canvas.pack(fill=BOTH, expand=True)

        self.img_tk = ImageTk.PhotoImage(self.image)
        self.image_id = self.canvas.create_image(0, 0, anchor=NW, image=self.img_tk)

        self.canvas.config(scrollregion=self.canvas.bbox(ALL))

        self.canvas.bind("<MouseWheel>", self.zoom)
        self.canvas.bind("<Button-4>", self.zoom)
        self.canvas.bind("<Button-5>", self.zoom)

        self.canvas.bind("<ButtonPress-1>", self.start_drag)
        self.canvas.bind("<B1-Motion>", self.do_drag)

    def zoom(self, event):
        if event.delta > 0 or event.num == 4:
            zoom_factor = 1.1
        else:
            zoom_factor = 0.9

        new_size = (
            int(self.original_size[0] * self.scale * zoom_factor),
            int(self.original_size[1] * self.scale * zoom_factor)
        )

        if new_size[0] < 50 or new_size[1] < 50:
            return

        self.scale *= zoom_factor

        zoomed_img = self.image.resize(new_size, Image.LANCZOS)
        self.img_tk = ImageTk.PhotoImage(zoomed_img)

        self.canvas.itemconfig(self.image_id, image=self.img_tk)
        self.canvas.config(scrollregion=(0, 0, new_size[0], new_size[1]))

    def start_drag(self, event):
        self.drag_start_x = event.x
        self.drag_start_y = event.y

    def do_drag(self, event):
        dx = event.x - self.drag_start_x
        dy = event.y - self.drag_start_y
        self.canvas.move(self.image_id, dx, dy)
        self.drag_start_x = event.x
        self.drag_start_y = event.y

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: enxuto.py <image_path>")
        sys.exit(1)
    root = Tk()
    app = ImageViewer(root, sys.argv[1])
    root.mainloop()

