import qrcode
from pyzbar.pyzbar import decode
from PIL  import Image

myqr = qrcode.make("https://www.youtube.com/watch?v=St48epdRDZw")
myqr1 = qrcode.make("https://www.youtube.com/watch?v=9l2Z3dNQsKk")
myqr.save("myqr.png",scale = 9)
myqr1.save("myqr1.png",scale = 10)
b = decode(Image.open("myqr.png"))
print(b[0].data.decode("ascii"))
