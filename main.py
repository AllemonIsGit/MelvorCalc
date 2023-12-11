import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from calculator import Calculator
from model import *

def main():
    calculator: Calculator = Calculator()

    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    window.setGeometry(500, 250, 1000, 500)
    window.setFixedSize(270, 430)
    window.setWindowTitle("Melvor Calculator")
    window.setWindowIcon(QtGui.QIcon("assets/melvor_icon.png"))

    # Label

    lbl_material_required = QtWidgets.QLabel(window)
    lbl_material_required.setText("Material required:")
    lbl_material_required.move(20, 20)

    lbl_material_cost = QtWidgets.QLabel(window)
    lbl_material_cost.setText("Material cost:")
    lbl_material_cost.move(20, 60)

    lbl_interval = QtWidgets.QLabel(window)
    lbl_interval.setText("Interval time:")
    lbl_interval.move(20, 100)

    lbl_interval_exp = QtWidgets.QLabel(window)
    lbl_interval_exp.setText("Exp per interval:")
    lbl_interval_exp.move(20, 140)

    lbl_current_exp = QtWidgets.QLabel(window)
    lbl_current_exp.setText("Current exp:")
    lbl_current_exp.move(20, 180)

    lbl_desired_exp = QtWidgets.QLabel(window)
    lbl_desired_exp.setText("Desired exp:")
    lbl_desired_exp.move(20, 220)

    lbl_time = QtWidgets.QLabel(window)
    lbl_time.setText("time: ")
    lbl_time.move(20, 320)
    lbl_time.setMinimumWidth(390)

    lbl_cost = QtWidgets.QLabel(window)
    lbl_cost.setText("cost: ")
    lbl_cost.move(20, 350)
    lbl_cost.setMinimumWidth(390)

    lbl_materials = QtWidgets.QLabel(window)
    lbl_materials.setText("materials: ")
    lbl_materials.move(20, 380)
    lbl_materials.setMinimumWidth(390)




    # TextBox

    tb_material_required = QtWidgets.QLineEdit(window)
    tb_material_required.setValidator(QtGui.QIntValidator())
    tb_material_required.move(150, 20)

    tb_material_cost = QtWidgets.QLineEdit(window)
    tb_material_cost.setValidator(QtGui.QIntValidator())
    tb_material_cost.move(150, 60)

    tb_interval = QtWidgets.QLineEdit(window)
    tb_interval.setValidator(QtGui.QDoubleValidator())
    tb_interval.move(150, 100)

    tb_interval_exp = QtWidgets.QLineEdit(window)
    tb_interval_exp.setValidator(QtGui.QIntValidator())
    tb_interval_exp.move(150, 140)

    tb_current_exp = QtWidgets.QLineEdit(window)
    tb_current_exp.setValidator(QtGui.QIntValidator())
    tb_current_exp.move(150, 180)

    tb_desired_exp = QtWidgets.QLineEdit(window)
    tb_desired_exp.setValidator(QtGui.QIntValidator())
    tb_desired_exp.move(150, 220)

    # Button

    def buttonClick():
        values_builder = ValuesBuilder()
        values_builder.materialCost(0 if tb_material_cost.text() == "" else int(tb_material_cost.text()))
        values_builder.materialRequired(0 if tb_material_required.text() == "" else int(tb_material_required.text()))
        values_builder.interval(0 if tb_interval.text() == "" else float(tb_interval.text()))
        values_builder.expPerInterval(0 if tb_interval_exp.text() == "" else int(tb_interval_exp.text()))
        values_builder.currentExp(0 if tb_current_exp.text() == "" else int(tb_current_exp.text()))
        values_builder.desiredExp(0 if tb_desired_exp.text() == "" else int(tb_desired_exp.text()))
        values = values_builder.build()

        result: CalculatedResults = calculator.calculate(values)

        lbl_time.setText("time: " + str(int(result.getTime() / 60)) + " minutes")
        lbl_cost.setText("cost: " + calculator.seperateNumber(str(result.getCost())))
        lbl_materials.setText("materials: " + str(result.getMaterials() + 1))


    btn_calculate = QtWidgets.QPushButton(window)
    btn_calculate.setText("Calculate")
    btn_calculate.clicked.connect(lambda: buttonClick())
    btn_calculate.move(150, 260)


    # exec stuff

    window.show()
    sys.exit(app.exec_())

main()
