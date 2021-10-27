from zhanbu import duanyi
from flask import Flask, render_template, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app = Flask(__name__, template_folder='.')

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["30 per minute", "2 per second"],
)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

    
@app.route('/yi', methods=['GET'])
@limiter.limit("10 per day")
def yi():
    m, s, c = duanyi()
    res = jsonify({'m' : m, 's':s, 'c':c})
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)