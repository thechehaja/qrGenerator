import qrcode
from PIL import Image, ImageOps

def generate_qr(data, filename="qrcode.png"):
    qr = qrcode.QRCode(
            version=1, # size of the qr code
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10, # size of each box in the qr code
            border=4, # 4 is the minimum border size
    )

    # adds data to the qr code
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")

    img = ImageOps.invert(img.convert("RGB"))

    img = img.convert("L")

    img.save(filename)
    print(f"QR Code saved as {filename}")

if __name__ == "__main__":
    # data to encode into the qr code
    data = input("Enter the data for the QR Code: ")
    filename = input("Enter the filename to save the QR Code (e.q., qrcode.png): ")

    generate_qr(data, filename)
