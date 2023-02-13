import sys
import os
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QListWidget, QHBoxLayout
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from matplotlib import pyplot as plt

class AnnotationTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Annotation Tool')

        # Create a QWidget to hold multiple views
        self.viewWidget = QWidget(self)
        self.setCentralWidget(self.viewWidget)

        # Create a layout to display multiple views
        self.layout = QHBoxLayout(self.viewWidget)

        # Create a file list widget
        self.fileList = QListWidget(self)
        self.fileList.setFixedWidth(200)
        self.fileList.itemClicked.connect(self.loadImage)

        # Populate the file list with images in the current directory
        for file in os.listdir():
            if file.endswith('.jpg') or file.endswith('.png'):
                self.fileList.addItem(file)

        # Create a QLabel for each view
        self.label1 = QLabel(self.viewWidget)
        self.label2 = QLabel(self.viewWidget)

        # Add the file list and labels to the layout
        self.layout.addWidget(self.fileList)
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.label2)

        # Add a button to trigger annotation
        self.annotateBtn = QPushButton('Annotate', self)
        self.annotateBtn.move(0, 0)
        self.annotateBtn.clicked.connect(self.annotate)

    def loadImage(self, item):
        # Load image using OpenCV
        self.img = cv2.imread(item.text())
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)

        # Convert image to QImage
        height, width, channel = self.img.shape
        bytesPerLine = 3 * width
        qImg = QImage(self.img.data, width, height, bytesPerLine, QImage.Format_RGB888)

        # Display the image in the two views
        self.label1.setPixmap(QPixmap.fromImage(qImg))
        self.label2.setPixmap(QPixmap.fromImage(qImg))

    def annotate(self):
        # Use Matplotlib to annotate the image
        plt.imshow(self.img)
        plt.title('Annotated Image')
        plt.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AnnotationTool()
    ex.show()
    sys.exit(app.exec_())
    
    
#multiviewer with gptchat3
