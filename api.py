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

    # POST endpoint: İki sayının çarpılması
@app.route('/multiply', methods=['POST'])
def multiply_numbers():
    data = request.get_json()
    try:
        num1 = int(data.get('num1'))
        num2 = int(data.get('num2'))
        result = num1 * num2
        return jsonify({"Çarpım": result}), 200
    except (TypeError, ValueError):
        return jsonify({"error": "Lütfen geçerli sayılar girin."}), 400

# POST endpoint: İki sayının bölünmesi
@app.route('/divide', methods=['POST'])
def divide_numbers():
    data = request.get_json()
    try:
        num1 = int(data.get('num1'))
        num2 = int(data.get('num2'))
        if num2 == 0:
            return jsonify({"error": "Bir sayı sıfıra bölünemez."}), 400
        result = num1 / num2
        return jsonify({"Bölüm": result}), 200
    except (TypeError, ValueError):
        return jsonify({"error": "Lütfen geçerli sayılar girin."}), 400

