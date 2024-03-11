from multiprocessing import Pool

from timebudget import timebudget

iterations_count = round(1e7)

@timebudget
def run_complex_operations_parallel(operation, input, pool):
    pool.map(operation, input)

def create_pool(processes_count):
    print(f'Creating {processes_count}')
    return Pool(processes=processes_count)