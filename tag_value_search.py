#!/usr/bin/python
# Best of The Best 6th Digital Forensic
# @Author L3ad0xff

from PIL import Image
import piexif
import sys
import os
import os.path


f_list = list()
exif_list = list()
tag_value_temp = list()
exif_value_list = list()
split_list = list()

collect_file_tag = {}
div_tag = {}
div_tag_temp = {}
div_tag_temp_Exif = {}
div_tag_temp_GPS = {}
div_tag_temp_Interop = {}
div_tag_temp_1st = {}

try :
	name1 = sys.argv[1]
	name2 = sys.argv[2]
except IndexError as e :
	pass


if len(sys.argv) != 3 :
	print ("Usage : value_group [idf key value] [tag name]")
	print ("idf key value : 0th, Exif, GPS, Interop, 1st")

else : 
	path = os.getcwd()
	for files in os.listdir(path) :
		if (files.split('.')[-1] =='jpg') | (files.split('.')[-1] == 'JPG') | (files.split('.')[-1] == 'jpeg') | (files.split('.')[-1] == 'JPEG') :
			f_list.append(files)

	for filename in f_list :
		exif_dict = piexif.load(filename)
		collect_file_tag[filename] = exif_dict

	#print (exif_dict.keys())

	for ifd in ("0th", "Exif", "GPS", "Interop", "1st") :
		for tag in piexif.TAGS[ifd] :
			for filename in f_list :
				for file_tag in collect_file_tag[filename][ifd] :
					if tag == file_tag :
						exif_list.append(ifd + " : "+ piexif.TAGS[ifd][file_tag]["name"] + " : " + str(collect_file_tag[filename][ifd][file_tag]) + " : " + filename)
						break

	for lenth in range (0, (len(exif_list))) :
		split_list.append(exif_list[lenth].split(" : "))

	#print (Exif_list)

	_0th_list = list()
	Exif_list = list()
	GPS_list = list()
	Interop_list = list()
	_1st_list = list()

	_0th_file_split = list()
	Exif_file_split = list()
	GPS__file_split = list()
	Interop_file_split = list()
	_1st_file_split = list()

	_0th_tag_list = list()
	Exif_tag_list = list()
	GPS_tag_list = list()
	Interop_tag_list = list()
	_1st_tag_list = list()

	_0th_value_list = list()
	Exif_value_list = list()
	GPS_value_list = list()
	Interop_value_list = list()
	_1st_value_list = list()
	final_tag_value = {}

	for lenth in range (0, len(split_list)) :
		if  "0th"== split_list[lenth][0] :
			_0th_list.append(split_list[lenth][1:4])
			_0th_tag_list.append(split_list[lenth][1])
			_0th_value_list.append(split_list[lenth][2])
			_0th_file_split.append(split_list[lenth][3])
		elif  "Exif"== split_list[lenth][0] :
			Exif_list.append(split_list[lenth][1:4])
			Exif_tag_list.append(split_list[lenth][1])
			Exif_value_list.append(split_list[lenth][2])
			Exif_file_split.append(split_list[lenth][3])
		elif  "GPS"== split_list[lenth][0] :
			GPS_list.append(split_list[lenth][1:4])
			GPS_tag_list.append(split_list[lenth][1])
			GPS_value_list.append(split_list[lenth][2])
			GPS__file_split.append(split_list[lenth][3])
		elif  "Interop"== split_list[lenth][0] :
			Interop_list.append(split_list[lenth][1:4])
			Interop_tag_list.append(split_list[lenth][1])
			Interop_value_list.append(split_list[lenth][2])
			Interop_file_split.append(split_list[lenth][3])
		elif "1st" == split_list[lenth][0] :
			_1st_list.append(split_list[lenth][1:4])
			_1st_tag_list.append(split_list[lenth][1])
			_1st_value_list.append(split_list[lenth][2])
			_1st_file_split.append(split_list[lenth][3])
		else :
			print ("!")

	_0th_tag_list = list(set(_0th_tag_list))
	Exif_tag_list = list(set(Exif_tag_list))
	GPS_tag_list = list(set(GPS_tag_list))
	Interop_tag_list = list(set(Interop_tag_list))
	_1st_tag_list = list(set(_1st_tag_list))

	_0th_value_list = list(set(_0th_value_list))
	Exif_value_list = list(set(Exif_value_list))
	GPS_value_list = list(set(GPS_value_list))
	Interop_value_list = list(set(Interop_value_list))
	_1st_value_list = list(set(_1st_value_list))

	#print (_0th_value_list)
	#_0th_value_list.sort()
	"""for q in range(0, len(_1st_list)) :
		if _1st_list[q][0] == "Orientation" :
			print (_1st_list[q])"""

	#split_ exif - [0] : ifd / [1] : tag_name / [2] : value / [3] : filename
	dic_tag_value = {}
	compare_value = list()
	fin_val = list()
	fin_val_1 = list()
	fin_val_2 = list()
	fin_val_3 = list()
	fin_val_4 = list()
	fin_val_5 = list()
	fin_val_6 = list()
	fin_val_7 = list()
	fin_val_8 = list()
	fin_val_9 = list()
	fin_val_10 = list()
	fin_val_11 = list()
	fin_val_12 = list()
	test = list()
	#print (_0th_list)

	if name1 == "0th" :
		for order in range(0, len(_0th_list)) :
			if name2 in _0th_tag_list :
				if name2 == _0th_list[order][0] :
					compare_value.append(_0th_list[order][1])
					compare_value = list(set(compare_value))
					#print (compare_value)
					if _0th_list[order][1] in compare_value :
						if len(compare_value) == 1 :
							fin_val_1.append(_0th_list[order][2])
							dic_tag_value[compare_value[0]] = fin_val_1
						elif len(compare_value) == 2 :
							if compare_value[0] == _0th_list[order][1] :
								fin_val_1.append(_0th_list[order][2])
								dic_tag_value[compare_value[0]] = fin_val_1
							else :
								fin_val_2.append(_0th_list[order][2])
								dic_tag_value[compare_value[1]] = fin_val_2
						elif len(compare_value) == 3:
							if compare_value[0] == _0th_list[order][1] :
								fin_val_1.append(_0th_list[order][2])
								dic_tag_value[compare_value[0]] = fin_val_1
							elif compare_value[1] == _0th_list[order][1] :
								fin_val_2.append(_0th_list[order][2])
								dic_tag_value[compare_value[1]] = fin_val_2
							else :
								fin_val_3.append(_0th_list[order][2])
								dic_tag_value[compare_value[2]] = fin_val_3
						elif len(compare_value) == 4 :
							if compare_value[0] == _0th_list[order][1] : 
								fin_val_1.append(_0th_list[order][2])
								dic_tag_value[compare_value[0]] = fin_val_1
							elif compare_value[1] == _0th_list[order][1] :
								fin_val_2.append(_0th_list[order][2])
								dic_tag_value[compare_value[1]] = fin_val_2
							elif compare_value[2] == _0th_list[order][1] :
								fin_val_3.append(_0th_list[order][2])
								dic_tag_value[compare_value[2]] = fin_val_3
							else :
								fin_val_4.append(_0th_list[order][2])
								dic_tag_value[compare_value[3]] = fin_val_4
						elif len(compare_value) == 5 :
							if compare_value[0] == _0th_list[order][1] :
								fin_val_1.append(_0th_list[order][2])
								dic_tag_value[compare_value[0]] = fin_val_1
							elif compare_value[1] == _0th_list[order][1] :
								fin_val_2.append(_0th_list[order][2])
								dic_tag_value[compare_value[1]] = fin_val_2
							elif compare_value[2] == _0th_list[order][1] :
								fin_val_3.append(_0th_list[order][2])
								dic_tag_value[compare_value[2]] = fin_val_3
							elif compare_value[3] == _0th_list[order][1] :
								fin_val_4.append(_0th_list[order][2])
								dic_tag_value[compare_value[3]] = fin_val_4
							else :
								fin_val_5.append(_0th_list[order][2])
								dic_tag_value[compare_value[4]] = fin_val_5
						elif len(compare_value) == 6 :
							if compare_value[0] == _0th_list[order][1] :
								fin_val_1.append(_0th_list[order][2])
								dic_tag_value[compare_value[0]] = fin_val_1
							elif compare_value[1] == _0th_list[order][1] :
								fin_val_2.append(_0th_list[order][2])
								dic_tag_value[compare_value[1]] = fin_val_2
							elif compare_value[2] == _0th_list[order][1] :
								fin_val_3.append(_0th_list[order][2])
								dic_tag_value[compare_value[2]] = fin_val_3
							elif compare_value[3] == _0th_list[order][1] :
								fin_val_4.append(_0th_list[order][2])
								dic_tag_value[compare_value[3]] = fin_val_4
							elif compare_value[4] == _0th_list[order][1] :
								fin_val_5.append(_0th_list[order][2])
								dic_tag_value[compare_value[4]] = fin_val_5
							else :
								fin_val_6.append(_0th_list[order][2])
								dic_tag_value[compare_value[5]] = fin_val_6
						elif len(compare_value) == 7 :
							if compare_value[0] == _0th_list[order][1] :
								fin_val_1.append(_0th_list[order][2])
								dic_tag_value[compare_value[0]] = fin_val_1
							elif compare_value[1] == _0th_list[order][1] :
								fin_val_2.append(_0th_list[order][2])
								dic_tag_value[compare_value[1]] = fin_val_2
							elif compare_value[2] == _0th_list[order][1] :
								fin_val_3.append(_0th_list[order][2])
								dic_tag_value[compare_value[2]] = fin_val_3
							elif compare_value[3] == _0th_list[order][1] :
								fin_val_4.append(_0th_list[order][2])
								dic_tag_value[compare_value[3]] = fin_val_4
							elif compare_value[4] == _0th_list[order][1] :
								fin_val_5.append(_0th_list[order][2])
								dic_tag_value[compare_value[4]] = fin_val_5
							elif compare_value[5] == _0th_list[order][1] :
								fin_val_6.append(_0th_list[order][2])
								dic_tag_value[compare_value[5]] = fin_val_6
							else :
								fin_val_7.append(_0th_list[order][2])
								dic_tag_value[compare_value[6]] = fin_val_7
						elif len(compare_value) == 8 :
							if compare_value[0] == _0th_list[order][1] :
								fin_val_1.append(_0th_list[order][2])
								dic_tag_value[compare_value[0]] = fin_val_1
							elif compare_value[1] == _0th_list[order][1] :
								fin_val_2.append(_0th_list[order][2])
								dic_tag_value[compare_value[1]] = fin_val_2
							elif compare_value[2] == _0th_list[order][1] :
								fin_val_3.append(_0th_list[order][2])
								dic_tag_value[compare_value[2]] = fin_val_3
							elif compare_value[3] == _0th_list[order][1] :
								fin_val_4.append(_0th_list[order][2])
								dic_tag_value[compare_value[3]] = fin_val_4
							elif compare_value[4] == _0th_list[order][1] :
								fin_val_5.append(_0th_list[order][2])
								dic_tag_value[compare_value[4]] = fin_val_5
							elif compare_value[5] == _0th_list[order][1] :
								fin_val_6.append(_0th_list[order][2])
								dic_tag_value[compare_value[5]] = fin_val_6
							elif compare_value[6] == _0th_list[order][1] :
								fin_val_7.append(_0th_list[order][2])
								dic_tag_value[compare_value[6]] = fin_val_7
							else :
								fin_val_8.append(_0th_list[order][2])
								dic_tag_value[compare_value[7]] = fin_val_8
						elif len(compare_value) == 9 :
							if compare_value[0] == _0th_list[order][1] :
								fin_val_1.append(_0th_list[order][2])
								dic_tag_value[compare_value[0]] = fin_val_1
							elif compare_value[1] == _0th_list[order][1] :
								fin_val_2.append(_0th_list[order][2])
								dic_tag_value[compare_value[1]] = fin_val_2
							elif compare_value[2] == _0th_list[order][1] :
								fin_val_3.append(_0th_list[order][2])
								dic_tag_value[compare_value[2]] = fin_val_3
							elif compare_value[3] == _0th_list[order][1] :
								fin_val_4.append(_0th_list[order][2])
								dic_tag_value[compare_value[3]] = fin_val_4
							elif compare_value[4] == _0th_list[order][1] :
								fin_val_5.append(_0th_list[order][2])
								dic_tag_value[compare_value[4]] = fin_val_5
							elif compare_value[5] == _0th_list[order][1] :
								fin_val_6.append(_0th_list[order][2])
								dic_tag_value[compare_value[5]] = fin_val_6
							elif compare_value[6] == _0th_list[order][1] :
								fin_val_7.append(_0th_list[order][2])
								dic_tag_value[compare_value[6]] = fin_val_7
							elif compare_value[7] == _0th_list[order][1] :
								fin_val_8.append(_0th_list[order][2])
								dic_tag_value[compare_value[7]] = fin_val_8
							else :
								fin_val_9.append(_0th_list[order][2])
								dic_tag_value[compare_value[8]] = fin_val_9
						elif len(compare_value) == 10 :
							if compare_value[0] == _0th_list[order][1] :
								fin_val_1.append(_0th_list[order][2])
								dic_tag_value[compare_value[0]] = fin_val_1
							elif compare_value[1] == _0th_list[order][1] :
								fin_val_2.append(_0th_list[order][2])
								dic_tag_value[compare_value[1]] = fin_val_2
							elif compare_value[2] == _0th_list[order][1] :
								fin_val_3.append(_0th_list[order][2])
								dic_tag_value[compare_value[2]] = fin_val_3
							elif compare_value[3] == _0th_list[order][1] :
								fin_val_4.append(_0th_list[order][2])
								dic_tag_value[compare_value[3]] = fin_val_4
							elif compare_value[4] == _0th_list[order][1] :
								fin_val_5.append(_0th_list[order][2])
								dic_tag_value[compare_value[4]] = fin_val_5
							elif compare_value[5] == _0th_list[order][1] :
								fin_val_6.append(_0th_list[order][2])
								dic_tag_value[compare_value[5]] = fin_val_6
							elif compare_value[6] == _0th_list[order][1] :
								fin_val_7.append(_0th_list[order][2])
								dic_tag_value[compare_value[6]] = fin_val_7
							elif compare_value[7] == _0th_list[order][1] :
								fin_val_8.append(_0th_list[order][2])
								dic_tag_value[compare_value[7]] = fin_val_8
							elif compare_value[8] == _0th_list[order][1] :
								fin_val_9.append(_0th_list[order][2])
								dic_tag_value[compare_value[8]] = fin_val_9
							else :
								fin_val_10.append(_0th_list[order][2])
								dic_tag_value[compare_value[9]] = fin_val_10
						elif len(compare_value) == 11 :
							if compare_value[0] == _0th_list[order][1] :
								fin_val_1.append(_0th_list[order][2])
								dic_tag_value[compare_value[0]] = fin_val_1
							elif compare_value[1] == _0th_list[order][1] :
								fin_val_2.append(_0th_list[order][2])
								dic_tag_value[compare_value[1]] = fin_val_2
							elif compare_value[2] == _0th_list[order][1] :
								fin_val_3.append(_0th_list[order][2])
								dic_tag_value[compare_value[2]] = fin_val_3
							elif compare_value[3] == _0th_list[order][1] :
								fin_val_4.append(_0th_list[order][2])
								dic_tag_value[compare_value[3]] = fin_val_4
							elif compare_value[4] == _0th_list[order][1] :
								fin_val_5.append(_0th_list[order][2])
								dic_tag_value[compare_value[4]] = fin_val_5
							elif compare_value[5] == _0th_list[order][1] :
								fin_val_6.append(_0th_list[order][2])
								dic_tag_value[compare_value[5]] = fin_val_6
							elif compare_value[6] == _0th_list[order][1] :
								fin_val_7.append(_0th_list[order][2])
								dic_tag_value[compare_value[6]] = fin_val_7
							elif compare_value[7] == _0th_list[order][1] :
								fin_val_8.append(_0th_list[order][2])
								dic_tag_value[compare_value[7]] = fin_val_8
							elif compare_value[8] == _0th_list[order][1] :
								fin_val_9.append(_0th_list[order][2])
								dic_tag_value[compare_value[8]] = fin_val_9
							elif compare_value[9] == _0th_list[order][1] :
								fin_val_10.append(_0th_list[order][2])	
								dic_tag_value[compare_value[9]] = fin_val_10
							else :
								fin_val_11.append(_0th_list[order][2])
								dic_tag_value[compare_value[10]] = fin_val_11
						elif len(compare_value) == 12 :
							if compare_value[0] == _0th_list[order][1] :
								fin_val_1.append(_0th_list[order][2])
								dic_tag_value[compare_value[0]] = fin_val_1
							elif compare_value[1] == _0th_list[order][1] :
								fin_val_2.append(_0th_list[order][2])
								dic_tag_value[compare_value[1]] = fin_val_2
							elif compare_value[2] == _0th_list[order][1] :
								fin_val_3.append(_0th_list[order][2])
								dic_tag_value[compare_value[2]] = fin_val_3
							elif compare_value[3] == _0th_list[order][1] :
								fin_val_4.append(_0th_list[order][2])
								dic_tag_value[compare_value[3]] = fin_val_4
							elif compare_value[4] == _0th_list[order][1] :
								fin_val_5.append(_0th_list[order][2])
								dic_tag_value[compare_value[4]] = fin_val_5
							elif compare_value[5] == _0th_list[order][1] :
								fin_val_6.append(_0th_list[order][2])
								dic_tag_value[compare_value[5]] = fin_val_6
							elif compare_value[6] == _0th_list[order][1] :
								fin_val_7.append(_0th_list[order][2])
								dic_tag_value[compare_value[6]] = fin_val_7
							elif compare_value[7] == _0th_list[order][1] :
								fin_val_8.append(_0th_list[order][2])
								dic_tag_value[compare_value[7]] = fin_val_8
							elif compare_value[8] == _0th_list[order][1] :
								fin_val_9.append(_0th_list[order][2])
								dic_tag_value[compare_value[8]] = fin_val_9
							elif compare_value[9] == _0th_list[order][1] :
								fin_val_10.append(_0th_list[order][2])	
								dic_tag_value[compare_value[9]] = fin_val_10
							elif compare_value[10] == _0th_list[order][1] :
								fin_val_11.append(_0th_list[order][2])
								dic_tag_value[compare_value[10]] = fin_val_11
							else :
								fin_val_12.append(_0th_list[order][2])
								dic_tag_value[compare_value[11]] = fin_val_12
						#print (str(Exif_list[order][3]) + " : " + str(Exif_list[order][2]))
			else :
				print ("\nPlease Cheak the tag_name!")	
	#Exif_list : [0] : name2 , [1] : value, [2] : filename
	elif name1 == "Exif" :
		compare_value = list()
		for order in range(0, len(Exif_list)) :
			if name2 in Exif_tag_list :
				if name2 == Exif_list[order][0] :
					compare_value.append(Exif_list[order][1])
					compare_value = list(set(compare_value))
			else :
				print ("\nPlease Cheak the tag_name!")	
					#print (compare_value)
		for order in range(0, len(Exif_list)) :
			if Exif_list[order][1] in compare_value :
				#print ("test")
				if len(compare_value) == 1 :
					fin_val_1.append(Exif_list[order][2])
					dic_tag_value[compare_value[0]] = fin_val_1
				elif len(compare_value) == 2 :
					if compare_value[0] == Exif_list[order][1] :
						fin_val_1.append(Exif_list[order][2])
						dic_tag_value[compare_value[0]] = fin_val_1
					else :
						fin_val_2.append(Exif_list[order][2])
						dic_tag_value[compare_value[1]] = fin_val_2
				elif len(compare_value) == 3:
					if compare_value[0] == Exif_list[order][1] :
						fin_val_1.append(Exif_list[order][2])
						dic_tag_value[compare_value[0]] = fin_val_1
					elif compare_value[1] == Exif_list[order][1] :
						fin_val_2.append(Exif_list[order][2])
						dic_tag_value[compare_value[1]] = fin_val_2
					else :
						fin_val_3.append(Exif_list[order][2])
						dic_tag_value[compare_value[2]] = fin_val_3
				elif len(compare_value) == 4 :
					#print("4ea")
					if compare_value[0] == Exif_list[order][1] : 
						fin_val_1.append(Exif_list[order][2])
						dic_tag_value[compare_value[0]] = fin_val_1
					elif compare_value[1] == Exif_list[order][1] :
						fin_val_2.append(Exif_list[order][2])
						dic_tag_value[compare_value[1]] = fin_val_2
					elif compare_value[2] == Exif_list[order][1] :
						fin_val_3.append(Exif_list[order][2])
						dic_tag_value[compare_value[2]] = fin_val_3
					else :
						fin_val_4.append(Exif_list[order][2])
						dic_tag_value[compare_value[3]] = fin_val_4
				elif len(compare_value) == 5 :
					#print("5ea")
					if compare_value[0] == Exif_list[order][1] :
						fin_val_1.append(Exif_list[order][2])
						dic_tag_value[compare_value[0]] = fin_val_1
					elif compare_value[1] == Exif_list[order][1] :
						fin_val_2.append(Exif_list[order][2])
						dic_tag_value[compare_value[1]] = fin_val_2
					elif compare_value[2] == Exif_list[order][1] :
						fin_val_3.append(Exif_list[order][2])
						dic_tag_value[compare_value[2]] = fin_val_3
					elif compare_value[3] == Exif_list[order][1] :
						fin_val_4.append(Exif_list[order][2])
						dic_tag_value[compare_value[3]] = fin_val_4
					else :
						fin_val_5.append(Exif_list[order][2])
						dic_tag_value[compare_value[4]] = fin_val_5
				elif len(compare_value) == 6 :
					#print ("6ea")
					if compare_value[0] == Exif_list[order][1] :
						fin_val_1.append(Exif_list[order][2])
						dic_tag_value[compare_value[0]] = fin_val_1
					elif compare_value[1] == Exif_list[order][1] :
						fin_val_2.append(Exif_list[order][2])
						dic_tag_value[compare_value[1]] = fin_val_2
					elif compare_value[2] == Exif_list[order][1] :
						fin_val_3.append(Exif_list[order][2])
						dic_tag_value[compare_value[2]] = fin_val_3
					elif compare_value[3] == Exif_list[order][1] :
						fin_val_4.append(Exif_list[order][2])
						dic_tag_value[compare_value[3]] = fin_val_4
					elif compare_value[4] == Exif_list[order][1] :
						fin_val_5.append(Exif_list[order][2])
						dic_tag_value[compare_value[4]] = fin_val_5
					else :
						fin_val_6.append(Exif_list[order][2])
						dic_tag_value[compare_value[5]] = fin_val_6
				elif len(compare_value) == 7 :
					#print("7ea")
					if compare_value[0] == Exif_list[order][1] :
						fin_val_1.append(Exif_list[order][2])
						dic_tag_value[compare_value[0]] = fin_val_1
					elif compare_value[1] == Exif_list[order][1] :
						fin_val_2.append(Exif_list[order][2])
						dic_tag_value[compare_value[1]] = fin_val_2
					elif compare_value[2] == Exif_list[order][1] :
						fin_val_3.append(Exif_list[order][2])
						dic_tag_value[compare_value[2]] = fin_val_3
					elif compare_value[3] == Exif_list[order][1] :
						fin_val_4.append(Exif_list[order][2])
						dic_tag_value[compare_value[3]] = fin_val_4
					elif compare_value[4] == Exif_list[order][1] :
						fin_val_5.append(Exif_list[order][2])
						dic_tag_value[compare_value[4]] = fin_val_5
					elif compare_value[5] == Exif_list[order][1] :
						fin_val_6.append(Exif_list[order][2])
						dic_tag_value[compare_value[5]] = fin_val_6
					else :
						fin_val_7.append(Exif_list[order][2])
						dic_tag_value[compare_value[6]] = fin_val_7
				elif len(compare_value) == 8 :
					if compare_value[0] == Exif_list[order][1] :
						fin_val_1.append(Exif_list[order][2])
						dic_tag_value[compare_value[0]] = fin_val_1
					elif compare_value[1] == Exif_list[order][1] :
						fin_val_2.append(Exif_list[order][2])
						dic_tag_value[compare_value[1]] = fin_val_2
					elif compare_value[2] == Exif_list[order][1] :
						fin_val_3.append(Exif_list[order][2])
						dic_tag_value[compare_value[2]] = fin_val_3
					elif compare_value[3] == Exif_list[order][1] :
						fin_val_4.append(Exif_list[order][2])
						dic_tag_value[compare_value[3]] = fin_val_4
					elif compare_value[4] == Exif_list[order][1] :
						fin_val_5.append(Exif_list[order][2])
						dic_tag_value[compare_value[4]] = fin_val_5
					elif compare_value[5] == Exif_list[order][1] :
						fin_val_6.append(Exif_list[order][2])
						dic_tag_value[compare_value[5]] = fin_val_6
					elif compare_value[6] == Exif_list[order][1] :
						fin_val_7.append(Exif_list[order][2])
						dic_tag_value[compare_value[6]] = fin_val_7
					else :
						fin_val_8.append(Exif_list[order][2])
						dic_tag_value[compare_value[7]] = fin_val_8
				elif len(compare_value) == 9 :
					if compare_value[0] == Exif_list[order][1] :
						dic_tag_value[compare_value[0]] = fin_val_1
						fin_val_1.append(Exif_list[order][2])
					elif compare_value[1] == Exif_list[order][1] :
						fin_val_2.append(Exif_list[order][2])
						dic_tag_value[compare_value[1]] = fin_val_2
					elif compare_value[2] == Exif_list[order][1] :
						fin_val_3.append(Exif_list[order][2])
						dic_tag_value[compare_value[2]] = fin_val_3
					elif compare_value[3] == Exif_list[order][1] :
						fin_val_4.append(Exif_list[order][2])
						dic_tag_value[compare_value[3]] = fin_val_4
					elif compare_value[4] == Exif_list[order][1] :
						fin_val_5.append(Exif_list[order][2])
						dic_tag_value[compare_value[4]] = fin_val_5
					elif compare_value[5] == Exif_list[order][1] :
						fin_val_6.append(Exif_list[order][2])
						dic_tag_value[compare_value[5]] = fin_val_6
					elif compare_value[6] == Exif_list[order][1] :
						fin_val_7.append(Exif_list[order][2])
						dic_tag_value[compare_value[6]] = fin_val_7
					elif compare_value[7] == Exif_list[order][1] :
						fin_val_8.append(Exif_list[order][2])
						dic_tag_value[compare_value[7]] = fin_val_8
					else :
						fin_val_9.append(Exif_list[order][2])
						dic_tag_value[compare_value[8]] = fin_val_9
				elif len(compare_value) == 10 :
					if compare_value[0] == Exif_list[order][1] :
						fin_val_1.append(Exif_list[order][2])
						dic_tag_value[compare_value[0]] = fin_val_1
					elif compare_value[1] == Exif_list[order][1] :
						fin_val_2.append(Exif_list[order][2])
						dic_tag_value[compare_value[1]] = fin_val_2
					elif compare_value[2] == Exif_list[order][1] :
						fin_val_3.append(Exif_list[order][2])
						dic_tag_value[compare_value[2]] = fin_val_3
					elif compare_value[3] == Exif_list[order][1] :
						fin_val_4.append(Exif_list[order][2])
						dic_tag_value[compare_value[3]] = fin_val_4
					elif compare_value[4] == Exif_list[order][1] :
						fin_val_5.append(Exif_list[order][2])
						dic_tag_value[compare_value[4]] = fin_val_5
					elif compare_value[5] == Exif_list[order][1] :
						fin_val_6.append(Exif_list[order][2])
						dic_tag_value[compare_value[5]] = fin_val_6
					elif compare_value[6] == Exif_list[order][1] :
						fin_val_7.append(Exif_list[order][2])
						dic_tag_value[compare_value[6]] = fin_val_7
					elif compare_value[7] == Exif_list[order][1] :
						fin_val_8.append(Exif_list[order][2])
						dic_tag_value[compare_value[7]] = fin_val_8
					elif compare_value[8] == Exif_list[order][1] :
						fin_val_9.append(Exif_list[order][2])
						dic_tag_value[compare_value[8]] = fin_val_9
					else :
						fin_val_10.append(Exif_list[order][2])
						dic_tag_value[compare_value[9]] = fin_val_10
				elif len(compare_value) == 11 :
					if compare_value[0] == Exif_list[order][1] :
						fin_val_1.append(Exif_list[order][2])
						dic_tag_value[compare_value[0]] = fin_val_1
					elif compare_value[1] == Exif_list[order][1] :
						fin_val_2.append(Exif_list[order][2])
						dic_tag_value[compare_value[1]] = fin_val_2
					elif compare_value[2] == Exif_list[order][1] :
						fin_val_3.append(Exif_list[order][2])
						dic_tag_value[compare_value[2]] = fin_val_3
					elif compare_value[3] == Exif_list[order][1] :
						fin_val_4.append(Exif_list[order][2])
						dic_tag_value[compare_value[3]] = fin_val_4
					elif compare_value[4] == Exif_list[order][1] :
						fin_val_5.append(Exif_list[order][2])
						dic_tag_value[compare_value[4]] = fin_val_5
					elif compare_value[5] == Exif_list[order][1] :
						fin_val_6.append(Exif_list[order][2])
						dic_tag_value[compare_value[5]] = fin_val_6
					elif compare_value[6] == Exif_list[order][1] :
						fin_val_7.append(Exif_list[order][2])
						dic_tag_value[compare_value[6]] = fin_val_7
					elif compare_value[7] == Exif_list[order][1] :
						fin_val_8.append(Exif_list[order][2])
						dic_tag_value[compare_value[7]] = fin_val_8
					elif compare_value[8] == Exif_list[order][1] :
						fin_val_9.append(Exif_list[order][2])
						dic_tag_value[compare_value[8]] = fin_val_9
					elif compare_value[9] == Exif_list[order][1] :
						fin_val_10.append(Exif_list[order][2])	
						dic_tag_value[compare_value[9]] = fin_val_10
					else :
						fin_val_11.append(Exif_list[order][2])
						dic_tag_value[compare_value[10]] = fin_val_11
				elif len(compare_value) == 12 :
					if compare_value[0] == Exif_list[order][1] :
						fin_val_1.append(Exif_list[order][2])
						dic_tag_value[compare_value[0]] = fin_val_1
					elif compare_value[1] == Exif_list[order][1] :
						fin_val_2.append(Exif_list[order][2])
						dic_tag_value[compare_value[1]] = fin_val_2
					elif compare_value[2] == Exif_list[order][1] :
						fin_val_3.append(Exif_list[order][2])
						dic_tag_value[compare_value[2]] = fin_val_3
					elif compare_value[3] == Exif_list[order][1] :
						fin_val_4.append(Exif_list[order][2])
						dic_tag_value[compare_value[3]] = fin_val_4
					elif compare_value[4] == Exif_list[order][1] :
						fin_val_5.append(Exif_list[order][2])
						dic_tag_value[compare_value[4]] = fin_val_5
					elif compare_value[5] == Exif_list[order][1] :
						fin_val_6.append(Exif_list[order][2])
						dic_tag_value[compare_value[5]] = fin_val_6
					elif compare_value[6] == Exif_list[order][1] :
						fin_val_7.append(Exif_list[order][2])
						dic_tag_value[compare_value[6]] = fin_val_7
					elif compare_value[7] == Exif_list[order][1] :
						fin_val_8.append(Exif_list[order][2])
						dic_tag_value[compare_value[7]] = fin_val_8
					elif compare_value[8] == Exif_list[order][1] :
						fin_val_9.append(Exif_list[order][2])
						dic_tag_value[compare_value[8]] = fin_val_9
					elif compare_value[9] == Exif_list[order][1] :
						fin_val_10.append(Exif_list[order][2])	
						dic_tag_value[compare_value[9]] = fin_val_10
					elif compare_value[10] == Exif_list[order][1] :
						fin_val_11.append(Exif_list[order][2])
						dic_tag_value[compare_value[10]] = fin_val_11
					else :
						fin_val_12.append(Exif_list[order][2])
						dic_tag_value[compare_value[11]] = fin_val_12
						#print (str(Exif_list[order][3]) + " : " + str(Exif_list[order][2]))

	elif name1 == "GPS" :
		compare_value = list()
		for order in range(0, len(GPS_list)) :
			if name2 in GPS_tag_list :
				if name2 == GPS_list[order][0] :
					if name2 == "GPSLatitude" :
						latDeg = int(GPS_list[order][1].split(",")[0][2:]) / float(int(GPS_list[order][1].split(",")[1].split(" ")[1][:-1]))
						latMin = int(GPS_list[order][1].split(",")[1].split(" ")[1][:-1]) / float(int(GPS_list[order][1].split(",")[3].split(" ")[1][:-1]))
						latSec = int(GPS_list[order][1].split(",")[4].split(" ")[1][1:]) / float(int(GPS_list[order][1].split(",")[5].split(" ")[1][:-2]))
						Lat = (latDeg + (latMin + latSec / 60.0) / 60.0)
						GPS_list[order][1] = round(Lat, 6)
					if name2 == "GPSLongitude" :					
						lonDeg = int(GPS_list[order][1].split(",")[0][2:]) / float(int(GPS_list[order][1].split(",")[1].split(" ")[1][:-1]))
						lonMin = int(GPS_list[order][1].split(",")[1].split(" ")[1][:-1]) / float(int(GPS_list[order][1].split(",")[3].split(" ")[1][:-1]))
						lonSec = int(GPS_list[order][1].split(",")[4].split(" ")[1][1:]) / float(int(GPS_list[order][1].split(",")[5].split(" ")[1][:-2]))
						Lon = (lonDeg + (lonMin + lonSec / 60.0) / 60.0)
						GPS_list[order][1] = round(Lon, 6)
					if name2 == "GPSTimeStamp" :							
						clock = round(int(GPS_list[order][1].split(",")[0][2:]) / int(GPS_list[order][1].split(",")[1].split(" ")[1][:-1]))
						minute = round(int(GPS_list[order][1].split(",")[1].split(" ")[1][:-1]) / float(int(GPS_list[order][1].split(",")[3].split(" ")[1][:-1])))
						second = round(int(GPS_list[order][1].split(",")[4].split(" ")[1][1:]) / float(int(GPS_list[order][1].split(",")[5].split(" ")[1][:-2])))
						time = str(clock) + ":" + str(minute) + ":" + str(second)
						GPS_list[order][1] = time
					if name2 == "GPSAltitude" :					
						alti = int(GPS_list[order][1].split(",")[0][1:]) / float(int(GPS_list[order][1].split(",")[1].split(" ")[1][:-1]))
						GPS_list[order][1] = alti
					compare_value.append(GPS_list[order][1])
					compare_value = list(set(compare_value))
			else :
				print ("\nPlease Cheak the tag_name!")	

		for order in range(0, len(GPS_list)) :
			if GPS_list[order][1] in compare_value :
				if len(compare_value) == 1 :
					fin_val_1.append(GPS_list[order][2])
					dic_tag_value[compare_value[0]] = fin_val_1
				elif len(compare_value) == 2 :
					if compare_value[0] == GPS_list[order][1] :
						fin_val_1.append(GPS_list[order][2])
						dic_tag_value[compare_value[0]] = fin_val_1
					else :
						fin_val_2.append(GPS_list[order][2])
						dic_tag_value[compare_value[1]] = fin_val_2
				elif len(compare_value) == 3:
					if compare_value[0] == GPS_list[order][1] :
						fin_val_1.append(GPS_list[order][2])
						dic_tag_value[compare_value[0]] = fin_val_1
					elif compare_value[1] == GPS_list[order][1] :
						fin_val_2.append(GPS_list[order][2])
						dic_tag_value[compare_value[1]] = fin_val_2
					else :
						fin_val_3.append(GPS_list[order][2])
						dic_tag_value[compare_value[2]] = fin_val_3
				elif len(compare_value) == 4 :
					if compare_value[0] == GPS_list[order][1] : 
						fin_val_1.append(GPS_list[order][2])
						dic_tag_value[compare_value[0]] = fin_val_1
					elif compare_value[1] == GPS_list[order][1] :
						fin_val_2.append(GPS_list[order][2])
						dic_tag_value[compare_value[1]] = fin_val_2
					elif compare_value[2] == GPS_list[order][1] :
						fin_val_3.append(GPS_list[order][2])
						dic_tag_value[compare_value[2]] = fin_val_3
					else :
						fin_val_4.append(GPS_list[order][2])
						dic_tag_value[compare_value[3]] = fin_val_4
				elif len(compare_value) == 5 :
					if compare_value[0] == GPS_list[order][1] :
						fin_val_1.append(GPS_list[order][2])
						dic_tag_value[compare_value[0]] = fin_val_1
					elif compare_value[1] == GPS_list[order][1] :
						fin_val_2.append(GPS_list[order][2])
						dic_tag_value[compare_value[1]] = fin_val_2
					elif compare_value[2] == GPS_list[order][1] :
						fin_val_3.append(GPS_list[order][2])
						dic_tag_value[compare_value[2]] = fin_val_3
					elif compare_value[3] == GPS_list[order][1] :
						fin_val_4.append(GPS_list[order][2])
						dic_tag_value[compare_value[3]] = fin_val_4
					else :
						fin_val_5.append(GPS_list[order][2])
						dic_tag_value[compare_value[4]] = fin_val_5
				elif len(compare_value) == 6 :
					if compare_value[0] == GPS_list[order][1] :
						fin_val_1.append(GPS_list[order][2])
						dic_tag_value[compare_value[0]] = fin_val_1
					elif compare_value[1] == GPS_list[order][1] :
						fin_val_2.append(GPS_list[order][2])
						dic_tag_value[compare_value[1]] = fin_val_2
					elif compare_value[2] == GPS_list[order][1] :
						fin_val_3.append(GPS_list[order][2])
						dic_tag_value[compare_value[2]] = fin_val_3
					elif compare_value[3] == GPS_list[order][1] :
						fin_val_4.append(GPS_list[order][2])
						dic_tag_value[compare_value[3]] = fin_val_4
					elif compare_value[4] == GPS_list[order][1] :
						fin_val_5.append(GPS_list[order][2])
						dic_tag_value[compare_value[4]] = fin_val_5
					else :
						fin_val_6.append(GPS_list[order][2])
						dic_tag_value[compare_value[5]] = fin_val_6
				elif len(compare_value) == 7 :
					if compare_value[0] == GPS_list[order][1] :
						fin_val_1.append(GPS_list[order][2])
						dic_tag_value[compare_value[0]] = fin_val_1
					elif compare_value[1] == GPS_list[order][1] :
						fin_val_2.append(GPS_list[order][2])
						dic_tag_value[compare_value[1]] = fin_val_2
					elif compare_value[2] == GPS_list[order][1] :
						fin_val_3.append(GPS_list[order][2])
						dic_tag_value[compare_value[2]] = fin_val_3
					elif compare_value[3] == GPS_list[order][1] :
						fin_val_4.append(GPS_list[order][2])
						dic_tag_value[compare_value[3]] = fin_val_4
					elif compare_value[4] == GPS_list[order][1] :
						fin_val_5.append(GPS_list[order][2])
						dic_tag_value[compare_value[4]] = fin_val_5
					elif compare_value[5] == GPS_list[order][1] :
						fin_val_6.append(GPS_list[order][2])
						dic_tag_value[compare_value[5]] = fin_val_6
					else :
						fin_val_7.append(GPS_list[order][2])
						dic_tag_value[compare_value[6]] = fin_val_7
				elif len(compare_value) == 8 :
					if compare_value[0] == GPS_list[order][1] :
						fin_val_1.append(GPS_list[order][2])
						dic_tag_value[compare_value[0]] = fin_val_1
					elif compare_value[1] == GPS_list[order][1] :
						fin_val_2.append(GPS_list[order][2])
						dic_tag_value[compare_value[1]] = fin_val_2
					elif compare_value[2] == GPS_list[order][1] :
						fin_val_3.append(GPS_list[order][2])
						dic_tag_value[compare_value[2]] = fin_val_3
					elif compare_value[3] == GPS_list[order][1] :
						fin_val_4.append(GPS_list[order][2])
						dic_tag_value[compare_value[3]] = fin_val_4
					elif compare_value[4] == GPS_list[order][1] :
						fin_val_5.append(GPS_list[order][2])
						dic_tag_value[compare_value[4]] = fin_val_5
					elif compare_value[5] == GPS_list[order][1] :
						fin_val_6.append(GPS_list[order][2])
						dic_tag_value[compare_value[5]] = fin_val_6
					elif compare_value[6] == GPS_list[order][1] :
						fin_val_7.append(GPS_list[order][2])
						dic_tag_value[compare_value[6]] = fin_val_7
					else :
						fin_val_8.append(GPS_list[order][2])
						dic_tag_value[compare_value[7]] = fin_val_8
				elif len(compare_value) == 9 :
					if compare_value[0] == GPS_list[order][1] :
						fin_val_1.append(GPS_list[order][2])
						dic_tag_value[compare_value[0]] = fin_val_1
					elif compare_value[1] == GPS_list[order][1] :
						fin_val_2.append(GPS_list[order][2])
						dic_tag_value[compare_value[1]] = fin_val_2
					elif compare_value[2] == GPS_list[order][1] :
						fin_val_3.append(GPS_list[order][2])
						dic_tag_value[compare_value[2]] = fin_val_3
					elif compare_value[3] == GPS_list[order][1] :
						fin_val_4.append(GPS_list[order][2])
						dic_tag_value[compare_value[3]] = fin_val_4
					elif compare_value[4] == GPS_list[order][1] :
						fin_val_5.append(GPS_list[order][2])
						dic_tag_value[compare_value[4]] = fin_val_5
					elif compare_value[5] == GPS_list[order][1] :
						fin_val_6.append(GPS_list[order][2])
						dic_tag_value[compare_value[5]] = fin_val_6
					elif compare_value[6] == GPS_list[order][1] :
						fin_val_7.append(GPS_list[order][2])
						dic_tag_value[compare_value[6]] = fin_val_7
					elif compare_value[7] == GPS_list[order][1] :
						fin_val_8.append(GPS_list[order][2])
						dic_tag_value[compare_value[7]] = fin_val_8
					else :
						fin_val_9.append(GPS_list[order][2])
						dic_tag_value[compare_value[8]] = fin_val_9
				elif len(compare_value) == 10 :
					if compare_value[0] == GPS_list[order][1] :
						fin_val_1.append(GPS_list[order][2])
						dic_tag_value[compare_value[0]] = fin_val_1
					elif compare_value[1] == GPS_list[order][1] :
						fin_val_2.append(GPS_list[order][2])
						dic_tag_value[compare_value[1]] = fin_val_2
					elif compare_value[2] == GPS_list[order][1] :
						fin_val_3.append(GPS_list[order][2])
						dic_tag_value[compare_value[2]] = fin_val_3
					elif compare_value[3] == GPS_list[order][1] :
						fin_val_4.append(GPS_list[order][2])
						dic_tag_value[compare_value[3]] = fin_val_4
					elif compare_value[4] == GPS_list[order][1] :
						fin_val_5.append(GPS_list[order][2])
						dic_tag_value[compare_value[4]] = fin_val_5
					elif compare_value[5] == GPS_list[order][1] :
						fin_val_6.append(GPS_list[order][2])
						dic_tag_value[compare_value[5]] = fin_val_6
					elif compare_value[6] == GPS_list[order][1] :
						fin_val_7.append(GPS_list[order][2])
						dic_tag_value[compare_value[6]] = fin_val_7
					elif compare_value[7] == GPS_list[order][1] :
						fin_val_8.append(GPS_list[order][2])
						dic_tag_value[compare_value[7]] = fin_val_8
					elif compare_value[8] == GPS_list[order][1] :
						fin_val_9.append(GPS_list[order][2])
						dic_tag_value[compare_value[8]] = fin_val_9
					else :
						fin_val_10.append(GPS_list[order][2])
						dic_tag_value[compare_value[9]] = fin_val_10
				elif len(compare_value) == 11 :
					if compare_value[0] == GPS_list[order][1] :
						fin_val_1.append(GPS_list[order][2])
						dic_tag_value[compare_value[0]] = fin_val_1
					elif compare_value[1] == GPS_list[order][1] :
						fin_val_2.append(GPS_list[order][2])
						dic_tag_value[compare_value[1]] = fin_val_2
					elif compare_value[2] == GPS_list[order][1] :
						fin_val_3.append(GPS_list[order][2])
						dic_tag_value[compare_value[2]] = fin_val_3
					elif compare_value[3] == GPS_list[order][1] :
						fin_val_4.append(GPS_list[order][2])
						dic_tag_value[compare_value[3]] = fin_val_4
					elif compare_value[4] == GPS_list[order][1] :
						fin_val_5.append(GPS_list[order][2])
						dic_tag_value[compare_value[4]] = fin_val_5
					elif compare_value[5] == GPS_list[order][1] :
						fin_val_6.append(GPS_list[order][2])
						dic_tag_value[compare_value[5]] = fin_val_6
					elif compare_value[6] == GPS_list[order][1] :
						fin_val_7.append(GPS_list[order][2])
						dic_tag_value[compare_value[6]] = fin_val_7
					elif compare_value[7] == GPS_list[order][1] :
						fin_val_8.append(GPS_list[order][2])
						dic_tag_value[compare_value[7]] = fin_val_8
					elif compare_value[8] == GPS_list[order][1] :
						fin_val_9.append(GPS_list[order][2])
						dic_tag_value[compare_value[8]] = fin_val_9
					elif compare_value[9] == GPS_list[order][1] :
						fin_val_10.append(GPS_list[order][2])	
						dic_tag_value[compare_value[9]] = fin_val_0
					else :
						fin_val_11.append(GPS_list[order][2])
						dic_tag_value[compare_value[10]] = fin_val_11
				elif len(compare_value) == 12 :
					if compare_value[0] == GPS_list[order][1] :
						fin_val_1.append(GPS_list[order][2])
						dic_tag_value[compare_value[0]] = fin_val_1
					elif compare_value[1] == GPS_list[order][1] :
						fin_val_2.append(GPS_list[order][2])
						dic_tag_value[compare_value[1]] = fin_val_2
					elif compare_value[2] == GPS_list[order][1] :
						fin_val_3.append(GPS_list[order][2])
						dic_tag_value[compare_value[2]] = fin_val_3
					elif compare_value[3] == GPS_list[order][1] :
						fin_val_4.append(GPS_list[order][2])
						dic_tag_value[compare_value[3]] = fin_val_4
					elif compare_value[4] == GPS_list[order][1] :
						fin_val_5.append(GPS_list[order][2])
						dic_tag_value[compare_value[4]] = fin_val_5
					elif compare_value[5] == GPS_list[order][1] :
						fin_val_6.append(GPS_list[order][2])
						dic_tag_value[compare_value[5]] = fin_val_6
					elif compare_value[6] == GPS_list[order][1] :
						fin_val_7.append(GPS_list[order][2])
						dic_tag_value[compare_value[6]] = fin_val_7
					elif compare_value[7] == GPS_list[order][1] :
						fin_val_8.append(GPS_list[order][2])
						dic_tag_value[compare_value[7]] = fin_val_8
					elif compare_value[8] == GPS_list[order][1] :
						fin_val_9.append(GPS_list[order][2])
						dic_tag_value[compare_value[8]] = fin_val_9
					elif compare_value[9] == GPS_list[order][1] :
						fin_val_10.append(GPS_list[order][2])
						dic_tag_value[compare_value[9]] = fin_val_10
					elif compare_value[10] == GPS_list[order][1] :
						fin_val_11.append(GPS_list[order][2])
						dic_tag_value[compare_value[10]] = fin_val_11
					else :
						fin_val_12.append(GPS_list[order][2])
						dic_tag_value[compare_value[11]] = fin_val_12

	elif name1 == "1st" :
		compare_value = list()
		for order in range(0, len(_1st_list)) :
			if name2 in _1st_tag_list :
				if name2 == _1st_list[order][0] :
					compare_value.append(_1st_list[order][1])
					compare_value = list(set(compare_value))
			else :
				print ("\nPlease Cheak the tag_name!")	

		for order in range(0, len(_1st_list)) :
			#print (compare_value)
			if _1st_list[order][1] in compare_value :
				if len(compare_value) == 1 :
					fin_val_1.append(_1st_list[order][2])
					dic_tag_value[compare_value[0]] = fin_val_1
				elif len(compare_value) == 2 :
					if compare_value[0] == _1st_list[order][1] :
						fin_val_1.append(_1st_list[order][2])
						dic_tag_value[compare_value[0]] = fin_val_1
					else :
						fin_val_2.append(_1st_list[order][2])
						dic_tag_value[compare_value[1]] = fin_val_2
				elif len(compare_value) == 3:
					if compare_value[0] == _1st_list[order][1] :
						fin_val_1.append(_1st_list[order][2])
						dic_tag_value[compare_value[0]] = fin_val_1
					elif compare_value[1] == _1st_list[order][1] :
						fin_val_2.append(_1st_list[order][2])
						dic_tag_value[compare_value[1]] = fin_val_2
					else :
						fin_val_3.append(_1st_list[order][2])
						dic_tag_value[compare_value[2]] = fin_val_3
				elif len(compare_value) == 4 :
					if compare_value[0] == _1st_list[order][1] : 
						fin_val_1.append(_1st_list[order][2])
						dic_tag_value[compare_value[0]] = fin_val_1
					elif compare_value[1] == _1st_list[order][1] :
						fin_val_2.append(_1st_list[order][2])
						dic_tag_value[compare_value[1]] = fin_val_2
					elif compare_value[2] == _1st_list[order][1] :
						fin_val_3.append(_1st_list[order][2])
						dic_tag_value[compare_value[2]] = fin_val_3
					else :
						fin_val_4.append(_1st_list[order][2])
						dic_tag_value[compare_value[3]] = fin_val_4
				elif len(compare_value) == 5 :
					if compare_value[0] == _1st_list[order][1] :
						fin_val_1.append(_1st_list[order][2])
						dic_tag_value[compare_value[0]] = fin_val_1
					elif compare_value[1] == _1st_list[order][1] :
						fin_val_2.append(_1st_list[order][2])
						dic_tag_value[compare_value[1]] = fin_val_2
					elif compare_value[2] == _1st_list[order][1] :
						fin_val_3.append(_1st_list[order][2])
						dic_tag_value[compare_value[2]] = fin_val_3
					elif compare_value[3] == _1st_list[order][1] :
						fin_val_4.append(_1st_list[order][2])
						dic_tag_value[compare_value[3]] = fin_val_4
					else :
						fin_val_5.append(_1st_list[order][2])
						dic_tag_value[compare_value[4]] = fin_val_5
				elif len(compare_value) == 6 :
					if compare_value[0] == _1st_list[order][1] :
						fin_val_1.append(_1st_list[order][2])
						dic_tag_value[compare_value[0]] = fin_val_1
					elif compare_value[1] == _1st_list[order][1] :
						fin_val_2.append(_1st_list[order][2])
						dic_tag_value[compare_value[1]] = fin_val_2
					elif compare_value[2] == _1st_list[order][1] :
						fin_val_3.append(_1st_list[order][2])
						dic_tag_value[compare_value[2]] = fin_val_3
					elif compare_value[3] == _1st_list[order][1] :
						fin_val_4.append(_1st_list[order][2])
						dic_tag_value[compare_value[3]] = fin_val_4
					elif compare_value[4] == _1st_list[order][1] :
						fin_val_5.append(_1st_list[order][2])
						dic_tag_value[compare_value[4]] = fin_val_5
					else :
						fin_val_6.append(_1st_list[order][2])
						dic_tag_value[compare_value[5]] = fin_val_6
				elif len(compare_value) == 7 :
					if compare_value[0] == _1st_list[order][1] :
						fin_val_1.append(_1st_list[order][2])
						dic_tag_value[compare_value[0]] = fin_val_1
					elif compare_value[1] == _1st_list[order][1] :
						fin_val_2.append(_1st_list[order][2])
						dic_tag_value[compare_value[1]] = fin_val_2
					elif compare_value[2] == _1st_list[order][1] :
						fin_val_3.append(_1st_list[order][2])
						dic_tag_value[compare_value[2]] = fin_val_3
					elif compare_value[3] == _1st_list[order][1] :
						fin_val_4.append(_1st_list[order][2])
						dic_tag_value[compare_value[3]] = fin_val_4
					elif compare_value[4] == _1st_list[order][1] :
						fin_val_5.append(_1st_list[order][2])
						dic_tag_value[compare_value[4]] = fin_val_5
					elif compare_value[5] == _1st_list[order][1] :
						fin_val_6.append(_1st_list[order][2])
						dic_tag_value[compare_value[5]] = fin_val_6
					else :
						fin_val_7.append(_1st_list[order][2])
						dic_tag_value[compare_value[6]] = fin_val_7
				elif len(compare_value) == 8 :
					if compare_value[0] == _1st_list[order][1] :
						fin_val_1.append(_1st_list[order][2])
						dic_tag_value[compare_value[0]] = fin_val_1
					elif compare_value[1] == _1st_list[order][1] :
						fin_val_2.append(_1st_list[order][2])
						dic_tag_value[compare_value[1]] = fin_val_2
					elif compare_value[2] == _1st_list[order][1] :
						fin_val_3.append(_1st_list[order][2])
						dic_tag_value[compare_value[2]] = fin_val_3
					elif compare_value[3] == _1st_list[order][1] :
						fin_val_4.append(_1st_list[order][2])
						dic_tag_value[compare_value[3]] = fin_val_4
					elif compare_value[4] == _1st_list[order][1] :
						fin_val_5.append(_1st_list[order][2])
						dic_tag_value[compare_value[4]] = fin_val_5
					elif compare_value[5] == _1st_list[order][1] :
						fin_val_6.append(_1st_list[order][2])
						dic_tag_value[compare_value[5]] = fin_val_6
					elif compare_value[6] == _1st_list[order][1] :
						fin_val_7.append(_1st_list[order][2])
						dic_tag_value[compare_value[6]] = fin_val_7
					else :
						fin_val_8.append(_1st_list[order][2])
						dic_tag_value[compare_value[7]] = fin_val_8
				elif len(compare_value) == 9 :
					if compare_value[0] == _1st_list[order][1] :
						fin_val_1.append(_1st_list[order][2])
						dic_tag_value[compare_value[0]] = fin_val_1
					elif compare_value[1] == _1st_list[order][1] :
						fin_val_2.append(_1st_list[order][2])
						dic_tag_value[compare_value[1]] = fin_val_2
					elif compare_value[2] == _1st_list[order][1] :
						fin_val_3.append(_1st_list[order][2])
						dic_tag_value[compare_value[2]] = fin_val_3
					elif compare_value[3] == _1st_list[order][1] :
						fin_val_4.append(_1st_list[order][2])
						dic_tag_value[compare_value[3]] = fin_val_4
					elif compare_value[4] == _1st_list[order][1] :
						fin_val_5.append(_1st_list[order][2])
						dic_tag_value[compare_value[4]] = fin_val_5
					elif compare_value[5] == _1st_list[order][1] :
						fin_val_6.append(_1st_list[order][2])
						dic_tag_value[compare_value[5]] = fin_val_6
					elif compare_value[6] == _1st_list[order][1] :
						fin_val_7.append(_1st_list[order][2])
						dic_tag_value[compare_value[6]] = fin_val_7
					elif compare_value[7] == _1st_list[order][1] :
						fin_val_8.append(_1st_list[order][2])
						dic_tag_value[compare_value[7]] = fin_val_8
					else :
						fin_val_9.append(_1st_list[order][2])
						dic_tag_value[compare_value[8]] = fin_val_9
				elif len(compare_value) == 10 :
					if compare_value[0] == _1st_list[order][1] :
						fin_val_1.append(_1st_list[order][2])
						dic_tag_value[compare_value[0]] = fin_val_1
					elif compare_value[1] == _1st_list[order][1] :
						fin_val_2.append(_1st_list[order][2])
						dic_tag_value[compare_value[1]] = fin_val_2
					elif compare_value[2] == _1st_list[order][1] :
						fin_val_3.append(_1st_list[order][2])
						dic_tag_value[compare_value[2]] = fin_val_3
					elif compare_value[3] == _1st_list[order][1] :
						fin_val_4.append(_1st_list[order][2])
						dic_tag_value[compare_value[3]] = fin_val_4
					elif compare_value[4] == _1st_list[order][1] :
						fin_val_5.append(_1st_list[order][2])
						dic_tag_value[compare_value[4]] = fin_val_5
					elif compare_value[5] == _1st_list[order][1] :
						fin_val_6.append(_1st_list[order][2])
						dic_tag_value[compare_value[5]] = fin_val_6
					elif compare_value[6] == _1st_list[order][1] :
						fin_val_7.append(_1st_list[order][2])
						dic_tag_value[compare_value[6]] = fin_val_7
					elif compare_value[7] == _1st_list[order][1] :
						fin_val_8.append(_1st_list[order][2])
						dic_tag_value[compare_value[7]] = fin_val_8
					elif compare_value[8] == _1st_list[order][1] :
						fin_val_9.append(_1st_list[order][2])
						dic_tag_value[compare_value[8]] = fin_val_9
					else :
						fin_val_10.append(_1st_list[order][2])
						dic_tag_value[compare_value[9]] = fin_val_10
				elif len(compare_value) == 11 :
					if compare_value[0] == _1st_list[order][1] :
						fin_val_1.append(_1st_list[order][2])
						dic_tag_value[compare_value[0]] = fin_val_1
					elif compare_value[1] == _1st_list[order][1] :
						fin_val_2.append(_1st_list[order][2])
						dic_tag_value[compare_value[1]] = fin_val_2
					elif compare_value[2] == _1st_list[order][1] :
						fin_val_3.append(_1st_list[order][2])
						dic_tag_value[compare_value[2]] = fin_val_3
					elif compare_value[3] == _1st_list[order][1] :
						fin_val_4.append(_1st_list[order][2])
						dic_tag_value[compare_value[3]] = fin_val_4
					elif compare_value[4] == _1st_list[order][1] :
						fin_val_5.append(_1st_list[order][2])
						dic_tag_value[compare_value[4]] = fin_val_5
					elif compare_value[5] == _1st_list[order][1] :
						fin_val_6.append(_1st_list[order][2])
						dic_tag_value[compare_value[5]] = fin_val_6
					elif compare_value[6] == _1st_list[order][1] :
						fin_val_7.append(_1st_list[order][2])
						dic_tag_value[compare_value[6]] = fin_val_7
					elif compare_value[7] == _1st_list[order][1] :
						fin_val_8.append(_1st_list[order][2])
						dic_tag_value[compare_value[7]] = fin_val_8
					elif compare_value[8] == _1st_list[order][1] :
						fin_val_9.append(_1st_list[order][2])
						dic_tag_value[compare_value[8]] = fin_val_9
					elif compare_value[9] == _1st_list[order][1] :
						fin_val_10.append(_1st_list[order][2])	
						dic_tag_value[compare_value[9]] = fin_val_10
					else :
						fin_val_11.append(_1st_list[order][2])
						dic_tag_value[compare_value[10]] = fin_val_11
				elif len(compare_value) == 12 :
					if compare_value[0] == _1st_list[order][1] :
						fin_val_1.append(_1st_list[order][2])
						dic_tag_value[compare_value[0]] = fin_val_1
					elif compare_value[1] == _1st_list[order][1] :
						fin_val_2.append(_1st_list[order][2])
						dic_tag_value[compare_value[1]] = fin_val_2
					elif compare_value[2] == _1st_list[order][1] :
						fin_val_3.append(_1st_list[order][2])
						dic_tag_value[compare_value[2]] = fin_val_3
					elif compare_value[3] == _1st_list[order][1] :
						fin_val_4.append(_1st_list[order][2])
						dic_tag_value[compare_value[3]] = fin_val_4
					elif compare_value[4] == _1st_list[order][1] :
						fin_val_5.append(_1st_list[order][2])
						dic_tag_value[compare_value[4]] = fin_val_5
					elif compare_value[5] == _1st_list[order][1] :
						fin_val_6.append(_1st_list[order][2])
						dic_tag_value[compare_value[5]] = fin_val_6
					elif compare_value[6] == _1st_list[order][1] :
						fin_val_7.append(_1st_list[order][2])
						dic_tag_value[compare_value[6]] = fin_val_7
					elif compare_value[7] == _1st_list[order][1] :
						fin_val_8.append(_1st_list[order][2])
						dic_tag_value[compare_value[7]] = fin_val_8
					elif compare_value[8] == _1st_list[order][1] :
						fin_val_9.append(_1st_list[order][2])
						dic_tag_value[compare_value[8]] = fin_val_9
					elif compare_value[9] == _1st_list[order][1] :
						fin_val_10.append(_1st_list[order][2])	
						dic_tag_value[compare_value[9]] = fin_val_10
					elif compare_value[10] == _1st_list[order][1] :
						fin_val_11.append(_1st_list[order][2])
						dic_tag_value[compare_value[10]] = fin_val_11
					else :
						fin_val_12.append(_1st_list[order][2])
						dic_tag_value[compare_value[11]] = fin_val_12
	else :
		print ("\nPlease, Input the right ifd value\n")
		print ("idf key value : 0th, Exif, GPS, 1st")
		
	if len(compare_value) == 1 :
		final_tag_value[name2] = dic_tag_value
	elif len(compare_value) == 2 :
		final_tag_value[name2] = dic_tag_value
	elif len(compare_value) == 3 :
		final_tag_value[name2] = dic_tag_value
	elif len(compare_value) == 4 :
		final_tag_value[name2] = dic_tag_value
	elif len(compare_value) == 5 :
		final_tag_value[name2] = dic_tag_value
	elif len(compare_value) == 6 :
		final_tag_value[name2] = dic_tag_value
	elif len(compare_value) == 7 :
		final_tag_value[name2] = dic_tag_value
	elif len(compare_value) == 8 :
		final_tag_value[name2] = dic_tag_value
	elif len(compare_value) == 9 :
		final_tag_value[name2] = dic_tag_value
	elif len(compare_value) == 10 :
		final_tag_value[name2] = dic_tag_value
	elif len(compare_value) == 11 :
		final_tag_value[name2] = dic_tag_value
	else :
		final_tag_value[name2] = dic_tag_value
	print ("\nifd : " + name1 + ", " + name2 + "'s value\n")
	print (final_tag_value[name2])
	print ("\n")
