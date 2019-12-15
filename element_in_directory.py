import psutil
import os
import time
import re


def get_size(start_path='.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size


class ElementsInCurrentDirectory:
    def __init__(self, current_position):
        self.current_position = current_position
        self.el_list = []
        i = 0
        im = len(os.listdir(current_position))
        for el in os.listdir(current_position):
            self.el_list.append(Element(el, self.current_position))
            time.sleep(0.1)
            print(f"{el} {i + 1}/{im}")
            i += 1
        print("Complete!")
        self.types = {}
        for el in self.el_list:
            if re.match(r".*\.[a-z]{1,3}", el.name):
                self.types[re.search(r"\.[a-z]{1,3}", el.name).group()] = []
        self.types[" "] = []
        time.sleep(1)
        # self.el_list = [Element(el, self.current_position) for el in os.listdir(current_position)]

    def sort_by_size(self):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(self.el_list) - 1):
                if self.el_list[i].size_in_bytes < self.el_list[i + 1].size_in_bytes:
                    self.el_list[i], self.el_list[i + 1] = self.el_list[i + 1], self.el_list[i]
                    swapped = True

    def sort_by_time(self):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(self.el_list) - 1):
                if self.el_list[i].date_modif < self.el_list[i + 1].date_modif:
                    self.el_list[i], self.el_list[i + 1] = self.el_list[i + 1], self.el_list[i]
                    swapped = True

    def sort_by_type(self):
        for el in self.el_list:
            if re.match(r".*\.[a-z]{1,3}", el.name):
                self.types[re.search(r"\.[a-z]{1,3}", el.name).group()].append(el)
            else:
                self.types[" "].append(el)
        self.el_list = []
        for key in self.types:
            self.el_list += self.types[key]
            self.types[key] = []

    def __str__(self):
        result = ""
        for i in range(len(self.el_list)):
            result += f"{i + 1}) {self.el_list[i]} {self.el_list[i].size_in_bytes/ 1024 / 1024:.2f}mb\n"
        return result


class Element:
    def __init__(self, name, current_position):
        self.name = name
        self.current_position = current_position
        self.date_modif = os.path.getmtime(current_position + "/" + name)
        temp = get_size(current_position + "/" + name)
        if not temp == 0:
            self.size_in_bytes = get_size(current_position + "/" + name)
        else:
            self.size_in_bytes = os.path.getsize(current_position + "/" + name)

    def __str__(self):
        return self.name
