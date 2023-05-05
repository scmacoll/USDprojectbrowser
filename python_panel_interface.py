import hou
import os
import sys
import project
import importlib

importlib.reload(project)
script_path = os.path.join(os.path.dirname(__file__), 'project.py')
sys.path.append(os.path.dirname(script_path))


def onCreateInterface():
    return project.UsdBrowser()
