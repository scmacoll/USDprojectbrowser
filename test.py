import os
import hou
from PySide2 import QtWidgets, QtUiTools, QtGui


class ProjectManager(QtWidgets.QWidget):
    def __init__(self):
        super(ProjectManager, self).__init__()

        self.proj = hou.getenv('JOB') + '/'
        self.visited_dirs = []
        self.current_index = -1
        # print(str((self.proj.split('/')[6] + '/ = ' + (
        #     str(self.current_index)))))

        # Load UI file
        loader = QtUiTools.QUiLoader()
        self.ui = loader.load('/Users/stu/Library/Preferences/houdini/19.5'
                              '/scripts/python/projectview/projectview.ui')

        # get UI elements (designer)
        self.set_proj = self.ui.findChild(QtWidgets.QPushButton, 'setproj')
        self.back_btn = self.ui.findChild(QtWidgets.QPushButton, 'backbtn')
        self.fwd_btn = self.ui.findChild(QtWidgets.QPushButton, 'fwdbtn')
        self.proj_path = self.ui.findChild(QtWidgets.QLabel, 'projpath')
        self.job_path = self.ui.findChild(QtWidgets.QLabel, 'jobpath')
        self.proj_name = self.ui.findChild(QtWidgets.QLabel, 'projname')
        self.scene_list = self.ui.findChild(QtWidgets.QListWidget, 'scenelist')

        back_icon_path = '/Users/stu/Documents/3D/QtDesigner/icons/BUTTONS' \
                         '/back.svg'
        back_icon = QtGui.QIcon(back_icon_path)
        self.back_btn.setIcon(back_icon)
        fwd_icon_path = '/Users/stu/Documents/3D/QtDesigner/icons/BUTTONS' \
                        '/forward.svg'
        fwd_icon = QtGui.QIcon(fwd_icon_path)
        self.fwd_btn.setIcon(fwd_icon)

        # create connections (/button functionality)
        self.set_proj.clicked.connect(self.set_project)
        self.back_btn.clicked.connect(self.back_button)
        self.fwd_btn.clicked.connect(self.forward_button)

        # Create layout (how widgets will be organised)
        main_layout = QtWidgets.QVBoxLayout()  # vertical layout

        main_layout.addWidget(self.ui)

        self.setLayout(main_layout)

    def set_project(self):
        set_job = hou.ui.selectFile(title='Select Project Folder',
                                    file_type=hou.fileType.Directory)
        hou.hscript('setenv JOB=' + set_job)
        self.proj = hou.getenv('JOB') + '/'

        proj_name = 'Project:  ' + set_job.split('/')[-2]
        set_job = 'JOB:  ' + os.path.dirname(set_job)
        proj_path = 'Path:  ' + os.path.split(set_job)[1]
        job_path = set_job

        self.proj_name.setText(proj_name)
        self.proj_path.setText(proj_path + '/')
        self.job_path.setText(job_path + '/')

        # if self.current_index == len(self.visited_dirs) - 1:
        #     self.visited_dirs.append(self.proj)
        # else:
        #     self.visited_dirs = self.visited_dirs[:self.current_index + 1]
        #     self.visited_dirs.append(self.proj)

        if self.proj in self.visited_dirs:
            index = self.visited_dirs.index(self.proj)
            self.visited_dirs[index] = self.proj
            self.current_index = index
        else:
            self.current_index = len(self.visited_dirs)
            self.visited_dirs.append(self.proj)

        self.create_interface()


    def back_button(self):
        home_dir = os.path.expanduser("~")
        job_path = self.job_path.text().split('JOB:  ')[1].replace('$HOME',
                                                                   home_dir)
        # if self.proj[-2:] == '//':
        #     self.proj = self.proj[:-1]
        if os.path.abspath(self.proj) + '/' == job_path:
            print("Can't go back any further on the $JOB PATH")
            return
        else:
            if self.current_index > -1:
                self.current_index -= 1
                self.proj = self.visited_dirs[self.current_index + 1]
                self.create_interface()

                # removing the last directory from the path
                if hasattr(self, 'first_path'):
                    proj_path = self.proj_path.text()
                    first_path_len = len(self.first_path)
                    if len(proj_path) > first_path_len:
                        # Find the second last occurrence of the path
                        # separator '/'
                        index = proj_path[:-1].rfind('/') + 1
                        self.proj_path.setText(
                            os.path.normpath(proj_path[:index]) + '/')

            else:
                print("Can't go back any further")

    def forward_button(self):
        if self.proj[-2:] == '//':
            self.proj = self.proj[:-1]
        # print(self.proj)
        highlight_item = self.scene_list.currentItem()

        # if index is not at the end of the list
        if self.current_index < len(self.visited_dirs) - 1 \
                and highlight_item is None:
            self.current_index += 1

            self.proj = self.visited_dirs[self.current_index]
            self.create_interface()

            # * project path label
            rel_path = os.path.relpath(self.proj, start=hou.getenv('JOB'))
            if not hasattr(self, 'first_path'):
                self.first_path = os.path.join(self.proj_path.text(), '')
            self.proj_path.setText(os.path.normpath(self.first_path +
                                                    rel_path) + '/')

        # elif hasattr(self, 'prev_proj') and highlight_item is None:
        #     self.proj = self.prev_proj
        #     self.create_interface()
        #
        #     del self.prev_proj
        #     # * project path label
        #     rel_path = os.path.relpath(self.proj, start=hou.getenv('JOB'))
        #     if not hasattr(self, 'first_path'):
        #         self.first_path = os.path.join(self.proj_path.text(), '')
        #     self.proj_path.setText(os.path.normpath(self.first_path +
        #                                             rel_path) + '/')

        elif highlight_item is not None and os.path.isdir(os.path.join(
                self.proj, highlight_item.text())):

            if self.proj not in self.visited_dirs:
                # print(self.proj)
                self.visited_dirs.append(self.proj)
                self.current_index += 1
            else:
                self.current_index = self.visited_dirs.index(self.proj)

            self.proj = os.path.join(self.proj, highlight_item.text()) + '/'
            # print(self.proj + ' = ' + str(self.current_index))
            self.create_interface()
            # * project path label
            rel_path = os.path.relpath(self.proj, start=hou.getenv('JOB'))
            if not hasattr(self, 'first_path'):
                self.first_path = os.path.join(self.proj_path.text(), '')
            self.proj_path.setText(os.path.normpath(self.first_path +
                                                    rel_path) + '/')

    def navigate_subdir(self):
        if self.proj[-2:] == '//':
            self.proj = self.proj[:-1]
        # print(self.proj)
        selected_item = self.scene_list.currentItem()

        if selected_item is not None and os.path.isdir(
                os.path.join(self.proj, selected_item.text())):

            if self.proj not in self.visited_dirs:
                self.visited_dirs.append(self.proj)
                self.current_index += 1
            else:
                self.current_index = self.visited_dirs.index(self.proj)

            self.proj = os.path.join(self.proj, selected_item.text()) + '/'
            # print(self.proj + ' = ' + str(self.current_index))
            # print(self.proj)
            self.create_interface()
            # * project path label
            rel_path = os.path.relpath(self.proj, start=hou.getenv('JOB'))
            if not hasattr(self, 'first_path'):
                self.first_path = os.path.join(self.proj_path.text(), '')
            self.proj_path.setText(os.path.normpath(self.first_path +
                                                    rel_path) + '/')
        # print('nav- ' + self.proj_path.text() + ' = ' + str(
        #     self.current_index))

    def create_interface(self):
        if self.proj[-2:] == '//':
            self.proj = self.proj[:-1]
        # print("loaded interface")

        print(self.proj + ' = '
              + 'Index: '
              + str(self.current_index)
              + ' Length: '
              + str(len(self.visited_dirs)))

        self.scene_list.clear()

        items = os.listdir(self.proj)
        items.sort()

        for file in items:
            path = os.path.join(self.proj, file)
            if os.path.isdir(path):
                self.scene_list.addItem(file)
                self.scene_list.doubleClicked.connect(self.navigate_subdir)
            elif file.endswith('.usda'):
                self.scene_list.addItem(file)
                # self.scene_list.doubleClicked.connect(
                #     lambda item: print("importing usda"))

        return self.scene_list



