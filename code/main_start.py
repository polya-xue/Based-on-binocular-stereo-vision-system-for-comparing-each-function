
from PyQt5 import QtCore, QtGui, QtWidgets  # 调用qt5制作界面
import cv2
import SIFT
import SURF
import SIFT_match
import SURF_match
import BM

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(843, 200)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.CamsgroupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.CamsgroupBox.setEnabled(True)
        self.CamsgroupBox.setGeometry(QtCore.QRect(10, 40, 821, 81))
        self.CamsgroupBox.setObjectName("CamsgroupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.CamsgroupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, 10, 821, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)


        self.SIFT = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.SIFT.setEnabled(True)
        self.SIFT.setObjectName("SIFT")
        self.horizontalLayout.addWidget(self.SIFT)
        self.SURF = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.SURF.setObjectName("SURF")
        self.horizontalLayout.addWidget(self.SURF)
        self.SIFT_match = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.SIFT_match.setObjectName("SIFTMatch")
        self.horizontalLayout.addWidget(self.SIFT_match)
        self.SURF_match = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.SURF_match.setObjectName("SURFMatch")
        self.horizontalLayout.addWidget(self.SURF_match)
        self.BM = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.BM.setObjectName("BM")
        self.horizontalLayout.addWidget(self.BM)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 843, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CamsgroupBox.setTitle(_translate("MainWindow", "双相机操作"))
        self.SIFT.setText(_translate("MainWindow", "特征提取SIFT"))
        self.SURF.setText(_translate("MainWindow", "特征提取SURF"))
        self.SIFT_match.setText(_translate("MainWindow", "SIFT立体匹配BF+FLANN"))
        self.SURF_match.setText(_translate("MainWindow", "SURF立体匹配BF+FLANN"))
        self.BM.setText(_translate("MainWindow", "双目测距BM"))

        # self.actionqidongxiangji.setText(_translate("MainWindow", "OpenCamera"))
        # self.actionCloseCamera.setText(_translate("MainWindow", "CloseCamera"))
        # self.actionTestCamera.setText(_translate("MainWindow", "TestCamera"))

        # 信号槽事件
        self.SIFT.clicked.connect(self.SIFT_Alg)
        self.SURF.clicked.connect(self.SURF_Alg)
        self.SIFT_match.clicked.connect(self.SIFT_match_Alg)
        self.SURF_match.clicked.connect(self.SURF_match_Alg)
        self.BM.clicked.connect(self.BM_Alg)

    # 点击启动SIFT算法，计算出特征点
    def SIFT_Alg(self):
        SIFT.start_SIFT()

    # 点击启动SURF算法，计算出特征点
    def SURF_Alg(self):
        SURF.start_SURF()

    #
    def SIFT_match_Alg(self):
        SIFT_match.start_SIFTmatch()

    #
    def SURF_match_Alg(self):
        SURF_match.start_SURFmatch()

    #
    def BM_Alg(self):
        bm = BM.Callback()
        bm.callbackForBM()

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())