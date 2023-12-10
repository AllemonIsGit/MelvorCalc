class Values:
    __material_cost: int
    __material_required: int
    __interval: float
    __exp_per_interval: int
    __current_exp: int
    __desired_exp: int

    def __init__(self):
        pass

    def setDesiredExp(self, value: int):
        self.__desired_exp = value

    def getDesiredExp(self) -> int:
        return self.__desired_exp

    def setCurrentExp(self, value: int):
        self.__current_exp = value

    def getCurrentExp(self) -> int:
        return self.__current_exp

    def setExpPerInterval(self, value: int):
        self.__exp_per_interval = value

    def getExpPerInterval(self) -> int:
        return self.__exp_per_interval

    def setInterval(self, value: int):
        self.__interval = value

    def getInterval(self) -> float:
        return self.__interval

    def setMaterialCost(self, material_cost: int):
        self.__material_cost = material_cost

    def getMaterialCost(self) -> int:
        return self.__material_cost

    def setMaterialRequired(self, value: int):
        self.__material_required = value

    def getMaterialRequired(self) -> int:
        return self.__material_required


class ValuesBuilder:
    __values: Values

    def __init__(self):
        self.__values = Values()

    def materialCost(self, value: int):
        self.__values.setMaterialCost(value)
        return self

    def materialRequired(self, value: int):
        self.__values.setMaterialRequired(value)
        return self

    def interval(self, value: int):
        self.__values.setInterval(value)
        return self

    def expPerInterval(self, value: int):
        self.__values.setExpPerInterval(value)
        return self

    def currentExp(self, value: int):
        self.__values.setCurrentExp(value)
        return self

    def desiredExp(self, value: int):
        self.__values.setDesiredExp(value)
        return self

    def build(self) -> Values:
        return self.__values


class CalculatedResults():
    __time: float
    __cost: int
    __materials: int

    def __init__(self, time: float, cost: int, materials: int):
        self.__time = time
        self.__cost = cost
        self.__materials = materials

    def setTime(self, value: float):
        self.__time = value

    def getTime(self) -> float:
        return self.__time

    def setCost(self, value: int):
        self.__cost = value

    def getCost(self) -> int:
        return self.__cost

    def setMaterials(self, value: int):
        self.__materials = value

    def getMaterials(self) -> int:
        return self.__materials