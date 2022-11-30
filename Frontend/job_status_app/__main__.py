from PyQt5 import QtWidgets
import sys
import view.login_view as login_view

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    main = login_view.Ui_LoginWindow(widget)
    widget.addWidget(main)
    widget.show()
    sys.exit(app.exec_())