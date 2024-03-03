from fastapi import FastAPI, Body
from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str
    category: str

app = FastAPI()

BOOKS=[
    {'title':'Title One', 'author':'Author One', 'category':'science'},
    {'title':'Title One and Half', 'author':'Author One', 'category':'korea'},
    {'title':'Title Two', 'author':'Author Two', 'category':'science'},
    {'title':'Title Three', 'author':'Author Three', 'category':'history'},
    {'title':'Title Four', 'author':'Author Four', 'category':'math'},
    {'title':'Title Five', 'author':'Author Five', 'category':'math'}
    ]
@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get('/booklists')
async def read_all_books():
    return BOOKS

@app.get('/books/mybook')
async def read_all_books():
    return {'mybook':'My Favorite Books'}


@app.get('/books/{book_title}')
async def read_book_title_by_pathparam(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

@app.get('/books/')#/books/?category=math
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return
         
@app.get('/books/{book_author}/')
async def read_books_with_path_and_query(book_author:str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get('/books/{dynamic_param}')
async def read_single_book(dynamic_param):
    return {'BOOK '+dynamic_param: BOOKS[int(dynamic_param)]}

@app.post('/books/create_book')
async def create_book(new_book = Body()):
    BOOKS.append(new_book)

@app.put('/books/update_book')
async def update_book(update_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == update_book.get('title').casefold():
            BOOKS[i] = update_book

@app.delete('/books/delete_book/{book_title}')
async def delete_book(book_title : str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
    
@app.post('/books/search_by_author/')
async def search_by_author(author: str):
    result = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            result.append(book)
    return result

@app.get('/books/search_by_author/{author}')
async def search_by_author(author: str):
    result = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            result.append(book)
    return result 