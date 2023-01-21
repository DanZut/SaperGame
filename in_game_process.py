from tkinter import Button
import random
import settings


class Cell:
    all = []

    def __init__(self, x, y, mine=False):
        self.mine = mine
        self.cell_object = None
        self.x = x
        self.y = y

        Cell.all.append(self)

    def button_creator(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            text=f'{self.x},{self.y}'
        )
        btn.bind('<Button-1>', self.button_action_left)
        btn.bind('<Button-3>', self.button_action_right)
        self.cell_object = btn

    def button_action_left(self, event):
        if self.mine:
            self.show_mine()
        else:
            self.show_cell()
            pass

    def button_action_right(self, event):
        print(event)
        print('it works')

    def get_cell_by_x(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def near_cell(self):
        """
        1,1:
            0,0 - V
            0,1 - V
            0,2 - V
            1,0 - V
            2,0 - V
            2,1 - V
            2,2 - V
            1,2 - V
        """
        cells = [
            self.get_cell_by_x(self.x - 1, self.y - 1),
            self.get_cell_by_x(self.x - 1, self.y),
            self.get_cell_by_x(self.x - 1, self.y + 1),
            self.get_cell_by_x(self.x, self.y - 1),
            self.get_cell_by_x(self.x + 1, self.y - 1),
            self.get_cell_by_x(self.x + 1, self.y),
            self.get_cell_by_x(self.x + 1, self.y + 1),
            self.get_cell_by_x(self.x, self.y + 1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    def near_mine_length(self):
        counter = 0
        for cell in self.near_cell:
            if cell.mine:
                counter += 1

        return counter

    def show_cell(self):
        print(self.near_mine_length())

    def show_mine(self):
        print(self.cell_object.configure(bg='red'))

    @staticmethod
    def random_mines():
        choosen_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for choosen_cell in choosen_cells:
            choosen_cell.mine = True

    def __repr__(self):
        return f'Cell {self.x}, {self.y}'
