# A pre-trained image classifier to identify dog breeds

Classifies pet images using a pretrained CNN model, compares these classifications to the true identity of the pets in the images, and summarizes how well the CNN performed on the image classification task.
This program compares the performance of 3 different CNN model architectures ('resnet', 'alexnet', and 'vgg') to determine which provides the 'best' classification.

# Usage
Use a text file (e.g. 'dogfile') that contains names of all dogs from the classifier function and dog names from the pet image files. This file should have one dog name per line.

Example call:
`python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt`
