import os
import sys
import numpy
import cv2
import glob

import json

from pathlib import Path

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



        self.folder_model = QStandardItemModel()
        self.listView.setModel(self.folder_model)
        self.listView.selectionModel().selectionChanged.connect(self.on_list_item_selection_changed)
        self.listView.selectionModel().selectionChanged.connect(self.image_viewer)

    def testclick(self):
        global folder
        folder = QFileDialog.getExistingDirectory(self, "Select Directory")
import os
import sys
import numpy
import cv2
import glob

import json

from pathlib import Path

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



        self.folder_model = QStandardItemModel()
        self.listView.setModel(self.folder_model)
        self.listView.selectionModel().selectionChanged.connect(self.on_list_item_selection_changed)
        self.listView.selectionModel().selectionChanged.connect(self.image_viewer)

    def testclick(self):
        global folder
        folder = QFileDialog.getExistingDirectory(self, "Select Directory")
        
    def list_update(self):
        global meta_map_list
        pathlist = []
        file_name = []

        self.folder_model.clear()

        meta_map = {}
        for p in Path(folder, 'meta').rglob('*.json'):
            with open(p, 'r', encoding='utf-8') as f:
                meta = json.load(f)
            meta_map[meta['data_key']] = meta['label_path'][0]
        meta_map_list=sorted(list(meta_map.keys()))

        for i in range(len(meta_map_list)):
            self.folder_model.appendRow(QStandardItem(meta_map_list[i]))

      
        self.listView.setModel(self.folder_model)

    def image_viewer(self):
        self.qPixmapVar = QPixmap()
        self.qPixmapVar.load('images/'+selected_item_text)
        self.qPixmapVar = self.qPixmapVar.scaledToWidth(600)
        self.label_1.setPixmap(self.qPixmapVar)
    
        target = selected_item_text.split('/')
        for i, camera in enumerate(['front_left_backward', 'front_right_forward', 'front_right_backward', 'front_center_forward', 'front_left_forward']):
            camera_target = target.copy()
            camera_target[-3] = 'camera_' + camera + '_fov100'
            camera_target = '/'.join(camera_target)
            qPixmapVar = QPixmap()
            qPixmapVar.load('images/'+camera_target)
            qPixmapVar = qPixmapVar.scaledToWidth(600)
            label = self.__getattribute__('label_' + str(i+2))
            label.setPixmap(qPixmapVar)

    def on_list_item_selection_changed(self):
        global selected_item_text 
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
#meta map-> key sort 하여 list view에 경로 띄우기, list view 이동시 label에 경로 이
#label 추가 및 같은 파일명 한단계위 상위폴더 탐색하여 띄우기 기능 추가 todo
#순회
