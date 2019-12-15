import pygame
import math
import random


class RenderAll:
    def __init__(self, list_all):
        self.list_all = list_all
        self.total_size = 0
        for el in list_all:
            self.total_size += el.size_in_bytes
        self.colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 255)]

    def render(self):

        display = pygame.display.set_mode((500, 500))

        run = True

        current_angle = 0
        another_size = 0
        temp = []

        for el in self.list_all:
            last_angle = current_angle

            if (2 * math.pi) * (el.size_in_bytes * 100 / self.total_size) / 100 < 0.1:
                another_size += el.size_in_bytes
                continue
            current_angle += (2 * math.pi) * (el.size_in_bytes * 100 / self.total_size) / 100

            temp.append(RenderEl(el.name, last_angle, current_angle, el.size_in_bytes))

            pygame.draw.arc(display, (random.randint(10, 240), random.randint(10, 240), random.randint(10, 240)),
                            pygame.Rect(150, 150, 200, 200),
                            last_angle,
                            current_angle,
                            100)

        temp.append(RenderEl("Another", current_angle, 2 * math.pi, another_size))
        pygame.draw.arc(display, (255, 255, 255),
                        pygame.Rect(150, 150, 200, 200),
                        current_angle,
                        2 * math.pi,
                        100)

        pygame.display.update()

        pygame.init()
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for el in temp:
                el.render(250, 250, mouse_x, mouse_y, display)
                pygame.display.update()

            # pygame.draw.rect(display, (0, 0, 0), pygame.Rect(0, 0, 500, 500))


class RenderEl:
    def __init__(self, name, last_angle, current_angle, size):
        self.name = name
        self.last_angle = last_angle
        self.current_angle = current_angle
        self.size = size

    def render(self, center_x, center_y, mouse_x, mouse_y, display):
        if mouse_x > center_x and 500 - center_y < 500 - mouse_y:
            mins = 0
            add_to_angle = 0
        elif mouse_x < center_x and 500 - center_y < 500 - mouse_y:
            mins = math.pi / 2
            add_to_angle = math.pi / 2
        elif mouse_x < center_x and 500 - center_y > 500 - mouse_y:
            mins = 0
            add_to_angle = math.pi
        else:
            mins = math.pi / 2
            add_to_angle = 1.5 * math.pi
        try:
            if mins != 0:
                angle = mins -\
                        math.atan(abs((500 - mouse_y) - (500 - center_y)) / abs(mouse_x - center_x)) +\
                        add_to_angle
            else:
                angle = math.atan(abs((500 - mouse_y) - (500 - center_y)) / abs(mouse_x - center_x)) + \
                        add_to_angle
        except ZeroDivisionError:
            angle = 10
        if self.last_angle < angle < self.current_angle:
            font = pygame.font.Font(None, 20)
            pygame.draw.rect(display, (0, 0, 0), pygame.Rect(0, 0, 500, 150))
            display.blit(font.render(f"{self.name}", False, (255, 255, 255)), (10, 0))
            display.blit(font.render(f"Size: {self.size/ 1024 / 1024:.2f}mb", False, (255, 255, 255)), (10, 20))
