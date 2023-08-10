import qrcode # https://pypi.org/project/qrcode/

img = qrcode.make('https://lego.com')
print(type(img))  # qrcode.image.pil.PilImage
img.save("test.png")