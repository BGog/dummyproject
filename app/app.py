from flask import Flask, render_template, jsonify
import time
import datetime

app = Flask(__name__)
start_time = time.time()

@app.route('/')
def hello_world():
    uptime = datetime.timedelta(seconds=int(time.time() - start_time))
    return render_template('index.html', uptime=uptime)

@app.route('/health')
def health():
    """Health check endpoint for k8s liveness and readiness probes."""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.datetime.now().isoformat(),
        'uptime': str(datetime.timedelta(seconds=int(time.time() - start_time)))
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
