import tkinter as tk
from tkinter import PhotoImage, Entry, messagebox
import subprocess
import os
import paramiko
import re  # Para validar la IP

class ApagarPCApp:
  def __init__(self, root):
