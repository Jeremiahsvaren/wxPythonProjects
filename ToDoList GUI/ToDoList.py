__author__ = 'Jeremiah'


import wx

class simple(wx.Frame):
    #The main frame that holds the todo list


    def __init__(self, *args, **kwargs):
        super(simple, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):
        #Sets the frame up
        self.SetSize((350, 600))
        self.SetTitle('Simple To Do List')
        self.Centre()
        self.Show(True)


        #Creates the top menu bar
        menuBar = wx.MenuBar()


        #Creates the File drop down and appends to the menu bar
        fileMenu = wx.Menu()
        menuBar.Append(fileMenu, '&File')
        self.SetMenuBar(menuBar)

        #Creates the file menu item which closes the program
        menuQuit = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        self.Bind(wx.EVT_MENU, self.OnQuit, menuQuit)

        #Creates toolbar
        toolbar = self.CreateToolBar()


        #This is the tool which opens a new frame,
        #allowing users to add new tasks.
        addTask = toolbar.AddLabelTool(wx.ID_ANY, 'Add Task', wx.Bitmap('images/add-icon.png'))
        self.Bind(wx.EVT_TOOL, self.OnAdd, addTask)

        #This will allow users to delete tasks.
        delTask = toolbar.AddLabelTool(wx.ID_ANY, 'Delete Task', wx.Bitmap('images/cancel-icon.png'))

        toolbar.Realize()





    def OnAdd(self, event):
        #Opens new window upon clicking the addTask button.
        newTaskWindow().Show()


    def OnQuit(self, event):
        #Closes the application upon clicking
        #the file menu button "Quit"
        self.Close()


class newTaskWindow(wx.Frame):
    #This is the window that opens upon,
    #clicking addTask button.

    title = "Add a new task."

    def __init__(self):
        #This part still needs some work.
        wx.Frame.__init__(self, wx.GetApp().TopWindow, title=self.title)

        pan = wx.Panel(self)
        self.txt = wx.TextCtrl(pan, -1, pos=(5,5), size=(375,100), style=wx.DEFAULT)


        self.SetSize((400, 200))
        self.Centre()




def main():

    app = wx.App()
    simple(None)
    app.MainLoop()


if __name__ == '__main__':
    main()




