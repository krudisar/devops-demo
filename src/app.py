import time
import random
from flask import Flask
from flask_api import status

serverPort = 5000
app = Flask(__name__)

@app.route('/')
def hello_world():
    global requestCounter
    requestCounter += 1
    return 'Hello, World! # {0}'.format(str(requestCounter))

@app.route('/fast')
def fast_response():
    global requestCounter
    requestCounter += 1
    return 'This is a very FAST response to your HTTP request ....! # {0}'.format(str(requestCounter))

@app.route('/slow')
def slow_response():
    global requestCounter
    requestCounter += 1
    time.sleep(500 / 1000) # add 500 ms latency
    return 'This is a SLOW response to your HTTP request ....! # {0}'.format(str(requestCounter))

@app.route('/unstable')
def errors_response():
    global requestCounter
    requestCounter += 1
    '''
        -> simulate 10% error rate
    '''
    random_int = random.randint(0,10000)
    if str(random_int)[0] == '1':
        return "Record not found", status.HTTP_400_BAD_REQUEST
    else:
        return 'This is a UNSTABLE response to your HTTP request ....! # {0}'.format(str(requestCounter)
        
    return 'This is a UNSTABLE response to your HTTP request ....! # {0}'.format(str(requestCounter))

if __name__ == "__main__":
    requestCounter = 0 # global variable to store total number of requests
    app.run('0.0.0.0',port=serverPort)

