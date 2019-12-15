import viewer
import sys
import render_elements


v = None
if len(sys.argv) > 1:
    v = viewer.Viewer(sys.argv[1])
else:
    print("write puth to directory!")
    quit()

print(v.elements_in_current_position.__str__())
while True:
    print(f"Current position: {v.current_pos}")
    command = input()
    if command == "quit":
        quit()
    v.go_to_this(command)
    v.sort_by_size(command)
    v.sort_by_time(command)
    v.sort_by_type(command)
    r = render_elements.RenderAll(v.elements_in_current_position.el_list)
    if command == "render":
        r.render()
    if command == "help":
        print("Команда go_to_this puth сменит текущую директорию на директорию по абсолютному пути puth.\n" +
              "Команда quit закончит выполнение программы\n" +
              "Команда sort_by_time, sort_by_type, sort_by_size отсортирует" +
              " файлы соответсвенно по времени, типу, размеру.\n" +
              "Команда render отрисует текущий список элементов директории в его текущем состоянии.")
