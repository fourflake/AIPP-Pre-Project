
# PROGRAMMER: Joeri Jessen
# DATE CREATED:  25/03/2020
# REVISED DATE:

from classifier import classifier

def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to
    the classifier labels, and adds the classifier label and the comparison of
    the labels to the results dictionary using the extend function.
    Parameters:
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List. Where the list will contain the following items:
                  index 0 = pet image label (string)
                --- where index 1 & index 2 are added by this function ---
                  NEW - index 1 = classifier label (string)
                  NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
      model - Indicates which CNN model architecture will be used by the
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
     Returns:
           None - results_dic is mutable data type so no return needed.
    """
    for image_name,value_list in results_dic.items():
        image_classification = classifier((images_dir+"/"+ image_name), model).lower().strip()
        if value_list[0] in image_classification:
            match = 1
        else:
            match = 0
        results_dic[image_name].extend([image_classification, match])
