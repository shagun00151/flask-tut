from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    user_logged_in = False
    return render_template('basic1.html',user_logged_in = user_logged_in)

# jinja template concept is used to insert or update the variables in the html file. 
# with jinja template we use {{variable}} syntax to insert the variables.
if __name__ == '__main__':
    app.run(debug=True)