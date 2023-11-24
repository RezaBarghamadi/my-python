import qrcode
PRODUCTS=[]
def my_list_story():

    file=open("database.txt","r")

    for line in file:
        res=line.split(",")

        my_dict={
                "code":res[0],
                "product":res[1],
                "price":res[2],
                "some":res[3]
                 }
        PRODUCTS.append(my_dict)
        
    
def show_menu():
    print("This  Menu 👀")
    print("1-Add")
    print("2-Edited")
    print("3-deleted")
    print("4-search")
    print("5-show")
    print("6-Buy")
    print("7-exit")
    print("Make Qr Product ")
def add():
    code=input("Enter Code product: ")
    product=input("Enter product: ")
    price=input("Enter price product: ")
    some=input("Enter count product: ")
    new_product={"code":code,"product":product,"price":price,"some":some}
    PRODUCTS.append(new_product)
   

def edit():
    print("List For Edit 👀")
    show()
    code=int(input("Enter New Code: "))

    for product in PRODUCTS:

         if code==product['code']:
            print("code=",product["code"],", product=",product["product"],", price=",product["price"],", some=",product["some"])
            name=input("enter new product to be edited: ")
            if name!='':
                product['product']=name

            price=input("enter new price to be edited: ")
            if price!='':
                product['price']=int(price)

            some=input("enter new count to be edited: ")
            if some!='':
                product['count']=int(some)
            
            print("The product edited successfully")
            break

    else:
        print("NOt  found!")



def delete():
     print("List For Deleted : ☹")
     show()
     r=int(input("Enter a Code Product For Deleted: "))
     PRODUCTS.pop(r-1)
     print("Your Product Removed ✔")
     show()
    

def search():
    s=input("Enter Your Keyword :")
    for product in PRODUCTS:
        if product["code"]==s or product["product"]==s:
            print(product["code"],"\t" ,product["product"],"\t",product["price"])
            break
    else:
             print("no")

def show():
    print("code\tproduct\tprice")
    for product in PRODUCTS:
        print(product["code"],"\t" ,product["product"],"\t",product["price"])



def  buy():
    while True:
        resived=int(input("Enter Your Product Code :"))
        for product in PRODUCTS:
            if product["code"]==resived or product["product"]==resived:
                print("This Product is avalible 🥰")

            number=input("Enter Number : ")

            if product["some"] < number:
                print("Not Available Some This Product ")
        
            break

def write_database():
    ...

def qr():
    while True:
        input_code = input("Enter a code or name to find : ")
        for p in PRODUCTS:
            if p["code"] == input_code or p["product"] == input_code:
                print(p["code"],"\t\t",p["product"],"\t\t",p["price"],"\t\t")
                product = str(p["code"]) + "\t\t" + str(p["product"]) + "\t\t" +str(p["price"])
                Qrcodeu = qrcode.make(product)
                Qrcodeu.save("Qrcode.png")
                print("Qrcode saved")
                break
        else:
            print("Not found")

print("Welcome to My Story")
print("Loading ....")
my_list_story()
print("Data Loading ...")
while True:
    show_menu()
    choice=int(input("Enter Your Choice : "))

    if choice==1:
        add()
    elif choice==2:
        edit()
    elif choice== 3:
        delete()
    elif choice==4:
        search()
    elif choice==5:
        show()
        break
    elif choice==6:
        buy()
    elif choice==7:
         write_database()
         exit(0)
    elif choice==8:
        qr()   
    else:
        print("Please Enter Num Just This Menu!!!!!!!")  