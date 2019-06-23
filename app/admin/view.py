from flask import Response,render_template

from . import admin


@admin.route('/')
def index():
    return render_template('admin/index.html')
