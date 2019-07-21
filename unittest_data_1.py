import unittest
import data1_update_1 as data

class TestData(unittest.TestCase):

	def test_nonhexinput(self):
		print("\nTesting non hexadecimal input case!")
		self.inc = "hiya"
		self.obj = data.Data(self.inc)  
		self.list1 = self.obj.generation()
		self.assertEqual(100,len(self.list1))
		print("=====================================================")
		
	def test_generation(self):
		print(
			"\nTesting generation if input is valid,\n"
			"with incremental data input as 'c304'!"
			)
		self.inc = "c304"
		self.obj = data.Data(self.inc)  
		self.list1 = self.obj.generation()
		self.assertEqual(100,len(self.list1))
		print("=====================================================")

	def test_leadingzeros(self):
		print(
			"\nTesting format of generated data,\n"
			"With incremental data input as '012'!"
			)
		self.inc = '012'
		self.obj = data.Data(self.inc)  
		self.list1 = self.obj.generation()
		self.assertEqual(100,len(self.list1))
		print("=====================================================")

	def test_spacing(self):
		print(
			"\nTesting input with white spaces,\n"
			"with incremental data input as 'c 3 0 4 '!"
			)
		self.inc = 'c 3 0 4'
		self.obj = data.Data(self.inc)  
		self.list1 = self.obj.generation()
		# for i in self.list1:
		# 	#print(i)
		# 	self.assertEqual(len(i),90)
		self.assertEqual(100,len(self.list1))
		print("=====================================================")

	def test_extraction(self):
		print(
			"\nTesting extraction if both start and end bytes are valid"
			"\nwith incremental data input as 'c304' and"
			"\nstart bytes input as 'c310' and end bytes input as 'c317'!"
			)
		self.inc = 'c304'
		self.obj = data.Data(self.inc)
		start = 'c310'
		end = 'c317'
		list1 = self.obj.generation()
		temp,corrupted_packets,dup_packets,skip_packets,exec_time = self.obj.extraction(start,end)
		self.assertLessEqual(len(temp),50)
		print("=====================================================")
	
	def test_userinpstart(self):
		print(
			"\nTesting extraction if start bytes are not valid"
			"\nWith incremental data input as 'c304' and"
			"\nstart bytes input as 'hello' and end bytes input as 'c317'!\n"
			)
		self.inc = 'c304'
		self.obj = data.Data(self.inc)
		start = 'hello'
		end = 'c317'
		list1 = self.obj.generation()
		temp,corrupted_packets,dup_packets,skip_packets,exec_time = self.obj.extraction(start,end)
		self.assertLessEqual(len(temp),50)
		print("=====================================================")

	def test_userinpend(self):
		print(
			"\nTesting extraction if end bytes are not valid"
			"\nWith incremental data input as 'c304' and"
			"\nstart bytes input as 'c310' and end bytes input as 'hello'!"
			)
		self.inc = 'c304'
		self.obj = data.Data(self.inc)
		start = 'c310'
		end = 'hello'
		list1 = self.obj.generation()
		temp,corrupted_packets,dup_packets,skip_packets,exec_time = self.obj.extraction(start,end)
		self.assertLessEqual(len(temp),50)
		print("=====================================================")

if __name__ == '__main__':

	unittest.main()

