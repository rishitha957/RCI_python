from tkinter import *
import data
import random
import time
import string

class Data_gui:
    def __init__(self):
        self.inc=""

    def process_gen(self,window,filename1):
        window.destroy()
        self.inc = random.randint(0,pow(16,4)-1)
        self.inc = f"{self.inc :x}"
        self.inc = f"{self.inc :0>4}"
        obj = data.Data(self.inc)
        list1 = obj.generation()

        if(filename1=='' or filename1[0]==" " or filename1[0]=='!' or filename1[0]=='?' or filename1[0]=="[" or filename1[0]==']'):
                msg = "You haven't entered any filename or \nmay be the filename format must be wrong\nso we are saving it in extracted_data.txt"
                self.error_box(msg)
                filename1 = "extracted_data.txt"

        if('.txt' in filename1):
            with open(filename1,'w') as f:
                for packets in list1:
                    f.write("%s\n"%packets)
            msg = "One file is generated with 50 packets of data \nand the filename as "+filename1
            self.filename = filename1
        else:
            with open(filename1+'.txt','w') as f:
                for packets in list1:
                    f.write("%s\n"%packets)
            msg = "One file is generated with 50 packets of data \nand the filename as "+filename1+'.txt'
            self.filename = filename1+'.txt'

        #self.error_box.destroy()

        process_gen = Tk()
        process_gen.title("msg box")
        process_gen.configure(background='grey')

        label_0 = Label(process_gen, text=msg,font="Times 12",bg='white',fg='black')
        label_0.grid(row=0,column=0,padx=10,pady=10)


    def error_box(self,msg):
        self.error_box = Tk()
        self.error_box.title("Error box")
        self.error_box.configure(background='grey')

        label_0 = Label(self.error_box, text=msg,font="Times 12",bg="white",fg="black")
        label_0.grid(row=0,column=0,padx=10,pady=10)

    def process_ext(self,window,start,end,filename2):
        if(self.inc==''):
            self.inc = random.randint(0,pow(16,4)-1)
            self.inc = f"{self.inc :x}"
            self.inc = f"{self.inc :0>4}"
        obj = data.Data(self.inc)
        list1 = obj.generation()

        self.start = start
        self.end = end

        print("#debug-- start, end: ",self.start,self.end)
        try:
            self.start = int(self.start,16)
        except(ValueError):
            self.check_inp(self.start,"Start input")
            print("After calling s:")
        time.sleep(0.5)
        try:
            self.end = int(self.end,16)
        except(ValueError):
            self.check_inp(self.end,"End input")
            print("After calling e:")

        print("#debug2-- start,end",self.start,self.end)
        
        list2 = obj.extraction(self.start,self.end)
        if(filename2=='' or filename2[0]==" " or filename2[0]=='!' or filename2[0]=='?' or filename2[0]=="[" or filename2[0]==']'):
            msg = "You haven't entered any filename or \nmay be the filename format must be wrong\nso we are saving it in sorted_data_in_range.txt"
            self.error_box(msg)
            filename2 = "sorted_data.txt"
        if('.txt' in filename2):
            with open(filename2,'w') as f:
                for packets in list1:
                    f.write("%s\n"%packets)
            msg = "Data in the range of "+start+" & "+end+"\n is extracted into the file "+filename2
        else:
            with open(filename2+'.txt','w') as f:
                for packets in list1:
                    f.write("%s\n"%packets)
            msg = "Data in the range of "+start+" & "+end+"\n is extracted into the file "+filename2+".txt"

        process_ext = Tk()
        process_ext.title("message!")
        process_ext.configure(background='grey')
        label_0 = Label(process_ext,text=msg,font="Times 12",bg="white",fg='black')
        label_0.grid(row=0,column=0,padx=10,pady=10)
        
        window.destroy()

        process_ext.mainloop()

    def check_inp(self,input_data,input_type):
        print("Entered check barrier!")
        #print(input_data)
        if(all(c in string.hexdigits for c in input_data) and input_data!=None):
            print("input_data is : ",input_data)
            if(input_type == "Start input"):
                self.start = input_data
            else:
                self.end = input_data
        else:
            check_inp = Tk()
            check_inp.title(input_type)
            check_inp.configure(background='grey')
            check_inp.geometry('390x273')

            frame = Frame(check_inp,bg="grey",highlightbackground='white',highlightcolor='white',highlightthickness=10,bd=10)
            frame.pack()

            msg1 = "\nPlease make sure you enter a 4 byte hexadecimal number\n"+"i.e the input ranges from [0000-ffff],\n(Each hexadecimal byte is in range 0-9 and a-f) \neg: sample input can be :fec4"
            label_0 = Label(check_inp, text=msg1,font="Times 12",bg='grey',fg='black')
            label_0.place(x=25,y=33) 
            
            label_1 = Label(check_inp, text=input_type+":",font=("bold", 10),bg='grey',fg='black')
            label_1.place(x=80,y=138)

            self.entry_check_inp = Entry(check_inp)
            self.entry_check_inp.place(x=160,y=138)

            Button(check_inp, text='Submit',command=lambda: self.set_inp(check_inp,"",input_type),width=20,bg='brown',fg='white').place(x=100,y=180)

    def set_inp(self,window,inp,input_type):
        inp = self.entry_check_inp.get()
        print("Entry 1 is : ",inp)
        window.destroy()
        if(all(c in string.hexdigits for c in inp) and inp!=None):
            print("input_data is : ",inp)
            if(input_type == "Start input"):
                self.start = inp
            else:
                self.end = inp  
            print("#debug2-- start,end",self.start,self.end)
        
            list2 = obj.extraction(self.start,self.end)
            if(filename2=='' or filename2[0]==" " or filename2[0]=='!' or filename2[0]=='?' or filename2[0]=="[" or filename2[0]==']'):
                msg = "You haven't entered any filename or \nmay be the filename format must be wrong\nso we are saving it in sorted_data_in_range.txt"
                self.error_box(msg)
                filename2 = "sorted_data.txt"
            if('.txt' in filename2):
                with open(filename2,'w') as f:
                    for packets in list1:
                        f.write("%s\n"%packets)
                msg = "Data in the range of "+start+" & "+end+"\n is extracted into the file "+filename2
            else:
                with open(filename2+'.txt','w') as f:
                    for packets in list1:
                        f.write("%s\n"%packets)
                msg = "Data in the range of "+start+" & "+end+"\n is extracted into the file "+filename2+".txt"

            process_ext = Tk()
            process_ext.title("message!")
            process_ext.configure(background='grey')
            label_0 = Label(process_ext,text=msg,font="Times 12",bg="white",fg='black')
            label_0.grid(row=0,column=0,padx=10,pady=10)
            
            window.destroy()

            process_ext.mainloop()
  
        else:
            self.check_inp(inp,input_type)
        

    def generate1(self,window):
        generate1 = Tk()
        generate1.geometry('500x300')
        generate1.title("Generation")
        generate1.configure(background='grey')

        label_0 = Label(generate1, text="Generation of Packets",width=20,font="Times 20 bold",bg='grey',fg='black')
        label_0.place(x=90,y=53)


        label_1 = Label(generate1, text="FileName: ",width=20,font=("bold", 10),bg='grey',fg='black')
        label_1.place(x=100,y=130)

        entry_1 = Entry(generate1)
        entry_1.place(x=240,y=130)

        Button(generate1, text='Submit',command= lambda: self.process_gen(generate1,entry_1.get()),width=20,bg='brown',fg='white').place(x=180,y=180)

        generate1.mainloop()

    def extract1(self,window):
        extract1 = Tk()
        extract1.geometry('500x450')
        extract1.title("Extraction")
        extract1.configure(background='grey')

        label_0 = Label(extract1, text="Extraction of Packets",width=20,font="Times 20 bold",bg='grey',fg='black')
        label_0.place(x=90,y=53)

        label_1 = Label(extract1, text="Start Bytes: ",width=20,font=("bold", 10),bg='grey',fg='black')
        label_1.place(x=100,y=130)

        entry_1 = Entry(extract1)
        entry_1.place(x=240,y=130)

        label_2 = Label(extract1, text="End Bytes: ",width=20,font=("bold",10),bg='grey',fg='black')
        label_2.place(x=100,y=180)

        entry_2 = Entry(extract1)
        entry_2.place(x=240,y=180)

        label_3 = Label(extract1, text="FileName: ",width=20,font=("bold",10),bg='grey',fg='black')
        label_3.place(x=100,y=230)

        entry_3 = Entry(extract1)
        entry_3.place(x=240,y=230)

        Button(extract1, text='Submit',command= lambda: self.process_ext(extract1,entry_1.get(),entry_2.get(),entry_3.get()),width=20,bg='brown',fg='white').place(x=180,y=280)

        window.destroy()
        extract1.mainloop()


    def start(self):
        mainpage = Tk()
        mainpage.geometry("400x200")
        mainpage.title("Packet generation and Extraction.")
        mainpage.configure(background='grey')
        button_props = {
            "bg": "white",
            "fg": "black",
            "height": 1,
            "width": 28,
            "font": "Times 15"
        }
    
        btn1 = Button(mainpage,text='GENERATE',command = lambda: self.generate1(mainpage),**button_props)
        btn1.place(x=50,y=50)

        btn2 = Button(mainpage,text='EXTRACT',command = lambda: self.extract1(mainpage),**button_props)
        btn2.place(x=50,y=100)

        mainpage.mainloop()

d = Data_gui()
d.start()