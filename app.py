from flask import Flask, request, jsonify

app = Flask(__name__)

# Webhook 接收邏輯
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if not data:
        return jsonify({"error": "No JSON data received"}), 400

    # 解析訊號數據
    ticker = data.get("ticker")  # 股票代碼
    price = data.get("price")    # 目標價格
    action = data.get("action", "buy")  # 動作（買入或賣出）

    # 日誌輸出（可選）
    print(f"Received data: Ticker={ticker}, Price={price}, Action={action}")

    # 回應成功
    return jsonify({"message": "Webhook received", "data": data}), 200

if __name__ == '__main__':
    # 將 Flask 運行在 port 80
    app.run(host='0.0.0.0', port=80)
