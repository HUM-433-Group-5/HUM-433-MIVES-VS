# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\33621\Documents\Romain\Cours_EPFL\Semestre_3\How_people_learn_2\Code\Graphic_output.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

class Ui_Dialog_for_graph(object):
    def setupUi_for_graph(self, Dialog,pilar_dictionnary,criteria_dictionnary,indicator_dictionnary,final_value,t,complete_dictionnary):
        self.final_value = final_value
        self.t = t
        self.complete_dictionnary = complete_dictionnary
        self.pilar_dictionnary = pilar_dictionnary
        self.criteria_dictionnary = criteria_dictionnary
        self.indicator_dictionnary = indicator_dictionnary
        Dialog.setObjectName("Dialog")
        Dialog.resize(1078, 861)
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(30, 30, 891, 721))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 0, 900, 21))
        self.label.setObjectName("label")
        i = 0
        self.final_value_string = ""
        if type(final_value) != list:
            self.final_value_string = "Var. 1 "+": "+str(round(final_value,3))
        else:
            for score in final_value:
                i = i + 1
                self.final_value_string = self.final_value_string + "Var. "+str(i)+": "+str(round(final_value[i-1],3)) + "  "

        label_text ="TOTAL VIEW - final sustainability score: "+ self.final_value_string
        self.label.setText(label_text)


        self.create_and_save_all_figures()
        self.plot_figure("Pilar_plot.png")




        width_between_buttons = 220
        num_button = 0

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(840, 800, 221, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Total view")
        self.pushButton.clicked.connect(lambda :self.plot_figure("Pilar_Plot.png"))

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(570, 800, 221, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText("Social")
        self.pushButton_2.clicked.connect(lambda :self.plot_figure("Criteria_plotSocial.png"))

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 800, 221, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Economic")
        self.pushButton_3.clicked.connect(lambda :self.plot_figure("Criteria_plotEconomic.png"))

        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 800, 221, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setText("Environmental")
        self.pushButton_4.clicked.connect(lambda :self.plot_figure("Criteria_plotEnvironmental.png"))


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.pushButton_2.setText(_translate("Dialog", "PushButton"))
        self.pushButton_3.setText(_translate("Dialog", "PushButton"))
        self.pushButton_4.setText(_translate("Dialog", "PushButton"))



    def plot_figure(self,image):
        plt.clf()
        self.grview = QtWidgets.QGraphicsView(self.graphicsView)
        scene = QtWidgets.QGraphicsScene(self.graphicsView)
        scene.clear()

        if image == "Criteria_plotEconomic.png":
                    label_text ="ECONOMIC VIEW - final sustainability score: "+ self.final_value_string
                    self.label.setText(label_text)
        if image == "Criteria_plotSocial.png":
                    label_text ="SOCIAL VIEW - final sustainability score: "+ self.final_value_string
                    self.label.setText(label_text)
        if image == "Criteria_plotEnvironmental.png":
                    label_text ="ENVIRONMENTAL VIEW - final sustainability score: "+ self.final_value_string
                    self.label.setText(label_text)
        if image == "Pilar_plot.png":
                    label_text ="TOTAL VIEW - final sustainability score: "+ self.final_value_string
                    self.label.setText(label_text)

        image = QPixmap(image)

        # Set it at the scale of the image to fit the window
        width = self.graphicsView.width()
        height = self.graphicsView.height()
        resized_image = image.scaled(width,height,QtCore.Qt.KeepAspectRatio) # To scale automaticall
        resized_image_1 = image.scaledToWidth(width) # To scale to the witdth of the window
        resized_image_2 = image.scaledToHeight(height) #To scale to the height of the window

        scene.addPixmap(resized_image)
        self.grview.setScene(scene)
        self.grview.show()


    def create_and_save_all_figures(self):
                    plt.clf()
                    #Plot all criteria plots and saves them
                    self.label_text ="CRITERIA VIEW - final sustainability score: "+str(self.final_value)


                    # We check if we have 1 variant or several variants:
                    for key in self.indicator_dictionnary:
                        if type(self.indicator_dictionnary[key])==list:
                            number_of_variants = len(self.indicator_dictionnary[key])
                        else:
                            number_of_variants = 1

                    colors = ["b","g","r","c","m","y","k","w"]
                    criteria_color_dictionnary = {}
                    num_of_color = 0
                    for criteria in self.criteria_dictionnary:
                        criteria_color_dictionnary[criteria] = colors[num_of_color]
                        num_of_color = num_of_color+1
                    final_crit_dictionnary = {}

                    if number_of_variants >1:
                        for pilar in self.pilar_dictionnary:
                                plt.clf()
                                final_crit_dictionnary[pilar] = {}
                                for var in range(0,number_of_variants):
                                    # To stack up variables in the bars
                                    previous_crit_value = 0
                                    num_crit = 0
                                    for crit in self.criteria_dictionnary:
                                        crit_parent = self.t.search_nodes(name=crit)[0].up.name
                                        if crit_parent == pilar:
                                            num_crit = num_crit+1

                                            crit_value = self.criteria_dictionnary[crit][var]
                                            crit_weight = self.complete_dictionnary[crit]
                                            final_crit_value =crit_value*crit_weight

                                            if crit not in final_crit_dictionnary and final_crit_value!=0:
                                                final_crit_dictionnary[pilar][crit] = final_crit_value

                                            col = criteria_color_dictionnary[crit]
                                            plt.bar(str("Variante "+str(var+1)),final_crit_value,0.1, color = col, bottom=previous_crit_value)

                                            previous_crit_value = previous_crit_value+final_crit_value

                                plt.ylabel("Scores")
                                handles = []
                                for crit in criteria_color_dictionnary:
                                    if crit in final_crit_dictionnary[pilar]:
                                        handle = mpatches.Patch(color=criteria_color_dictionnary[crit], label=crit)
                                        handles.append(handle)
                                plt.legend(handles= handles)
                                Criteria_plot = "Criteria_plot"+pilar+".png"
                                plt.savefig(Criteria_plot,bbox_inches = "tight")


                        self.label_text ="PILLAR VIEW - final sustainability score: "+str(self.final_value)
                        self.label.setObjectName(self.label_text)


                        #Plots indicators plots and saves them
                        plt.clf()
                        for key in self.indicator_dictionnary:
                            number_of_variants = len(self.indicator_dictionnary[key])

                        colors = ["b","g","r","c","m","y","k","w"]
                        pilar_color_dictionnary = {}
                        num_of_color = 0
                        for pilar in self.pilar_dictionnary:
                            pilar_color_dictionnary[pilar] = colors[num_of_color]
                            num_of_color = num_of_color+1

                        final_pilar_dictionnary = {}
                        for var in range(0,number_of_variants):
                                previous_pilar_value = 0
                                for pilar in self.pilar_dictionnary:
                                    # For each variant, we reset the number of the color, so that we have a color associated to a
                                    # criteria, and criterias are the same between variants
                                    # To stack up variables in the bars
                                    pilar_value = self.pilar_dictionnary[pilar][var]
                                    pilar_weight = self.complete_dictionnary[pilar]
                                    final_pilar_value =pilar_value*pilar_weight
                                    col = pilar_color_dictionnary[pilar]

                                    if pilar not in final_pilar_dictionnary and final_pilar_value!=0:
                                        final_pilar_dictionnary[pilar] = final_pilar_value
                                    plt.bar(str("Variante "+str(var+1)),final_pilar_value,0.1, color = col, bottom=previous_pilar_value)
                                    previous_pilar_value = previous_pilar_value+final_pilar_value

                        plt.ylabel("Scores")
                        handles = []
                        for pil in pilar_color_dictionnary:
                            if pil in final_pilar_dictionnary:
                                    handle = mpatches.Patch(color=pilar_color_dictionnary[pil], label=pil)
                                    handles.append(handle)
                        plt.legend(handles= handles)
                        plt.savefig("Pilar_plot.png",bbox_inches = "tight")

                    else:
                        for pilar in self.pilar_dictionnary:
                                plt.clf()
                                final_crit_dictionnary[pilar] = {}
                                # To stack up variables in the bars
                                previous_crit_value = 0
                                num_crit = 0
                                for crit in self.criteria_dictionnary:
                                    crit_parent = self.t.search_nodes(name=crit)[0].up.name
                                    if crit_parent == pilar:
                                        num_crit = num_crit+1

                                        crit_value = self.criteria_dictionnary[crit][0]
                                        crit_weight = self.complete_dictionnary[crit]
                                        final_crit_value = crit_value*crit_weight

                                        if crit not in final_crit_dictionnary and final_crit_value!=0:
                                            final_crit_dictionnary[pilar][crit] = final_crit_value

                                        col = criteria_color_dictionnary[crit]
                                        plt.bar("Variant 1",final_crit_value,0.1, color = col, bottom=previous_crit_value)

                                        previous_crit_value = previous_crit_value+final_crit_value

                                plt.ylabel("Scores")
                                handles = []
                                for crit in criteria_color_dictionnary:
                                    if crit in final_crit_dictionnary[pilar]:
                                        handle = mpatches.Patch(color=criteria_color_dictionnary[crit], label=crit)
                                        handles.append(handle)
                                plt.legend(handles= handles)
                                plt.xticks([-1,0,1])
                                Criteria_plot = "Criteria_plot"+pilar+".png"
                                plt.savefig(Criteria_plot,bbox_inches = "tight")

                        self.label_text ="PILLAR VIEW - final sustainability score: "+str(self.final_value)
                        self.label.setObjectName(self.label_text)
                        #Plots indicators plots and saves them
                        plt.clf()

                        colors = ["b","g","r","c","m","y","k","w"]
                        pilar_color_dictionnary = {}
                        num_of_color = 0
                        for pilar in self.pilar_dictionnary:
                            pilar_color_dictionnary[pilar] = colors[num_of_color]
                            num_of_color = num_of_color+1

                        final_pilar_dictionnary = {}
                        previous_pilar_value = 0
                        for pilar in self.pilar_dictionnary:
                            # For each variant, we reset the number of the color, so that we have a color associated to a
                            # criteria, and criterias are the same between variants
                            # To stack up variables in the bars
                            pilar_value = self.pilar_dictionnary[pilar][0]
                            pilar_weight = self.complete_dictionnary[pilar]
                            final_pilar_value =pilar_value*pilar_weight
                            col = pilar_color_dictionnary[pilar]

                            if pilar not in final_pilar_dictionnary and final_pilar_value!=0:
                                final_pilar_dictionnary[pilar] = final_pilar_value
                                plt.bar("Variant 1",final_pilar_value,0.1, color = col, bottom=previous_pilar_value)
                                previous_pilar_value = previous_pilar_value+final_pilar_value

                        plt.ylabel("Scores")
                        handles = []
                        for pil in pilar_color_dictionnary:
                            if pil in final_pilar_dictionnary:
                                    handle = mpatches.Patch(color=pilar_color_dictionnary[pil], label=pil)
                                    handles.append(handle)
                        plt.legend(handles= handles)
                        plt.xticks([-1,0,1])
                        plt.savefig("Pilar_plot.png",bbox_inches = "tight")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_for_graph()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

##
