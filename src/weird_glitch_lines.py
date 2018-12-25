from glitcher import *
import scipy.misc
import matplotlib.pyplot as plt

hue_array = np.random.rand(5)
value_array = np.random.rand(5)

nebula = Glitched_Image('../examples/nebula_image.jpg')
image_size = np.shape(nebula.glitch_image)[0:2]
cut_p = image_size[0] - 600
#image_size = [800,800]

shift_amounts = image_size[1]*np.random.rand(5)
shift_deviations = np.zeros(5)

starting_pixel_row = np.random.uniform(low=0, high=image_size[0], size=5)
starting_pixel_col = np.random.uniform(low=0, high=image_size[1], size=5)

print(starting_pixel_row)
print(starting_pixel_col)

ending_pixel_row = starting_pixel_row + np.random.uniform(low=50, high=200, size=5)
ending_pixel_col = starting_pixel_col + np.random.uniform(low=50, high=200, size=5)

ending_pixel_row[ending_pixel_row > image_size[0]] = image_size[0]
ending_pixel_col[ending_pixel_col > image_size[1]] = image_size[1]

for i in range(0,4):
    lines(nebula.glitch_image, rows=True,
          starting_pixel=(int(starting_pixel_row[i]),int(starting_pixel_col[i])),
          ending_pixel=(int(ending_pixel_row[i]),int(ending_pixel_col[i])),
          shift_amount = shift_amounts[i],
          value=value_array[i])

cut(nebula.glitch_image, cut_point=cut_p, shift=200)


plt.imshow(nebula.glitch_image)
plt.show()

scipy.misc.imsave('outfile.jpg', nebula.glitch_image)
