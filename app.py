from flask import Flask, render_template, request, jsonify, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bill')
def bill_splitter():
    return render_template('bill.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    total_amount = float(data['totalAmount'])
    members = int(data['members'])
    tip_percentage = int(data['tip'])

    if members <= 0:
        return jsonify({'error': 'Number of members must be greater than zero.'})

    # Calculate the bill with tip
    total_tip = (total_amount * tip_percentage) / 100
    total_bill = total_amount + total_tip
    per_person = round(total_bill / members, 2)

    return jsonify({'perPerson': per_person})

if __name__ == '__main__':
    app.run(debug=True)
