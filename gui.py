# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F1_2022_standings.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from main import list_of_pilots
import matplotlib.pyplot as plt


class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(895, 840)
                MainWindow.setMinimumSize(QtCore.QSize(895, 840))
                MainWindow.setMaximumSize(QtCore.QSize(895, 840))
                MainWindow.setMouseTracking(True)
                MainWindow.setStyleSheet("background: rgb(45,45,68);")
                MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")

                #label for image
                self.label_image = QtWidgets.QLabel(self.centralwidget)
                self.label_image.setGeometry(QtCore.QRect(10, 10, 551, 821))
                self.label_image.setAcceptDrops(True)
                self.label_image.setStyleSheet("width: auto;\n height: auto;\n")
                self.label_image.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.label_image.setLineWidth(0)
                self.label_image.setText("")
                self.label_image.setPixmap(QtGui.QPixmap("assets/453be7bf305ba1db8a5af5df8134bd27.jpg"))
                self.label_image.setScaledContents(True)
                self.label_image.setWordWrap(True)
                self.label_image.setObjectName("label_image")


                #buttons
                """
                self.pushButtonOvertakeSimulator = QtWidgets.QPushButton(self.centralwidget)
                self.pushButtonOvertakeSimulator.setGeometry(QtCore.QRect(170, 700, 231, 71))
                self.pushButtonOvertakeSimulator.setStyleSheet("background-color: rgb(48,48,63);\n"
                                                                "color: white;\n"
                                                                "border-radius: 5px;\n"
                                                                "padding: 10px 20px;\n"
                                                                "font-size: 16px;\n"
                                                                "font-weight: bold;\n"
                                                                "cursor: pointer;\n")
                self.pushButtonOvertakeSimulator.setObjectName("pushButtonOvertakeSimulator")
                """

                self.pushButtonConstructor = QtWidgets.QPushButton(self.centralwidget)
                self.pushButtonConstructor.setGeometry(QtCore.QRect(170, 600, 231, 71))
                self.pushButtonConstructor.setStyleSheet("background-color: rgb(48,48,63);\n"
                                                        "color: white;\n"
                                                        "border-radius: 5px;\n"
                                                        "padding: 10px 20px;\n"
                                                        "font-size: 12px;\n"
                                                        "font-weight: bold;\n"
                                                        "cursor: pointer;\n""")
                self.pushButtonConstructor.setObjectName("pushButtonConstructor")

                self.pushButtonChampion = QtWidgets.QPushButton(self.centralwidget)
                self.pushButtonChampion.setGeometry(QtCore.QRect(170, 700, 231, 71))
                self.pushButtonChampion.setStyleSheet("background-color: rgb(48,48,63);\n"
                                                        "color: white;\n"
                                                        "border-radius: 5px;\n"
                                                        "padding: 10px 20px;\n"
                                                        "font-size: 16px;\n"
                                                        "font-weight: bold;\n"
                                                        "cursor: pointer;\n")
                self.pushButtonChampion.setObjectName("pushButtonChampion")

                self.pushButtonSearch = QtWidgets.QPushButton(self.centralwidget)
                self.pushButtonSearch.setGeometry(QtCore.QRect(740, 30, 131, 31))
                self.pushButtonSearch.setStyleSheet("background-color: rgb(0,0,0);\n"
                                                "color: rgb(255,255,255);\n"
                                                "border-radius: 5px;\n"
                                                "padding: 10px 20px;\n"
                                                "font-size: 12px;\n"
                                                "font-weight: bold;\n"
                                                "cursor: pointer;\n")
                self.pushButtonSearch.setObjectName("pushButtonSearch")


                #combo box
                self.comboBox = QtWidgets.QComboBox(self.centralwidget)
                self.comboBox.setGeometry(QtCore.QRect(590, 30, 131, 31))
                self.comboBox.setStyleSheet("color: rgb(255,255,255);\n font: center;\n")
                self.comboBox.setObjectName("comboBox")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.addItem("")


                #labels
                self.label_title = QtWidgets.QLabel(self.centralwidget)
                self.label_title.setGeometry(QtCore.QRect(20, 50, 541, 101))
                self.label_title.setStyleSheet("background-color: transparent;\n"
                                                "font: 30px;\n"
                                                "color: rgb(255,255,255);\n")
                self.label_title.setAlignment(QtCore.Qt.AlignCenter)
                self.label_title.setObjectName("label_title")


                self.label_introduction = QtWidgets.QLabel(self.centralwidget)
                self.label_introduction.setGeometry(QtCore.QRect(20, 160, 541, 191))
                self.label_introduction.setStyleSheet("background-color: transparent;\nfont-size: 12px;\n color: rgb(255,255,255);\n")
                self.label_introduction.setAlignment(QtCore.Qt.AlignCenter)
                self.label_introduction.setObjectName("label_introduction")


                self.label_name = QtWidgets.QLabel(self.centralwidget)
                self.label_name.setGeometry(QtCore.QRect(590, 100, 291, 21))
                self.label_name.setStyleSheet("background-color: transparent;\nfont-size: 15px;\n color: rgb(255,255,255);\n")
                self.label_name.setObjectName("label_name")


                self.label_Win = QtWidgets.QLabel(self.centralwidget)
                self.label_Win.setGeometry(QtCore.QRect(590, 190, 291, 21))
                self.label_Win.setStyleSheet("background-color: transparent;\nfont-size: 15px;\n color: rgb(255,255,255);\n")
                self.label_Win.setObjectName("label_Win")


                self.label_Win_loc = QtWidgets.QLabel(self.centralwidget)
                self.label_Win_loc.setGeometry(QtCore.QRect(590, 240, 291, 21))
                self.label_Win_loc.setStyleSheet("background-color: transparent;\nfont-size: 15px;\n color: rgb(255,255,255);\n")
                self.label_Win_loc.setObjectName("label_Win_loc")


                self.label_DNF = QtWidgets.QLabel(self.centralwidget)
                self.label_DNF.setGeometry(QtCore.QRect(590, 510, 291, 21))
                self.label_DNF.setStyleSheet("background-color: transparent;\nfont-size: 15px;\n color: rgb(255,255,255);\n")
                self.label_DNF.setObjectName("label_DNF")


                self.label_DNF_loc = QtWidgets.QLabel(self.centralwidget)
                self.label_DNF_loc.setGeometry(QtCore.QRect(590, 550, 291, 21))
                self.label_DNF_loc.setStyleSheet("background-color: transparent;\nfont-size: 15px;\n color: rgb(255,255,255);\n")
                self.label_DNF_loc.setObjectName("label_DNF_loc")


                self.label_team = QtWidgets.QLabel(self.centralwidget)
                self.label_team.setGeometry(QtCore.QRect(590, 140, 291, 21))
                self.label_team.setStyleSheet("background-color: transparent;\nfont-size: 15px;\n color: rgb(255,255,255);\n")
                self.label_team.setObjectName("label_team")


                self.label_Win_list = QtWidgets.QLabel(self.centralwidget)
                self.label_Win_list.setGeometry(QtCore.QRect(600, 270, 281, 211))
                self.label_Win_list.setStyleSheet("background-color: transparent;\n font-size: 11px;\n color: rgb(255,255,255);\n")
                self.label_Win_list.setAlignment(QtCore.Qt.AlignCenter)
                self.label_Win_list.setObjectName("label_Win_list")


                self.label_DNF_list = QtWidgets.QLabel(self.centralwidget)
                self.label_DNF_list.setGeometry(QtCore.QRect(600, 580, 281, 211))
                self.label_DNF_list.setStyleSheet("background-color: transparent;\n font-size: 13px;\n color: rgb(255,255,255);\n")
                self.label_DNF_list.setAlignment(QtCore.Qt.AlignCenter)
                self.label_DNF_list.setObjectName("label_DNF_list")

                self.pushButtonSearch.clicked.connect(self.search_pressed)
                self.pushButtonChampion.clicked.connect(lambda: self.draw_champ())
                self.pushButtonConstructor.clicked.connect(lambda: self.draw_constructor())

                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)


        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "F1 2022 Standings"))
                #self.pushButtonOvertakeSimulator.setText(_translate("MainWindow", "Overtake Simulator"))
                self.pushButtonConstructor.setText(_translate("MainWindow", "2022 Constructor Champion"))
                self.pushButtonChampion.setText(_translate("MainWindow", "2022 World Champion"))
                self.pushButtonSearch.setText(_translate("MainWindow", "Search"))

                self.comboBox.setItemText(0, _translate("MainWindow", "-pilots-"))
                self.comboBox.setItemText(1, _translate("MainWindow", "Hamilton"))
                self.comboBox.setItemText(2, _translate("MainWindow", "Leclerc"))
                self.comboBox.setItemText(3, _translate("MainWindow", "Sainz"))
                self.comboBox.setItemText(4, _translate("MainWindow", "Verstappen"))
                self.comboBox.setItemText(5, _translate("MainWindow", "Russell"))
                self.comboBox.setItemText(6, _translate("MainWindow", "Ocon"))
                self.comboBox.setItemText(7, _translate("MainWindow", "Gasly"))
                self.comboBox.setItemText(8, _translate("MainWindow", "Ricciardo"))
                self.comboBox.setItemText(9, _translate("MainWindow", "Norris"))
                self.comboBox.setItemText(10, _translate("MainWindow", "Bottas"))
                self.comboBox.setItemText(11, _translate("MainWindow", "Zhou"))
                self.comboBox.setItemText(12, _translate("MainWindow", "Stroll"))
                self.comboBox.setItemText(13, _translate("MainWindow", "Alonso"))
                self.comboBox.setItemText(14, _translate("MainWindow", "Magnussen"))
                self.comboBox.setItemText(15, _translate("MainWindow", "Schumacher"))
                self.comboBox.setItemText(16, _translate("MainWindow", "Tsunoda"))
                self.comboBox.setItemText(17, _translate("MainWindow", "Albon"))
                self.comboBox.setItemText(18, _translate("MainWindow", "Latifi"))
                self.comboBox.setItemText(19, _translate("MainWindow", "Vettel"))
                self.comboBox.setItemText(20, _translate("MainWindow", "Perez"))
                self.label_title.setText(_translate("MainWindow", "F1 2022 season\n""-standings-"))
                self.label_introduction.setText(_translate("MainWindow", "Formula One (also known as Formula 1 or F1) is the highest class of international racing\n"
                                                        " for open-wheel single-seater racing cars\n" 
                                                        "sanctioned by the Fédération Internationale de l'Automobile (FIA).\n" 
                                                        "The World Drivers' Championship, which became the FIA Formula One World Championship in 1981\n"
                                                        "has been one of the premier forms of racing around the world since its inaugural season in 1950.\n"
                                                        "This is a piece of software that is ment\n"
                                                                "for who is new to this sport.\n"
                                                        "It provides you with the results of last F1 season, \n"
                                                        "that had 22 races and took place in 19 different countries. \n"
                                                        "Enjoy!"))
                self.label_name.setText(_translate("MainWindow", "Full name:"))
                self.label_Win.setText(_translate("MainWindow", "Season Wins:"))
                self.label_Win_loc.setText(_translate("MainWindow", "Win Locations:"))
                self.label_DNF.setText(_translate("MainWindow", "Seasson DNFs: "))
                self.label_DNF_loc.setText(_translate("MainWindow", "DNF Locations:"))
                self.label_team.setText(_translate("MainWindow", "Team:"))

        #eveniment asociat butonului de afisare a pilotilor campioni
        def search_pressed(self):
                if(self.comboBox.currentText() == "Hamilton"):
                        self.label_name.setText("Full name: " + list_of_pilots[0].get_name())
                        self.label_team.setText("Team: " + list_of_pilots[0].get_team())
                        self.label_Win.setText("Season Wins: " + str(list_of_pilots[0].get_season_wins()))
                        string_aux = ""
                        for index in list_of_pilots[0].get_win_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_Win_list.setText(string_aux)
                        self.label_DNF.setText("Season DNFs: " + str(list_of_pilots[0].get_season_DNF()))
                        string_aux = ""
                        for index in list_of_pilots[0].get_DNF_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_DNF_list.setText(string_aux)

                if(self.comboBox.currentText() == "Russell"):
                        self.label_name.setText("Full name: " + list_of_pilots[1].get_name())
                        self.label_team.setText("Team: " + list_of_pilots[1].get_team())
                        self.label_Win.setText("Season Wins: " + str(list_of_pilots[1].get_season_wins()))
                        string_aux = ""
                        for index in list_of_pilots[1].get_win_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_Win_list.setText(string_aux)
                        self.label_DNF.setText("Season DNFs: " + str(list_of_pilots[1].get_season_DNF()))
                        string_aux = ""
                        for index in list_of_pilots[1].get_DNF_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_DNF_list.setText(string_aux)

                if(self.comboBox.currentText() == "Verstappen"):
                        self.label_name.setText("Full name: " + list_of_pilots[2].get_name())
                        self.label_team.setText("Team: " + list_of_pilots[2].get_team())
                        self.label_Win.setText("Season Wins: " + str(list_of_pilots[2].get_season_wins()))
                        string_aux = ""
                        for index in list_of_pilots[2].get_win_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_Win_list.setText(string_aux)
                        self.label_DNF.setText("Season DNFs: " + str(list_of_pilots[2].get_season_DNF()))
                        string_aux = ""
                        for index in list_of_pilots[2].get_DNF_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_DNF_list.setText(string_aux)

                if(self.comboBox.currentText() == "Perez"):
                        self.label_name.setText("Full name: " + list_of_pilots[3].get_name())
                        self.label_team.setText("Team: " + list_of_pilots[3].get_team())
                        self.label_Win.setText("Season Wins: " + str(list_of_pilots[3].get_season_wins()))
                        string_aux = ""
                        for index in list_of_pilots[3].get_win_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_Win_list.setText(string_aux)
                        self.label_DNF.setText("Season DNFs: " + str(list_of_pilots[3].get_season_DNF()))
                        string_aux = ""
                        for index in list_of_pilots[3].get_DNF_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_DNF_list.setText(string_aux)

                if(self.comboBox.currentText() == "Leclerc"):
                        self.label_name.setText("Full name: " + list_of_pilots[4].get_name())
                        self.label_team.setText("Team: " + list_of_pilots[4].get_team())
                        self.label_Win.setText("Season Wins: " + str(list_of_pilots[4].get_season_wins()))
                        string_aux = ""
                        for index in list_of_pilots[4].get_win_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_Win_list.setText(string_aux)
                        self.label_DNF.setText("Season DNFs: " + str(list_of_pilots[4].get_season_DNF()))
                        string_aux = ""
                        for index in list_of_pilots[4].get_DNF_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_DNF_list.setText(string_aux)

                if(self.comboBox.currentText() == "Sainz"):
                        self.label_name.setText("Full name: " + list_of_pilots[5].get_name())
                        self.label_team.setText("Team: " + list_of_pilots[5].get_team())
                        self.label_Win.setText("Season Wins: " + str(list_of_pilots[5].get_season_wins()))
                        string_aux = ""
                        for index in list_of_pilots[5].get_win_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_Win_list.setText(string_aux)
                        self.label_DNF.setText("Season DNFs: " + str(list_of_pilots[5].get_season_DNF()))
                        string_aux = ""
                        for index in list_of_pilots[5].get_DNF_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_DNF_list.setText(string_aux)

                if(self.comboBox.currentText() == "Gasly"):
                        self.label_name.setText("Full name: " + list_of_pilots[6].get_name())
                        self.label_team.setText("Team: " + list_of_pilots[6].get_team())
                        self.label_Win.setText("Season Wins: " + str(list_of_pilots[6].get_season_wins()))
                        string_aux = ""
                        for index in list_of_pilots[6].get_win_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_Win_list.setText(string_aux)
                        self.label_DNF.setText("Season DNFs: " + str(list_of_pilots[6].get_season_DNF()))
                        string_aux = ""
                        for index in list_of_pilots[6].get_DNF_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_DNF_list.setText(string_aux)

                if(self.comboBox.currentText() == "Tsunoda"):
                        self.label_name.setText("Full name: " + list_of_pilots[7].get_name())
                        self.label_team.setText("Team: " + list_of_pilots[7].get_team())
                        self.label_Win.setText("Season Wins: " + str(list_of_pilots[7].get_season_wins()))
                        string_aux = ""
                        for index in list_of_pilots[7].get_win_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_Win_list.setText(string_aux)
                        self.label_DNF.setText("Season DNFs: " + str(list_of_pilots[7].get_season_DNF()))
                        string_aux = ""
                        for index in list_of_pilots[7].get_DNF_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_DNF_list.setText(string_aux)

                if(self.comboBox.currentText() == "Bottas"):
                        self.label_name.setText("Full name: " + list_of_pilots[8].get_name())
                        self.label_team.setText("Team: " + list_of_pilots[8].get_team())
                        self.label_Win.setText("Season Wins: " + str(list_of_pilots[8].get_season_wins()))
                        string_aux = ""
                        for index in list_of_pilots[8].get_win_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_Win_list.setText(string_aux)
                        self.label_DNF.setText("Season DNFs: " + str(list_of_pilots[8].get_season_DNF()))
                        string_aux = ""
                        for index in list_of_pilots[8].get_DNF_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_DNF_list.setText(string_aux)

                if(self.comboBox.currentText() == "Guanyu"):
                        self.label_name.setText("Full name: " + list_of_pilots[9].get_name())
                        self.label_team.setText("Team: " + list_of_pilots[9].get_team())
                        self.label_Win.setText("Season Wins: " + str(list_of_pilots[9].get_season_wins()))
                        string_aux = ""
                        for index in list_of_pilots[9].get_win_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_Win_list.setText(string_aux)
                        self.label_DNF.setText("Season DNFs: " + str(list_of_pilots[9].get_season_DNF()))
                        string_aux = ""
                        for index in list_of_pilots[9].get_DNF_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_DNF_list.setText(string_aux)

                if(self.comboBox.currentText() == "Ricciardo"):
                        self.label_name.setText("Full name: " + list_of_pilots[10].get_name())
                        self.label_team.setText("Team: " + list_of_pilots[10].get_team())
                        self.label_Win.setText("Season Wins: " + str(list_of_pilots[10].get_season_wins()))
                        string_aux = ""
                        for index in list_of_pilots[10].get_win_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_Win_list.setText(string_aux)
                        self.label_DNF.setText("Season DNFs: " + str(list_of_pilots[10].get_season_DNF()))
                        string_aux = ""
                        for index in list_of_pilots[10].get_DNF_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_DNF_list.setText(string_aux)

                if(self.comboBox.currentText() == "Norris"):
                        self.label_name.setText("Full name: " + list_of_pilots[11].get_name())
                        self.label_team.setText("Team: " + list_of_pilots[11].get_team())
                        self.label_Win.setText("Season Wins: " + str(list_of_pilots[11].get_season_wins()))
                        string_aux = ""
                        for index in list_of_pilots[11].get_win_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_Win_list.setText(string_aux)
                        self.label_DNF.setText("Season DNFs: " + str(list_of_pilots[11].get_season_DNF()))
                        string_aux = ""
                        for index in list_of_pilots[11].get_DNF_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_DNF_list.setText(string_aux)

                if(self.comboBox.currentText() == "Latifi"):
                        self.label_name.setText("Full name: " + list_of_pilots[12].get_name())
                        self.label_team.setText("Team: " + list_of_pilots[12].get_team())
                        self.label_Win.setText("Season Wins: " + str(list_of_pilots[12].get_season_wins()))
                        string_aux = ""
                        for index in list_of_pilots[12].get_win_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_Win_list.setText(string_aux)
                        self.label_DNF.setText("Season DNFs: " + str(list_of_pilots[12].get_season_DNF()))
                        string_aux = ""
                        for index in list_of_pilots[12].get_DNF_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_DNF_list.setText(string_aux)

                if(self.comboBox.currentText() == "Albon"):
                        self.label_name.setText("Full name: " + list_of_pilots[13].get_name())
                        self.label_team.setText("Team: " + list_of_pilots[13].get_team())
                        self.label_Win.setText("Season Wins: " + str(list_of_pilots[13].get_season_wins()))
                        string_aux = ""
                        for index in list_of_pilots[13].get_win_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_Win_list.setText(string_aux)
                        self.label_DNF.setText("Season DNFs: " + str(list_of_pilots[13].get_season_DNF()))
                        string_aux = ""
                        for index in list_of_pilots[13].get_DNF_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_DNF_list.setText(string_aux)

                if(self.comboBox.currentText() == "Magnussen"):
                        self.label_name.setText("Full name: " + list_of_pilots[14].get_name())
                        self.label_team.setText("Team: " + list_of_pilots[14].get_team())
                        self.label_Win.setText("Season Wins: " + str(list_of_pilots[14].get_season_wins()))
                        string_aux = ""
                        for index in list_of_pilots[14].get_win_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_Win_list.setText(string_aux)
                        self.label_DNF.setText("Season DNFs: " + str(list_of_pilots[14].get_season_DNF()))
                        string_aux = ""
                        for index in list_of_pilots[14].get_DNF_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_DNF_list.setText(string_aux)

                if(self.comboBox.currentText() == "Schumacher"):
                        self.label_name.setText("Full name: " + list_of_pilots[15].get_name())
                        self.label_team.setText("Team: " + list_of_pilots[15].get_team())
                        self.label_Win.setText("Season Wins: " + str(list_of_pilots[15].get_season_wins()))
                        string_aux = ""
                        for index in list_of_pilots[15].get_win_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_Win_list.setText(string_aux)
                        self.label_DNF.setText("Season DNFs: " + str(list_of_pilots[15].get_season_DNF()))
                        string_aux = ""
                        for index in list_of_pilots[15].get_DNF_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_DNF_list.setText(string_aux)

                if(self.comboBox.currentText() == "Stroll"):
                        self.label_name.setText("Full name: " + list_of_pilots[16].get_name())
                        self.label_team.setText("Team: " + list_of_pilots[16].get_team())
                        self.label_Win.setText("Season Wins: " + str(list_of_pilots[16].get_season_wins()))
                        string_aux = ""
                        for index in list_of_pilots[16].get_win_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_Win_list.setText(string_aux)
                        self.label_DNF.setText("Season DNFs: " + str(list_of_pilots[16].get_season_DNF()))
                        string_aux = ""
                        for index in list_of_pilots[16].get_DNF_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_DNF_list.setText(string_aux)

                if(self.comboBox.currentText() == "Vettel"):
                        self.label_name.setText("Full name: " + list_of_pilots[17].get_name())
                        self.label_team.setText("Team: " + list_of_pilots[17].get_team())
                        self.label_Win.setText("Season Wins: " + str(list_of_pilots[17].get_season_wins()))
                        string_aux = ""
                        for index in list_of_pilots[17].get_win_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_Win_list.setText(string_aux)
                        self.label_DNF.setText("Season DNFs: " + str(list_of_pilots[17].get_season_DNF()))
                        string_aux = ""
                        for index in list_of_pilots[17].get_DNF_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_DNF_list.setText(string_aux)

                if(self.comboBox.currentText() == "Alonso"):
                        self.label_name.setText("Full name: " + list_of_pilots[18].get_name())
                        self.label_team.setText("Team: " + list_of_pilots[18].get_team())
                        self.label_Win.setText("Season Wins: " + str(list_of_pilots[18].get_season_wins()))
                        string_aux = ""
                        for index in list_of_pilots[18].get_win_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_Win_list.setText(string_aux)
                        self.label_DNF.setText("Season DNFs: " + str(list_of_pilots[18].get_season_DNF()))
                        string_aux = ""
                        for index in list_of_pilots[18].get_DNF_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_DNF_list.setText(string_aux)

                if(self.comboBox.currentText() == "Ocon"):
                        self.label_name.setText("Full name: " + list_of_pilots[19].get_name())
                        self.label_team.setText("Team: " + list_of_pilots[19].get_team())
                        self.label_Win.setText("Season Wins: " + str(list_of_pilots[19].get_season_wins()))
                        string_aux = ""
                        for index in list_of_pilots[19].get_win_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_Win_list.setText(string_aux)
                        self.label_DNF.setText("Season DNFs: " + str(list_of_pilots[19].get_season_DNF()))
                        string_aux = ""
                        for index in list_of_pilots[19].get_DNF_loc():
                                string_aux = string_aux + "\n" + index
                        self.label_DNF_list.setText(string_aux)

        #eveniment asociat butonului de afisare a pilotilor campioni
        def draw_champ(self):
                x_axes = []
                y_axes = []
                for x in list_of_pilots:
                        if(x.get_season_wins() != 0):
                                x_axes.append(x.get_name())
                                y_axes.append(x.get_season_wins())
                plt.figure(figsize=(10,7))
                plt.bar(x_axes, y_axes, width = 0.8, color = ['red', 'black'])
                plt.xlabel('Winning Pilots')
                plt.ylabel('No. of wins')
                plt.title("F1 2022 Championship Histogram")
                plt.show()

        #eveniment asociat butonului de afisare a echipelor castigatoare de curse in acest sezon
        def draw_constructor(self):
                x_axes = []
                y_axes = []
                aux = []
                for x in list_of_pilots:
                        if(x.get_season_wins() != 0) and (x.get_team() not in x_axes):
                                x_axes.append(x.get_team())
                                aux.append({'team': x.get_team(), 'wins': 0})
                        for i in aux:
                                if(x.get_season_wins() != 0) and (x.get_team() == i['team']):
                                        i['wins'] += x.get_season_wins()
                for i in aux:
                        y_axes.append(i['wins'])
                plt.figure(figsize=(10,7))
                plt.bar(x_axes, y_axes, width = 0.8, color = ['red'])
                plt.xlabel('Winning Teams')
                plt.ylabel('No. of wins')
                plt.title("F1 2022 Championship Histogram")
                plt.show()


if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
