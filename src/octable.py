from PyQt5.QtWidgets import QApplication, QLabel

def main():
  app = QApplication([])
  label = QLabel('Welcome to the Octable client')
  label.show()
  app.exec_()

if __name__ == '__main__':
  main()
