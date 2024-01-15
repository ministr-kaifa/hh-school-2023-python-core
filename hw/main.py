from datetime import date
from wine import Wine
from beer import Beer
from market import Market

wine1 = Wine(title='Dom Perignon', production_date=date(2023, 4, 1))
wine2 = Wine(title=None, production_date=date(2023, 3, 1))
beer1 = Beer(title='Bud light', production_date=date(2023, 1, 1))
beer2 = Beer(title='Bud', production_date=None)

market = Market(beers=[beer1, beer2], wines=[wine1, wine2])

print(market.has_drink_with_title('Bud'))
print(*market.get_drinks_sorted_by_title(), sep='\n')
print(*market.get_drinks_by_production_date(from_date=date(2023, 3, 1), to_date=date(2023, 5, 1)), sep='\n')
