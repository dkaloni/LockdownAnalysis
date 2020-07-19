# import the necessary packages
from skimage.measure import compare_ssim
import argparse
import imutils
import cv2



#####SHAPE OF THE IMAGES
print("The type of this input is {}".format(type(no2_22032020)))
print("Shape: {}".format(no2_19032020.shape))
print("Shape: {}".format(no2_22032020.shape))
plt.imshow(no2_19032020)
#image = cv2.cvtColor(no2_21032020, cv2.COLOR_BGR2RGB)
cv2.imshow("image", image)

#gray_image = cv2.cvtColor(no2_21032020, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray_image", gray_image)

#####SHOW IMAGES
cv2.imshow("no2_19032020", no2_19032020)
cv2.imshow("no2_22032020",no2_22032020)


diff1 = cv2.subtract(no2_19032020, no2_22032020)
diff2 = cv2.subtract(no2_22032020, no2_19032020)

cv2.imshow("difference19-22",diff1)
cv2.imshow("difference22-19",diff2)
b, g, r =cv2.split(diff2)
print(cv2.countNonZero(b))
print(cv2.countNonZero(g))
print(cv2.countNonZero(r))
b, g, r = cv2.split(difference)

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True, help="nitrogendioxide_tropospheric_in_S5P_OFFL_L2__NO2____20200319T064212_202003.png")
ap.add_argument("-s", "--second", required=True, help="nitrogendioxide_tropospheric_in_S5P_OFFL_L2__NO2____20200322T054527_202003.png")
args = vars(ap.parse_args())
# load the two input images
imageA = cv2.imread(args["first"])
imageB = cv2.imread(args["second"])
# convert the images to grayscale
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
# compute the Structural Similarity Index (SSIM) between the two
# images, ensuring that the difference image is returned
(score, diff) = compare_ssim(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")
print("SSIM: {}".format(score))

#threshold the difference image, followed by finding contours to
# obtain the regions of the two input images that differ
thresh = cv2.threshold(diff, 0, 255,
cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
# loop over the contours
for c in cnts:
# compute the bounding box of the contour and then draw the
# bounding box on both input images to represent where the two
# images differ
(x, y, w, h) = cv2.boundingRect(c)
cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)



# show the output images
cv2.imshow("Original", imageA)
cv2.imshow("Modified", imageB)
cv2.imshow("Diff", diff)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)



