from qrcode import QRCode
from time import sleep

nick = input("Enter nickname: ")
data = input("Enter data: ")
qr = QRCode(version=5, box_size=10, border=5)

if nick.strip():
    if data:
        qr.add_data(data)
        img = qr.make_image(fill="black", back_color="white")
        img.save(f"{nick}.jpeg")
        sleep(1)
    else:
        print("Please enter the data!")
        sleep(3)
else:
    print("Enter the nickname!")
    sleep(3)



