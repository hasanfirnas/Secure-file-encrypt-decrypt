# Secure File Encryption and Decryption with Fernet Key

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

This Python project provides a user-friendly graphical interface for securely encrypting and decrypting files using the Fernet encryption scheme. Fernet is a symmetric key encryption method that ensures the confidentiality and integrity of your files.

## Features

- **Encryption:** Protect your sensitive files by encrypting them with a Fernet key.
- **Decryption:** Easily decrypt files using the same Fernet key that was used for encryption.
- **Key Generation:** Generate strong Fernet encryption keys with a single click.
- **User-Friendly Interface:** A simple and intuitive GUI for easy file encryption and decryption.
- **Log Management:** Keep track of your encryption and decryption activities with an integrated logging system.

## Usage

### Setup

Before using this project, ensure you have Python 3.8 or higher installed on your system.

1. Clone this repository:

   ```bash
   git clone https://github.com/hasanfirnas/Secure-file-encrypt-decrypt.git
    ```
2. Navigate to the project directory:

    ```bash
   cd Secure-file-encrypt-decrypt
    ```
3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```
## Running the Application

Run the Main.py script to launch the graphical interface:

   ```bash
   python Main.py
   ```

### Example

Let's walk through an example of how to use the application to securely encrypt and decrypt a file:

1. **Launch the Application:**
   - Run the `Main.py` script to start the graphical interface.

2. **Generate a Fernet Key:**
   - Click the "Generate Key" button to create a new Fernet encryption key. The generated key will be automatically copied to your clipboard for easy access.

3. **Select the Input File to Encrypt:**
   - Click "Select Input File" to choose the file you want to encrypt. This could be a sensitive document, image, or any file you want to protect.

4. **Choose the Output Location:**
   - Click "Select Output File" to specify where the encrypted file should be saved. Provide a file name and location for the encrypted result.

5. **Encrypt the File:**
   - Once you've selected the input file and specified the output location, click the "Encrypt" button. The application will use the generated Fernet key to encrypt the selected file.

<div style="text-align:center">
    <img src="https://github.com/hasanfirnas/Secure-file-encrypt-decrypt/assets/63351774/f35e1fa4-7cd7-49c0-ad87-a08336c2c13d" width="600" alt="Example">
</div>

6. **Decrypt the File (Optional):**
   - If you ever need to access the original content, follow the same steps to decrypt the file:
     - Click "Select Input File" and choose the encrypted file.
     - Select the output location for the decrypted result.
     - Click the "Decrypt" button. The application will use the same Fernet key for decryption.

By following these steps, you can securely protect your files with Fernet encryption, ensuring their confidentiality and integrity. The generated key is conveniently copied to your clipboard for safekeeping.
