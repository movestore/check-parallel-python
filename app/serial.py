from timebudget import timebudget


@timebudget
def run_complex_operations_serial(operation, input):
    for i in input:
        operation(i)
