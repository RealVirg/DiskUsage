import psutil
import element_in_directory


class Viewer:
    def __init__(self, start_pos):
        self.current_pos = start_pos  # self.disk_list[0].__str__()
        self.elements_in_current_position = element_in_directory.ElementsInCurrentDirectory(self.current_pos)

    def refresh_elements(self):
        self.elements_in_current_position = element_in_directory.ElementsInCurrentDirectory(self.current_pos)

    def sort_by_size(self, command):
        try:
            commands = command.split(" ")
            if commands[0] == "sort_by_size":
                self.elements_in_current_position.sort_by_size()
                print(self.elements_in_current_position.__str__())
        except IndexError:
            print("error param")

    def sort_by_time(self, command):
        try:
            commands = command.split(" ")
            if commands[0] == "sort_by_time":
                self.elements_in_current_position.sort_by_time()
                print(self.elements_in_current_position.__str__())
        except IndexError:
            print("error param")

    def sort_by_type(self, command):
        try:
            commands = command.split(" ")
            if commands[0] == "sort_by_type":
                self.elements_in_current_position.sort_by_type()
                print(self.elements_in_current_position.__str__())
        except IndexError:
            print("error param")

    def go_to_this(self, command):
        temp = self.current_pos
        try:
            commands = command.split(" ")
            if commands[0] == "go_to_this":
                self.current_pos = commands[1]
                self.refresh_elements()
                print(f"Current position: {self.current_pos}")
                print(self.elements_in_current_position.__str__())
        except IndexError:
            print("error param")
        except FileNotFoundError:
            print("error found")
            self.current_pos = temp
