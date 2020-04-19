
# PROGRAMMER: Joeri Jessen
# DATE CREATED: 25/03/2020
# REVISED DATE:

def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model
    architecture to classifying pet images. Then puts the results statistics in a
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and
                            0 = pet Image 'is-NOT-a' dog.
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image
                            'as-a' dog and 0 = Classifier classifies image
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics 
    """
    n_images = len(results_dic)     # number of images
    index_sums = [sum(tup) for tup in list((zip(*results_dic.values())))[2:]]
    n_match = index_sums[0]    # number of matches between pet & classifier labels
    n_dogs_img = index_sums[1]  # number of dog images
    n_notdogs_img = n_images-n_dogs_img  # number of NON-dog images

    n_correct_dogs = len([x for x in results_dic.values() if (x[3]==1 and x[4]==1)])  # number of correctly classified dog images
    n_correct_notdogs = len([x for x in results_dic.values() if (x[3]==0 and x[4]==0)])       # number of correctly classified NON-dog images
    n_correct_breed = len([x for x in results_dic.values() if (x[2]==1 and x[3]==1 )])# number of correctly classified dog breeds]

    pct_match = n_match/n_images*100 # percentage of correct matches
    if n_dogs_img != 0:
            pct_correct_dogs = n_correct_dogs/n_dogs_img*100 # percentage of correctly classified dogs
            pct_correct_breed = n_correct_breed/n_dogs_img*100 #percentage of correctly classified dog breeds
    else:
        pct_correct_dogs = 100
        pct_correct_breed = 100

    if n_notdogs_img != 0:
        pct_correct_notdogs = n_correct_notdogs/n_notdogs_img*100 # percentage of correctly classified NON-dogs
    else:
        pct_correct_notdogs = 100

    results_stats_dic = {"n_images" : n_images,
                        "n_dogs_img" : n_dogs_img,
                         "pct_match": pct_match,
                         "n_notdogs_img": n_notdogs_img,
                         "n_match" : n_match,
                         "n_correct_dogs" : n_correct_dogs,
                         "n_correct_notdogs": n_correct_notdogs,
                         "n_correct_breed" : n_correct_breed,
                         "n_correct_dogs" : n_correct_dogs,
                         "pct_correct_dogs" : pct_correct_dogs,
                         "pct_correct_breed" : pct_correct_breed,
                         "pct_correct_notdogs": pct_correct_notdogs
                        }

    return results_stats_dic
