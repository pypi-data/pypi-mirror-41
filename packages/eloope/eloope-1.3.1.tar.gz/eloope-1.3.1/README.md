# Eloope

## 介绍

## 安装
```
pip3 install eloope
```

## 单进程
```
from eloope import Engine

def function(param):  # 自定义方法
    print(f'param: {param}')
    
engine = Engine()
for index in range(100):
    engine.add_task(function, index)
engine.run()
```
- 详细参考: https://github.com/Czw96/Eloope/blob/master/demo/spider_dili.py

## 多进程
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
manager.start()
```
###### 方法二
```
manager = Manager(name='manager')
manager.add_engines('engine1', 'engine2')
for index in range(100):
    manager.add_task('engine1', function, index)
    manager.add_task('engine2', function, index)
manager.start()
```
#### 启动


## 分布式

### Engine(name=None, pool_size=50)
###### name
###### tasks
###### redis
###### is_run
###### task_count
###### add_task(exe_func, *param)
###### switch_engine(engine_name)
###### run()

### Manager(name=None, host='localhost', port=6379)
###### name
###### processes
###### add_processes(*engines)
###### add_engines(*engine_names)
###### add_task(engine_name, exe_func, *params)
###### start()

# Demo
### spider_dili.py
### speed_test.py
### more_engine（more_engine_1.py、more_engine_2.py、more_engine_3.py）
