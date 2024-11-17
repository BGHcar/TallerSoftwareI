from database import Database
from menu import Menu

def main():
    db = Database()
    menu = Menu(db)
    menu.display()

if __name__ == "__main__":
    main()
