NATS wrapper for BorderControl
==========================================

----------------------------------------------------
Instruction for add a new instance of scanner.
----------------------------------------------------

```python
    from bc.dev.handlers import WorkerThreadHandler

    counter = 0

    def worker_function(data):
        global counter
        counter += 1
        print(counter)

        return {"results": [1, 2, 3, 45]}


    a = WorkerThreadHandler(worker_function=worker_function)
    a.run()
```

**data** - here you see all data which send in sheduler in your channel

**{"results": [1, 2, 3, 45]}** - send to _reporter as:
    ```
        {
            'task_data': data,
            'result': result,
        }
    ```

**worker_function** - required arg
**name** - optional
**hostname** - optional

Module send to channel `_registration`:
    ```
        {"hostname": "hostname", "name": "name"}
    ```

Module must receive from channel `_registration`:
    ```
        {
            'subjects_to_subscribe': ['test'],
            'unique_name': 'test_module1',
        }
    ```
