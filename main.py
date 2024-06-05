from flask import Flask, render_template
import requests

app = Flask(__name__)
blog_url="https://api.npoint.io/c790b4d5cab58020d391"
response=requests.get(blog_url)
all_data=response.json()

@app.route('/')
def home():
    return render_template("index.html",blog=all_data)


@app.route("/blog/<int:id>")
def get_blog(id):
    req_blog=[blog for blog in all_data if blog["id"]==id]
    return render_template("post.html",blog=req_blog[0])

if __name__ == "__main__":
    app.run(debug=True)
