import tkinter as tk
from tkinter import PhotoImage, Entry, messagebox
import subprocess
import os
import paramiko
import re  # Para validar la IP

class ApagarPCApp:
  def __init__(self, root):
      self.root = root
      self.root.title("Ciberseguridad")

      # Obtener la resolución de la pantalla
      ancho_pantalla = root.winfo_screenwidth()
      alto_pantalla = root.winfo_screenheight()
      self.root.geometry(f"{ancho_pantalla}x{alto_pantalla}")
      self.root.configure(bg='#2c3e50')

       # Configuración de las columnas y filas
      for i in range(6):
        root.grid_columnconfigure(i, weight=1)
      for i in range(9):
        root.grid_rowconfigure(i, weight=1)

    # Llamada a la configuración de la interfaz
