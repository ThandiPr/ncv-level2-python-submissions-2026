def place_order(item):
        print('order placed: your order is', item )
        
def calculate_total(item):
    base_price= 2.25
    VAT = 0.15
    totalPrice= (base_price +len(item))
    return totalPrice

def get_order():
    print("preparing order")
    return 'collect your order '
myFood = input('What would you like?')
place_order(myFood)

print(get_order())

order_total = calculate_total(myFood)
print('Your order costs: R',round(order_total,2))