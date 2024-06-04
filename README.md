# Gifify 
Make a gif out of a loop of `matplotlib` plots.

Example:
```python
import numpy as np
import matplotlib.pyplot as plt
from gifify import gifify

x = np.linspace(0, 2*np.pi, 100)

for i in gifify(range(100)):
    plt.plot(x, np.sin(x + i/10))

```
