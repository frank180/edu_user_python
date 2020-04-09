import cv2
import npu_tool

if __name__ == '__main__' :
	frame = cv2.imread('/home/khadas/dog.jpg')
	p = npu_tool.yolo()
	a = p.disc_picture(frame)
	print(type(a))
	print(a[1]['name'])

