import multiprocessing

counter = multiprocessing.Value('i', 0) # устанавливаем переменную integer, start 0


def increment(cnt):
    for _ in range(10_000):
        with cnt.get_lock(): # блокировна на время процесса прибавления
            cnt.value += 1
    print(f"Значение счетчика: {cnt.value:_}")
    
    
if __name__ == '__main__':
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=increment, args=(counter, ))
        processes.append(p)
        p.start()
        
    for p in processes:
        p.join()
    
    
    print(f"Значение счетчика в финале: {counter.value:_}")#50000