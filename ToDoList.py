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
        newTaskWindow().Show()


    def OnQuit(self, event):
        self.Close()


class newTaskWindow(wx.Frame):

    title = "Add a new task."

    def __init__(self):
        wx.Frame.__init__(self, wx.GetApp().TopWindow, title=self.title)

        self.SetSize((400, 200))
        self.Centre()

    # def GetTask(self):
    #     task = wx.TextEntryDialog(self.panel, "What's the task?", 'Task-Maker', "",
    #                               style=wx.OK)
    #     task.ShowModal()
    #     self.txt.SetValue(task.GetValue())
    #     task.Destory()




def main():

    app = wx.App()
    simple(None)
    app.MainLoop()


if __name__ == '__main__':
    main()




