# gs_artifact

#### 介绍
gs_artifact 是一个 Genshin 圣遗物有效词条计算网页。前端由 Vue.js + Element-UI 搭建，后端基于 Django 框架开发，数据库使用 MySQL + Navicat。前端通过 axios 请求后端，以获取封装了计算所需数值的 json 文件。项目所使用的数值由爬虫爬取相关网页并自动填入数据库。

#### 安装

1. 在项目根目录 /gs_artifact 下，创建虚拟环境

```
python -m vnev proj_env  # proj_env 为虚拟环境文件名, 可自定义
```

2. 进入虚拟环境

```
proj_env/bin/activate  # Linux 下使用
proj_env\Scripts\Acticate  # Windows 下使用
```

3.  安装 Django 依赖

```
pip install -r requirments.txt
```

4.  在 /gs_artifact/client 下，安装 Vue.js 依赖

```
npm install
```

5. 打包 Vue.js 项目文件

```
npm run build
```

6.  在项目根目录 /gs_artifact 下，迁移数据库

```
python manage.py makemigrations
python manage.py migrate
```


#### 运行
在虚拟环境下，输入以下指令即可运行项目(本地)，默认运行在 localhost:8000

```
python manage.py runserver
```


#### 使用说明

1.  建议使用 3.7.0 以上版本的 Python 及 16.16.0 以上版本的 Node.JS
2.  运行项目前，务必建立并连接 MySQL 数据库
3. 这里是列表文本项目所需的角色、武器数据可在 MySQL 手动增添，也可使用 [miyolab_crawl](https://github.com/haneball/miyolab_crawl) 爬虫快速填充数据库。


#### 效果图
网页正常运行时，如图所示
![输入图片说明](sample.png)