import os

import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError


def chek_for_redirect(response):
    if response.history:
        return HTTPError('был редирект ')

def dowloand_books(book_id, save_dir='books'):
    url = f'https://tululu.org/txt.php?id={book_id}'
    response = requests.get(url)

    try:
        chek_for_redirect(response)
        if response.status_code == 200:
            os.makedirs(save_dir, exist_ok=True)
            file_name = f'book {book_id}.txt'
            file_path = os.path.join(save_dir, file_name)

            with open(file_path, 'wb') as file:
                file.write(response.content)
    except HTTPError as e:
        print(f'книга отсутсвует {e}')

start_id =4020
end_id =4030


for book in range(start_id , end_id +1):
    dowloand_books(book)