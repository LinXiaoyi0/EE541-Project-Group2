import os
import cv2
# image = cv2.imread("D:\\USC-Master\\Deep learning\\project\\asl_alphabet_test\\A\\A4_test.JPG")
# image = cv2.resize(image, (200, 200))
# cv2.imshow("resize", image)
# cv2.waitKey(0)
source_dir = "D:\\USC-Master\\Deep learning\\project\\asl_alphabet_test"
target_dir = "D:\\USC-Master\\Deep learning\\project\\asl_test"
for dir in os.listdir(source_dir):
    class_dir = os.path.join(source_dir, dir)
    class_test_dir = os.path.join(target_dir, dir)
    if not os.path.exists(class_test_dir):
        os.makedirs(class_test_dir)
    for filename in os.listdir(class_dir):
        source_file = os.path.join(class_dir, filename)
        image = cv2.imread(source_file)
        image = cv2.resize(image, (200, 200))
        path = os.path.join(class_test_dir, filename)
        cv2.imwrite(path, image)
    print(class_dir, 'finish')