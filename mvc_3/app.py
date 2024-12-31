# app.py

from flask import Flask, render_template, request
from controller.menu_controller import MenuController

app = Flask(__name__)

@app.route("/")
def show_menu():
    controller = MenuController()
    return controller.request_menu()


# as BACK SYSTEM
@app.route("/admin/menu/list")
def show_menu_list():
    controller = MenuController()
    return controller.list_menu()

@app.route("/admin/menu/create")
def create_menu():
    controller = MenuController()
    return controller.create_menu()

@app.route("/admin/menu/store", methods=['POST'])
def store_menu():
    controller = MenuController()
    return controller.store_menu()

if __name__ == "__main__":
    app.run(debug=True)
