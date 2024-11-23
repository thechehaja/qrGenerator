import qrcode
from PIL import Image, ImageOps

def generate_qr(data, filename="qrcode.png", fill_color="black", back_color="white"):
    try:
        qr = qrcode.QRCode(
                version=1, # size of the qr code
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10, # size of each box in the qr code
                border=4, # 4 is the minimum border size
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        img.save(filename)
        print(f"QR Code saved as {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    data = input("Enter the data for the QR Code: ")
    filename = input("Enter the filename to save the QR Code (e.q., qrcode.png): ")
    fill_color = input("Enter the QR Code color (e.g., black): ") or "black"
    back_color = input("Enter the background color (e.g., white): ") or "white"
    generate_qr(data, filename, fill_color, back_color)
