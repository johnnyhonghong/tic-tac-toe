import tkinter
import numpy as np
# 格子中心點
position_x = []
position_y = []
# 紀錄
rec_matrix = [['_','_','_'],
              ['_','_','_'],
              ['_','_','_']]

round_flag = [False, False, False] # circle_flag, cross_flag, win_flag


def create_background():
    
    
    bg_canvas.create_image(width / 2, height / 2, image = bg_image)
    
    # 格子中心點
    for i in range(9):
        position_x.append(44 + 88 * (i % 3))
        position_y.append(44 + 88 * (i // 3))
    # 格線
    for i in range(2):
        bg_canvas.create_line(0, 88*(i + 1), 264, 88*(i + 1), fill = "black", width=2)
        bg_canvas.create_line(88*(i + 1), 0, 88*(i + 1), 264, fill = "black", width=2)
    # 綁定事件
    bg_canvas.bind('<Button>',process_mouse_event)
    
    # 顯示
    bg_frame.grid(row = 0, column = 0)
    bg_canvas.grid(row = 0, column = 0, padx = 10, pady = 10)
def draw_circle(x,y):
    bg_canvas.create_oval(x-30, y-30, x+30, y+30, width=6, outline='red')

def draw_cross(x,y):
    bg_canvas.create_line(x-30, y-30, x+30, y+30, width=6, fill='blue')
    bg_canvas.create_line(x+30, y-30, x-30, y+30, width=6, fill='blue')

def process_mouse_event(event):
    if not round_flag[2]:
        i = 0
        rec = 0
        while(i < 9):
            x = event.x - position_x[i]
            y = event.y - position_y[i]
            dis = (x**2) + (y**2)
            if i == 0:
                mdis = dis
                mx = position_x[i]
                my = position_y[i]
            elif dis < mdis:
                mdis = dis
                mx = position_x[i]
                my = position_y[i]      
                rec = i
            i += 1
        
        if rec_matrix[rec // 3][rec % 3] == '_':
            if event.num == 1 and not round_flag[0]:
                draw_circle(mx, my)
                rec_matrix[rec // 3][rec % 3] = 'O'
                round_flag[0] = True
                round_flag[1] = False
            elif event.num == 3 and not round_flag[1]:
                draw_cross(mx, my)
                rec_matrix[rec // 3][rec % 3] = 'X'
                round_flag[0] = False
                round_flag[1] = True
        else:
            print('confict')
        
        for row_number, matrix_row in enumerate(rec_matrix):
            if set(matrix_row) == set(['O']):
                bg_canvas.create_line(5, 44 + 88 * row_number,
                                      259, 44 + 88 * row_number,
                                      fill = "#ff8c00", width=5)
                round_flag[2] = True
                break
            elif set(matrix_row) == set(['X']):
                bg_canvas.create_line(5, 44 + 88 * row_number,
                                      259, 44 + 88 * row_number,
                                      fill = "#ff8c00", width=5)
                round_flag[2] = True
                break
        for row_number, matrix_row in enumerate(np.transpose(rec_matrix)):
            if set(matrix_row) == set(['O']):
                bg_canvas.create_line( 44 + 88 * row_number, 5,
                                       44 + 88 * row_number, 259,
                                      fill = "#ff8c00", width=5)
                round_flag[2] = True
                break
            elif set(matrix_row) == set(['X']):
                bg_canvas.create_line( 44 + 88 * row_number, 5,
                                       44 + 88 * row_number, 259,
                                      fill = "#ff8c00", width=5)
                round_flag[2] = True
                break
        if set([rec_matrix[0][2],rec_matrix[1][1],rec_matrix[2][0]]) == set(['O']):
            bg_canvas.create_line(250, 14,
                                  14, 250,
                                  fill = "#ff8c00", width=5)
            round_flag[2] = True
        elif set([rec_matrix[0][2],rec_matrix[1][1],rec_matrix[2][0]]) == set(['X']):
            bg_canvas.create_line(250, 14,
                                  14, 250,
                                  fill = "#ff8c00", width=5)
            round_flag[2] = True
        if set([rec_matrix[0][0],rec_matrix[1][1],rec_matrix[2][2]]) == set(['O']):
            bg_canvas.create_line(14, 14,
                                  250, 250,
                                  fill = "#ff8c00", width=5)
            round_flag[2] = True
        elif set([rec_matrix[0][0],rec_matrix[1][1],rec_matrix[2][2]]) == set(['X']):
            bg_canvas.create_line(14, 14,
                                  250, 250,
                                  fill = "#ff8c00", width=5)
            round_flag[2] = True
    print("result: ")
    print(rec_matrix[0])
    print(rec_matrix[1])
    print(rec_matrix[2])
    if round_flag[2]:
        if round_flag[0]:
            print("Game over. The circle O win!")
        elif round_flag[1]:
            print("Game over. The cross X win!")
if __name__ =="__main__":    
    
    window = tkinter.Tk()
    # 圖片
    bg_image = tkinter.PhotoImage(file = './image/bg.gif')
    circle_image = tkinter.PhotoImage(file = './image/O.gif')
    cross_image = tkinter.PhotoImage(file = './image/X.gif')
    white_image = tkinter.PhotoImage(file = './image/white.gif')
    # 畫布
    width = 264
    height = 264
    # Frame
    bg_frame = tkinter.Frame(window)
    bg_canvas = tkinter.Canvas(bg_frame, width = width, height = height)
    bg_canvas = tkinter.Canvas(bg_frame, width = width, height = height)
    create_background()
    
    
    
    
    
    
    
    window.title('ooxx')
    window.geometry('285x285')
    window.mainloop()


