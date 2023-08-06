# Eloope

## 介绍
支持分布式、多进程的异步事件轮询引擎。单进程每秒请求可达 60余次。

## 安装
```
pip3 install eloope
```

## 单进程
- 建议在首行导入 `eloope` 模块
- 详细参考: https://github.com/Czw96/Eloope/blob/master/demo/spider_dili.py
```
from eloope import Engine, __engine__

def function(param):  # 自定义方法
    print(f'engine_name: {__engine__.name}, param: {param}')
    
engine = Engine(name='engine')
for index in range(100):
    engine.add_task(function, index)
engine.run()
```
- `__engine__` 指向当前方法体所运行的 Engine

## 多进程
- 需要安装 Redis4.0+
- 详细参考: https://github.com/Czw96/Eloope/blob/master/demo/more_engine/more_engine_3.py
```
from eloope import Engine, Manager

def function(param):  # 自定义方法
    print(f'param: {param}')
```

#### 创建 Manager
###### 方法一
```
manager = Manager(name='manager')
engine1 = Engine(name='engine1')
engine2 = Engine(name='engine2')
for index in range(100):
    engine1.add_task(function, index)
for index in range(100):
    engine2.add_task(function, index)
manager.add_processes(engine1, engine2)
manager.start()  # 程序挂起，等待控制台/终端命令启动：eloope run
```
###### 方法二
```
manager = Manager(name='manager')
manager.add_engines('engine1', 'engine2')
for index in range(100):
    manager.add_task('engine1', function, index)
    manager.add_task('engine2', function, index)
manager.start()  # 程序挂起，等待控制台/终端命令启动：eloope run
```
- 方法一可以自定义 `engine` 属性；方法二 `engine` 采用默认属性，相对方法一更简洁
- 方法体中可以通过 `__engine__.switch_engine('engine2')` 切换 `engine`
- 当 `__engine__.switch_engine()` 中没有参数，将由 `manager` 自动分配任务

#### 启动
- 打开控制台或终端输入命令 `eloope run`（可以输入 `eloope help` 查看所有命令），开始执行任务

## 分布式
- 需要配置 Redis，能够被外部访问（Redis 默认只能本地访问）
- 在每个机器部署项目，并运行相应 `manager`（`manager.start()`）
- 打开控制台或终端输入命令 `eloope run host:port`（需要指定 Redis 服务地址）

## API
### Engine(name=None, pool_size=50)
###### name --- 名称
###### is_run engine --- 是否在运行
###### pool_size --- 协程数量
###### task_count --- 任务数量
###### add_task(exe_func, *param) --- 添加任务
###### switch_engine(engine_name) --- 切换 engine
###### run() --- 开始任务

### Manager(name=None, redis_socket='localhost:6379')
###### name --- 名称
###### processes --- engines
###### add_processes(*engines) --- 添加engine实列
###### add_engines(*engine_names) --- 通过名称添加engine实列
###### add_task(engine_name, exe_func, *params) --- 添加任务到指定 engine
###### start() --- 挂起程序，等待命令

## Demo
#### spider_dili.py（单进程示例）
#### more_engine3.py（多进程示例）
