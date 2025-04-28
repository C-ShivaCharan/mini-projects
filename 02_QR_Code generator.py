import qrcode

data=input("enter the QR CODE or TEXT:").strip()
filename=input("Enter the name of the file:")

qr=qrcode.QRCode(box_size=15,border=5,version=15)
qr.add_data(data)

image=qr.make_image(fill_color="black",back_color="white")
image.save(filename)

print(f"The file is saved as {filename}")