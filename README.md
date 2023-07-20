# Action-Recognition(项目开发中🏃‍♂️🏃‍♂️🏃‍♂️)
* 2023大创项目仓库
* 危险行为识别
## 代码测试
### Docker
* 可以通过拉取[docker镜像](https://hub.docker.com/repository/docker/azusaing/ar/general)的方式获取代码运行环境(也可以使用项目中的 **/Docker/Dockerfile** 自行构建镜像)
```shell
  docker pull azusaing/ar:0.0.1
```
* 或者直接下载[压缩的镜像](http://azusaing.top/ar-docker)并解压
```shell
  docker load -i ar.tar # 解压后加载镜像
```
* 实例化后容器会在后台运行
```shell
  docker run --gpus all -p [SSH_PORT]:22 ar
  # 参数解释
  # --gpus all  赋予容器调用GPU的权限
  # [SSH_PORT]:22 将容器的22端口转发到[SSH_PORT]，之后外界通过端口[SSH_PORT]进行通信
  # ar          镜像名称
  # 记得替换[SSH_PORT]
```
* 此时可以通过ssh服务连接远程连接容器
```shell
  ssh root@[HOST] -p [SSH_PORT]
  # 记得替换掉[HOST]以及[SSH_PORT]
  # root默认初始密码0000
```
## Libirary
* 在**pytorch， opencv，yolov5**等库上进行开发
* 使用**PySide6**(Python-Qt)进行可视化界面展示
* 目前使用**DroidCamX**作为网络摄像头采集数据
## Progress
* 2023/4/27:目前正在搭建基本图像处理框架，包装基本函数以便后续调用
* 2023/5/22:基本的ui框架已经搭好，需要细节美化
* 2023/6/29:已经实现图像分割客户端，之后需要优化UI，并打包到docker
* 2023/7/14:打包到了docker 
## 本项目不用作商业用途仅供学习参考
