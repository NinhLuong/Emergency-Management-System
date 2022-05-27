def weather(self):
        api_address='https://api.openweathermap.org/data/2.5/weather?lat=10.850145464871641&lon=106.7716601973813&appid=d80948795e2ec6257f1f62303cf81808&lang=vi'
        json_data = requests.get(api_address).json()
        format_add = json_data['main']

        T_weather = """<html><head/><body><p><span style=" font-size:18pt; color:#ff0808;">{VALUE}</span><span style=" font-size:18pt; color:#ff0808; vertical-align:super;">0</span><span style=" font-size:18pt; color:#ff0808;">C</span></p></body></html>"""
        Value_1 = str(int(format_add["temp"]-273))

        new_T_Weather = T_weather.replace("{VALUE}",Value_1)
        self.T_Weather_label.setText(new_T_Weather)

        # rem = json_data['main']['humidity']
        # ram = json_data['weather'][0]['description']
        print(json_data["weather"][0]["icon"])

        if json_data['weather'][0]['icon'] == '04d':
            icon10 = QtGui.QIcon()
            icon10.addPixmap(QtGui.QPixmap("../image/nhieu_may-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton_3.setIcon(icon10)


        elif json_data['weather'][0]['main'] == 'rain':
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/Weather/animated/rainy-7.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton_3.setIcon(icon)

        elif json_data['weather'][0]['main'] == 'Thunderstorm':
            text = """<html><head/><body><p><span style=" font-size:16pt; color:#3b3b3b;">{VALUE}</span></p></body></html>"""
            new_text = text.replace("{VALUE}",str("sét đánh chết mẹ m"))
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/Weather/animated/thunder.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton_3.setIcon(icon)
            self.label_text_weather.setText(new_text)


    self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 10, 61, 61))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("image: url(:/images/images/images/114.png);\n"
"border: 3px solid rgb(255, 255, 255);\n"
"border-radius: 29px;")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")