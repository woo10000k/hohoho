import os
import sys
import numpy
import cv2
import glob

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
from PyQt5 import uic


form = 'test.ui'
form_class = uic.loadUiType(form)[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_test.clicked.connect(self.list_update)
        self.btn_test.clicked.connect(self.image_viewer)


        self.model = QStandardItemModel()
        self.listView.setModel(self.model)
        self.listView.selectionModel().selectionChanged.connect(self.on_list_item_selection_changed)

    def testclick(self):
        global folder
        folder = QFileDialog.getExistingDirectory(self, "Select Directory")
        
    def list_update(self):
        pathlist = []
        file_name = []
        folder_list = folder+"/meta/"
        folder_model = QStandardItemModel()
        for (folder_list, dir, file) in os.walk(folder_list):
            if len(file) != 0:
                file = sorted(file)
                for i in range(len(file)):
                    pathlist.append(folder_list + "/" + file[i])
                    folder_model.appendRow(QStandardItem(str(i+1)+"."+file[i]))

        for k in range(len(pathlist)):
            file_name = pathlist[k]        
        self.listView.setModel(folder_model)

    def image_viewer(self):
        self.qPixmapVar = QPixmap()
        self.qPixmapVar.load('test/SCENE-N-0002_FRAME_000000.png')
        self.qPixmapVar = self.qPixmapVar.scaledToWidth(600)
        self.label.setPixmap(self.qPixmapVar)

    def on_list_item_selection_changed(self):
        selected_item_text = self.get_selected_item_text()
        print("Selected item text: ", selected_item_text)

    def get_selected_item_text(self):
        selected_indexes = self.listView.selectedIndexes()
        if selected_indexes:
            return selected_indexes[0].data()
        else:
            return None   


#    def list_viewer(self):
        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
#    imageViewer = ImageViewer()
#    imageViewer.show()
    app.exec_()
  
#2.20 button click, directory 선택, meta 들어가서 json filelist list view에 뿌려주기
#label 에 image sample 띄우기
#list view with gpt
