# Eloope

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
###### add_processes(*spider_engines)
###### add_engines(*engine_names)
###### add_task(engine_name, exe_func, *params)
###### start()

# Demo
### spider_dili.py
### speed_test.py
### more_engine（more_engine_1.py、more_engine_2.py、more_engine_3.py）
