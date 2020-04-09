import os
import sys
import cv2
import json

def cut_data(raw_data, cut_parameter):
	cut_len = len(cut_parameter)
	cut_out = raw_data.find(cut_parameter)
	prefix_data = raw_data[:cut_out]
	suffix_data = raw_data[cut_out+cut_len:]
	return prefix_data,suffix_data


def get_prob(raw_data,num):
	cut_parameter = 'prob[' + str(num) + ']'
	NULL,suffix_data = cut_data(raw_data,cut_parameter)
	NULL,suffix_data = cut_data(suffix_data,'[')
	NULL,suffix_data = cut_data(suffix_data,':')
	name,possibility = cut_data(suffix_data,',')
	possibility,NULL = cut_data(possibility,']')
	prob_data = '"name":"' + name + '","possibility":' + possibility
	return prob_data


def get_coordinate(raw_data,num):
	cut_parameter = 'coordinate[' + str(num) + ']'
	NULL,suffix_data = cut_data(raw_data,cut_parameter)
	NULL,suffix_data = cut_data(suffix_data,"'[")
	x1,suffix_data = cut_data(suffix_data,',')
	y1,suffix_data = cut_data(suffix_data,',')
	x2,suffix_data = cut_data(suffix_data,',')
	y2,suffix_data = cut_data(suffix_data,']')
	coordinate_data = '"location":[' + x1 + ',' + y1 + ',' + x2 + ',' + y2 + ']' 
	return coordinate_data



class yolo:
#	def __init__():
#	def __del__():
	def disc_picture( self, frame):
		picture_path = 'image.png'
		cv2.imwrite('image.png', frame,[int(cv2.IMWRITE_PNG_COMPRESSION), 0])
		cmd = ('picture_discriminate 2 ' + picture_path)
		yolo_disc = os.popen(cmd)
		raw_info = yolo_disc.read()
		NULL,vaild_data =cut_data(raw_info,'resultData.detect_num=')
		reco_num = int(vaild_data[:+1])
		if reco_num <= 0 :
			print('No object was identified!!!')
			return 0
		list_prob = ''
		list_coordinate = ''
		result = '['
		for i in range(reco_num) :
			#get prob
			list_prob += get_prob(raw_info,i)
			#get coordinate
			list_coordinate += get_coordinate(vaild_data,i)
			result += '{' + get_prob(raw_info,i) + ',' + get_coordinate(vaild_data,i) + '},'
		result = result[:-1] + ']'
		dic = json.loads(result)
		cmd = 'rm '+ picture_path
		os.system(cmd)
		return dic







