import tkinter as tk
from tkinter import filedialog, messagebox, PhotoImage
from PIL import Image, ImageTk
import qrcode

def generate_qr():
    data = data_entry.get()
    filename = filename_entry.get()
    fill_color = fill_color_entry.get() or "black"
    back_color = back_color_entry.get() or "white"
    logo_path = logo_path_entry.get() or None

    if not data:
        messagebox.showerror("Error", "Data for the QR Code cannot be empty.")
        return

    if not any(filename.lower().endswith(ext) for ext in [".png", ".jpg", ".jpeg", ".bmp", ".gif"]):
        filename += ".png"

    try:
        qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size = 10,
                border = 4,
            )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGB")

        if logo_path:
            try:
                logo = Image.open(logo_path)
                qr_width, qr_height = img.size
                logo_size = int(qr_width * 0.2)
                logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
                pos = (qr_width - logo_size - 10, qr_height - logo_size - 10)
                img.paste(logo, pos, mask=logo.convert("RGBA"))
            except Exception as e:
                messagebox.showerror("Error", f"Failed to add logo: {e}")
                return

        img.save(filename)
        preview_qr(img)
        messagebox.showinfo("Success", f"QR Code saved as {filename}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def browse_logo():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")])
    logo_path_entry.delete(0, tk.END)
    logo_path_entry.insert(0, file_path)

def preview_qr(image):
    img = image.resize((200, 200), Image.Resampling.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)
    preview_label.configure(image=img_tk)
    preview_label.image = img_tk

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x700")
root.resizable(False, False)

tk.Label(root, text="Data for QR Code:").pack(pady=5)
data_entry = tk.Entry(root, width=40, justify=tk.CENTER)
data_entry.pack(pady=5)

tk.Label(root, text="Filename:").pack(pady=5)
filename_entry = tk.Entry(root, width=40, justify=tk.CENTER)
filename_entry.pack(pady=5)

tk.Label(root, text="QR Code Color (default: black):").pack(pady=5)
fill_color_entry = tk.Entry(root, width=40, justify=tk.CENTER)
fill_color_entry.pack(pady=5)

tk.Label(root, text="Background color (default: white):").pack(pady=5)
back_color_entry = tk.Entry(root, width=40, justify=tk.CENTER)
back_color_entry.pack(pady=5)

tk.Label(root, text="Logo Path (optional):").pack(pady=5)
logo_frame = tk.Frame(root)
logo_frame.pack(pady=5)

logo_path_entry = tk.Entry(logo_frame, width=29, justify=tk.CENTER)
logo_path_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(logo_frame, text="Browse", height=1, command=browse_logo).grid(row=0, column=2, padx=5, pady=5)

tk.Button(root, text="Generate QR Code", command=generate_qr).pack(pady=20)

tk.Label(root, text="QR Code Preview:").pack(pady=5)
default_image = PhotoImage(width=200, height=200)
preview_label = tk.Label(root, image=default_image, bg="white", width=200, height=200, bd=2, relief="solid")
preview_label.image = default_image
preview_label.pack(pady=5)

root.mainloop()
