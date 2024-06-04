import matplotlib.pyplot as plt
import imageio


def gifify(iterator, filename="out.gif", temp_filename="temp.png"):
    images = []
    it = iter(iterator)
    # check if the iterator is empty
    while True:
        try:
            thing = next(it)
            yield thing
        except StopIteration:
            imageio.mimsave(filename, images)
            return
        plt.savefig(temp_filename)
        plt.close()
        images.append(imageio.imread(temp_filename))
