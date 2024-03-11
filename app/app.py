import logging
import math

from movingpandas import TrajectoryCollection

from app.parallel import create_pool, run_complex_operations_parallel
from app.serial import run_complex_operations_serial
from sdk.moveapps_spec import hook_impl


class App(object):

    def __init__(self, moveapps_io):
        self.moveapps_io = moveapps_io

    @hook_impl
    def execute(self, data: TrajectoryCollection, config: dict) -> TrajectoryCollection:
        """Your app code goes here"""
        logging.info(f'Welcome to the {config}')

        input = range(10)
        run_complex_operations_serial(complex_operation, input)
        processes_count = config.cpus or 8
        run_complex_operations_parallel(complex_operation, input, create_pool(8))

        # return some useful data for next apps in the workflow
        return data

iterations_count = round(1e7)

def complex_operation(input_index):
    print("Complex operation. Input index: {:2d}".format(input_index))

    [math.exp(i) * math.sinh(i) for i in [1] * iterations_count]