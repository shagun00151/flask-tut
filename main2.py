from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    some_variable = "jose"
    return render_template('basic.html',my_variable = some_variable)

# jinja template concept is used to insert or update the variables in the html file. 
# with jinja template we use {{variable}} syntax to insert the variables.
if __name__ == '__main__':
    app.run(debug=True)