from flask import Flask, request, jsonify
import qcClientService
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def connectionStatus():
    return "Backend running properly"

@app.route("/getNextClient", methods = ['POST', 'GET'])
def getNextClient():
    if request.method == 'POST':
        jsonResponse = qcClientService.main()
        print("\n-- JSON Response: --\n")
        print(jsonResponse)
        return jsonify(jsonResponse)
    
if __name__ == '__main__':
   app.run(debug=True)
