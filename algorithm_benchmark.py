from timeit import time
from random import randrange

# Lista di partenza da ordinare
mylist = [randrange(1000) for _ in range(1000)]
copy_list = mylist.copy()

# Mi riscrivo una funzione che trova il minimo di una lista
def mymin(list):
    m_idx = 0
    m = list[0]
    for n_idx, n in enumerate(list):
        if n < m:
            m = n
            m_idx = n_idx
    return m, m_idx



# Algoritmo di ordinamento
def selection_sort(list_):
    start_time = time.time()
    for idx in range(len(list_)):
        # compute minimum and the index relative to the slice
        m, m_idx = mymin(list_[idx::])
        # convert relative index into global index
        m_idx += idx
        swap = list_[idx]
        list_[idx] = m
        list_[m_idx] = swap

    stop_time = time.time()
    print(f"Selection Sort Time: {(stop_time-start_time):.7f}")
        

def ownBubbleSort(_list):
    start_time = time.time() 

    limit = len(_list) - 1
    while limit > 0:
        for i in range(limit):
            if _list[i] > _list[i + 1]:
                # SWAP ---->
                copy = _list[i]
                _list[i] = _list[i + 1]
                _list[i + 1] = copy
                # ----->
        limit -= 1 #Decrement the range of the Cycle

    stop_time = time.time()
    print(f"Bubble Sort Time: {(stop_time-start_time):.7f}")



selection_sort(mylist)
ownBubbleSort(copy_list)