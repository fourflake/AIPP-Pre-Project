
# PROGRAMMER: Joeri Jessen
# DATE CREATED:  25/03/2020
# REVISED DATE:

from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames
    of the image files.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    image_list = listdir(image_dir)
    results_dic = {}
    for path in image_list:
        if path[0] != ".":
            path_strip = path.rstrip(".jpg")
            results_dic[path] = [''.join([i for i in path_strip if not i.isdigit()]).lower().replace("_"," ").strip()]

    return results_dic
