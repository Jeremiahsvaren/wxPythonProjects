__author__ = 'Jeremiah'


import wx

class simple(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(simple, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        menuBar = wx.MenuBar()

        fileMenu = wx.Menu()
        quit = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menuBar.Append(fileMenu, '&File')

        toolbar = self.CreateToolBar()
        addTask = toolbar.AddLabelTool(wx.ID_ANY, 'Add Task', wx.Bitmap('images/add-icon.png'))
        delTask = toolbar.AddLabelTool(wx.ID_ANY, 'Delete Task', wx.Bitmap('images/cancel-icon.png'))
        toolbar.Realize()

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnQuit, quit)
        self.Bind(wx.EVT_TOOL, self.OnAdd, addTask)


        self.SetSize((350, 600))
        self.SetTitle('Simple To Do List')
        self.Centre()
        self.Show(True)

    def OnAdd(self, event):
        self.Close() #Need this to open another window to add a task


    def OnQuit(self, event):
        self.Close()


def main():

    app = wx.App()
    simple(None)
    app.MainLoop()


if __name__ == '__main__':
    main()




