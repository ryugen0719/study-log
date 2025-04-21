from flask import Flask, render_template, request, redirect
import json
import os
from datetime import datetime

app = Flask(__name__)
DATA_FILE = 'data/log.json'

# データを読み込む関数
def load_logs():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

# データを保存する関数
def save_logs(logs):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(logs, f, ensure_ascii=False, indent=2)

@app.route('/', methods=['GET', 'POST'])
def index():
    logs = load_logs()

    if request.method == 'POST':
        name = request.form['name']
        subject = request.form['subject']
        minutes = request.form['minutes']
        time = datetime.now().strftime('%Y-%m-%d %H:%M')

        logs.append({
            'name': name,
            'subject': subject,
            'minutes': minutes,
            'time': time
        })

        save_logs(logs)
        return redirect('/')

    return render_template('index.html', logs=logs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
