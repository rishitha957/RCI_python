from tkinter import *
import data
import random

class Data_gui:
    def __init__(self):
        self.inc=""

    def process_gen(self,window,filename1):
        self.inc = random.randint(0,pow(16,4)-1)
        self.inc = f"{self.inc :x}"
        self.inc = f"{self.inc :0>4}"
        obj = data.Data(self.inc)
        list1 = obj.generation()
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
        process_gen = Tk()
        process_gen.title("msg box")
        process_gen.configure(background='grey')
        label_0 = Label(process_gen, text=msg,font="Times 12",bg='white',fg='black')
        label_0.grid(row=0,column=0,padx=10,pady=10)
        process_gen.mainloop()

    def process_ext(self,window,start,end,filename2):
        if(self.inc!=''):
            obj = data.Data(self.inc)
            list1 = obj.generation()
            list2 = obj.extraction(start,end)
            if('.txt' in filename2):
                with open(filename2,'w') as f:
                    for packets in list1:
                        f.write("%s\n"%packets)
                msg = "Data from file "+self.filename+"\n in the range of "+start+" & "+end+"\n is extracted into the file "+filename2
            else:
                with open(filename2+'.txt','w') as f:
                    for packets in list1:
                        f.write("%s\n"%packets)
                msg = "Data from file "+self.filename+"\n in the range of "+start+" & "+end+"\n are extracted into the file "+filename2+".txt"
        process_ext = Tk()
        process_ext.title("message!")
        process_ext.configure(background='grey')
        label_0 = Label(process_ext,text=msg,font="Times 12",bg="white",fg='black')
        label_0.grid(row=0,column=0,padx=10,pady=10)
        process_ext.mainloop()

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
        extract1.geometry('500x500')
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

        extract1.mainloop()


    def start(self):
        mainpage = Tk()
        mainpage.geometry("350x200")
        mainpage.title("Packet generation and Extraction.")
        mainpage.configure(background='grey')
        button_props = {
            "bg": "white",
            "fg": "black",
            "height": 1,
            "width": 28,
            "font": "200"
        }
    
        btn1 = Button(mainpage,text='Generate',command = lambda: self.generate1(mainpage),**button_props)
        btn1.place(x=50,y=50)

        print("inc is(1): ",self.inc)

        btn2 = Button(mainpage,text='Extract',command = lambda: self.extract1(mainpage),**button_props)
        btn2.place(x=50,y=100)

        mainpage.mainloop()

d = Data_gui()
d.start()