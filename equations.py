#!/usr/bin/python
import sys
import re
from decimal import *

def getEnglishNumbers(qt):
	number_dict = dict()
	number_dict = {'१':1,'२':2,'३':3,'४':4,'५':5,'६':6,'७':7,'८':8,'९':9,'०':0}
	#qt = '३६१'
	number=0
	for i in range(0, len(qt)):
		if qt[i] in number_dict:
			digit = number_dict[qt[i]]
			#print (digit)
			number = number*10 + digit
		
	return number



input_arguments = sys.argv
file_labels = open("nboutput.txt", "r", encoding="utf8")
file_test = open(input_arguments[1], 'r')
file_output = open("output", "w+", encoding="utf8")

if len(input_arguments) != 2:
	print ("Wrong input")
else:
	for line in file_test.readlines():
		words = line.strip().split(' ')
		line_label= file_labels.readline()
		line_label= line_label.strip().split(' ')
		class_label = line_label[1]
		index_FF = []
		index_QT = []
		num_list = []
		unknown_index = -1
		identifier = words[0]



		if class_label.strip() == "addition":
			for i in range(1, len(words)):
				word_tag = words[i].strip().split('/')
				#print (word_tag) 
				if (word_tag[1] == "FF"):
					#print (i)
					index_FF.append(i)
				elif (word_tag[1] == "QT"):
					index_QT.append(i)
					num_list.append(word_tag[0])
				elif (word_tag[0] == "किती"):
					unknown_index = i
			
			# Type 3 and type 4 problems (addition)
			# There are 6 frogs in the pond. 2 more frogs hop in the pond. How  many frogs are there in the pond?
			# Rahul has 6 cars. Nikita gave him 9 more cars. How many cars does Rahul have altogether?
			if (len(index_FF) >= 3 and len(index_QT) >= 2):
				if index_FF[0] > index_QT[0] and index_FF[1] > index_QT[1] and unknown_index > index_QT[0] and unknown_index > index_QT[1]:
					qt1 = getEnglishNumbers(num_list[0])
					qt2 = getEnglishNumbers(num_list[1])
					unknown = qt1 + qt2
					print (identifier + " " + "x=" + str(qt1) + "+" + str(qt2) + " x=" + str(unknown))
				else:
					print(identifier + " " + "Invalid addition type")
				
			#Type 6 (addition)
			#William has 5 red cars and 9 blue cars. How many cars does he have in total?
			elif (len(index_FF) >= 2 and len(index_QT) >= 2):
				if index_FF[0] > index_QT[0] and index_FF[0] > index_QT[1] and unknown_index > index_QT[0] and unknown_index > index_QT[1]:
					qt1 = getEnglishNumbers(num_list[0])
					qt2 = getEnglishNumbers(num_list[1])
					unknown = qt1 + qt2
					print (identifier + " " + "x=" + str(qt1) + "+" + str(qt2) + " x=" + str(unknown))
			else:
				print(identifier + " " + "Invalid addition type")
						
				
		elif class_label.strip() == "subtraction":
			for i in range(1, len(words)):
				word_tag = words[i].strip().split('/')
				#print (word_tag) 
				if (word_tag[1] == "FF"):
					#print (i)
					index_FF.append(i)
				elif (word_tag[1] == "QT"):
					index_QT.append(i)
					num_list.append(word_tag[0])
				elif (word_tag[0] == "काही"):
					unknown_index = i
				elif (word_tag[0] == "किती" and  unknown_index == -1):
					unknown_index = i
			
						
			if (len(index_FF) >= 3 and len(index_QT) >= 2):
				
				# Type 1 (subtraction)
				# Rekha has few books. Shyam gave her 6 books. Now she has 12 books. How many books did Rekha have earlier?
				if index_FF[0] > unknown_index:
					qt2 = getEnglishNumbers(num_list[0])
					qt3 = getEnglishNumbers(num_list[1])
					unknown = qt3 - qt2
					print (identifier + " " + "x=" + str(qt3) + "-" + str(qt2) + " x=" + str(unknown))
				
				#Type 2 (subtraction)
				#Ali has 9 bags. He sold 3 bags. How many bag does he now have? 
				# Type 7 (subtraction)
				# Radha has 7 cars in all. She has 5 red cars and remaining blue cars. How many blue cars does she have?
				elif index_FF[0] > index_QT[0] and index_FF[1] > index_QT[1] and unknown_index > index_QT[0] and unknown_index > index_QT[1]:
					qt1 = getEnglishNumbers(num_list[0])
					qt2 = getEnglishNumbers(num_list[1])
					unknown = qt1 - qt2
					print (identifier + " " + "x=" + str(qt1) + "-" + str(qt2) + " x=" + str(unknown))

				else:
					print(identifier + " " + "Invalid subtraction1 type")
			
			elif (len(index_FF) >= 2 and len(index_QT) >= 2):
				
				# Type 5 (subtraction)
				# Jordan has 3 cars. How  many more cars he needs to buy to have 12 cars?
				if index_FF[0] > index_QT[0] and unknown_index < index_QT[1] and unknown_index > index_QT[0]:
					qt1 = getEnglishNumbers(num_list[0])
					qt3 = getEnglishNumbers(num_list[1])
					unknown = qt3 - qt1
					print (identifier + " " + "x=" + str(qt3) + "-" + str(qt1) + " x=" + str(unknown))
				else:
					print (identifier + " " + "Invalid subtraction2 Type")

			#Type 8 (subtraction)
			#Lata has 23 pearls. She gave few of them to Asha. Now she has 16 pearls. How many pearls did she give to Asha?
			#Type 9 (subtraction)
			#Sam has 40 radios. He gets few more radios. Now he has 73 radios. How many radios did he get?
			else:
				print (identifier + " " + "Invalid subtraction2 Type")
		else:
			print (identifier + " " + "Invalid Type")



