import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

# 定義 Webhook 接收端點
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json  # 解析 JSON 數據

    if not data:
        return jsonify({"error": "No JSON data received"}), 400

    # 解析 Webhook 內容
    ticker = data.get("ticker")  # 股票代碼
    price = data.get("price")  # 價格
    action = data.get("action", "buy")  # 買入或賣出（預設 buy）

    if not ticker or not price or not action:
        return jsonify({"error": "Missing required fields"}), 400

    # 轉換為下單大師指令
    command = ""
    if action.lower() == "buy":
        command = f"C:\OrderMaster\4.0(x64)\OrderMaster64.exe buy {ticker} {price}"
    elif action.lower() == "sell":
        command = f"C:\OrderMaster\4.0(x64)\OrderMaster64.exe sell {ticker} {price}"

    # 執行下單指令
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print(f"Executed command: {command}")
        print(f"Command Output: {result.stdout}")
        
        return jsonify({
            "message": "Order sent to 下單大師",
            "command": command,
            "output": result.stdout
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
