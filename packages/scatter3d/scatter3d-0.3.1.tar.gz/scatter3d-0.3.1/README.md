##示例代码
```python
import numpy as np
from scatter3d.scatter3d import scatter3d

num = 1000
x = np.random.random(500)*num-num/2
y = np.random.random(500)*num-num/2
z = np.random.random(500)*num-num/2

scatter3d.set_data(x, y, z)
# scatter3d.host="127.0.0.1"
# scatter3d.port=80
# scatter3d.start_color = "#ffffff" # 开始渐变色
# scatter3d.end_color = "#ffffff"  # 结束渐变色
# scatter3d.autorotation=0.0005  # 自动旋转 数字表示旋转速度， 默认不旋转
scatter3d.run()
```
然后在浏览器中输入 [http://127.0.0.1:80](http://127.0.0.1:80) 即可查看3d散点图