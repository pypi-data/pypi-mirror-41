# wxbot

###### WXBot: A conversation robot base on Tencent's Webweixin

###### version: v1.2.1

###### 本项目托管于Github上，地址：https://github.com/ileapy/wxbot

#### v1.2.1 新增功能
    1. 恢复登录功能
    2. 解决获得的信息中文乱码的问题
    3. 优化系统
    
#### 目录结构

    ├── log                 // 运行日志
    ├── plugins             // 插件
    ├── wxbot               // 项目核心文件
    |   ├── wxconf.py       // 项目配置文件 
    |   ├── wxcore.py       // 项目运行文件  
    |   ├── wxmail.py       // 邮件模块  
    |   ├── wxmessage.py    // 项目运行文件  
    |   ├── wxparse.py      // 程序逻辑处理
    |   ├── wxserver.py     // 用于socket服务
    |   ├── wxsession.py    // 处理wx登录信息
    ├── wxbotdb             // 数据文件
    |   ├── dbconnect.py    // sqlite 数据库连接文件
    ├── setup.py            // 程序安装文件
    ├── README.md           // README

#### 运行环境要求
   * Python3.x 
   * setuptools
   * requests
   * certifi
   * apscheduler
   
#### 安装方法
    1. 下载项目文件后解压
    python setup.py install
    2. 使用pip安装
    pip install wxbot
    
#### 使用说明
    [wxbot]
        启动服务：wxbot
        选项：
            -v, --version    显示版本信息
            -h, --help       帮助信息
            -r, --restart    重新登录
            -s, --stop       停止服务
    [wx命令]
        更新：
            update group     更新群组
            update buddy     更新联系人
        查询：
            list group       查询群组
            list buddy       查询联系人
        发送：
            send group xxx xxx   发送群组消息
            send buddy xxx xxx   发送好友消息