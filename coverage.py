import cv2
import numpy as np
import os
from pdf2image import convert_from_path, convert_from_bytes

def calculatePercentCoverage(imgName):
	global directory
	img=cv2.imread(os.path.join(directory, imgName),0)
	height, width = img.shape[:2]
	wimg = np.ones((height,width), dtype="uint8") * 255
	s = cv2.subtract(wimg,img)
	# cv2.imwrite("sub.jpg", s)
	return (100 * (cv2.countNonZero(s))/(height*width))

def pdfToImages(pdfName, saveFolder):
	convert_from_path(pdfName, dpi=200, output_folder=saveFolder, first_page=None, last_page=None, fmt='jpeg',
	thread_count=1, userpw=None, use_cropbox=False, strict=False, transparent=False, single_file=False,
  	output_file=pdfName, poppler_path=None, grayscale=True, size=None)

directory = ".\\tempCoverage"


if os.path.exists(directory):
	images = os.listdir(directory)
	for image in images:
		os.remove(os.path.join(directory, image))
	os.rmdir(directory)


os.makedirs(directory)
pdfToImages("biomed.pdf",directory)
images = os.listdir(directory)
for image in images:
	print(calculatePercentCoverage(image))
	os.remove(os.path.join(directory, image))
os.rmdir(directory)