import tkinter as tk
from tkinter import ttk
import customtkinter as ctk


class LoginPage:
    def __init__(self):
        self.win = ctk.CTk()
        self.win.title("Login Page")
        self.win.geometry("320x320")
        self.win.resizable(0, 0)

        self.lbl1 = None
        self.userName = None
        self.password = None
        self.btn1 = None
        self.btn2 = None
        self.info_label = None

        self.createWidgets()
        self.setupDatabase()  # Set up the database
