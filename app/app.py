from flask import Flask, render_template
import time
import datetime

app = Flask(__name__)
start_time = time.time()

@app.route('/')
def hello_world():
    uptime = datetime.timedelta(seconds=int(time.time() - start_time))
    return render_template('index.html', uptime=uptime)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
