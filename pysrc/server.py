import Flask from flask
import jsonify
import recognition

app = Flask(__name__)

@app.route('/runrecognizer/<id>', methods=['GET'])
def runRecognizer(id):
    result = recognition.runSpeechRecognizer(id)
    if result == "fail":
        return jsonify({"code": 400,
                        "message": "fail"})
    return jsonify({"code": 200,
                    "message": "success",
                    "data": result})

if __name__ == '__main__':
    app.run(debug=False)