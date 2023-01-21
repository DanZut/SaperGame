from tkinter import *
from in_game_process import Cell
import settings
import utility

# main file
if __name__ == '__main__':
    root = Tk()
    root.configure(bg='black')
    root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
    root.title('Game Name: Saper')
    root.resizable(False, False)

    upper_frame = Frame(
        root,
        bg='black',
        width=settings.WIDTH,
        height=utility.height_prct(25)
    )
    upper_frame.place(x=0, y=0)

    left_frame = Frame(
        root,
        bg='black',
        width=utility.width_prct(25),
        height=utility.height_prct(75)
    )
    left_frame.place(x=0, y=utility.height_prct(25))

    center_frame = Frame(
        root,
        bg='black',
        width=utility.width_prct(75),
        height=utility.height_prct(75)
    )
    center_frame.place(
        x=utility.width_prct(25),
        y=utility.height_prct(25)
    )

    # dynamic button creator
    for x in range(settings.GRID_SIZE):
        for y in range(settings.GRID_SIZE):
            new_cell = Cell(x, y)
            new_cell.button_creator(center_frame)
            new_cell.cell_object.grid(column=x, row=y)

    Cell.random_mines()


    # active window
    root.mainloop()



