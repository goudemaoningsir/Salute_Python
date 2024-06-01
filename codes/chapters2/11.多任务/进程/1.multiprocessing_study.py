# multiprocessing
flag = False
if flag == True:
    import multiprocessing

    def func():
        # 进程要执行的代码
        print("Hello， I'm a new process!")

    if __name__ == "__main__":
        process = multiprocessing.Process(target=func)
        process.start()
        process.join()


# 进程间通信-队列
flag = False
if flag == True:
    import multiprocessing

    def producer(queue):
        for i in range(5):
            queue.put(i)
            print(f"Produced item: {i}")

    def consumer(queue):
        while True:
            item = queue.get()
            if item is None:
                break
            print(f"Consumed item: {item}")

    if __name__ == "__main__":
        queue = multiprocessing.Queue()
        p1 = multiprocessing.Process(target=producer, args=(queue,))
        p2 = multiprocessing.Process(target=consumer, args=(queue,))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        queue.put(None)

# 进程间通信-管道
flag = False
if flag == True:
    import multiprocessing

    def sender(conn):
        conn.send("Hello from sender")
        conn.close()

    def receiver(conn):
        msg = conn.recv()
        print(f"Received message: {msg}")
        conn.close()

    if __name__ == "__main__":
        parent_conn, child_conn = multiprocessing.Pipe()
        p1 = multiprocessing.Process(target=sender, args=(parent_conn,))
        p2 = multiprocessing.Process(target=receiver, args=(child_conn,))
        p1.start()
        p2.start()
        p1.join()
        p2.join()

# 共享内存
flag = False
if flag == True:
    import multiprocessing

    def increment(n):
        n.value += 1  # 原子操作，递增共享变量

    if __name__ == "__main__":
        num = multiprocessing.Value("i", 0)  # 'i' 表示整型
        processes = []
        for _ in range(5):
            p = multiprocessing.Process(target=increment, args=(num,))
            processes.append(p)
            p.start()
        for p in processes:
            p.join()
        print(f"Final value: {num.value}")

flag = True
if flag == True:
    import multiprocessing

    def func(x):
        return x * x

    if __name__ == "__main__":
        with multiprocessing.Pool(processes=4) as pool:
            results = pool.map(func, range(10))
        print(results)
