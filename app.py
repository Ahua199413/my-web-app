from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>這是我的第一個自動化網頁！</h1><p>CI/CD 成功跑通了！</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)