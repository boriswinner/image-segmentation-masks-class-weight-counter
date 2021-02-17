import cv2
import glob
import os
import numpy as np
from tqdm import tqdm
from matplotlib import pyplot as plt

IMAGES_FOLDER = "images"


def get_list_of_images(dataset_folder, types=None):
    if types is None:
        types = ["*.png", "*.jpg", "*.jpeg", "*.bmp", "*.tiff", "*.tif"]
    img_paths = []
    for files in types:
        img_paths.extend(glob.glob(os.path.join(dataset_folder, files)))
    return img_paths


def count_percentage_in_image(image_array):
    image_classes, image_pixel_counts_for_classes = np.unique(image_array, return_counts=True)
    sum_of_pixel_counts = np.sum(image_pixel_counts_for_classes)
    percentages = []
    for class_count in image_pixel_counts_for_classes:
        percentages.append(class_count / sum_of_pixel_counts)
    return list(image_classes), percentages, list(image_pixel_counts_for_classes)


def count_percentage_in_dataset(image_paths_list):
    counts = [0] * 255
    total_count = 0
    for image_path in tqdm(image_paths_list):
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        image_classes, image_class_percentages, image_class_counts = count_percentage_in_image(image)
        for class_name, class_count in zip(image_classes, image_class_counts):
            counts[class_name] += class_count
            total_count += class_count
    resulting_classes = []
    resulting_percentages = []
    resulting_counts = []
    for idx, class_count in enumerate(counts):
        if class_count > 0:
            resulting_classes.append(idx)
            resulting_percentages.append(class_count / total_count)
            resulting_counts.append(class_count)
    return resulting_classes, resulting_percentages, resulting_counts, total_count


list_of_images_path = get_list_of_images(IMAGES_FOLDER)
assert len(list_of_images_path), "Can't find images in the folder!"
print("Found {} images. Processing...".format(len(list_of_images_path)))
dataset_classes, dataset_percentages, dataset_pixel_counts, total_count = count_percentage_in_dataset(list_of_images_path)

formatted_dataset_percentages = ['%.3f' % elem for elem in dataset_percentages]

row_format = "{:>20}" * (len(dataset_classes) + 1)
print(row_format.format("Class name", *dataset_classes))
print(row_format.format("Class percentage", *formatted_dataset_percentages))
print(row_format.format("Class pixel count", *dataset_pixel_counts))
row_format = "{:>20}" * 2
print(row_format.format("Total pixel count", total_count))

plt.figure()
plt.grid()
plt.pie(dataset_percentages, labels=dataset_classes, autopct='%1.1f%%')
plt.title(u'Percentage of pixels for each class', fontsize=15)
plt.legend(fontsize=15)
plt.show()
