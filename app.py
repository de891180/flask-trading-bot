import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# 本地 Webhook 接收端點
@app.route('/webhook', methods=['POST'])
def local_webhook():
    # 接收下單大師的數據
    data = request.json
    if not data:
        return jsonify({"error": "No JSON data received"}), 400

    # 日誌輸出
    print(f"Received from 下單大師: {data}")

    # 轉發到 Render 的伺服器
    render_url = "https://api.render.com/deploy/srv-cuchbqpopnds739884h0?key=yyjzWbp1Nv4/webhook"  # 替換為 Render 的 URL
    try:
        response = requests.post(render_url, json=data)
        print(f"Forwarded to Render: {response.status_code}, {response.text}")
        return jsonify({"message": "Forwarded to Render", "render_response": response.json()}), response.status_code
    except Exception as e:
        print(f"Error forwarding to Render: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # 本地伺服器運行在 5000 埠
    app.run(host='0.0.0.0', port=5000)
