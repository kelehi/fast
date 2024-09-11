# from fastapi import FastAPI
#
#
# app = FastAPI()
from fastapi import FastAPI, Query, Body, Cookie, Response, Header
from datetime import *
from templ import Book, Genre, Bookout
from typing import List
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.post('/v')
def crate_book(item: Genre = Body(..., embed=True)):
    return {'item': item}


@app.get("/date")
def root(response: Response):
    now = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")   # получаем текущую дату и время
    response.set_cookie(key="last_visit", value=now)
    return {"message": "куки установлены"}


@app.get("/cookies")
def root(last_visit=Cookie()):
    return {"last visit": last_visit}


@app.get("/user_agent")
def root(user_agent: str = Header()):
    return {"User-Agent": user_agent}

# @router.post("/logout", status_code=204)
# async def logout_user(response: Response):
#     response.delete_cookie("example_access_token")


@app.get('/book')
def q(q1: List[str] = Query('test', description='book')):
    return q1


@app.post('/create_book')
def crate_book(item: Book, b: Genre, v1: int = Body(...)):
    return {'item': item, 'b': b, 'body': v1}


@app.post('/user/', response_model=Bookout, response_model_exclude={'title'})
def table(create: Book):
    return Bookout(**create.dict(), id=3)
# новый роут


@app.get("/admin_login/{login}&{password}")
def read_custom_message(login, password):
    if login == 'login_admin' and password == 'password_admin':
        return {'admin': {"message": login, "password": password}}
    return {"info": "error"}


@app.get("")
def read_custom_message(login, password):
    if login == 'login_admin' and password == 'password_admin':
        return {'admin': {"message": login, "password": password}}
    return {"info": "error"}


fake_db = [{"username": "vasya", "user_info": "любит колбасу"}, {"username": "katya", "user_info": "любит петь"}]


@app.get("/greet/{name}")
def greet_user(name: str):
    return {"message": f"Hello, {name}!"}

# @app.get('/{user_id}') # тут объявили параметр пути
# async def search_user_by_id(user_id: int): # тут указали его тип данных
#     # какая-то логика работы поиска
#     return {"вы просили найти юзера с id": user_id}
# """Fast api"""
#
# """python -m uvicorn main:app --reload"""
#
# from fastapi import FastAPI
# from pydantic import BaseModel
# from fastapi.responses import FileResponse
#
# app = FastAPI()
#
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/index")
# async def root_1():
#     return FileResponse('templates/index.html')
#
#
# @app.get('/{user_id}') # тут объявили параметр пути
# async def search_user_by_id(user_id: int): # тут указали его тип данных
#     # какая-то логика работы поиска
#     return {"вы просили найти юзера с id": user_id}
#
#
# class User(BaseModel):
#     username: str
#     message: str
#
#
# @app.post('/')
# async def root123(user: User):
#     '''тут мы можем с переменной user, которая в себе содержит объект класса User с соответствующими полями (и указанными типами), делать любую логику
#     - например, мы можем сохранить информацию в базу данных
#     - или передать их в другую функцию
#     - или другое'''
#     print(
#         f'Мы получили от юзера {user.username} такое сообщение: {user.message}')  # тут мы просто выведем полученные данные на экран в отформатированном варианте
#     return user  # или можем вернуть обратно полученные данные, как символ того, что данные получили, или другая логика на ваш вкус