# import sys
# import unittest
# from unittest.mock import MagicMock
# import os
#
# sys.modules['hou'] = MagicMock()
#
# from project import ProjectManager, Node, Tree
#
#
# # create Test Cases
# # 1st create a test class that inherits from unittest.TestCase
#
# class TestMyProject(unittest.TestCase):
#     def setUp(self):
#         self.project = ProjectManager()
#
#     def test_back_button(self):
#         home_dir = os.path.expanduser("~")
#         job_path = os.path.join(home_dir, "test_job_path")
#
#         # Set the necessary attributes for the test
#         self.project.job_path.setText("JOB:  " + job_path)
#         self.project.current_node.path = os.path.join(job_path,
#                                                       "test_directory")
#
#         # Call the back_button method
#         self.project.back_button()
#
#         # Check if the current_node.path has been updated as expected
#         self.assertEqual(self.project.current_node.path, job_path)
#
#     def test_forward_button(self):
#         # Set the necessary attributes for the test
#         self.project.current_node.path = os.path.join("test_directory")
#         self.project.scene_list.addItem("subdirectory")
#
#         # Select the first item in the scene_list
#         self.project.scene_list.setCurrentRow(0)
#
#         # Call the forward_button method
#         self.project.forward_button()
#
#         # Check if the current_node.path has been updated as expected
#         self.assertEqual(self.project.current_node.path, os.path.join(
#             "test_directory", "subdirectory"))
#
#
# if __name__ == '__main__':
#     unittest.main()
