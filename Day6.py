import os
folder="Shop"
file="stock.txt"
file2="stock_backup.txt"


price_total=0
expensive_items=0
backup_path = os.path.join(folder, file2)


if not os.path.exists(folder):
    os.mkdir(folder)
stock_path=os.path.join(folder,file)
backup_path=os.path.join(folder,file2)


with open(stock_path,"w",encoding="utf-8")as f:
    f.write("Pen,10\nBook,50\nBag,400\nಟೀ,15")
with open(stock_path,"a",encoding="utf-8") as f:
    f.write("\nBottle,60")
try:
    with open(stock_path,"r",encoding="utf-8")as f:
        print(" Items: ")
        for line in f:
           
            data=line.strip().split(",")
            
            print(f"{data[0]}:{data[1]}")
            price=int(data[1])
            price_total=price_total+price
            if price > 20:
                expensive_items=expensive_items+1
        print("Pointer is at: ",f.tell())
        f.seek(0)
        print("First line: ",f.readline().strip())

except FileNotFoundError:
    print("File not found")
print("Total: ",price_total)
print("Expensive items count: ",expensive_items)
if os.path.exists(backup_path):
    os.remove(backup_path)
os.rename(stock_path,backup_path)

print(os.path.exists(stock_path))
print(os.path.exists(backup_path))
print("Directory: ",os.listdir(folder))