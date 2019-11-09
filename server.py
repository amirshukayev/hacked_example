from flask import Flask, jsonify

# access token: 2579652295455383
app = Flask(__name__)


# this wil be the main function
@app.route("/get_data")
def home():
    response = jsonify({"price": 1230, "acommodate": 1000})

    # response.headers.add('Access-Control-Allow-Origin', '*')
    # response.headers.add('Access-Control-Allow-Headers', '*')

    return response

if __name__ == "__main__":
    app.run()
