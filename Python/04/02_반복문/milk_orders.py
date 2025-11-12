milk_orders = {'101': {'milk':1, 'yogurt': 5},
               '102': {'milk':2},
               '103': {'milk': 1, 'yogurt': 10},
               '104': {'yogurt': 15}}

for house, drink in milk_orders.items():
    milk = drink.get('milk', 0)
    print(f"{house}호: milk: {milk}")