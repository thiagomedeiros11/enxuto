# Enxuto

Minimal image viewer built with Python and Tkinter. Simple, fast, no distractions — just open an image and zoom with the mouse wheel.

## Features

- Opens `.jpg`, `.jpeg`, `.png`, `.webp`, etc.
- Zoom with mouse wheel
- Click and drag to move the image
- Close with ❌ button
- Lightweight and fast

## Installation

### Requirements

- Python 3
- Pillow

You can install Pillow with:

```bash
pip install pillow
```

### Make the script executable:

```bash
chmod +x enxuto.py
```

### (Optional) Move it to a system-wide location:


```bash
sudo cp enxuto.py /usr/local/bin/enxuto
```

## Usage

### To open an image:
```bash
./enxuto.py path/to/image.jpg
```

Or, if installed globally:

```bash
enxuto path/to/image.jpg
```

## In Thunar:

Right-click any image (.jpg, .png, etc)

Go to Properties → Open With

Select Enxuto from the list (or click "Open with another application..." and choose it)

Click Set as default

Done! Now images will open with Enxuto by default when double-clicked.

