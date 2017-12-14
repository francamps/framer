import cv2
import numpy as np
import scipy.misc as smp

cap = cv2.VideoCapture('file.mov')

frameTotal = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps    = cap.get(cv2.CAP_PROP_FPS)

if cap.isOpened() is False:
	print("Unable to open video file")
else:
	print("Video opened. Number of frames: ", frameTotal, ", fps: ", fps)

# Create a 1024x1024x3 array of 8 bit unsigned integers
newImg = np.zeros( (1080, frameTotal ,3), dtype=np.uint8 )

success = True
frameCount = 0
while frameCount < frameTotal and success:
	success,image = cap.read()
	row = 0
	col = 0
	# color info is b, g, r
	while row < height:
		blue = 0.0
		green = 0.0
		red = 0.0
		while col < width:
			blue += image[row, col][0]
			green += image[row, col][1]
			red += image[row, col][2]
			col += 1
		col = 0
		newImg.itemset((row, frameCount, 0), int(blue/width))
		newImg.itemset((row, frameCount, 1), int(green/width))
		newImg.itemset((row, frameCount, 2), int(red/width))
		row += 1

	print('Processing frame %d...' % frameCount)
	frameCount += 1

#img = smp.toImage( newImg )       # Create a PIL image
#img.show()
cv2.imwrite("averaged.jpg", newImg)
