import os
import cv2

def transfer_img(img_path, output_path):
    img = cv2.imread(img_path)
    img = cv2.resize(img, (224, 224))
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    transfer_img("/Users/baishuai/Desktop/plot_rebuttal.png", "output.jpg")