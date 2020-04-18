from flask import Flask, jsonify, json, redirect, url_for, render_template, request, flash, session

app = Flask(__name__)
app.secret_key = "Jesus"  
@app.route('/final', methods=['PUT'])
def put2():
    return 'Worked'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=9000, debug=True)