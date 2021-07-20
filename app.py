from flask import Flask, request, Response
from typing import Optional
from utils.data import data
from utils.empty import empty
from utils.jsjson_encoder import JSJSONEncoder
from models.user import User
from models.article import Article
from models.comment import Comment



app = Flask(__name__)

app.json_encoder = JSJSONEncoder


# user
@app.get('/users')
async def users():
    return data(await User.find())

@app.get('/users/<id>')
async def user(id: str) -> Response:
    user = await User.id(id)
    print(user)
    return data(user)

@app.post('/users')
async def create_user() -> Response:
    return data(User(**request.json).save())

@app.patch('/users/<id>')
async def update_user(id: str) -> Response:
    return data((await User.id(id)).set(**request.json).save())

@app.delete('/users/<id>')
async def delete_user(id: str) -> Response:
    return empty((await User.id(id)).delete())

# article
@app.get('/users/<user_id>/articles')
async def articles(user_id: str) -> Response:
    return data(await Article.find(user_id=user_id))

@app.post('/users/articles')
async def create_article() -> Response:
    return data(Article(**request.json).save())

@app.get('/articles/<id>')
async def article(id: str) -> Response:
    return data(await Article.id(id))

@app.patch('/articles/<id>')
async def update_article(id: str) -> Response:
    return data((await Article.id(id)).set(**request.json).save())

@app.delete('/articles/<id>')
async def delete_article(id: str) -> Response:
    return empty((await Article.id(id)).delete())

# comment
@app.get('/articles/<article_id>/comments')
async def commments(article_id: str) -> Response:
    return data(await Comment.find(article_id=article_id))

@app.post('/articles/<article_id>/comments')
async def create_comment(article_id: str) -> Response:
    return data(Comment(article_id=article_id, **request.json).save())

@app.get('/comments/<id>')
async def comment(id: str) -> Response:
    return data(await Comment.id(id))

@app.patch('/comments/<id>')
async def update_comment(id: str) -> Response:
    return data((await Comment.id(id)).set(**request.json).save())

@app.delete('/comments/<id>')
async def delete_comment(id: str) -> Response:
    return empty((await Comment.id(id)).delete())