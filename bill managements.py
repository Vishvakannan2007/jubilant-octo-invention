from tkinter import *
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pandas as pd

root = Tk()
root.geometry("1200x700")
root.title("Bill Management")
root.resizable(False, False)

def Reset():
    entry_dosa.delete(0, END)
    entry_cookies.delete(0, END)
    entry_Tea.delete(0, END)
    entry_cofee.delete(0, END)
    entry_juice.delete(0, END)
    entry_pancakes.delete(0, END)
    entry_eggs.delete(0, END)
    Total_bill.set("")

def Total():
    try: a1 = int(dosa.get())
    except: a1 = 0
    try: a2 = int(cookies.get())
    except: a2 = 0
    try: a3 = int(Tea.get())
    except: a3 = 0
    try: a4 = int(cofee.get())
    except: a4 = 0
    try: a5 = int(juice.get())
    except: a5 = 0
    try: a6 = int(pancakes.get())
    except: a6 = 0
    try: a7 = int(eggs.get())
    except: a7 = 0

    # Define cost per item
    c1=60*a1
    c2=30*a2
    c3=7*a3
    c4=100*a4
    c5=20*a5
    c6=15*a6
    c7=7*a7

    lbl_total=Label(f2,font=('aria',20,'bold'),text="Total",width=16,fg="lightyellow",bg="black")
    lbl_total.place(x=0,y=50)

    entry_total=Entry(f2,font=('aria',20,'bold'),textvariable=Total_bill,bd=6,width=15,bg="lightgreen")
    entry_total.place(x=20,y=100)

    totalcost=c1+c2+c3+c4+c5+c6+c7
    string_bill="Rs. " + str('%.2f' %totalcost)
    Total_bill.set(string_bill)

Label(text="BILL MANAGEMENT",bg="black",fg="white",font=("calibri",33),width="300",height="2").pack()

def Generate_PDF():
    bill_items = [
        ("Dosa", dosa.get(), 60),
        ("Cookies", cookies.get(), 30),
        ("Tea", Tea.get(), 7),
        ("Coffee", cofee.get(), 100),
        ("Juice", juice.get(), 20),
        ("Pancakes", pancakes.get(), 15),
        ("Eggs", eggs.get(), 7)
    ]

    filename = "bill_invoice.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    c.setFont("Helvetica", 12)

    y_position = 750
    c.drawString(50, y_position, "Bill Invoice")
    c.drawString(50, y_position - 20, "---------------------------")
    y_position -= 40
    total_amount = 0

    for item, qty, price in bill_items:
        try:
            qty = int(qty)
            if qty > 0:
                total = qty * price
                total_amount += total
                c.drawString(50, y_position, f"{item}: {qty} x Rs.{price} = Rs.{total}")
                y_position -= 20
        except:
            pass

    c.drawString(50, y_position - 20, "---------------------------")
    c.drawString(50, y_position - 40, f"Total Amount: Rs. {total_amount:.2f}")
    c.save()
    print(f"PDF generated successfully: {filename}")

def Generate_Excel():
    bill_data = {
        "Item": ["Dosa", "Cookies", "Tea", "Coffee", "Juice", "Pancakes", "Eggs"],
        "Quantity": [dosa.get(), cookies.get(), Tea.get(), cofee.get(), juice.get(), pancakes.get(), eggs.get()],
        "Price per Unit": [60, 30, 7, 100, 20, 15, 7],
    }

    df = pd.DataFrame(bill_data)
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors='coerce').fillna(0).astype(int)
    df["Total Price"] = df["Quantity"] * df["Price per Unit"]

    total_amount = df["Total Price"].sum()
    df.loc[len(df)] = ["Total", "", "", total_amount]

    filename = "bill_invoice.xlsx"
    df.to_excel(filename, index=False)
    print(f"Excel file generated successfully: {filename}")



#MENU CARD
f=Frame(root,bg="lightgreen",highlightbackground="black",highlightthickness=1,width=300,height=370)
f.place(x=10,y=130)

Label(f,text="Menu",font=("Gabriola",40,"bold"),fg="black",bg="lightgreen").place(x=80,y=0)

Label(f,font=("Lucida Calligraphy",15,'bold'),text="Dosa......Rs.60/plate",fg="black",bg="lightgreen").place(x=10,y=80)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Cookies......Rs.30/plate",fg="black",bg="lightgreen").place(x=10,y=110)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Tea......Rs.7/cup",fg="black",bg="lightgreen").place(x=10,y=140)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Coffee......Rs.100/cup",fg="black",bg="lightgreen").place(x=10,y=170)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Juice......Rs.20/glass",fg="black",bg="lightgreen").place(x=10,y=200)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Pancakes......Rs.15/pack",fg="black",bg="lightgreen").place(x=10,y=230)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Eggs......Rs.7/egg",fg="black",bg="lightgreen").place(x=10,y=260)

#BILL
f2=Frame(root,bg="lightyellow",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=890,y=118)

Bill=Label(f2,text="Bill",font=('calibri',20),bg="lightyellow")
Bill.place(x=120,y=10)
#ENTRY WORK
f1=Frame(root,bd=5,height=500,width=450,relief=RAISED)
f1.pack()

dosa=StringVar()
cookies=StringVar()
Tea=StringVar()
cofee=StringVar()
juice=StringVar()
pancakes=StringVar()
eggs=StringVar()
Total_bill=StringVar()
 
#Label
lbl_dosa=Label(f1,font=("aria",20,'bold'),text="Dosa",width=12,fg="blue4")
lbl_cookies=Label(f1,font=("aria",20,'bold'),text="Cookies",width=12,fg="blue4")
lbl_Tea=Label(f1,font=("aria",20,'bold'),text="Tea",width=12,fg="blue4")
lbl_cofee=Label(f1,font=("aria",20,'bold'),text="Coffee",width=12,fg="blue4")
lbl_juice=Label(f1,font=("aria",20,'bold'),text="Juice",width=12,fg="blue4")
lbl_pancakes=Label(f1,font=("aria",20,'bold'),text="Pancakes",width=12,fg="blue4")
lbl_eggs=Label(f1,font=("aria",20,'bold'),text="Eggs",width=12,fg="blue4")
lbl_dosa.grid(row=1,column=0)
lbl_cookies.grid(row=2,column=0)
lbl_Tea.grid(row=3,column=0)
lbl_cofee.grid(row=4,column=0)
lbl_juice.grid(row=5,column=0)
lbl_pancakes.grid(row=6,column=0)
lbl_eggs.grid(row=7,column=0)

#Entry
entry_dosa=Entry(f1,font=("aria",20,'bold'),textvariable=dosa,bd=6,width=8,bg="lightpink")
entry_cookies=Entry(f1,font=("aria",20,'bold'),textvariable=cookies,bd=6,width=8,bg="lightpink")
entry_Tea=Entry(f1,font=("aria",20,'bold'),textvariable=Tea,bd=6,width=8,bg="lightpink")
entry_cofee=Entry(f1,font=("aria",20,'bold'),textvariable=cofee,bd=6,width=8,bg="lightpink")
entry_juice=Entry(f1,font=("aria",20,'bold'),textvariable=juice,bd=6,width=8,bg="lightpink")
entry_pancakes=Entry(f1,font=("aria",20,'bold'),textvariable=pancakes,bd=6,width=8,bg="lightpink")
entry_eggs=Entry(f1,font=("aria",20,'bold'),textvariable=eggs,bd=6,width=8,bg="lightpink")



entry_dosa.grid(row=1,column=1)
entry_cookies.grid(row=2,column=1)
entry_Tea.grid(row=3,column=1)
entry_cofee.grid(row=4,column=1)
entry_juice.grid(row=5,column=1)
entry_pancakes.grid(row=6,column=1)
entry_eggs.grid(row=7,column=1)

#buttons
btn_reset=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,'bold'),width=8,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)

btn_total=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,'bold'),width=10,text="Total",command=Total)
btn_total.grid(row=8,column=1)

btn_Generate_PDF=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,'bold'),width=15,text="Generate_PDF",command=Generate_PDF)
btn_Generate_PDF.grid(row=8,column=2)

btn_Generate_Excel=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,'bold'),width=15,text="Generate_Excel",command=Generate_Excel)
btn_Generate_Excel.grid(row=7,column=2)

root.mainloop()

