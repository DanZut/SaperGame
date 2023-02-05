from tkinter import Button, Label, messagebox
import random
import settings



class CellClass:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_open = False
        self.is_candidate = False
        self.cell_button_object = None
        self.x = x
        self.y = y
        CellClass.all.append(self)  # add all object to list named by all

    def create_button_object(self, location):
        new_button = Button(
            location,
            width=12,
            height=4
        )
        new_button.bind('<Button-1>', self.left_click)
        new_button.bind('<Button-3>', self.right_click)
        self.cell_button_object = new_button

    @staticmethod
    def create_cell_count_label(location):
        new_label = Label(
            location,
            bg='black',
            fg='white',
            text=f'Cells left: {CellClass.cell_count}',
            width=12,
            height=4,
            font=('', 30)
        )
        CellClass.cell_count_label_object = new_label

    def left_click(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mine_length == 0:
                for c in self.surrounded_cells:
                    c.show_cell()
            self.show_cell()

    def get_cells(self, x, y):
        # return a cell object based on the value of x and y
        for cell in CellClass.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cells(self.x - 1, self.y - 1),
            self.get_cells(self.x - 1, self.y),
            self.get_cells(self.x - 1, self.y + 1),
            self.get_cells(self.x, self.y - 1),
            self.get_cells(self.x + 1, self.y - 1),
            self.get_cells(self.x + 1, self.y),
            self.get_cells(self.x + 1, self.y + 1),
            self.get_cells(self.x, self.y + 1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mine_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_cell(self):
        if not self.is_open:
            CellClass.cell_count -= 1
            self.cell_button_object.configure(text=f'{self.surrounded_cells_mine_length}')
            # Replace the text of cell count label with the newer count
            if CellClass.cell_count_label_object:
                CellClass.cell_count_label_object.configure(text=f'Cells left: {CellClass.cell_count}')

        # mark the cell as open
        self.is_open = True

    def show_mine(self):
        self.cell_button_object.configure(text='MINE', fg='red')
        # improve the ending go to https://docs.python.org/3.10/library/tkinter.messagebox.html
        msng = messagebox.askquestion('GAME OVER', 'Another Round?')
        print(msng)
        if msng == True:
            #find a way to restart program
        else:
            quit()

    def right_click(self, event):
        if not self.is_candidate:
            self.cell_button_object.configure(bg='blue')
            self.is_candidate = True
        else:
            self.cell_button_object.configure(bg='gray85')
            self.is_candidate = False

    @staticmethod
    def randomize_mines():
        choosen_cells = random.sample(CellClass.all, settings.MINES_COUNT)
        for cell in choosen_cells:
            cell.is_mine = True

    def __repr__(self):
        return f'Cell ({self.x},{self.y}) '
