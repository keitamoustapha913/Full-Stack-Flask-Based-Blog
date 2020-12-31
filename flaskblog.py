from flask import Flask, render_template, url_for


app = Flask(__name__)

posts = [

    {
        'author' : ' Mouhamed KEITA',
        'title' : 'Blog Post 1',
        'content' : 'First Post content',
        'date_posted': 'April 20 , 2020'
    },
    {
        'author' : ' Mouhamed Moustapha',
        'title' : 'Blog Post 2',
        'content' : 'Second Post content',
        'date_posted': 'April 22 , 2020'
    }
    

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/Hello")
def hello_page():
    return "<h1> Hello World Page </h1> <br> <hr> <h5> Hello World </h5>"


@app.route("/about")
def about():
    return render_template('about.html', title = 'About')


if __name__ == '__main__':
    app.run(debug=True)
