from PyQt5 import QtCore, QtGui, QtWidgets
import icon_yup
import requests
import re
# Import required libraries

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(337, 206)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input = QtWidgets.QLineEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(60, 100, 221, 23))
        self.input.setObjectName("input")
        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(129, 130, 91, 23))
        self.run.setObjectName("run")
        self.iconShow = QtWidgets.QLabel(self.centralwidget)
        self.iconShow.setGeometry(QtCore.QRect(70, 10, 101, 91))
        self.iconShow.setObjectName("iconShow")
        self.nameCity = QtWidgets.QLabel(self.centralwidget)
        self.nameCity.setGeometry(QtCore.QRect(160, 40, 171, 16))
        self.nameCity.setObjectName("nameCity")
        self.dama = QtWidgets.QLabel(self.centralwidget)
        self.dama.setGeometry(QtCore.QRect(160, 70, 171, 16))
        self.dama.setObjectName("dama")
        self.Error = QtWidgets.QLabel(self.centralwidget)
        self.Error.setGeometry(QtCore.QRect(240, 140, 91, 20))
        self.Error.setText("")
        self.Error.setObjectName("Error")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 337, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.t = None
        self.retranslateUi(MainWindow)
        self.run.clicked.connect(self.prossec)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def prossec(self):
        # Get the names of cities (abbreviation only the first three letters must be entered) for example: London, lon.
        nameCity = self.input.text()
        URLForFindCity = f"https://www.metaweather.com/api/location/search/?query={nameCity}"
        self.input.clear()
        '''
        URL required to send requests to API service provider "www.metaweather.com"
        Note: This request is in the source code. And in the continuation of the program, 
        to send the ID of each city and get information, it will definitely send more requests
        '''
        response = requests.get(URLForFindCity)
        convert = str(response.text)
        Woeid = re.search(":\d+", convert).group(0).replace(":", "")
        #Send a request and receive Weather information about this city
        URLWeather = f"https://www.metaweather.com/api/location/{Woeid}"
        responseFrom = requests.get(URLWeather)
        responseData = str(responseFrom.text)

        #Converting Response to Accessible Data Tip is easier with Json :)
        dataweather = responseData.split(",")
        dataTemp = dict()
        for i in range(0 , len(dataweather)):
            splity = dataweather[i].split(":")
            if len(splity) <= 1:
                continue
            dataTemp[splity[0]] = splity[1]

        # output Weather Data
        y = dataTemp['"min_temp"']
        s = dataTemp['"wind_speed"']
        t = dataTemp['"weather_state_name"']
        print(self.t)
        if t == '"Snow"':
            self.iconShow.setText("<html><head/><body><p><img src=\":/icon/PNG/sn.png\"/></p></body></html>")
        elif t =='"Sleet"':
            self.iconShow.setText("<html><head/><body><p><img src=\":/icon/PNG/h.png\"/></p></body></html>")
        elif t =='"Hail"':
            self.iconShow.setText("<html><head/><body><p><img src=\":/icon/PNG/sl.png\"/></p></body></html>")
        elif t =='"Thunderstorm"':
            self.iconShow.setText("<html><head/><body><p><img src=\":/icon/PNG/t.png\"/></p></body></html>")
        elif t =='"Heavy Rain"':
            self.iconShow.setText("<html><head/><body><p><img src=\":/icon/PNG/hr.png\"/></p></body></html>")
        elif t =='"Light Rain"':
            self.iconShow.setText("<html><head/><body><p><img src=\":/icon/PNG/lr.png\"/></p></body></html>")
        elif t =='"Showers"':
            self.iconShow.setText("<html><head/><body><p><img src=\":/icon/PNG/s.png\"/></p></body></html>")
        elif t =='"Heavy Cloud"':
            self.iconShow.setText("<html><head/><body><p><img src=\":/icon/PNG/hc.png\"/></p></body></html>")
        elif t =='"Light Cloud"':
            self.iconShow.setText("<html><head/><body><p><img src=\":/icon/PNG/lc.png\"/></p></body></html>")
        elif t =='"Clear"':
            self.iconShow.setText("<html><head/><body><p><img src=\":/icon/PNG/c.png\"/></p></body></html>")
        p = dataTemp['"timezone"']
        newTimezone = p.replace('}','')
        self.dama.setText(f"{y}'C")
        self.nameCity.setText(f"City : {newTimezone}")
        



    ## <html><head/><body><p><img src=":/icon/PNG/t.png"/></p></body></html>
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.input.setPlaceholderText(_translate("MainWindow", "Please Enter name city."))
        self.run.setText(_translate("MainWindow", "Show"))
        self.nameCity.setText(_translate("MainWindow", "None"))
        self.dama.setText(_translate("MainWindow", "0 \'C"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
