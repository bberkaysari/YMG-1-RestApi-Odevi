from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sum', methods=['GET'])
def sum_numbers():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    if a is not None and b is not None:
        result = a + b
        return jsonify({"Toplam": result}), 200
    else:
        return jsonify({"error": "Lütfen iki geçerli sayı girin."}), 400

# GET endpoint: İki sayının çıkarılması
@app.route('/subtract', methods=['GET'])
def subtract_numbers():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    if a is not None and b is not None:
        result = a - b
        return jsonify({"Fark": result}), 200
    else:
        return jsonify({"error": "Lütfen iki geçerli sayı girin."}), 400

