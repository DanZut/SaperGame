from tkinter import *
import settings
import utility
from in_game_process import CellClass

if __name__ == '__main__':
    # window settings
    root = Tk()
    root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
    root.title('Minesweeper Game')
    root.resizable(False, False)
    root.configure(bg='black')

    # Create sections
    top_frame = Frame(
        root,
        bg='black',
        width=settings.WIDTH,
        height=utility.height_prct(25)
        )
    top_frame.place(x=0, y=0)

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
    center_frame.place(x=utility.width_prct(25), y=utility.height_prct(25))

    # create buttons
    for x in range(settings.GRID_SIZE):
        for y in range(settings.GRID_SIZE):
            new_cell = CellClass(x, y)
            new_cell.create_button_object(center_frame)
            new_cell.cell_button_object.grid(column=x, row=y)

    # init the label
    CellClass.create_cell_count_label(left_frame)
    CellClass.cell_count_label_object.place(x=0, y=0)

    CellClass.randomize_mines()

    # run the window
    root.mainloop()
