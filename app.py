from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def input():
    return render_template('input.html')

@app.route('/display', methods=['POST'])
def display():
    name = request.form['name']
    id = request.form['id']
    age = request.form['age']
    address = request.form['address']
    phone = request.form['phone']
    return render_template('display.html', name=name, id=id, age=age, address=address, phone=phone)

if __name__ == '__main__':
    app.run(debug=True)