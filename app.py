from flask import Flask, request, jsonify

app = Flask(__name__)

# Render 端 Webhook
@app.route('/webhook', methods=['POST'])
def render_webhook():
    data = request.json
    if not data:
        return jsonify({"error": "No JSON data received"}), 400

    # 日誌輸出
    print(f"Received on Render: {data}")

    # 返回成功響應
    return jsonify({"message": "Webhook received", "data": data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
