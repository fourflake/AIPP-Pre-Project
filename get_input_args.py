
# PROGRAMMER: Joeri Jessen
# DATE CREATED: 25/03/2020                                  
# REVISED DATE:

import argparse

def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window.
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", type=str,help="Image folder" ,default ="pet_images")
    parser.add_argument("--arch", type=str,help="CNN Model Architecture" ,default ="vgg")
    parser.add_argument("--dogfile", type=str,help="Text File" ,default ="dognames.txt")

    return parser.parse_args()
