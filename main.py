import sys
import requests
import PyQt5.QtWidgets as Qt
import qdarkstyle
from PyQt5.QtGui import QIcon

sites = [
    "Instagram",
    "Facebook",
    "Twitter",
    "Snapchat",
    "TikTok",
    "Pinterest",
    "Reddit",
    "Twitch",
]

def dark_mode(darkMode):
    if darkMode.isChecked():
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

        optionsButton.setIcon(QIcon("icons/Settings-Dark.png"))
        startButton.setIcon(QIcon("icons/Play-Dark.png"))

        wordlistLabel.move(15, 420)
        siteLabel.move(218, 420)
    else:
        app.setStyleSheet("")

        optionsButton.setIcon(QIcon("icons/Settings-Light.png"))
        startButton.setIcon(QIcon("icons/Play-Light.png"))
        
        wordlistLabel.move(20, 420)
        siteLabel.move(223, 420)

def options():
    e = Qt.QWidget()
    e.setWindowTitle("Options")
    e.setWindowIcon(QIcon("icon.png"))
    e.setFixedSize(300, 200)
    e.show()

    # Dark mode toggle
    darkMode = Qt.QCheckBox("Dark Mode", e)
    darkMode.move(10, 10)
    darkMode.setChecked(False)
    darkMode.stateChanged.connect(lambda: dark_mode(darkMode))
    darkMode.show()

    while True:
        try:
            app.processEvents()
        except:
            break

def wordlist_open():
    file , check = Qt.QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "", "Text Files (*.txt)")
    if check:
        wordlistPath.setText(file)

if __name__ == "__main__":
    # Creating the window
    app = Qt.QApplication(sys.argv)
    w = Qt.QWidget()
    w.setFixedSize(640, 480)
    w.setWindowTitle("Username Checker")


    # Wordlist button & path
    wordlistLabel = Qt.QLabel(w)
    wordlistLabel.setText("Wordlist")
    wordlistLabel.resize(100, 20)
    wordlistLabel.move(20, 420)
    wordlistLabel.show()

    wordlistButton = Qt.QPushButton(w)
    wordlistButton.setText("Open")
    wordlistButton.resize(75, 22)
    wordlistButton.move(19, 439)
    wordlistButton.clicked.connect(wordlist_open)
    wordlistButton.show()

    wordlistPath = Qt.QLineEdit(w)
    wordlistPath.setFixedWidth(100)
    wordlistPath.move(103, 440)
    wordlistPath.show()

    # Site dropdown
    siteLabel = Qt.QLabel(w)
    siteLabel.setText("Site")
    siteLabel.resize(100, 20)
    siteLabel.move(223, 420)
    siteLabel.show()

    siteDropdown = Qt.QComboBox(w)
    siteDropdown.resize(75, 20)
    siteDropdown.move(223, 440)
    siteDropdown.show()
    for i in sites:
        siteDropdown.addItem(i)

    # Options button
    optionsButton = Qt.QPushButton(w)
    optionsButton.setIcon(QIcon("icons/Settings-Light.png"))
    optionsButton.resize(50, 22)
    optionsButton.move(503, 440)
    optionsButton.clicked.connect(options)
    optionsButton.show()

    # Start button
    startButton = Qt.QPushButton(w)
    startButton.setIcon(QIcon("icons/Play-Light.png"))
    startButton.resize(50, 22)
    startButton.move(571, 440)
    startButton.show()

    # Text box
    text_box = Qt.QTextEdit(w)
    text_box.setReadOnly(True)
    text_box.setFixedSize(600, 385)
    text_box.move(20, 20)
    text_box.show()
    
    w.show()
    sys.exit(app.exec_())