## 深证信数据服务平台API数据获取程序

### 项目介绍
```
功能点：
    该程序为深证信数据服务平台API数据获取用户端辅助程序。通过该程序可以更加便利地获取API数据。
```
### 平台目录结构说明
```
├─cninfowebapi----------------------------父项目，公共依赖
│  │
│  ├─business--------------------------业务数据获取函数
│  │  │
│  │  ├─bond------------------债券接口
│  │  │
│  │  ├─english---------------英文接口
│  │  │
│  │  ├─fund------------------基金数据接口
│  │  │
│  │  ├─futures---------------期货数据接口
│  │  │
│  │  ├─macro-----------------宏观数据接口
│  │  │
│  │  ├─neeq------------------三板数据接口
│  │  │
│  │  ├─news------------------资讯新闻接口
│  │  │
│  │  ├─oversea---------------海外数据接口
│  │  │
│  │  ├─public----------------公共编码接口
│  │  │
│  │  ├─stock-----------------A股市场上市公司
│  │
│  ├─data------------------------------数据临时存储路径
│  │
│  ├─dataapir--------------------------API获取客户端
│  │  │
│  │  ├─conf-----------------服务端及客户端配置信息(***重要：跟用户相关 clientinfo.py***)
│  │
│  ├─docs------------------------------帮助文档和其他说明
│  │
│  ├─lib-------------------------------项目依赖的基础lib
│  │
│  ├─logs------------------------------日志目录
│  │
│  ├─test------------------------------项目测试相关
│  │
│  ├─tools-----------------------------其他用户辅助工具
│  │
│  ├─util------------------------------公共程序集、通用辅助函数
│  │
```

### 使用说明--Quick Start
```
一、前提条件
1.提前安装配置好 Anaconda3(建议使用) 或 python3
2.用IDE开发工具打开工程 或 把工程目录 cninfo-data-platform 加入环境变量PATH

二、获取数据
两行代码以内完成调用和数据获取及保存。
方法1：
from dataapi.datamart import datamart
return datamart.getapidata('p_public0001', paramsdict={'sdate': startdate, 'edate': enddate})

方法2：
from business.stock.baseinfo import getstockinfos
codelist = getstockinfos()

三、查看API文档
from dataapi.datamart import datamart
datamart.apihelp('p_stock2301')

更详细的使用步骤见：docs/使用指引.md
```
### FAQ
```
1.不知道有哪些API和数据，可以从哪里获取这些信息呢？
答：这里有你想要的地图：http://webapi.cninfo.com.cn/#/apiDoc

2.如何开始试用？
答：先在深证信数据服务平台http://webapi.cninfo.com.cn 注册用户，
    在"个人中心>我的凭证"功能中先获取"Access Key"和"Access Secret"，
    把获取的两个值填写到 dataapi/conf/clientinfo.py里面的 USER_CLIENT_ID 和 USER_CLIENT_SECRET
    (注意根据使用的环境是开发或者生产需要先修改 dataapi/conf/serverinfo.py 里面的 API_SERVER_URL)
    然后就可以按照上面使用说明的方式欢快的使用数据了。

3.是否支持落地数据？还有支持落地成什么样的数据？
答：必须支持。而且同时支持 CSV\EXCEL\JSON\HDF5\MySQL等关系型数据库\NoSQL数据库\直接打印控制台

4.如何选择落地数据的格式？
答：修改dataapi/conf/clientinfo.py里面的 CLIENT_SAVE_TYPE 即可。具体配置值详见文件里面说明。
    默认存储本地sqllite 文件 business\apidb.db只需要安装tools下面的"InstallSQLiteStudio-3.2.1.exe"就可以打开使用sql查询。
```
### 传送门
```
深证信数据服务平台：http://webapi.cninfo.com.cn
API文档：http://webapi.cninfo.com.cn/#/apiDoc
巨潮资讯网：http://www.cninfo.com.cn

API测试环境：http://api1.before.com:9091/
联系方式:apidata@cninfo.com.cn
```
### Change Logs
```

V0.1.0 2019-01-30
- 创建第一个测试版本
- 实现接口数据的获取
```
```
ruitian.chen   20190130
```