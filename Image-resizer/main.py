import cv2

# Configurable Parameters
source = "cat-7905702.jpg"
destination = 'newImage.png'
# percent by which the image is resized
scale_percent = 50



src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imread("title", src)


# calculate the 50 percent of orignal dimensions
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

# resized image
output = cv2.resize(src, (new_width, new_height))

cv2.imwrite(destination, output)
# cv2.waitKey(0)
