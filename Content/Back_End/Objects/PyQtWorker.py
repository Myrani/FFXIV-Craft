
import threading
import traceback
import sys

from Content.Back_End.Objects.WorkerSignals import WorkerSignals
from PyQt5.QtCore import QRunnable, pyqtSlot


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            self.fn()
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            error = (exctype, value, traceback.format_exc())
            self.signals.result.emit("Error"+str(exctype))
            self.signals.result.emit("Couldn't finish the crafts ... Sorry")
        else:
            # Return the result of the processing
            self.signals.result.emit("Done")
        finally:
            self.signals.finished.emit()  # Done
