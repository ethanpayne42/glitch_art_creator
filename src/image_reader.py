import numpy as np
from matplotlib.image import imread
import matplotlib.pyplot as plt

class Image(object):
    """
    docstring for Image class, imports and shows the original image
    """

    def __init__(self, file_path, **kwargs):
        self.file_path = file_path
        self.image = imread(file_path)

    def show_image(self):
        """
        Function to show the image
        """
        plt.imshow(self.image)
        plt.show()
