from datetime import date

class Beer:
    def __init__(self, title=None, production_date: date=None) -> None:
        self.title = title
        self.production_date = production_date

    def __repr__(self) -> str:
        return f'{{title: {self.title}, production_date: {self.production_date}}}'
