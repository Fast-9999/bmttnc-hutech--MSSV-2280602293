from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher  # Đảm bảo module này tồn tại và đúng đường dẫn

app = Flask(__name__)

# Khởi tạo đối tượng mã hóa Caesar
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    try:
        data = request.json
        print(f"📥 Dữ liệu nhận được: {data}")
        
        # Lấy giá trị từ request, tránh lỗi KeyError
        plain_text = data.get("plain_text", "")
        key = int(data.get("key", 0))
        
        print(f"🔑 Đang mã hóa: '{plain_text}' với key {key}")
        encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
        print(f"📝 Kết quả mã hóa: '{encrypted_text}'")
        
        return jsonify({"encrypted_message": encrypted_text})
    except Exception as e:
        print(f"❌ Lỗi mã hóa: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    try:
        data = request.json
        print(f"📥 Dữ liệu nhận được: {data}")
        
        cipher_text = data.get("cipher_text", "")
        key = int(data.get("key", 0))
        
        print(f"🔑 Đang giải mã: '{cipher_text}' với key {key}")
        decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
        print(f"📝 Kết quả giải mã: '{decrypted_text}'")
        
        return jsonify({"decrypted_message": decrypted_text})
    except Exception as e:
        print(f"❌ Lỗi giải mã: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("🔥 Flask app is starting...")  # Debug log
    app.run(host="0.0.0.0", port=5000, debug=True)
