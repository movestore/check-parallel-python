import logging
import math

from movingpandas import TrajectoryCollection
from timebudget import timebudget
from timebudget.timebudget import TimeBudgetRecorder

from app.parallel import create_pool, run_complex_operations_parallel
from app.serial import run_complex_operations_serial
from sdk.moveapps_spec import hook_impl


class MyTimeBudgetRecorder(TimeBudgetRecorder):

    def _print(self, msg: str):
        logging.info(f'[timebudget] {msg}')


class App(object):

    def __init__(self, moveapps_io):
        self.moveapps_io = moveapps_io
        # timebudget._default_recorder = MyTimeBudgetRecorder()
        timebudget.report_at_exit()

    @hook_impl
    def execute(self, data: TrajectoryCollection, config: dict) -> TrajectoryCollection:
        """Your app code goes here"""
        input = range(10)
        run_complex_operations_serial(complex_operation, input)
        processes_count = config['cores']
        run_complex_operations_parallel(complex_operation, input, create_pool(8))

        # return some useful data for next apps in the workflow
        return data


iterations_count = round(1e7)


def complex_operation(input_index):
    logging.info("Complex operation. Input index: {:2d}".format(input_index))

    [math.exp(i) * math.sinh(i) for i in [1] * iterations_count]
