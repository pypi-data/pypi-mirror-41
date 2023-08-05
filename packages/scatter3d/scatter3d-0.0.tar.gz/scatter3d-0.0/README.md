##示例代码
```python
import numpy as np
from src.scatter3d import scatter3d

num = 1000
x = np.random.random(500)*num-num/2
y = np.random.random(500)*num-num/2
z = np.random.random(500)*num-num/2

scatter3d.set_data(x, y, z)
scatter3d.run()

```