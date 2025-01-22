import os
from flask import Flask, render_template
from flask_flatpages import FlatPages

debug = True
posts_root_dir = 'posts'
DEBUG = debug
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = posts_root_dir

app = Flask(__name__)
app.config.from_object(__name__)
flatpages = FlatPages(app)

@app.route('/')
def home():
    files = os.listdir(posts_root_dir)
    pages = [file[:-3] for file in files if file.endswith('.md') and not file.startswith('.')]
    return render_template('index.html', pages=pages)

@app.route('/post/<name>')
def render_post(name):
    post = flatpages.get_or_404(name)
    return render_template('post.html', post=post)

if __name__ == "__main__":
    app.run(debug=debug)