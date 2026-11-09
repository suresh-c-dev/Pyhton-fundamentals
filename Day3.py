stock = {"rice": 20, "sugar": 10, "oil": 5}

print(stock["rice"])
print(stock.get("salt", 0))

stock["salt"] = 8
stock["oil"] = stock["oil"] + 10
removed = stock.pop("sugar")

print(stock)
print(removed)
print(len(stock))

######################################################################################################

orders = ["dosa", "idli", "dosa", "vada", "dosa", "idli", "pizza", "vada", "dosa"]

menu = {
    "dosa": {"price": 30, "stock": 10},
    "idli": {"price": 20, "stock": 3},
    "vada": {"price": 15, "stock": 2},
}
menu.update({"puri":{"price":25,"stock":8}})

count={}
total=0
highest_count=0
top_item=""
for item in orders:
    count[item]=count.get(item,0)+1
for item,qty in count.items():
    if item in menu:
        money=qty*menu[item]["price"]
        total+=money
        print(item,qty,money)
    else:
        print(item,"not available")
print("Total amount earned:",total)
for x,y in count.items():
    if y > highest_count:
        highest_count=y
        top_item=x
print(top_item)

for item,qty in count.items():
    if item in menu:
        qty_left=menu[item]["stock"]-qty
        menu[item]["stock"]=qty_left
    else:
        print(item,"not available")
print(menu)
#################################################################################################
requests = ["pen", "pen", "book", "pen", "ink", "book", "pen", "ruler"]

shop = {
    "pen": {"price": 5, "stock": 3},
    "book": {"price": 40, "stock": 4},
    "ink": {"price": 20, "stock": 1},
}
count={}
for item in requests:
    count[item]=count.get(item,0)+1

for item,qty in count.items():
    if item in shop:
        
        if qty<=shop[item]["stock"]:
            shop[item]["stock"]=shop[item]["stock"]-qty
            print(item,"served",qty)
        
        else:
            print(item,"only",shop[item]["stock"],"left,cannot serve",item)   
    else:
        print(item,"not available")
print(shop)
###################################################







breakfast = ["Ravi", "Anu", "Ravi", "Kiran", "Manu", "Anu"]
dinner = ["Anu", "Suma", "Kiran", "Suma", "Divya"]
breakfast_set=set(breakfast)
dinner_set=set(dinner)
breakfast_set.add("Raju")
breakfast_set.discard("Manu")
print("Breakfast ate by",len(breakfast_set),"Students")
print("Students who ate both Breakfast and dinner: ",breakfast_set.intersection(dinner_set))
print("Students who ate any meal: ",breakfast_set.union(dinner_set))
print("Students who ate breakfast but not Dinner: ",breakfast_set.difference(dinner_set))
print("Students who ate Dinner but not Brakfast: ",dinner_set.difference(breakfast_set))
################################################





gym = ("Fit Club", 2026)
signups = ["Ravi", "Anu", "Ravi", "Kiran", "Anu", "Ravi", "Manu"]
paid = {"Anu", "Manu", "Suma"}
fees = {"Ravi": 500, "Anu": 300, "Kiran": 300, "Manu": 400,"Raju": 200}

total_fees=0
print(gym[0])
signed=set(signups)
print(len(signed))
count={}

times_signed=0
total=0

for person in signups:
    count[person]=count.get(person,0)+1
for x,y in count.items():
    if y>times_signed:
        human=x
        times_signed=y

owe=signed.difference(paid)
for name in owe:
    total+=fees[name]
print("Fees Pending: ",total)

print("signed up persons: ",count)
print("signed but not paid:",signed.difference(paid))
print("paid but not signed: ",paid.difference(signed))
print(human,"signed",times_signed,"times")
   #################################################




clubs = {
    "Coding": {"Ravi", "Anu", "Kiran"},
    "Music": {"Anu", "Suma", "Manu"},
    "Sports": {"Kiran", "Manu", "Raju"},
}
most_count=0
most_peoples=[]
all_members=set()
count={}
clubs["Music"].add("Divya")
clubs["Sports"].discard("Raju")
for club,members in clubs.items():
    print(club,"Club","have:",len(members),"students")
    all_members=all_members.union(members)
    
    for s in members:
        count[s]=count.get(s,0)+1
both=clubs["Coding"].intersection(clubs["Music"])
for students,clubs_joined in count.items():
    if clubs_joined>most_count:
        most_count=clubs_joined
for students,clubs_joined in count.items():
    if clubs_joined==most_count:
        most_peoples.append(students)    


print("Students in all club: ",all_members)
print(most_peoples,most_count)
print("Students who learn both coding and music:",both)
print(count)