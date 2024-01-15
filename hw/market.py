from utils import log_call
from datetime import date

class Market:
    def __init__(self, wines: list = None, beers: list = None) -> None:
        self.beers = beers 
        self.wines = wines

    def get_all_drinks(self):
        return ({beer.title: beer for beer in self.beers} if self.beers is not None else {}) | (
          {wine.title: wine for wine in self.wines} if self.wines is not None else {})

    @log_call
    def has_drink_with_title(self, title=None) -> bool:
        """
        Проверяет наличие напитка в магазине за О(1)

        :param title:
        :return: True|False
        """
        return title in self.beers or title in self.wines
    
    @log_call
    def get_drinks_sorted_by_title(self) -> list:
        """
        Метод получения списка напитков (вина и пива) отсортированных по title

        :return: list
        """
        return [drink[1] for drink in sorted(
          [drink for drink in self.get_all_drinks().items() if drink[0] is not None])]
    
    @log_call
    def get_drinks_by_production_date(self, from_date: date=None, to_date: date=None) -> list:
        """
        Метод получения списка напитков в указанном диапазоне дат: с from_date по to_date

        :return: list
        """
        return [*filter(
            lambda drink: (from_date is None or from_date <= drink.production_date) and
                      (to_date is None or drink.production_date <= to_date),
            [drink for drink in self.get_all_drinks().values() if drink.production_date is not None]
          )]
