from PyQt5.QtCore import QObject,pyqtSignal



class WorkerSignals(QObject):
    
    finished = pyqtSignal()
    addLabel = pyqtSignal(str)
    changeText = pyqtSignal(str)


