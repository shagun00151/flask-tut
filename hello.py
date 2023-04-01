from flask import Flask
app = Flask(__name__)
@app.route('/') #127.0.0.1:5000
def index():
    return "<h1>Hello world i have started flask</h1>"
# we can enter the information in front of the above index IP address
@app.route('/information')  #127.0.0.1:5000/information 
def info():
    return "<h1>I am learning flask for backend</h1>" 

@app.route('/puppy/<name>')
def puppy(name):
    return "<h1>This is a page for {}</h1>".format(name[10])
 # debug = true is used to catch the error inside the code
if __name__ == '__main__':
    app.run(debug=True)
