from multiprocessing import Process


def worker():
    print("工作进程正在运行")


if __name__ == "__main__":
    # 创建一个进程对象
    p = Process(target=worker)
    # 启动进程
    p.start()
    # 等待进程结束
    p.join()
    print("主进程结束")
