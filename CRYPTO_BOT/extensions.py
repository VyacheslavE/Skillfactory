import requests
from bs4 import BeautifulSoup
from config import keys

class APIException(Exception):
    pass


class MyConverter:
    @staticmethod
    def get_price(qoute: str, base: str, amount: str):
        if qoute == base:
            raise APIException('Клиент года! - но нельзя переводить валюту саму в себя')

        if qoute not in keys or base not in keys:
            raise APIException(f"Можно конвертировать только предложенные валюты.\n{qoute} - {base}")

        try:
            amount = int(amount)
        except ValueError:
            raise APIException(f"Не удалось обработать количество {amount}")

        r = requests.get(
            f'https://minfin.com.ua/ua/currency/converter/?from={keys[qoute]}&to={keys[base]}&val1={amount}&val2=')
        raw_content = BeautifulSoup(r.content, 'lxml')
        div = raw_content.find_all('div', class_="sc-1xh0v1v-0 chYljb")
        return div[1].find('input')['value']