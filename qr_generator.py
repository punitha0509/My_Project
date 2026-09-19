import qrcode

def make_qr(text, filename="qr_code.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    return filename

def main():
    url = "https://www.bioxsystems.com/"
    path = make_qr(url)
    print(f"Saved {path} for {url}")

main()