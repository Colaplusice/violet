from flask import render_template, request

from app.models.user import Tag, Article
from . import admin


@admin.route('/', methods=['GET', 'POST'])
def index():
    tags = Tag.select()
    if request.method == 'POST':
        title = request.form['title']
        tag = request.form['tags']
        file = request.files['article']
        content = file.read().decode('utf-8')
        Article.create(author=1, title=title, tag=tag, content=content)
    return render_template('admin/index.html', tags=tags)
