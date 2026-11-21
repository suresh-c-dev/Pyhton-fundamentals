
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
    print("Bill with discount: ",total_bill)
  
boss({"pen": 10, "book": 150, "bag": 500, "pencil": 5})