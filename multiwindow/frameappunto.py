import wx

from filemanager import  FileManager

class FrameAppunto(wx.Frame):


    def __init__(self, parent, ID, title, idAppunto):

        #definisco il frame principale (la window)
        wx.Frame.__init__(self, parent, ID, title,wx.DefaultPosition,
                            wx.Size(400,220),  wx.DEFAULT_FRAME_STYLE & ~ (wx.RESIZE_BOX ))

        #textarea
        textarea = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE|wx.BORDER_SUNKEN|
                                wx.TE_RICH2, size=(200,100))

        #proprieta usertext dell'oggetto
        self.usertext = textarea
        self.title = title
        self.idAppunto = idAppunto


        self.Bind(wx.EVT_CLOSE, self.OnClose)


    def OnClose(self, event):

        fm = FileManager.Instance()
        fm.save(self.idAppunto, self.title, self.usertext.GetValue())
        print self.usertext.GetValue()
        self.Destroy()

#wx.EXPAND
        """
        #ppannello per i controlli
        userin = wx.Panel(self, -1, (0,100), (200,100))
        wx.StaticText(userin, -1, "Type\nHere", pos=(15,0))
        userbox = wx.TextCtrl(userin, -1, "", pos=(48,5))
        self.box1 = userbox

        # ------ Button to take text from userbox and place it in textarea
        Press = wx.Button(userin, -1, "Press", (60,30))

        Press.Bind(wx.EVT_BUTTON, self.inserttext)


    def inserttext(self, event):
        getit = self.box1.GetLineText(1)
        print getit
        self.box1.Clear()
        self.usertext.AppendText(getit)

    def mouseclick(self, event):

        self.box1.Clear()

"""

"""class MainApp(wx.App):
    def OnInit(self):
        myWindow = FrameAppunto(None, -1, "Text to Textarea")
        myWindow.Show(True)
        self.SetTopWindow(myWindow)
        return(True)

AppStart = MainApp(0)
AppStart.MainLoop()
"""