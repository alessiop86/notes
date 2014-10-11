import wx
import sys
from filemanager import  FileManager

class FrameAppunto(wx.Frame):


    def __init__(self, parent, ID, title, idAppunto,father):

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
        self.father = father


        if (idAppunto != 0):
            fm = FileManager.Instance()
            text = fm.getTextEsistente(idAppunto)
            self.usertext.SetValue(text)

        self.Bind(wx.EVT_CLOSE, self.OnClose)


    def OnClose(self, event):

        try:
            fm = FileManager.Instance()

            if  (str(self.idAppunto) == str(0)):
                fm.salvaNuovo(self.title, self.usertext.GetValue())
            else:
                fm.salvaEsistente(self.idAppunto, self.usertext.GetValue())
            self.father.loadDataAndRefreshListBox()
        except:
            print "Unexpected error:", sys.exc_info()
        self.Destroy()

