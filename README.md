## 推荐系统项目代码

### 仓库列表
dataset
课程项目数据集
recall-service
召回服务
rank-service
排序服务
api-service
API接口服务
web-service
前端web网页
feature-engineer
特征处理相关代码
运行整个系统
整个系统由若干模块组成，为了方便使用我这里给大家提供了一个入口脚本用来一键启动整个系统。


首先大家将本仓库中的start.sh文件下载到本地，然后依次在start.sh脚本同目录下clone下面几个仓库：

dataset
recall-service
rank-service
api-service
web-service
### 最终的项目目录结构如下：

    - concrec/
        - start.sh
        - dataset/
        - recall-service/
        - rank-service/
        - api-service/
        - web-service/
在运行之前，大家还需要分别进入上面4个服务的目录中，切换到相应的章节分支, 如cp2分支. 并执行python虚拟环境的搭建 (本操作只需执行一次）：

virtualenv venv --python=python3
pip install -r requirements.txt
然后，大家打开根目录下的start.sh脚本，把dataset文件夹的绝对路径填到DATASET_PATH变量中。

之后我们就可以在根目录运行./start.sh脚本启动项目了，启动后可以访问http://localhost:8080查看运行效果。