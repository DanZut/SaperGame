from tkinter import Button


class Cell:
    def __init__(self, mine=False):
        self.mine = mine
        self.cell_object = None

    def button_creator(self, location):
        btn = Button(
            location,
            text='1'
        )
        btn.bind('<Button-1>', self.button_action_left)
        btn.bind('<Button-3>', self.button_action_right)
        self.cell_object = btn

    def button_action_left(self, event):
        print(event)
        print('it works')

    def button_action_right(self, event):
        print(event)
        print('it works')
