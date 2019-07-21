import random
import time

class Data:
    def __init__(self,inc):
        self.flag1 = 0  #Used to terminate program if the inc is invalid
        self.flag2 = 0  #Used to terminate program if the start bytes is invalid
        self.flag3 = 0  #Used to terminate program if the end bytes is invalid 
        self.loop_end = 1
        inc1 = '0x'+inc
        inc1 = inc1.replace(" ","")
        while(self.loop_end==1):
            while(len(inc1.replace("0x",""))>4):

                inc = input("Please enter only 4 bytes: ")
                inc1 = '0x'+inc
                inc1 = inc1.replace(" ","")
            self.loop_end = 0
            try:
                self.inc = int(inc1,16)
            except(ValueError):
                self.loop_end = 1
                print(
                    "\nPlease make sure you are entering 4 byte hexdecimal input\n"
                    "Ex: ff04, Each hexdecimal byte is of range[0-9]and[a-f]\n"
                    "Input must be in range 0000 to ffff\n"
                )
                s = input("Want to continue(Y/N):")
                print()
                if(s=='Y' or s=='y'):
                    inc = input("\nEnter 4 byte hexadecimal input: ")
                    inc1 = '0x'+inc
                    inc1 = inc1.replace(" ","")
                elif(s=='N' or s=='n'):
                    self.flag1 = 1 
                    self.loop_end = 0
                else:
                    print("\nPlease enter Y or N!")
                    
        self.header = "55 AA"

    def generation(self,incl_dup=False,force_skip=False):
        self.li = []
        self.inc_save_start = self.inc
        self.const_data = ""
        self.curr = 0
        for j in range(19):
            b = f"{random.randint(0,255):x}"
            b = f"{b:0>2}"
            c = b[:2].upper()+" "
            self.const_data = self.const_data+c
        corrupt_count = random.randint(0,5)
        self.corrupt_index = []
        for i in range(corrupt_count):
            self.corrupt_index.append(random.randint(1,50))
        if(self.flag1==0):
            def incremental_data(p):
            
                if(force_skip):
                    count_skip = random.randint(1,9)
                    self.skip_ind = []
                    for i in range(count_skip):
                        self.skip_ind.append(random.randint(0,50))
            
                for i in range(p):
                    if(force_skip):
                        for j in self.skip_ind:
                            if j==i:
                               temp = self.li.pop()
                    a = f"{self.inc :x}"
                    a = f"{a:0>4}"

                    if(i in self.corrupt_index):
                        str1 = f"{random.randint(0,16) :x}"
                        ind = random.randint(0,19)
                        self.const_data_corrupt = self.const_data[:ind-1]+str1+self.const_data[ind:]
                        self.curr = 1
                    if(self.curr==0):
                        self.li.append(
                            f"{self.header} {a[:2].upper()} {a[2:].upper()} {self.const_data}"+'00 '*7
                        )
                    else:
                        self.li.append(
                            f"{self.header} {a[:2].upper()} {a[2:].upper()} {self.const_data_corrupt}"+'00 '*7
                        )
                        self.curr = 0
                    self.inc = self.inc + 1
                
                self.inc_save_end =self.inc
                
            def random_data(a):
                for i in range(a):
                    str = ""
                    for j in range(21):
                        b = f"{random.randint(0,255):x}"
                        b = f"{b:0>2}"
                        c = b[:2].upper()+" "
                        str = str+c
                    self.li.append(f"{self.header} {str}"+'00 '*7)
            incremental_data(50)
            random_data(50)

            if(incl_dup):
                count_dup = random.randint(1,9)
                for i in range(count_dup):
                    dup_index = random.randint(0,49)
                    self.li.append(self.li[dup_index])
                
            print(len(self.li))
            random.shuffle(self.li)
        return self.li
    def extraction(self,start,end):
        start = start.replace(" ","")
        end = end.replace(" ","")
        self.start = '0x'+start.lower()
        self.end = '0x'+end.lower()
        self.sorted_packets = []
        if(self.flag1==0):
            self.li2 = []
            def read_packets(self):
                self.li2 = self.li
                for i in range(len(self.li2)):
                    self.li2[i] = self.li2[i].split(" ")

            def user_input_start(self):
                
                self.loop_end = 1
                while(self.loop_end==1):
                    self.loop_end = 0
                    try:
                        self.start = int(self.start,16)
                    except(ValueError):
                        self.loop_end = 1
                        print(
                            "Please make sure you are entering 4 byte hexdecimal input\n" 
                            "Ex: ff04, Each hexdecimal byte is of range[0-9]and[a-f]\n"
                            "Input could be in range 0000 to ffff\n"
                        )
                        s = input("Want to continue(Y/N):")
                        if(s=='Y' or s=='y'):
                            self.start = input("\nEnter 4 byte hexadecimal input: ")
                            self.start = self.start.replace(" ","")
                        elif(s=='N' or s=='n'):
                            self.flag2 = 1
                            self.loop_end = 0
                        else:
                            print("\nPlease enter a (Y/N):")
                return self.start
            def user_input_end(self):   
                if(self.flag2!=1):
                    
                    self.loop_end = 1
                    while(self.loop_end==1):
                        self.loop_end = 0
                        try:
                            self.end = int(self.end,16)
                        except(ValueError):
                            self.loop_end = 1
                            print(
                                "\nPlease make sure you are entering 4 byte hexdecimal input\n"
                                "Ex: ff04, Each hexdecimal byte is of range[0-9]and[a-f]\n"
                                "Input could be in range 0000 to ffff\n"
                            )
                            s = input("Want to continue(Y/N):")
                            if(s=='Y' or s=='y'):
                                self.end = input("\nEnter 4 byte end hexadecimal input: ")
                                self.end = self.end.replace(" ","")
                            elif(s=='N' or s=='n'):
                                self.flag2 = 1
                                self.loop_end = 0
                            else:
                                print("\nPlease enter Y or N: ")
                return self.end

            def check_dup(self):
                dict1 = {}
                self.dup_packets = []
                for i in range(len(self.li)):
                    temp = self.li[i][2]+self.li[i][3]
                    temp = int(temp,16)
                    if(temp>self.inc_save_start and temp<self.inc_save_end):
                        try:
                            a = dict1[temp]
                        except(KeyError):
                            dict1[temp] = ""+str(i)
                        else:
                            self.dup_packets.append(self.li[i])
            
            def check_skip(self):
                dict1 = {}
                self.skip_packets = []
                for i in range(self.inc_save_start,self.inc_save_end):
                    dict1[i] = 1
                for i in range(len(self.li)):
                    temp = self.li[i][2]+self.li[i][3]
                    temp = int(temp,16)
                    if(temp>self.inc_save_start and temp<self.inc_save_end):
                        dict1[temp] = 2
                for i in range(self.inc_save_start,self.inc_save_end):
                    a = f"{i :x}"
                    a = f"{a:0>4}"
                    if(dict1[i]==1):
                        self.skip_packets.append(f"{self.header} {a[:2].upper()} {a[2:].upper()} {self.const_data}"+'00 '*7)

            def check_corrupted_data(self):
                
                self.corrupted_packets = []
                for i in range(len(self.li)):
                    temp = self.li[i][2]+self.li[i][3]
                    temp = int(temp,16)
                    if(temp>self.inc_save_start and temp<self.inc_save_end):
                        for i in range()

            def extract_packets_in_range(self):
                d = {}
                if(self.start>self.end):
                    print("Your entered start bytes are greater than end bytes!")
                    self.ch = int(input(
                        "Enter your choice:\n"
                        "1 - Do you want us to swap?\n"
                        "2 - Will you enter new start bytes?\n"
                        "3 - Will you enter new end bytes?\n"
                        "4 - quit?\n"
                    ))
                    if(self.ch==1):
                        print()
                        self.start,self.end = self.end,self.start
                        print("After swapping:")
                    elif(self.ch==2):
                        print("your end bytes are: ",self.end)
                        user_input_start()
                    elif(self.ch==3):
                        print("your start bytes are: ",self.start)
                        user_input_end()   
                    elif(self.ch==4):
                        self.flag3 = 1

                if(self.flag3!=1):
                    print("#debug- start is ",self.start)
                    print("#debug- end is ",self.end)
                    res = list(
                        filter(
                            lambda x:int(x[2]+x[3],16)>self.start 
                            and 
                            int(x[2]+x[3],16)<self.end,self.li2
                            )
                        )
                
                    for i in range(len(res)):
                        a = int(res[i][2]+res[i][3],16)
                        b = " ".join(j for j in res[i])
                        d[a] = b
                    li3 = list(d.keys())
                    list.sort(li3)
                    for i in li3:
                        self.sorted_packets.append(d[i])
               
            read_packets(self)
            self.start = user_input_start(self)
            self.end = user_input_end(self)
            check_dup(self)
            print("dup packets are: ",self.dup_packets)
            with open("dup_packets.txt","w") as f1:
                for i in range(len(self.dup_packets)):
                    f1.write("%s\n"%self.dup_packets[i])
            check_skip(self)
            print("Skipped packets are: ",self.skip_packets)
            with open("skipped_packets.txt","w") as f2:
                for i in self.skip_packets:
                    f2.write("%s\n"%i)
            if(self.flag2!=1):
                extract_packets_in_range(self)
                
        return self.sorted_packets

if __name__ == '__main__':
    x = time.time()
    inc = input("Enter 4 byte hexadecimal input: ")
    d1 = Data(inc)
    data_packets_list = d1.generation(force_skip=True)
    #print("Data packets list is:")
    #print(data_packets_list)
    start = input("Enter 4 byte hexadecimal start input: ")
    end = input("Enter 4 byte hexadecimal end input: ")
    temp = d1.extraction(start,end)
    #print("Extracted data in range is: ")
    #print(temp)
    y = time.time()
    print("Total exec time is: ",y-x)
