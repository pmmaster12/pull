from flask import Flask
from flask import request

app =Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>hello,world!</h1>"
@app.route("/hello_world2")
def hello_world2():
    return "<h1>hello,world!1</h1>"
@app.route("/hello_world3")
def hello_world3():
    return "<h1>hello,world!2</h1>"
@app.route("/test")
def test():
    a=5+6
    return "test completed {}".format(a)
@app.route("/test2/test2")
def test2():
    data=request.args.get('x')
    return "test completed {}".format(data)
if __name__ =="__main__":
    app.run(host="0.0.0.0")
     