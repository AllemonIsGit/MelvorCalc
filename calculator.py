from model import Values, CalculatedResults
import re

class Calculator:

    def __init__(self):
        pass

    def calculate(self, values: Values) -> CalculatedResults:
        intervals = self.__calculateIntervals(values)
        cost = int(self.__calculateCost(values, intervals))
        time = int(self.__calculateTime(values, intervals))

        return CalculatedResults(time, cost, int(intervals * values.getMaterialRequired()))


    def __calculateIntervals(self, values: Values) -> int:
        current_exp = values.getCurrentExp()
        desired_exp = values.getDesiredExp()
        interval_exp = values.getExpPerInterval()

        loop = 0

        x = (desired_exp - current_exp) / interval_exp

        return x


    def __calculateCost(self, values: Values, intervals: int) -> int:
        material_required = values.getMaterialRequired()
        material_cost = values.getMaterialCost()

        return material_cost * material_required * intervals

    def __calculateTime(self, values: Values, intervals: int) -> float:
        return intervals * values.getInterval()

    def seperateNumber(self, value: str) -> str:
        return re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', value)