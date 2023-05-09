# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\33621\Documents\Romain\Cours_EPFL\Semestre_3\How_people_learn_2\Code\Indicators_dialog_box.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
#from PyQt5.QtGui import *
from PyQt5.QtGui import QPixmap
from Indicator_function import *


class indicator_updated(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(804, 498)
        self.descending_checkbox = QtWidgets.QCheckBox(Dialog)
        self.descending_checkbox.setGeometry(QtCore.QRect(20, 423, 120, 51))
        self.descending_checkbox.setObjectName("descending_checkbox")
        descending = self.descending_checkbox.isChecked()
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(450, 460, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.main_graphic = QtWidgets.QGraphicsView(Dialog)
        self.main_graphic.setGeometry(QtCore.QRect(300, 20, 471, 361))
        self.main_graphic.setObjectName("main_graphic")
        self.sub_graphic_1 = QtWidgets.QGraphicsView(Dialog)
        self.sub_graphic_1.setGeometry(QtCore.QRect(140, 30, 121, 101))
        self.sub_graphic_1.setObjectName("sub_graphic_1")

         # Display the linear plot in the subgraphic 1
        grview = QtWidgets.QGraphicsView(self.sub_graphic_1)
        scene = QtWidgets.QGraphicsScene(self.sub_graphic_1)
        image = QPixmap("LinearPlot.png")

        # Set it at the scale of the image to fit the window
        width = self.sub_graphic_1.width()
        height = self.sub_graphic_1.height()
        resized_image = image.scaled(width,height,QtCore.Qt.KeepAspectRatio) # To scale automaticall
        resized_image_1 = image.scaledToWidth(width) # To scale to the witdth of the window
        resized_image_2 = image.scaledToHeight(height) #To scale to the height of the window


        scene.addPixmap(resized_image)
        grview.setScene(scene)
        grview.show()


        self.min_value_input = QtWidgets.QLineEdit(Dialog)
        self.min_value_input.setGeometry(QtCore.QRect(30, 100, 51, 16))
        self.min_value_input.setText("1")
        self.min_value_input.setObjectName("min_value_input")
        self.max_value_input = QtWidgets.QLineEdit(Dialog)
        self.max_value_input.setGeometry(QtCore.QRect(30, 230, 51, 16))
        self.max_value_input.setText("10")
        self.max_value_input.setObjectName("max_value_input")
        self.units_input = QtWidgets.QLineEdit(Dialog)
        self.units_input.setGeometry(QtCore.QRect(30, 320, 51, 16))
        self.units_input.setText("")
        self.units_input.setObjectName("units_input")
        self.binary_checkbox = QtWidgets.QCheckBox(Dialog)
        self.binary_checkbox.setGeometry(QtCore.QRect(20, 393, 81, 51))
        self.binary_checkbox.setObjectName("binary_checkbox")
        self.min_value_label = QtWidgets.QLabel(Dialog)
        self.min_value_label.setGeometry(QtCore.QRect(30, 70, 81, 31))
        self.min_value_label.setObjectName("min_value_label")
        self.max_value_label = QtWidgets.QLabel(Dialog)
        self.max_value_label.setGeometry(QtCore.QRect(30, 190, 81, 41))
        self.max_value_label.setObjectName("max_value_label")
        self.units_label = QtWidgets.QLabel(Dialog)
        self.units_label.setGeometry(QtCore.QRect(30, 300, 51, 16))
        self.units_label.setObjectName("units_label")
        self.parameters_label = QtWidgets.QLabel(Dialog)
        self.parameters_label.setGeometry(QtCore.QRect(370, 390, 271, 31))
        self.parameters_label.setObjectName("parameters_label")
        self.geometrical_C_input = QtWidgets.QLineEdit(Dialog)
        self.geometrical_C_input.setGeometry(QtCore.QRect(320, 440, 51, 16))
        self.geometrical_C_input.setText("1")
        self.geometrical_C_input.setObjectName("geometrical_P_input")
        self.geometrical_K_input = QtWidgets.QLineEdit(Dialog)
        self.geometrical_K_input.setGeometry(QtCore.QRect(450, 440, 51, 16))
        self.geometrical_K_input.setText("0")
        self.geometrical_K_input.setObjectName("geometrical_K_input")
        self.geometrical_P_input = QtWidgets.QLineEdit(Dialog)
        self.geometrical_P_input.setGeometry(QtCore.QRect(590, 440, 51, 16))
        self.geometrical_P_input.setText("1")
        self.geometrical_P_input.setObjectName("geometrical_C_input")
        self.main_graph_label = QtWidgets.QLabel(Dialog)
        self.main_graph_label.setGeometry(QtCore.QRect(300, 0, 341, 16))
        self.main_graph_label.setObjectName("main_graph_label")

         # Display the main initial graph
        x_min = float(self.min_value_input.text())
        x_max = float(self.max_value_input.text())
        inflection_point_coord = [float(self.geometrical_C_input.text()), float(self.geometrical_K_input.text())]
        P = float(self.geometrical_P_input.text())

        # Create the plot function
        plot_function(P, inflection_point_coord, x_min,x_max,descending)

        # Display the plot
        grview = QtWidgets.QGraphicsView(self.main_graphic)
        scene = QtWidgets.QGraphicsScene(self.main_graphic)
        image = QPixmap("Plot.png")

        # Set it at the scale of the image to fit the window
        width = self.main_graphic.width()
        height = self.main_graphic.height()
        resized_image = image.scaled(width,height,QtCore.Qt.KeepAspectRatio) # To scale automaticall
        resized_image_1 = image.scaledToWidth(width) # To scale to the witdth of the window
        resized_image_2 = image.scaledToHeight(height) #To scale to the height of the window


        scene.addPixmap(resized_image)
        grview.setScene(scene)
        grview.show()



        self.geometric_C_label = QtWidgets.QLabel(Dialog)
        self.geometric_C_label.setGeometry(QtCore.QRect(290, 420, 141, 21))
        self.geometric_C_label.setObjectName("geometric_C_label")
        self.geometric_K_label = QtWidgets.QLabel(Dialog)
        self.geometric_K_label.setGeometry(QtCore.QRect(430, 420, 131, 20))
        self.geometric_K_label.setObjectName("geometric_K_label")
        self.geometric_P_label = QtWidgets.QLabel(Dialog)
        self.geometric_P_label.setGeometry(QtCore.QRect(590, 420, 41, 16))
        self.geometric_P_label.setObjectName("geometric_P_label")
        self.sub_graphic_2 = QtWidgets.QGraphicsView(Dialog)
        self.sub_graphic_2.setGeometry(QtCore.QRect(140, 190, 121, 101))
        self.sub_graphic_2.setObjectName("sub_graphic_2")

         # Display the linear plot in the subgraphic 2
        grview = QtWidgets.QGraphicsView(self.sub_graphic_2)
        scene = QtWidgets.QGraphicsScene(self.sub_graphic_2)
        image = QPixmap("ConvexPlot.png")

        # Set it at the scale of the image to fit the window
        width = self.sub_graphic_2.width()
        height = self.sub_graphic_2.height()
        resized_image = image.scaled(width,height,QtCore.Qt.KeepAspectRatio) # To scale automaticall
        resized_image_1 = image.scaledToWidth(width) # To scale to the witdth of the window
        resized_image_2 = image.scaledToHeight(height) #To scale to the height of the window


        scene.addPixmap(resized_image)
        grview.setScene(scene)
        grview.show()


        self.sub_graphic_3 = QtWidgets.QGraphicsView(Dialog)
        self.sub_graphic_3.setGeometry(QtCore.QRect(140, 350, 121, 101))
        self.sub_graphic_3.setObjectName("sub_graphic_3")

        # Display the linear plot in the subgraphic 3
        grview = QtWidgets.QGraphicsView(self.sub_graphic_3)
        scene = QtWidgets.QGraphicsScene(self.sub_graphic_3)
        image = QPixmap("ConcavePlot.png")

        # Set it at the scale of the image to fit the window
        width = self.sub_graphic_2.width()
        height = self.sub_graphic_2.height()
        resized_image = image.scaled(width,height,QtCore.Qt.KeepAspectRatio) # To scale automaticall
        resized_image_1 = image.scaledToWidth(width) # To scale to the witdth of the window
        resized_image_2 = image.scaledToHeight(height) #To scale to the height of the window


        scene.addPixmap(resized_image)
        grview.setScene(scene)
        grview.show()


        self.sub_graph_2_button = QtWidgets.QPushButton(Dialog)
        self.sub_graph_2_button.setGeometry(QtCore.QRect(140, 300, 121, 31))
        self.sub_graph_2_button.setObjectName("sub_graph_2_button")
        self.sub_graph_3_button = QtWidgets.QPushButton(Dialog)
        self.sub_graph_3_button.setGeometry(QtCore.QRect(140, 460, 121, 31))
        self.sub_graph_3_button.setObjectName("sub_graph_3_button")
        self.sub_graph_1_button = QtWidgets.QPushButton(Dialog)
        self.sub_graph_1_button.setGeometry(QtCore.QRect(140, 140, 121, 31))
        self.sub_graph_1_button.setObjectName("sub_graph_1_button")
        self.sub_graph_1_button.setText("Linear")
        self.update_button = QtWidgets.QPushButton(Dialog)
        self.update_button.setGeometry(QtCore.QRect(570, 390, 191, 31))
        self.update_button.setObjectName("update_button")
        self.retranslateUi(Dialog)
        # BUTTONS

        self.sub_graph_1_button.clicked.connect(self.linear_button_clicked)
        self.sub_graph_2_button.clicked.connect(self.concave_button_clicked)
        self.sub_graph_3_button.clicked.connect(self.convex_button_clicked)
        self.update_button.clicked.connect(self.update_geometry)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.binary_checkbox.setText(_translate("Dialog", "Binary "))
        self.descending_checkbox.setText(_translate("Dialog", "Descending "))
        self.min_value_label.setText(_translate("Dialog", "Min. Value"))
        self.max_value_label.setText(_translate("Dialog", "Max. Value"))
        self.units_label.setText(_translate("Dialog", "Units"))
        self.parameters_label.setText(_translate("Dialog", "Geometrical parameters"))
        self.main_graph_label.setText(_translate("Dialog", "INDICATOR FUNCTION"))
        self.geometric_C_label.setText(_translate("Dialog", "Abs. infl.point (C)"))
        self.geometric_K_label.setText(_translate("Dialog", "Ord. infl.point (K)"))
        self.geometric_P_label.setText(_translate("Dialog", "P"))
        self.sub_graph_2_button.setText(_translate("Dialog", "Convex"))
        self.sub_graph_3_button.setText(_translate("Dialog", "Concave"))
        self.sub_graph_1_button.setText(_translate("Dialog", "Linear"))
        self.update_button.setText(_translate("Dialog", "Update geometry"))

    def linear_button_clicked(self):
        x_min = float(self.min_value_input.text())
        x_max = float(self.max_value_input.text())
        descending = self.descending_checkbox.isChecked()
        P, infl_points_coords = plot_linear_function(x_min,x_max,descending)
        self.binary_checkbox.setChecked(False)
        self.geometrical_P_input.setText(str(P))
        self.geometrical_C_input.setText(str(infl_points_coords[0]))
        self.geometrical_K_input.setText(str(infl_points_coords[1]))

        # Display the plot
        grview = QtWidgets.QGraphicsView(self.main_graphic)
        scene = QtWidgets.QGraphicsScene(self.main_graphic)
        image = QPixmap("Plot.png")

        # Set it at the scale of the image to fit the window
        width = self.main_graphic.width()
        height = self.main_graphic.height()
        resized_image = image.scaled(width,height,QtCore.Qt.KeepAspectRatio) # To scale automaticall
        resized_image_1 = image.scaledToWidth(width) # To scale to the witdth of the window
        resized_image_2 = image.scaledToHeight(height) #To scale to the height of the window


        scene.addPixmap(resized_image)
        grview.setScene(scene)
        grview.show()

    def concave_button_clicked(self):
        x_min = float(self.min_value_input.text())
        x_max = float(self.max_value_input.text())
        descending = self.descending_checkbox.isChecked()
        P, infl_points_coords = plot_concave_function(x_min,x_max,descending)
        print(P)
        self.binary_checkbox.setChecked(False)
        self.geometrical_P_input.setText(str(P))
        self.geometrical_C_input.setText(str(infl_points_coords[0]))
        self.geometrical_K_input.setText(str(infl_points_coords[1]))

        # Display the plot
        grview = QtWidgets.QGraphicsView(self.main_graphic)
        scene = QtWidgets.QGraphicsScene(self.main_graphic)
        image = QPixmap("Plot.png")

        # Set it at the scale of the image to fit the window
        width = self.main_graphic.width()
        height = self.main_graphic.height()
        resized_image = image.scaled(width,height,QtCore.Qt.KeepAspectRatio) # To scale automaticall
        resized_image_1 = image.scaledToWidth(width) # To scale to the witdth of the window
        resized_image_2 = image.scaledToHeight(height) #To scale to the height of the window


        scene.addPixmap(resized_image)
        grview.setScene(scene)
        grview.show()

    def convex_button_clicked(self):
        x_min = float(self.min_value_input.text())
        x_max = float(self.max_value_input.text())
        descending = self.descending_checkbox.isChecked()
        P, infl_points_coords = plot_convex_function(x_min,x_max,descending)
        self.binary_checkbox.setChecked(False)
        self.geometrical_P_input.setText(str(P))
        self.geometrical_C_input.setText(str(infl_points_coords[0]))
        self.geometrical_K_input.setText(str(infl_points_coords[1]))


        # Display the plot
        grview = QtWidgets.QGraphicsView(self.main_graphic)
        scene = QtWidgets.QGraphicsScene(self.main_graphic)
        image = QPixmap("Plot.png")

        # Set it at the scale of the image to fit the window
        width = self.main_graphic.width()
        height = self.main_graphic.height()
        resized_image = image.scaled(width,height,QtCore.Qt.KeepAspectRatio) # To scale automaticall
        resized_image_1 = image.scaledToWidth(width) # To scale to the witdth of the window
        resized_image_2 = image.scaledToHeight(height) #To scale to the height of the window


        scene.addPixmap(resized_image)
        grview.setScene(scene)
        grview.show()


    def update_geometry(self):

        # Get user input values for the plot
        binary = self.binary_checkbox.isChecked()
        descending = self.descending_checkbox.isChecked()
        if binary:
            plot_binary_function(descending)
        else:
            x_min = float(self.min_value_input.text())
            x_max = float(self.max_value_input.text())
            inflection_point_coord = [float(self.geometrical_C_input.text()), float(self.geometrical_K_input.text())]
            P = float(self.geometrical_P_input.text())
            # Create the plot function
            plot_function(P, inflection_point_coord, x_min,x_max,descending)
        # Display the plot
        grview = QtWidgets.QGraphicsView(self.main_graphic)
        scene = QtWidgets.QGraphicsScene(self.main_graphic)
        image = QPixmap("Plot.png")

        # Set it at the scale of the image to fit the window
        width = self.main_graphic.width()
        height = self.main_graphic.height()
        resized_image = image.scaled(width,height,QtCore.Qt.KeepAspectRatio) # To scale automaticall
        resized_image_1 = image.scaledToWidth(width) # To scale to the witdth of the window
        resized_image_2 = image.scaledToHeight(height) #To scale to the height of the window


        scene.addPixmap(resized_image)
        grview.setScene(scene)
        grview.show()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = indicator_updated()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
