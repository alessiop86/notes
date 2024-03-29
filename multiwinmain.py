import wx

from frameappunto import FrameAppunto
from filemanager import FileManager


ID_NEW = 1
#ID_RENAME = 2 #TODO
ID_DELETE = 4


class PostItVirtuali(wx.Frame):
    def __init__(self, parent, id, title):

        wx.Frame.__init__(self, parent, id, title, size=(400, 220))

        #creo un panel
        panel = wx.Panel(self, -1)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.listbox = wx.ListBox(panel, -1)
        hbox.Add(self.listbox, 1, wx.EXPAND | wx.ALL, 20)

        #pannello dei bottoni
        btnPanel = wx.Panel(panel, -1)
        new = wx.Button(btnPanel, ID_NEW, 'New', size=(90, 30))
      #  ren = wx.Button(btnPanel, ID_RENAME, 'Rename', size=(90, 30))
        dlt = wx.Button(btnPanel, ID_DELETE, 'Delete', size=(90, 30))


        #definisco eventi associati ai bottoni
        self.Bind(wx.EVT_BUTTON, self.NewItem, id=ID_NEW)
        #self.Bind(wx.EVT_BUTTON, self.OnRename, id=ID_RENAME)
        self.Bind(wx.EVT_BUTTON, self.OnDelete, id=ID_DELETE)
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.wantToEdit)

        #verticalbox su cui metto i bottoni
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add((-1, 20))
        vbox.Add(new)
       # vbox.Add(ren, 0, wx.TOP, 5)
        vbox.Add(dlt, 0, wx.TOP, 5)

        btnPanel.SetSizer(vbox)
        hbox.Add(btnPanel, 0.6, wx.EXPAND | wx.RIGHT, 20)
        panel.SetSizer(hbox)

        self.Centre()
        self.Show(True)
        self.loadDataAndRefreshListBox()

    def loadDataAndRefreshListBox(self):
        self.listbox.Clear()
        fm = FileManager.Instance()
        dictionary = fm.getDictionary()
        files = dictionary['files']
        print files
        for obj in files:
            self.listbox.Append(obj['title'],str(obj['id']))

    def wantToEdit(self,event):
        selectedIndex = self.listbox.GetSelection()
        selectedTitle = self.listbox.GetStringSelection()
        selectedId = self.listbox.GetClientData(selectedIndex)
        displayedTitle = "(" + str(selectedId) + ".txt)" + selectedTitle
        myWindow = FrameAppunto(None, -1, displayedTitle ,selectedId,self)
        myWindow.Show(True)
        #self.SetTopWindow(myWindow)


    def NewItem(self, event):

        title = wx.GetTextFromUser('Nome della nota', ':-)')
        if title != '':
        #   self.listbox.Append(text)
            myWindow = FrameAppunto(None, -1, title,0,self)
            myWindow.Show(True)
            #self.SetTopWindow(myWindow)
            #self.loadDataAndRefreshListBox()

    #TODO
    """
    def OnRename(self, event):
        sel = self.listbox.GetSelection()
        text = self.listbox.GetString(sel)
        renamed = wx.GetTextFromUser('Rename item', 'Rename dialog', text)
        if renamed != '':
            self.listbox.Delete(sel)
            self.listbox.Insert(renamed, sel)
    """


    def OnDelete(self, event):
        selectedIndex = self.listbox.GetSelection()
        selectedId = self.listbox.GetClientData(selectedIndex)
        #print self.listbox.GetString()

        fm = FileManager.Instance()
        fm.delete(selectedId)

        if selectedIndex != -1:
            self.listbox.Delete(selectedIndex)


#Lancio l'app
app = wx.App()
PostItVirtuali(None, -1, 'NonMiFreghiPiuDonnaDellePulizie') #parent, id, titolo
app.MainLoop()

