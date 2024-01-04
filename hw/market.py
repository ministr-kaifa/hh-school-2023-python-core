from utils import log_call
from datetime import date

class Market:
    def __init__(self, wines: list = None, beers: list = None) -> None:
        self.drinks = {beer.title: beer for beer in beers} | {wine.title: wine for wine in wines}

    @log_call
    def has_drink_with_title(self, title=None) -> bool:
        """
        Проверяет наличие напитка в магазине за О(1)

        :param title:
        :return: True|False
        """
        return title in self.drinks
    
    @log_call
    def get_drinks_sorted_by_title(self) -> list:
        """
        Метод получения списка напитков (вина и пива) отсортированных по title

        :return: list
        """
        return [drink[1] for drink in sorted(
          [drink for drink in self.drinks.items() if drink[0] is not None])]
    
    @log_call
    def get_drinks_by_production_date(self, from_date: date=None, to_date: date=None) -> list:
        """
        Метод получения списка напитков в указанном диапазоне дат: с from_date по to_date

        :return: list
        """
        return [*filter(
          lambda drink: from_date <= drink.production_date <= to_date,
          [drink for drink in self.drinks.values() if drink.production_date is not None])]
