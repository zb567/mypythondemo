from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(message="Hello, World!")

@app.route('/api/data')
def get_data():
    # 返回一些示例数据
    return jsonify(data={"key": "value"})

if __name__ == "__main__":
    app.run(debug=True)
