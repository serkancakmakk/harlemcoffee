import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Product List")
        self.resize(600, 400)

        # Veritabanı bağlantısı oluştur
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("db.sqlite")  # SQLite veritabanı adı
        if not self.db.open():
            print("Veritabanı bağlantısı başarısız:", self.db.lastError().text())
            sys.exit(1)

        # Veritabanındaki product tablosundan verileri al
        self.query = QSqlQueryModel()
        self.query.setQuery("SELECT * FROM product")

        # Verileri göstermek için bir TableView oluştur
        self.table_view = QTableView()
        self.table_view.setModel(self.query)

        self.setCentralWidget(self.table_view)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())