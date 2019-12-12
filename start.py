import psutil
import os
import viewer
import sys
v = None
if len(sys.argv) > 1:
    v = viewer.Viewer(sys.argv[1])

# os.listdir, os.path.getsize, os.remove, os.rmdir()
# disks = psutil.disk_partitions()
# free = psutil.disk_usage(disks[iterator].mountpoint).free / (1024 * 1024 * 1024)
# total = psutil.disk_usage(disks[iterator].mountpoint).total / (1024 * 1024 * 1024)
# used = psutil.disk_usage(disks[iterator].mountpoint).used / (1024 * 1024 * 1024)
# ft = round(free / total * 100)
# ut = round(used / total * 100)
else:
    print("write puth for directory!")
    quit()
print(f"Current position: {v.current_pos}")
print(v.elements_in_current_position.__str__())
while True:
    command = input()
    v.go_to_this(command)
    v.get_disk_list(command)
    # v.select_disk(command)
    v.get_info_about_disk(command)
    v.sort_by_size(command)
    v.sort_by_time(command)
    v.sort_by_type(command)
    if command == "quit":
        quit()
