from flask import Flask, request, jsonify

app = Flask(__name__)

# 🛠 Class CaesarCipher để xử lý mã hóa & giải mã
class CaesarCipher:
    @staticmethod
    def encrypt_text(plain_text, key):
        encrypted_text = ""
        for char in plain_text:
            if char.isalpha():
                shift = key % 26  # Chỉ dịch chuyển trong bảng chữ cái
                if char.isupper():
                    encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                else:
                    encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_text += char  # Giữ nguyên ký tự không phải chữ cái
        return encrypted_text

    @staticmethod
    def decrypt_text(cipher_text, key):
        return CaesarCipher.encrypt_text(cipher_text, -key)  # Giải mã chỉ là mã hóa ngược

# 🔗 Khởi tạo class mã hóa
caesar_cipher = CaesarCipher()

# 📌 API mã hóa
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    try:
        plain_text = data['plain_text']
        key = int(data['key'])
        encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
        return jsonify({'encrypted_message': encrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 📌 API giải mã
@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    try:
        cipher_text = data['cipher_text']
        key = int(data['key'])
        decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
        return jsonify({'decrypted_message': decrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    print("🔥 Flask app is running...")
    app.run(host="0.0.0.0", port=5000, debug=True)
