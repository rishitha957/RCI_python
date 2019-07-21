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
        self.inc = int(inc1,16)
        self.header = "55 AA"

    def generation(self):
        self.li = []
        
        def incremental_data(p):
            for i in range(p):
                a = f"{self.inc :x}"
                a = f"{a:0>4}"
                str = ""
                for j in range(19):
                    b = f"{random.randint(0,255):x}"
                    b = f"{b:0>2}"
                    c = b[:2].upper()+" "
                    str = str+c
                self.li.append(
                    f"{self.header} {a[:2].upper()} {a[2:].upper()} {str}"+'00 '*7
                )
                self.inc = self.inc + 1
            
        def random_data(a):
            for i in range(a):
                str = ""
                for j in range(21):
                    b = f"{random.randint(0,255):x}"
                    b = f"{b:0>2}"
                    c = b[:2].upper()+" "
                    str = str+c
                self.li.append(f"{self.header} {str}"+'00 '*7)
        incremental_data(20)
        random_data(30)
        random.shuffle(self.li)
        return self.li

    def extraction(self,start,end):

        self.start = start
        self.end = end
        self.sorted_packets = []
        if(self.flag1==0):
            self.li2 = []
            def read_packets(self):
                self.li2 = self.li
                for i in range(len(self.li2)):
                    self.li2[i] = self.li2[i].split(" ")

            def user_input_start(self):
                return self.start
            def user_input_end(self):   
                return self.end

          
            def extract_packets_in_range(self):
                d = {}
                self.flag3 = 0
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
            if(self.flag2!=1):
                extract_packets_in_range(self)
                
        return self.sorted_packets

if __name__ == '__main__':
    x = time.time()
    inc = input("Enter 4 byte hexadecimal input: ")
    d1 = Data(inc)
    data_packets_list = d1.generation()
    print("Data packets list is:")
    print(data_packets_list)
    start = input("Enter 4 byte hexadecimal start input: ")
    end = input("Enter 4 byte hexadecimal end input: ")
    temp = d1.extraction(start,end)
    print("Extracted data in range is: ")
    print(temp)
    y = time.time()
    print("Total exec time is: ",y-x)

