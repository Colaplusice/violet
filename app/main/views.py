import os

import markdown2
from flask import current_app, render_template, url_for,flash

from app.main import main
from app.models.user import Article, Tag


@main.route("/")
def index():
    articles = Article.select().order_by(Article.created_at.desc())
    tags = Tag.select()
    flash('qweqewqe')
    return render_template("index.html", articles=articles, tags=tags)

@main.route("/blog/<int:article_id>")
def blog(article_id):
    article = Article.get_by_id(article_id)
    markdown = markdown2.Markdown()
    content = markdown.convert(article.content)
    related_articles = (
        Article.select()
            .where(Article.tag == article.tag)
            .limit(10)
            .order_by(Article.view_num.desc())
    )
    return render_template("article.html", article=article, content=content, related_articles=related_articles)


@main.route("/about")
def about():
    return render_template("about.html")


@main.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == "static":
        filename = values.get("filename", None)
        if filename:
            file_path = os.path.join(current_app.root_path, endpoint, filename)
            values["q"] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)
