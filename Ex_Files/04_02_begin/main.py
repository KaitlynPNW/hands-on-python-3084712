from flask import Flask

app = Flask(__name__) #flask object __name__

@app.route("/")
def hello():
  return "hello, world!"

app.run(debug=True)