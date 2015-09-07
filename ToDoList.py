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


        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnQuit, quit)

        self.SetSize((350, 600))
        self.SetTitle('Simple To Do List')
        self.Centre()
        self.Show(True)

    def OnQuit(self, e):
        self.Close()


def main():

    app = wx.App()
    simple(None)
    app.MainLoop()


if __name__ == '__main__':
    main()




