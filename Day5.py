#                       -----Program 1 Tea Stall -----
print("\n-----Program 1:-----\n")
shop = "Raju Tea Stall"
orders_done = 0
menu = {"tea": 15, "coffee": 20, "samosa": 12}

def item_cost(name, qty=1):
    if name in menu:
        return menu[name] * qty
    return 0

def order_total(order, delivery=0):
    total = 0
    for name, qty in order.items():
        total = total + item_cost(name, qty)
    return total + delivery

def place_order(order, delivery=0, coupon=0):
    global orders_done
    bill = order_total(order, delivery) - coupon
    if bill < 0:
        bill = 0
    orders_done = orders_done + 1
    return bill

def show(customer, amount):
    print(shop, "-", customer, "pays", amount)

o1 = {"tea": 2, "samosa": 3}
o2 = {"coffee": 1, "pizza": 2}

b1 = place_order(o1)
b2 = place_order(o2, coupon=50, delivery=10)
b3 = place_order(delivery=20, order={"tea": 4})

show("Ravi", b1)
show("Anu", b2)
show("Kiran", b3)
print(orders_done)
print(item_cost("coffee"))


#                       -----Program 2 Shop Discount-----

print("\n-----Program 2:-----\n")
def discount_list(shop,discount=0.90):
    disc_itm={}
    for item,price in shop.items():
        if price>=100:
            disc_itm[item]=price*discount
    return disc_itm
def discounted_bill(discounted):
    dis_bill=0
    for item,price in discounted.items():
        dis_bill=dis_bill+price
    return(dis_bill)
def normal_bill(shop):
    normal_price=0
    for item,price in shop.items():
        if price<100:
            normal_price=normal_price+price
    return normal_price
def boss(shop):
    discounted=discount_list(shop)
    print("Discounted itmes: " ,list(discounted.keys()))
    total_bill=discounted_bill(discounted)+normal_bill(shop)
    print("Bill with discount: ",total_bill,"\n")
  
boss({"pen": 10, "book": 150, "bag": 500, "pencil": 5})