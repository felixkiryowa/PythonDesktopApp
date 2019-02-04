from  PyQt5.QtCore import  (
 Qt, QTime, QDateTime, QDate
)

datetime = QDateTime.currentDateTime()
print(datetime)
print(datetime.toString())
print(datetime.toString(Qt.ISODate))
print(datetime.toString(Qt.DefaultLocaleLongDate))
print(datetime.toUTC().toString())

date = QDate.currentDate()
print(date.toString())
print(date.toString(Qt.ISODate))
print(date.toString(Qt.DefaultLocaleLongDate))

time = QTime.currentTime()
print(time.toString())
print(time.toString(Qt.ISODate))
print(time.toString(Qt.DefaultLocaleLongDate))