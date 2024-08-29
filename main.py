import qrcode
from PIL import Image
##install qrcode library from terminal

upi_id=input("Enter UPI-ID to generate QR:- ")
cat=input("You wants to generate qr code only for UPI-Id or qr code with UPI-Id and certain ammount(For only UPI-Id type- upi & for qr code with ammount type- amt):- ")

'''upi://pay?pa=&pn=&am=&cu=&tn= where: pa = Payee address or business virtual payment address (VPA). pn = Payee name or business name. am = Transaction amount.'''

if cat=='upi':
    ###UPI-Id qr code format is copied from google.Simply search UPI-Id qr code format in your browser
    upi_url=f"upi://pay?pa={upi_id}&pn=&am=&cu=&tn"
    ###If you wants to make different qr code for different apps , uncomment below...
    # paytm_url=f"upi://pay?pa={upi_id}&pn=&am=&cu=&tn"
    # phonepe_url=f"upi://pay?pa={upi_id}&pn=&am=&cu=&tn"
    # gpay_url=f"upi://pay?pa={upi_id}&pn=&am=&cu=&tn"

    ###to generate qr code
    upi_qr=qrcode.make(upi_url)
    # paytm_qr=qrcode.make(paytm_url)
    # phonepe_qr=qrcode.make(phonepe_url)
    # gpay_qr=qrcode.make(gpay_url)

    ###to view qr code
    upi_qr.show()
    # paytm_qr.show()
    # phonepe_qr.show()
    # gpay_qr.show()

    ###To save qr code in ".png" format
    upi_qr.save('upi_qr.png') #save in the  urrent working directory
    # paytm_qr.save('paytm_qr.png')
    # phonepe_qr.save('phonepe_qr.png')
    # gpay_qr.save('phonepe_qr.png')

else:
    amt=input("Enter your ammount in rupee:- ₹")

    upi_url2=f"upi://pay?pa={upi_id}&pn=&am={amt}&cu=&tn"
    # paytm_url2=f"upi://pay?pa={upi_id}&pn=&am={amt}&cu=&tn"
    # phonepe_url2=f"upi://pay?pa={upi_id}&pn=&am={amt}&cu=&tn"
    # gpay_url2=f"upi://pay?pa={upi_id}&pn=&am={amt}&cu=&tn"

    upi_qr2=qrcode.make(upi_url2)
    # paytm_qr2=qrcode.make(paytm_url2)
    # phonepe_qr2=qrcode.make(phonepe_url2)
    # gpay_qr2=qrcode.make(gpay_url2)

    upi_qr2.show()
    # paytm_qr2.show()
    # phonepe_qr2.show()
    # gpay_qr2.show()

    upi_qr2.save('upiamtqr_image.png') 
    # paytm_qr2.save('paytm_qr.png')
    # phonepe_qr2.save('phonepe_qr.png')
    # gpay_qr2.save('phonepe_qr.png')
