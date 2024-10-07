
from hack_ui import MyUI_Hack

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib
from gi.repository import Vte

AVAILABLE = ['MyPrefs2']

import terminatorlib.plugin as plugin
from terminatorlib.terminal import PrefsEditor



class MyPrefs2(plugin.MenuItem, MyUI_Hack):
    capabilities = ['terminal_menu']
    def __init__(self):
        print('--MyPrefs2 __init__')
        # plugin.MenuItem.__init__(self)
        # super(MyPrefs, self).__init__()
        super().__init__()
        self.ui = None
        self.setup_prefs()

    def callback(self, menuitems, menu, terminal):
        item = Gtk.CheckMenuItem(' -  MyPrefs2')
        menuitems.append(item)
        # print('MyPrefs2 __init__..')

    def show_my_ui(self):
        if self.ui:
            return self.ui

        # ------ new ui
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.my_ui = vbox

        label = Gtk.Label(label="Prefs for " + self.__class__.__name__)
        # input = Gtk.Entry(text='world')
        button = Gtk.Button(label="test")

        def on_btn_click(button):
            print('--button click!')

        button.connect("clicked", on_btn_click)

        # Add the new widgets to the vbox
        vbox.pack_start(label, False, False, 0)
        # vbox.pack_start(input, False, False, 0)
        vbox.pack_start(button, False, False, 0)

        vbox.set_margin_top(20)
        vbox.set_margin_bottom(20)
        vbox.set_margin_start(15)
        vbox.set_margin_end(15)

        return vbox
