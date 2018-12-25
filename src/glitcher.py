"""
This is the code to apply the glitchy edits to the images, based off the
image class from image_reader.py
"""
from image_reader import Image
import numpy as np
import colorsys
import matplotlib.pyplot as plt

# =============================================================================
# ===================== Functions for editing the array of the image ==========
# =============================================================================

def lines(image, **kwargs):

    default_kwargs = {'rows':True, 'starting_pixel':(100,0),
                      'ending_pixel':(220,0),
                      'shift_amount':250, 'shift_deviation':0,
                      'hue':1.7, 'value':1.0
                     }


    default_kwargs.update(kwargs)
    kwargs = default_kwargs

    image_size = np.shape(image)[0:2]

    ind1 = 0
    ind2 = 1


    if kwargs['rows'] == False:
        image = image.reshape((image_size[1], image_size[0], 3))

    for i in range(kwargs['starting_pixel'][ind1]+1,
                   kwargs['ending_pixel'][ind1]):

        for j in range(0, image_size[ind2]):

            shift = int(kwargs['shift_amount'] + \
                    kwargs['shift_deviation']*np.random.randn(1))

            image[i,j] = image[i,np.mod(j+shift,image_size[ind2])]

            #image[i,j] = image[kwargs['starting_pixel'][ind1]+1,j]

            hsv = list(colorsys.rgb_to_hsv(*image[i,j]/255.))

            hsv[0] = kwargs['hue']; hsv[2] = kwargs['value']

            image[i,j] = np.array(colorsys.hsv_to_rgb(*hsv))*255.

    if kwargs['rows'] == False:
        image = image.reshape((image_size[0], image_size[1], 3))

    return None
    #plt.imshow(image)
    #plt.show()


def cut(image, cut_point=500, shift = 100):
    """
    Cut the image in two and shifting the upper bit
    """
    image_size = np.shape(image)[0:2]

    for i in range(cut_point, image_size[0]):
        for j in range(0, image_size[1]):
            if j+shift < image_size[1]:
                image[i,j] = image[i,j+shift]
            else:
                image[i,j] = image[i,shift]

    return None


# =============================================================================
# ============================ Class for the glitched image ===================
# =============================================================================

class Glitched_Image(Image):
    def __init__(self, file_path, **kwargs):

        # Super runs the initialization from the other class and so
        # Glitched_Image(file_path).image exists
        # Note that this also inherents show_image()
        super().__init__(file_path)

        self.glitch_image = np.array(self.image)


    def show_image(self):
        """
        Function to show the image
        """
        plt.imshow(self.glitch_image)
        plt.show()
