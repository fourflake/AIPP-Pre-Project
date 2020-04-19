
# PROGRAMMER: Joeri Jessen
# DATE CREATED: 25/03/2020
# REVISED DATE:

def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly
    classified images 'as a dog' or 'not a dog' especially when not a match.
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a
                    List. Where the list will contain the following items:
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
                ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and
                            0 = pet Image 'is-NOT-a' dog.
                 NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image
                            'as-a' dog and 0 = Classifier classifies image
                            'as-NOT-a' dog.
     dogfile - A text file that contains names of all dogs from the classifier
               function and dog names from the pet image files. 
    Returns:
           None - results_dic is mutable data type so no return needed.
    """
    with open("dognames.txt", "r") as f:
        dog_list = f.read().splitlines()

    for file_name, results in results_dic.items():
        print(results[0],"results[0]")
        if results[0] in dog_list:
            results_dic[file_name].extend([1])
        else:
            results_dic[file_name].extend([0])

        results_dic[file_name].extend([0])
        for pet_name in results[1].split(", "):
            if pet_name in dog_list:
                print(pet_name, "pet_name")
                results_dic[file_name][4]=1
