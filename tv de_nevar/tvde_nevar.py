from PyQt5.QtWidgets import QGridLayout,QPushButton,QApplication,QWidget,QHBoxLayout,QVBoxLayout,QLabel,QLayout,QLineEdit,QTextEdit
from PyQt5 import QtGui
import sys
import chanel
from datetime import datetime
import urllib3


class tv(QWidget):
    def __init__(self):
        super().__init__()
        aylar = {1:"ocak",2:"şubat",3:"mart",4:"nisan",5:"mayıs",6:"haziran",7:"temmuz",8:"ağustos",9:"eylül",10:"ekim",11:"kasım",12:"aralık"}
        days = {0:"Pazartesi",1:"Salı",2:"Çarşamba",3:"Perşembe",4:"Cuma",5:"Cumartesi",6:"Pazar"}

        self.today = str(datetime.now().day)+"  "+str(aylar[datetime.now().month]+" "+str(days[datetime.today().weekday()]))
        self.ekstra()
        
    def ekstra(self):
        
        self.setWindowTitle("                                  "+"TV de Ne var")
        self.setWindowIcon(QtGui.QIcon("tv.jpg"))
        self.textedit = QTextEdit()
        self.d_max = QPushButton("Dmax")
        self.kanal_d = QPushButton("Kanal d")
        self.show_tv = QPushButton("show")
        self.star_tv = QPushButton("star")
        self.trt1_tv = QPushButton("trt 1")
        self.label = QLabel(self.today)
        self.font = QtGui.QFont()
        self.font.setPointSize(15)
        self.label.setFont(self.font)



        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        gbox = QGridLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.d_max)
        vbox.addWidget(self.kanal_d)
        vbox.addWidget(self.show_tv)
        vbox.addWidget(self.star_tv)
        vbox.addWidget(self.trt1_tv)
        vbox.addStretch()
        hbox.addLayout(vbox)
        hbox.addStretch()
        hbox.addWidget(self.textedit)
        self.setLayout(hbox)
        self.setFixedSize(500,500)
        self.d_max.clicked.connect(self.max)
        self.kanal_d.clicked.connect(self.kanal_d1)
        self.show_tv.clicked.connect(self.show_1)
        self.star_tv.clicked.connect(self.star_1)
        self.trt1_tv.clicked.connect(self.trt_1)

        self.show()
        self.font1 = QtGui.QFont()
        self.font1.setPointSize(8)
        try:
            self.Dmax = chanel.Dmax()
            self.Kanald = chanel.Kanald()
            self.Show = chanel.show()
            self.Star = chanel.star()
            self.Trt1 = chanel.trt1()
        except:
            self.textedit.setText("internet yok")

        
    def max(self):

        self.textedit.setText("----------------Dmax----------------"+"\n"+str(self.Dmax.progams()))
        self.textedit.setFont(self.font1)
    def kanal_d1(self):
        self.textedit.setText("----------------Kanald----------------"+"\n"+str(self.Kanald.progams()))
        self.textedit.setFont(self.font1)
    def show_1(self):
        self.textedit.setText("----------------Show Tv----------------"+"\n"+str(self.Show.progams()))
        self.textedit.setFont(self.font1)
    def star_1(self):
        self.textedit.setText("----------------Star Tv----------------"+"\n"+str(self.Star.progams()))
        self.textedit.setFont(self.font1)
    def trt_1(self):
        self.textedit.setText("----------------Trt1----------------"+"\n"+str(self.Trt1.progams()))
        self.textedit.setFont(self.font1)






        
        
        
        
        
        
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tv  = tv()
    sys.exit(app.exec_())       
