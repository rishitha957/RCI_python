import unittest
import data

class TestData(unittest.TestCase):

	def test_nonhexinput(self):
		print("\nTesting non hexadecimal input case!")
		self.inc = input("Enter any non hexadecimal input to test: ")
		self.obj = data.Data(self.inc)  
		self.list1 = self.obj.generation()
		self.assertEqual(50,len(self.list1))
		print("=====================================================")
		
	def test_generation(self):
		print(
			"\nTesting generation if input is valid,\n"
			"Please try to enter a valid input!"
			)
		self.inc = input("Enter 4 byte hexadecimal input: ")
		self.obj = data.Data(self.inc)  
		self.list1 = self.obj.generation()
		self.assertEqual(50,len(self.list1))
		print("=====================================================")

	def test_leadingzeros(self):
		print(
			"\nTesting format of generated data,\n"
			"Please try to enter less than 4 bytes!"
			)
		self.inc = input("Enter hexadecimal input: ")
		self.obj = data.Data(self.inc)  
		self.list1 = self.obj.generation()
		for i in self.list1:
			li1 = i.split(" ")
			#print(li1)
			for j in range(len(li1)-1):
				self.assertEqual(len(li1[j]),2)
		print("=====================================================")

	def test_spacing(self):
		print(
			"\nTesting input with white spaces,\n"
			"Please Enter data accordingly!"
			)
		self.inc = input("Enter 4 byte hexadecimal input: ")
		self.obj = data.Data(self.inc)  
		self.list1 = self.obj.generation()
		for i in self.list1:
			#print(i)
			self.assertEqual(len(i),90)
		print("=====================================================")

	def test_userinputstart(self):
		self.inc = input("Enter 4 byte hexadecimal input: ")
		self.obj = data.Data(self.inc)
		start = input("Enter 4 byte hexadecimal start input: ")
		end = input("Enter 4 byte hexadecimal end input: ")
		list1 = self.obj.generation()
		list2 = self.obj.extraction(start,end)
		self.assertLessEqual(len(list2),50)

if __name__ == '__main__':

	unittest.main()

