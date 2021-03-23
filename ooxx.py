import tkinter
def processMouseEvent_1(event):
    if event.num==1:
        button_1['image']=OImage
    if event.num==2:
        button_1['image']=whiteImage
    elif event.num==3:
        button_1['image']=XImage
def processMouseEvent_2(event):
    if event.num==1:
        button_2['image']=OImage
    if event.num==2:
        button_2['image']=whiteImage
    elif event.num==3:
        button_2['image']=XImage
def processMouseEvent_3(event):
    if event.num==1:
        button_3['image']=OImage
    if event.num==2:
        button_3['image']=whiteImage
    elif event.num==3:
        button_3['image']=XImage
def processMouseEvent_4(event):
    if event.num==1:
        button_4['image']=OImage
    if event.num==2:
        button_4['image']=whiteImage
    elif event.num==3:
        button_4['image']=XImage
def processMouseEvent_5(event):
    if event.num==1:
        button_5['image']=OImage
    if event.num==2:
        button_5['image']=whiteImage
    elif event.num==3:
        button_5['image']=XImage
def processMouseEvent_6(event):
    if event.num==1:
        button_6['image']=OImage
    if event.num==2:
        button_6['image']=whiteImage
    elif event.num==3:
        button_6['image']=XImage
def processMouseEvent_7(event):
    if event.num==1:
        button_7['image']=OImage
    if event.num==2:
        button_7['image']=whiteImage
    elif event.num==3:
        button_7['image']=XImage
def processMouseEvent_8(event):
    if event.num==1:
        button_8['image']=OImage
    if event.num==2:
        button_8['image']=whiteImage
    elif event.num==3:
        button_8['image']=XImage
def processMouseEvent_9(event):
    if event.num==1:
        button_9['image']=OImage
    if event.num==2:
        button_9['image']=whiteImage
    elif event.num==3:
        button_9['image']=XImage
window=tkinter.Tk()

# 圖片
bgImage=tkinter.PhotoImage(file='./bg.gif')
OImage=tkinter.PhotoImage(file='./O.gif')
XImage=tkinter.PhotoImage(file='./X.gif')
whiteImage=tkinter.PhotoImage(file='./white.gif')
# Frame
bgFrame=tkinter.Frame(window)
# 畫布
bgCanvas=tkinter.Canvas(bgFrame,width=264,height=264)
bgCanvas.create_image(130,130,image=bgImage)
# 按鈕
button_1=tkinter.Button(bgFrame,image=whiteImage)
button_2=tkinter.Button(bgFrame,image=whiteImage)
button_3=tkinter.Button(bgFrame,image=whiteImage)
button_4=tkinter.Button(bgFrame,image=whiteImage)
button_5=tkinter.Button(bgFrame,image=whiteImage)
button_6=tkinter.Button(bgFrame,image=whiteImage)
button_7=tkinter.Button(bgFrame,image=whiteImage)
button_8=tkinter.Button(bgFrame,image=whiteImage)
button_9=tkinter.Button(bgFrame,image=whiteImage)

bgCanvas.create_window(46,46,window=button_1)
bgCanvas.create_window(132,46,window=button_2)
bgCanvas.create_window(218,46,window=button_3)

bgCanvas.create_window(46,132,window=button_4)
bgCanvas.create_window(132,132,window=button_5)
bgCanvas.create_window(218,132,window=button_6)

bgCanvas.create_window(46,218,window=button_7)
bgCanvas.create_window(132,218,window=button_8)
bgCanvas.create_window(218,218,window=button_9)

button_1.bind('<Button>',processMouseEvent_1)
button_2.bind('<Button>',processMouseEvent_2)
button_3.bind('<Button>',processMouseEvent_3)
button_4.bind('<Button>',processMouseEvent_4)
button_5.bind('<Button>',processMouseEvent_5)
button_6.bind('<Button>',processMouseEvent_6)
button_7.bind('<Button>',processMouseEvent_7)
button_8.bind('<Button>',processMouseEvent_8)
button_9.bind('<Button>',processMouseEvent_9)
# 顯示
bgFrame.grid(row=0,column=0)
bgCanvas.grid(row=0,column=0,padx=10,pady=10)


window.mainloop()
