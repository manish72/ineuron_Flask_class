from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def homepage():
    return "<h1>Welcome to Flask class</h1>"

@app.route("/add",methods=['GET'])
def addition():
    add = 2 + 3
    return str(add)

if __name__ == "__main__":    
    # host:local IP address where application host is there
    # port: through which port we need to access the application, default : 5000
    app.run(host='0.0.0.0',port=5001)