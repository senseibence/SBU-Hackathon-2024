from flask import Flask, request, render_template, make_response, redirect, jsonify
from db import create_user, get_session

application = Flask(__name__)

@application.route('/sessions', methods=['GET', 'POST'])
def processSession():

    if request.method == "POST":
        
        payloadType = request.headers.get('Content-Type')
        if (payloadType == 'application/json'):

            data = request.get_json() 
            print(data)
            return jsonify(data)

    if request.method == "GET":
        return 'This is a GET request test'
        data = request.get_json() 
    
    return 'TEST RETURN AMOUNT'''
    
@application.route('/test', methods=['GET'])
def test_create():
    result = create_user()
    print(result)
    return jsonify({'user_id': str(result)})

if __name__ == '__main__':
    application.run(debug=True) # deployment: remove debug=True
    