import cv2
import numpy as np
def build_t_pyramid(image, levels):
    pyramid = [image]
    for _ in range(levels - 1):
        image = cv2.pyrDown(image)
        pyramid.append(image)
    return pyramid
def main():
    image_path = "D:/lake.jpg"
    levels = 5
    original_image = cv2.imread(image_path)
    if original_image is None:
        print("Error: Could not load the image.")
        return
    t_pyramid = build_t_pyramid(original_image, levels)
    for i, level_image in enumerate(t_pyramid): 
        cv2.imshow(f"Level {i}", level_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
