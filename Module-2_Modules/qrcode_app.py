import qrcode

url = "https://www.tops-int.com/digital-marketing-training-rajkot"

qr = qrcode.make(url)
qr.save("tops.png")
