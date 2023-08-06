import os
import sys
import logging

from soma.qt_gui.qt_backend import QtGui, QtCore
from soma.qt_gui import qt_backend
from .File import FileControlWidget

if sys.version_info[0] >= 3:
    unicode = str


class DirectoryControlWidget(FileControlWidget):

    """ Control to enter a directory.
    """

    @staticmethod
    def is_valid(control_instance, *args, **kwargs):
        """ Method to check if the new control value is correct.

        If the new entered value is not correct, the backroung control color
        will be red.

        Parameters
        ----------
        control_instance: QWidget (mandatory)
            the control widget we want to validate

        Returns
        -------
        out: bool
            True if the control value is a file,
            False otherwise
        """
        # Get the current control palette
        control_palette = control_instance.path.palette()

        # Get the control current value
        control_value = control_instance.path.text()

        # If the control value contains a file, the control is valid and the
        # backgound color of the control is white
        is_valid = False
        if os.path.isdir(control_value) \
                or (control_instance.output and control_value != ""):
            control_palette.setColor(
                control_instance.path.backgroundRole(), QtCore.Qt.white)
            is_valid = True

        # If the control value is optional, the control is valid and the
        # backgound color of the control is yellow
        elif control_instance.optional is True and control_value == "":
            control_palette.setColor(
                control_instance.path.backgroundRole(), QtCore.Qt.yellow)
            is_valid = True

        # If the control value is empty, the control is not valid and the
        # backgound color of the control is red
        else:
            control_palette.setColor(
                control_instance.path.backgroundRole(), QtCore.Qt.red)

        # Set the new palette to the control instance
        control_instance.path.setPalette(control_palette)

        return is_valid

    #
    # Callbacks
    #

    @staticmethod
    def onBrowseClicked(control_instance):
        """ Browse the file system and update the control instance accordingly.

        If a valid direcorty has already been entered the dialogue will
        automatically point to this folder, otherwise the current working
        directory is used.

        Parameters
        ----------
        control_instance: QWidget (mandatory)
            the directory widget item
        """
        # Get the current directory
        current_control_value = os.path.join(os.getcwd(), os.pardir)
        if DirectoryControlWidget.is_valid(control_instance):
            current_control_value = unicode(control_instance.path.text())

        # Create a dialogue to select a directory
        folder = qt_backend.getExistingDirectory(
            control_instance, "Open directory", current_control_value,
            QtGui.QFileDialog.ShowDirsOnly
                | QtGui.QFileDialog.DontUseNativeDialog)

        # Set the selected directory to the path sub control
        control_instance.path.setText(unicode(folder))
