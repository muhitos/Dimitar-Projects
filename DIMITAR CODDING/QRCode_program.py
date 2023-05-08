import pyqrcode
import png
from pyqrcode import QRCode

qr_url = 'https://www.mobile.bg/pcgi/mobile.cgi?act=4&adv=21636474682849145'
url = pyqrcode.create(qr_url)
url.png('my_qrcode', scale=8)

