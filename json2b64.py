from pathlib import Path
import tkinter as tk
from tkinter import filedialog
import base64

root = tk.Tk()
root.withdraw()

# Open dialog starting at the current working directory in one step
file_path = filedialog.askopenfilename(initialdir=str(Path.cwd()), filetypes=[("JSON files", "*.json")])

if file_path:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    b64_encoded = base64.b64encode(content.encode()).decode()
    print(b64_encoded)