#!pip install numpy
#!pip install qrcode[pil]
import qrcode

def generate_qrcode(text, output_path):
    # Create a QRCode instance
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the QRCode instance
    qr.add_data(text)
    qr.make(fit=True)

    # Create an image from the QRCode instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to the specified output path
    img.save(output_path)

if __name__ == "__main__":
    # Get text input from the user
    input_text = input("Enter the text you want to encode as a QR code: ")

    # Specify the output path for the QR code image
    output_path = r"C:\Users\NaradaJayasuriyaBIST\Desktop\Dev\QR_Generater_python\output.png"

    # Generate the QR code
    generate_qrcode(input_text, output_path)

    print(f"QR code generated and saved to {output_path}")
