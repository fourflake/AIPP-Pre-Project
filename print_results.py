
# PROGRAMMER: Joeri Jessen
# DATE CREATED: 25/03/2020
# REVISED DATE:

def print_results(results_dic, results_stats_dic, model,
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Prints summary results on the classification and then prints incorrectly
    classified dogs and incorrectly classified dog breeds if user indicates
    they want those printouts (use non-default values)
    """
    print("\n ---------------------------------- \n RESULTS: \n")
    print("Model used: ", model)
    print("N Images: {:2d}  N Dog Images: {:2d}  N NotDog Images: {:2d} \nPct Corr dog: {:5.1f} Pct Corr NOTdog: {:5.1f}  Pct Corr Breed: {:5.1f}".format(
              results_stats_dic['n_images'], results_stats_dic['n_dogs_img'],
              results_stats_dic['n_notdogs_img'], results_stats_dic['pct_correct_dogs'],
              results_stats_dic['pct_correct_notdogs'],
              results_stats_dic['pct_correct_breed']))
    print("Pct match: ",results_stats_dic["pct_match"])

    if print_incorrect_dogs and results_stats_dic["n_correct_dogs"] + results_stats_dic["n_correct_notdogs"] != results_stats_dic["n_images"]:
        print("\nDogs classified incorrectly:\n")
        [print(x) for x in results_dic.values() if (x[4]==0 and x[3]==1)]

    if print_incorrect_breed and results_stats_dic["pct_correct_breed"] != 100:
        print("\nDogs breed classified incorrectly:")
        [print(x) for x in results_dic.values() if (x[2]==0 and x[3]==1)]
