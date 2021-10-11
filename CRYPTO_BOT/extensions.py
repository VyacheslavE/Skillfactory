import json
import requests
#from bs4 import BeautifulSoup
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

        # json + API variant
        r = requests.get(f'http://api.exchangeratesapi.io/v1/latest?access_key=f390b600dca7472d0dd52d9bb4115729')
        return round(json.loads(r.content)['rates'][keys[qoute]] * amount, 2)

