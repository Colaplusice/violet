from flask import request, abort, Response,render_template,flash

from app.models.user import Article, Tag
from app.utils import convert_and_save
from . import admin


@admin.route('/', methods=['GET', 'POST'])
def index():
    tags = Tag.select()
    if request.method == 'POST':
        title = request.form['title']
        tag = request.form['tags']
        file = request.files['article']
        if convert_and_save(file, file.filename):
            abort(Response(status=400, response='文件格式错误'))
        content = file.read().decode('utf-8')
        Article.create(author=1, title=title, tag=tag, content=content)
        flash(message='创建成功!')
    return render_template('admin/index.html', tags=tags)
