from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(message="Hello, World@@@")

@app.route('/api/data')
def get_data():
    # 返回一些示例数据
    return jsonify(data={"key": "value"})

if __name__ == "__main__":
    # 获取环境变量中的端口，如果没有设置则使用默认值 8061
    port = int(os.getenv("FLASK_PORT", 8062))
    app.run(host='0.0.0.0', port=port)
