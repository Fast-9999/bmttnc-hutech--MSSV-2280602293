import sys
import os
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ui.caesar import Ui_MainWindow  # Import class từ caesar.py trong ui

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Kết nối nút với chức năng
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)  # Nút Encrypt
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)  # Nút Decrypt

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {
            "plain_text": self.ui.txt_plain_text.toPlainText(),
            "key": self.ui.txt_key.text()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setText(data["encrypted_message"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
                print(f"Errors: {response.text} % RequestException")
        except requests.exceptions.RequestException as e:
            print(f"Error: {str(e)} % RequestException")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            "cipher_text": self.ui.txt_cipher_text.toPlainText(),
            "key": self.ui.txt_key.text()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setText(data["decrypted_message"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
                print(f"Errors: {response.text} % RequestException")
        except requests.exceptions.RequestException as e:
            print(f"Error: {str(e)} % RequestException")

if __name__ == "__main__":
    # Cấu hình đường dẫn đến thư mục platforms
    dirname = os.path.dirname(__file__)
    plugin_path = os.path.join(dirname, 'platforms')
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

    