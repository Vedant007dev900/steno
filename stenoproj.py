import cv2
import os
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


def hide_message():
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not filepath:
        return

    img = cv2.imread(filepath)
    msg = entry_message.get()
    password = entry_password.get()

    if not msg or not password:
        messagebox.showerror("Error", "Message and password cannot be empty!")
        return

    d = {chr(i): i for i in range(255)}
    msg_length = len(msg)

    n, m, z = 0, 0, 0

    img[n, m, z] = msg_length  # Store message length in first pixel
    m += 1  # Move to next pixel

    for char in msg:
        if n >= img.shape[0] or m >= img.shape[1]:
            messagebox.showerror("Error", "Message too long for the selected image.")
            return
        img[n, m, z] = d[char]
        m += 1
        if m >= img.shape[1]:
            m = 0
            n += 1
        z = (z + 1) % 3

    output_path = "encryptedImage.png"
    cv2.imwrite(output_path, img)
    messagebox.showinfo("Success", f"Message hidden successfully! Saved as {output_path}")
    os.system(output_path)


def extract_message():
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not filepath:
        return

    img = cv2.imread(filepath)
    password = entry_password.get()
    input_password = entry_passcode.get()

    if password != input_password:
        messagebox.showerror("Error", "Incorrect password!")
        return

    c = {i: chr(i) for i in range(255)}

    n, m, z = 0, 0, 0
    msg_length = img[n, m, z]  # Retrieve stored message length
    m += 1  # Move to next pixel

    message = ""
    for _ in range(msg_length):
        message += c[img[n, m, z]]
        m += 1
        if m >= img.shape[1]:
            m = 0
            n += 1
        z = (z + 1) % 3

    messagebox.showinfo("Decrypted Message", f"Message: {message}")


# GUI Setup
root = tk.Tk()
root.title("Image Steganography")
root.geometry("400x300")

frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="Enter Secret Message:").grid(row=0, column=0)
entry_message = tk.Entry(frame, width=30)
entry_message.grid(row=0, column=1)

tk.Label(frame, text="Set Password:").grid(row=1, column=0)
entry_password = tk.Entry(frame, width=30, show="*")
entry_password.grid(row=1, column=1)

tk.Label(frame, text="Enter Password (For Decryption):").grid(row=2, column=0)
entry_passcode = tk.Entry(frame, width=30, show="*")
entry_passcode.grid(row=2, column=1)

tk.Button(root, text="Hide Data", command=hide_message).pack(pady=10)
tk.Button(root, text="Extract Data", command=extract_message).pack(pady=10)

tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

root.mainloop()
