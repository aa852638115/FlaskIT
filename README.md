# FlaskIT
## 基于Flask构建的一个IT管理网站。
- 动态自动加载功能目录
- 图形化功能管理
- 账号管理（登录，添加账号，更新账号，找回密码）
- 多权限组管理

## 安装方法
> 安装Python依赖
```
pip install -r requirements.txt
```
> 创建数据库
```
create user 'flaskit'@'%' identified by "flaskit";

grant all on flaskit.* to 'flaskit'@'%';

create database flaskit DEFAULT CHARACTER SET utf8 COLLATE utf8_bin;
```
> 导入数据库
```
mysql -uroot < db_schema/flaskit.sql
```
> 启动应用
```
python run.py
```
> 浏览器网问：http://127.0.0.1:5000
```
账号：admin 密码：123456
```
## 作者介绍
```
作者：潘晓华

邮箱：pxhua@aliyun.com
```