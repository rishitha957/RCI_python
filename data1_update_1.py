import random
import time
import crcmod.predefined
import os

class Data:
    def __init__(self,inc):
        self.flag1 = 0  
        self.flag2 = 0  
        self.flag3 = 0  
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
        for j in range(17):
            b = f"{random.randint(0,255):x}"
            b = f"{b:0>2}"
            c = b[:2].upper()+" "
            self.const_data = self.const_data+c

        corrupt_count = random.randint(1,5)
        sum_corrupt_count = random.randint(1,5)
        self.corrupt_index = []
        for i in range(corrupt_count):
            self.corrupt_index.append(random.randint(1,50))
        self.sum_corrupt_index = []
        for i in range(sum_corrupt_count):
            self.sum_corrupt_index.append(random.randint(1,50))

        #print("check sum corrupt index is: ",self.sum_corrupt_index)
        if(self.flag1==0):
            def incremental_data(p):
            
                if(force_skip):
                    count_skip = random.randint(1,9)
                    self.skip_ind = []
                    for i in range(count_skip):
                        self.skip_ind.append(random.randint(1,50))
            
                for i in range(p):
                    if(force_skip):
                        for j in self.skip_ind:
                            if j==i:
                               temp = self.li.pop()
                    a = f"{self.inc :x}"
                    a = f"{a:0>4}"

                    if(i in self.corrupt_index):
                        str2 = f"{random.randint(0,16) :x}"
                        ind = random.randint(0,19)
                        self.const_data_corrupt = self.const_data[:ind-1]+str2+self.const_data[ind:]
                        # crc16_func = crcmod.predefined.mkCrcFun('crc-16')
                        # #print(a[:2].upper()+" "+a[2:4].upper()+" "+self.const_data_corrupt)
                        # bytedata = bytearray.fromhex(a[:2].upper()+" "+a[2:4].upper()+" "+self.const_data_corrupt)
                        # str1 = crc16_func(bytedata)
                        
                        b = f"{random.randint(0,255):x}"
                        b = f"{b:0>2}"
                        c = b[:2].upper()+" "
                        b = f"{random.randint(0,255):x}"
                        b = f"{b:0>2}"
                        d = b[:2].upper()+" "
                        self.const_data_corrupt = self.const_data_corrupt+c+d
                        str1 = ""
                        self.curr = 1
                    if(self.curr==0):
                        if i in self.sum_corrupt_index:
                            b = f"{random.randint(0,255):x}"
                            b = f"{b:0>2}"
                            c = b[:2]
                            b = f"{random.randint(0,255):x}"
                            b = f"{b:0>2}"
                            d = b[:2]
                            str1 = c+d
                        else:
                            crc16_func = crcmod.predefined.mkCrcFun('crc-16')
                            bytedata = bytearray.fromhex(a[:2].upper()+" "+a[2:4].upper()+" "+self.const_data)
                            str1 = crc16_func(bytedata)
                            str1 = f"{str1 :x}"
                            str1 = f"{str1 :0>4}"

                        self.const_data1 = self.const_data+str1[:2].upper()+" "+str1[2:4].upper()+" "
                        str1 = ""
                        
                        self.li.append(
                            f"{self.header} {a[:2].upper()} {a[2:].upper()} {self.const_data1}"+'00 '*7
                        )
                        self.const_data1 = ""
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
            with open("before_shuffling.txt","w") as f:
                for i in self.li:
                    f.write("%s\n"%i)    
            #print(len(self.li))
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
                    if(temp>self.start and temp<self.end):
                        try:
                            a = dict1[temp]
                        except(KeyError):
                            dict1[temp] = ""+str(i)
                        else:
                            self.dup_packets.append(self.li[i])
            
            def check_skip(self):
                dict1 = {}
                self.skip_packets = []
                for i in range(self.start,self.end):
                    dict1[i] = 1
                for i in range(len(self.li)):
                    temp = self.li[i][2]+self.li[i][3]
                    temp = int(temp,16)
                    if(temp>=self.start and temp<self.end):
                        dict1[temp] = 2
                for i in range(self.start,self.end):
                    a = f"{i :x}"
                    a = f"{a:0>4}"
                    if(dict1[i]==1):
                        self.skip_packets.append(f"{self.header} {a[:2].upper()} {a[2:].upper()} {self.const_data}"+'00 '*7)

            def check_corrupted_data(self):
                self.str1 = ""
                self.corrupted_packets = []
                for i in range(len(self.li)):
                    temp = self.li[i][2]+self.li[i][3]
                    temp = int(temp,16)
                    if(temp>=self.start and temp<self.end):
                        for j in range(4,21):
                            self.str1 += self.li[i][j]+" "
                        if(self.const_data!=self.str1):
                            self.str2 = ""
                            for j in range(len(self.li[i])):
                                self.str2 += self.li[i][j]+" "
                            self.corrupted_packets.append(self.str2)
                            self.str2 = ""
                    self.str1 = ""

            def check_sum(self):
                flag = 0
                self.sum_corrupted = []
                for i in range(len(self.li)):
                    temp = self.li[i][2]+self.li[i][3]
                    temp = int(temp,16)
                    if(temp>=self.start and temp<self.end):
                        for j in range(2,21):
                            self.str1 += self.li[i][j]+" "
                        crc16_func = crcmod.predefined.mkCrcFun('crc-16')
                        try:
                            bytedata = bytearray.fromhex(self.str1)
                        except(ValueError):
                            if(len(self.corrupted_packets) > 0):
                                # self.str2 = ""
                                # for j in range(len(self.li[i])):
                                #     self.str2 += self.li[i][j]+" "
                                # print("in def: ",self.str2)
                                # self.sum_corrupted.append(self.str2)
                                # self.str2 = ""
                                flag = 1

                        if flag==0:
                            str1 = crc16_func(bytedata)
                            str1 = f"{str1 :x}"
                            str1 = f"{str1 :0>4}"
                            
                            self.str1 = ""
                            
                            if(str1 != self.li[i][21].lower()+self.li[i][22].lower()):
                                self.str2 = ""
                                for j in range(len(self.li[i])):
                                    self.str2 += self.li[i][j]+" "
                                if self.str2 not in self.corrupted_packets:
                                    self.sum_corrupted.append(self.str2)
                                self.str2 = ""
                        flag = 0

            def count_valid_packets(self):
                self.total_ext_packets = self.end-self.start-1
                self.valid_count = self.total_ext_packets - len(self.dup_packets)

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
                    #print("#debug- start is ",self.start)
                    #print("#debug- end is ",self.end)
                    x = time.time()
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
                    y = time.time()
                    self.exec_time = y-x
            read_packets(self)
            self.start = user_input_start(self)
            self.end = user_input_end(self)
            check_corrupted_data(self)
            with open("corrupted_packets.txt","w") as f0:
                for i in range(len(self.corrupted_packets)):
                    f0.write("%s\n"%self.corrupted_packets[i])

            check_sum(self)
            #print(self.sum_corrupted)
            with open("invalid_checksum.txt","w") as f3:
                for i in range(len(self.sum_corrupted)):
                    f3.write("%s\n"%self.sum_corrupted[i])

            check_dup(self)
            with open("dup_packets.txt","w") as f1:
                for i in range(len(self.dup_packets)):
                    for j in self.dup_packets[i]:
                        f1.write("%s "%j)
                    f1.write("\n")

            check_skip(self)
            with open("skipped_packets.txt","w") as f2:
                for i in self.skip_packets:
                    f2.write("%s\n"%i)
                    
            count_valid_packets(self)
            self.exec_time = 0
            if(self.flag2!=1):
                extract_packets_in_range(self)
                
        return self.sorted_packets,len(self.corrupted_packets),len(self.dup_packets),len(self.skip_packets),self.exec_time

if __name__ == '__main__':
    inc = input("Enter 4 byte hexadecimal input: ")
    d1 = Data(inc)
    data_packets_list = d1.generation(force_skip=True,incl_dup=True)
    with open("generated_data.txt","w") as f:
        for i in data_packets_list:
            f.write("%s\n"%i)
    start = input("Enter 4 byte hexadecimal start input: ")
    end = input("Enter 4 byte hexadecimal end input: ")
    x = time.time()
    temp,corrupted_packets,dup_packets,skip_packets,exec_time = d1.extraction(start,end)
    y = time.time()
    print("No. of corrupted packets are: ",corrupted_packets)
    print("No. of duplicate packets are: ",(dup_packets))
    print("No. of Skipped packets are: ",(skip_packets))
    print("No. of extracted packets are : ",len(temp))
    print("No. of valid packets are: ",len(temp)-dup_packets)
    print(f"Percentage of valid packets is: {(len(temp)-dup_packets)*100/len(temp)}%")
    os.chdir("C:/Users/rishi/Desktop/rishitha/r")
    print("\nThe below are the few useful file paths:")
    print(os.path.abspath("generated_data.txt"))
    print(os.path.abspath("extracted_data.txt"))
    print(os.path.abspath("dup_packets.txt"))
    print(os.path.abspath("skip_packets.txt"))
    print(os.path.abspath("corrupted_packets.txt"))
    print(os.path.abspath("invalid_checksum.txt"))
    with open("extracted_data.txt","w") as f1:
        for i in temp:
            f1.write("%s\n"%i)
    
    print("Total exec time is: ",exec_time)
