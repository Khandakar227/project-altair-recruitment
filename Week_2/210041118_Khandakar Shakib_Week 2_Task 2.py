import cv2 as cv
import numpy as np

def detect_red_and_white_region(image):
    # BGR value
    red_lower_bound = np.array([0, 0, 85], dtype = np.uint8)
    red_upper_bound = np.array([100, 85, 255], dtype = np.uint8)
    white_lower_bound = np.array([150, 150, 150], dtype = np.uint8)
    white_upper_bound = np.array([255, 255, 255], dtype = np.uint8)
    # Red color mask
    red_mask = cv.inRange(image, red_lower_bound, red_upper_bound)
    # white color mask
    white_mask = cv.inRange(image, white_lower_bound, white_upper_bound)
    mask = cv.bitwise_or(red_mask, white_mask)    
    regions = cv.bitwise_and(image, image, mask=mask)
    cv.imshow("Original Image", image)
    cv.imshow("RED AND WHITE REGION", regions)
    cv.waitKey(0)
    cv.destroyAllWindows()

def analyze_goat(image_array):
    image = cv.cvtColor(image_array, cv.COLOR_BGR2GRAY)
    min_pix_val = np.min(image)
    max_pix_val = np.max(image)
    average_pix_val = np.mean(image)
    non_zero_pix = np.count_nonzero(image)
    total_pix = image.shape[0] * image.shape[1]
    zero_pix = total_pix - non_zero_pix

    print("Minimum Pixel Value", min_pix_val)
    print("Maximum Pixel Value", max_pix_val)
    print("Average Pixel Value", average_pix_val)
    print("Total number of Non zero pixels", non_zero_pix)
    print("Total number of Zero pixels", zero_pix)

if __name__ == "__main__":
    img = cv.imread("photos\GOAT.jpg")
    np_img = np.array(img)
    analyze_goat(np_img)
    detect_red_and_white_region(np_img)
