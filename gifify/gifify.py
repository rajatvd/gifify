import matplotlib.pyplot as plt
from IPython.display import Image, display
from io import BytesIO
import imageio
from collections.abc import Iterable


# %%
class Gifify(Iterable):
    def __init__(self, iterator, filename="out.gif", display=True):
        self.iterator = iterator
        self.filename = filename
        self.images = []
        self.counter = 0
        self.it = iter(iterator)
        self.display = display

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter > 0:
            b = BytesIO()
            plt.savefig(b, format="png")
            b.seek(0)
            img = plt.imread(b)
            img = (img * 255).astype("uint8")
            b.close()
            del b
            self.images.append(img)
            plt.close()

        thing = next(self.it)
        self.counter += 1
        return thing

    def __del__(self):
        self.cleanup()

    def cleanup(self):
        imageio.mimsave(self.filename, self.images)
        if self.display:
            display(Image(self.filename))


# %%
def gifify(
    iterator,
    filename="out.gif",
    display=True,
):
    """gifify.

    :param iterator: iterable
    :param filename: the filename to save the gif to
    :param display: whether to display the gif in the notebook after the loop
    """
    return Gifify(
        iterator,
        filename=filename,
        display=display,
    )
