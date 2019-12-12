import psutil


class Disk:
    def __init__(self, name):
        self.name = name
        self.free = psutil.disk_usage(name).free / (1024 * 1024 * 1024)
        self.total = psutil.disk_usage(name).total / (1024 * 1024 * 1024)
        self.used = psutil.disk_usage(name).used / (1024 * 1024 * 1024)

    def __str__(self):
        return self.name

    def get_info(self):
        return f"Name disk: {self.name}\nFree memory: {self.free:.2f} gb" + \
               f"\nUsed memory: {self.used:.2f} gb\nTotal memory: {self.total:.2f} gb\n"
