### 简介
python django+微信公众平台，名称为：killme，未认证服务号，后期将改为认证的服务号。

### 公众号功能


```
- 1.调用公共接口（图灵机器人、人脸识别等）或查询数据库（人员信息查询）实现的基本功能

- 2.爬虫信息获取（煎蛋妹子、rosi、tumbler等)，公众平台做图文回复，后台django应用提供图片展示页共url跳转

- 3.网盘搜索资源显示

- 4.(50%)向服务号发送迅雷资源链接，后台下载到硬盘(可以结合小米路由器的迅雷离线功能)

- 5.(50%)发送书籍名称，后台接收后执行采集任务（商城价格，可下载百度云链接，汇总到另一个项目vermouth，中并提供页面查看）

- 6.(20%)发送人员信息(指定json格式，如姓名+号码),后台执行社工库查询。并记录查询信息至vermouth

- 7.(60%)主动文章推送：hacknews top3文章，仅做图文url跳转，django提供文章的h5页面展示。
```


### 后台功能：


```
- 1.支持自定义回复规则

- 2.支持插件式添加方法作为规则，上传py文件后，后台配置规则符

- 3.认证后的用户和任务管理
```



### 补充：


```
之后会将本服务号换成认证的服务号，区别和拓展为：

- 1.服务号未认证的情况下，无法进行素材管理，即无法回复图片和video信息，如煎蛋妹子图片，目前只能采用图文跳转第三方应用的方式折中。

- 2.服务号未认证的情况下，无法获取用户基础信息，无法细化权限控制，并且在跳转第三方应用时，无法获取当前登录用户。

- 3.服务号未认证的情况下，无法使用客服接口，客服接口允许48小时内再对用户的消息进行回复，适用于后台耗时较长的复杂操作，
如功能5和6，后台采集信息需要很长时间，无法及时回复。如果支持客服接口，可执行完成后，再回复任务情况的url。目前，只能的折中方式是：用户发出任务，返回task_id,用户不断通过task_id回查。

- 4.其他暂无....
```


### 图片展示：

![image](https://github.com/yasongxu/wechat/blob/master/pic/w1.jpg?raw=true)

![image](https://github.com/yasongxu/wechat/blob/master/pic/w2.jpg?raw=true)

![image](https://github.com/yasongxu/wechat/blob/master/pic/w3.jpg?raw=true)

![image](https://github.com/yasongxu/wechat/blob/master/pic/w4.jpg?raw=true)

![image](https://github.com/yasongxu/wechat/blob/master/pic/w5.png?raw=true)

