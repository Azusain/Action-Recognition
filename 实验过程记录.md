## 开发过程遇到的问题
* cv读取图像为bgr格式，使用Qt自带rgbSwap()进行通道交换后，按照RGB_888格式传入QImage()显示在Qt界面上
* Qt中重载paintEvent()使用QPainter中的drawPixmap函数可以大幅度提升处理速度，以代替在QLabel上进行绘制，（似乎是可以使用GPU计算？）
* pytorch创建的Tensor默认在CPU上进行运算，可以通过device=’cuda 0‘类似的Tensor初始化参数将该Tensor放到显存中
* Qt窗口必须设置CentralWidget，通过设置该组件布局以及其他布局的stretch策略（布局中Widgets的比例），可以完成基本的窗口布局工作

