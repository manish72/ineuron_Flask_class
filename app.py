from flask import Flask,request,jsonify,render_template

# defining app end point
app = Flask(__name__)

## Routes
@app.route("/")
def welcome():
    return render_template("index.html")

# defining each route
@app.route("/aboutus")
def aboutus():
    return "We are ineuron"

@app.route('/demo',methods=['POST'])
def math_operation():
    if request.method == 'POST':
        operation = request.json['operation']
        num1 = request.json['num1']
        num2 = request.json['num2']
        result = 0

        if operation == 'addition':
            result = num1 + num2

        elif operation == 'multiplication':
            result = num1 * num2

        elif operation == 'division':
            result = num1 / num2
        
        else:
            result = num1 - num2

        return render_template("result.html",result=result)
    
@app.route('/math',methods=['POST'])
def operation1():
    if request.method == 'POST':
        operation = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = 0

        if operation == 'addition':
            result = num1 + num2

        elif operation == 'multiplication':
            result = num1 * num2

        elif operation == 'division':
            result = num1 / num2
        
        else:
            result = num1 - num2
        return render_template("result.html",result=result)

if __name__ == "__main__":    
    # host:local IP address where application host is there
    # port: through which port we need to access the application, default : 5000
    app.run(host='0.0.0.0',port=5001)
