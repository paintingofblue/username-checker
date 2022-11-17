import sys
import PyQt5.QtWidgets as Qt
import PyQt5.QtGui as QtGui

class Styles:
    dark = """
        * {
            background-color: #2A3132;
            color: #F0F0F0;
        }
        
        QTextEdit {
            background-color: #3A4142;
            color: #F0F0F0;
    }"""

    light = """
    * {
        background-color: #F0F0F0;
        color: #000000;
    }

    QTextEdit {
        background-color: #FFFFFF;
        color: #000000;
    }"""

    isDarkMode = False

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

def dark_mode(darkmode):
    global isDarkMode
    if darkmode.isChecked():
        app.setStyleSheet(Styles.dark)
        optionsButton.setIcon(QtGui.QIcon("icons/Settings-Dark.png"))
        startButton.setIcon(QtGui.QIcon("icons/Play-Dark.png"))
        Styles.isDarkMode = True
    else:
        app.setStyleSheet(Styles.light)
        optionsButton.setIcon(QtGui.QIcon("icons/Settings-Light.png"))
        startButton.setIcon(QtGui.QIcon("icons/Play-Light.png"))
        Styles.isDarkMode = False

def options():
    optionsWindow = Qt.QWidget()
    optionsWindow.setWindowTitle("Options")
    optionsWindow.setWindowIcon(QtGui.QIcon("icon.png"))
    optionsWindow.setFixedSize(300, 200)
    optionsWindow.show()

    # Dark mode toggle
    darkMode = Qt.QCheckBox("Dark Mode", optionsWindow)
    darkMode.move(10, 10)
    darkMode.setChecked(Styles.isDarkMode)
    darkMode.stateChanged.connect(lambda: dark_mode(darkMode))
    darkMode.show()

    while True:
        try:
            app.processEvents()
        except:
            break

def wordlist_open():
    file, check = Qt.QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "", "Text Files (*.txt)")
    if check:
        wordlistPath.setText(file)

if __name__ == "__main__":
    # Creating the window
    app = Qt.QApplication(sys.argv)
    app.setStyle('Fusion')

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
    optionsButton.setIcon(QtGui.QIcon("icons/Settings-Light.png"))
    optionsButton.resize(50, 22)
    optionsButton.move(503, 440)
    optionsButton.clicked.connect(options)
    optionsButton.show()

    # Start button
    startButton = Qt.QPushButton(w)
    startButton.setIcon(QtGui.QIcon("icons/Play-Light.png"))
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