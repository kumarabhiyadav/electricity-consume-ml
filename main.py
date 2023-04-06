from flask import Flask, jsonify, request
from model import getPredictedValue
# creating a Flask app
app = Flask(__name__)

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.


@app.route('/', methods=['GET', 'POST'])
def home():
    if(request.method == 'GET'):

        data = "hello world"
        return jsonify({'data': data})


# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)
@app.route('/year/<int:year>/month/<int:month>', methods=['GET'])
def disp(year, month):
    if(len(str(year)) < 5 and month <= 12 and month >= 1):
     expectedConsumption = getPredictedValue(year, month)
     return jsonify({'year': year, 'month': month, 'watt': expectedConsumption})
    else :
        return jsonify({'error': 'Invalid Year and month'})


# driver function
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
