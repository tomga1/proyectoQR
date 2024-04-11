import qrcode
import qrcode.constants

qr = qrcode.QRCode(version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=7,
                    border=2)

qr.add_data('https://www.derdistribuciones.com.ar/?page_id=2911')
qr.make(fit=True)

img = qr.make_image(fill_color='black', back_color='white')

img.save('QR.png') #MODIFICAR NOMBRE DEL ARCHIVO PNG

