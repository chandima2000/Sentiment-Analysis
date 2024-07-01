from flask import Flask, request, jsonify, send_file, render_template


app= Flask(__name__)


## Test Route
@app.route("/test",methods=["GET"])
def test():
    return "Test request received successfully. Service is running."



if __name__ == "__main__":
    app.run(port=5000, debug=True)
