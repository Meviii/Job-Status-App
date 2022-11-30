import view.home_view as hv

def load_home_view(self, app_user):
    home_view = hv.Ui_HomeWindow(self.widget, app_user)
    self.widget.addWidget(home_view)
    self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
