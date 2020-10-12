from flask import Flask, jsonify, escape, request, Response
import random
import hashlib
import math

# instansiate the Flask object
app = Flask(__name__)

# the main route url route
@app.route('/')
def hello():
    return "Hello, Welcome to group project #5."

''' example
@app.route('/md5/<string>')
def json_response():
    resp = Response('{ "foo": "bar", "baz": "bat" }')
    resp.headers['Content-Type'] = 'application/json'
    return resp
'''

@app.route('/md5/')
def md5_response():
    resp = hashlib.md5({string})
    return resp

@app.route('/factoral/')
def factoral_response():
    resp = math.factoral({int})
    return resp

'''@app.route('/fibonacci/')
def fibonacci_response():
    resp = 
'''

@app.route('/is-prime/')
def prime_response():
    if {int} > 1:
        for i in range(2, {int}):
            if ({int} % i) == 0:
                resp = False
                break
            else:
                resp = True
    else:
        resp = False
    
    return resp
         

'''@app.route('/slack-alert/')
def slack_alert_response():
    resp =
'''

# Run  this flask server if file is called directly
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
