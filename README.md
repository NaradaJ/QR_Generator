# QR_Generator
Efficient Python QR Code Generator: Easily encode text into QR codes.
# QR Code Generator in Python

This Python script allows you to easily generate QR codes for any text input. Whether you want to encode URLs, contact information, or any other text data into a QR code, this script provides a simple and efficient solution.

## Features

- Generates QR codes from user-provided text input.
- Customizable QR code parameters such as error correction level, box size, and border width.
- Saves generated QR codes as image files for easy sharing and distribution.

## Prerequisites

- Python 3.x
- pip package manager

## Installation

1. Clone the repository:

    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd QR_Code_Generator_Python
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:

    ```bash
    python qr_code_generator.py
    ```

2. Enter the text you want to encode as a QR code when prompted.

3. The generated QR code will be saved as `output.png` in the project directory.

## Customization

You can customize the QR code parameters by modifying the `generate_qrcode` function in `qr_code_generator.py`. Adjust the version, error correction level, box size, and border width according to your preferences.

## Example

Here's an example of how to generate a QR code for the text "Hello, World!":

```bash
python qr_code_generator.py
Enter the text you want to encode as a QR code: Hello, World!
