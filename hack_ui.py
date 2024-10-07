'''
Terminator plugin helper
   to implement custom plugin configration (at Preferences >> Plugins tab)
   which Not Originally supported

 Author: yurenchen@yeah.net
License: GPLv2
   Site: https://github.com/yurenchen000/terminator-plugins
'''


import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import sys

## disable log
# print = lambda *a:None

## HACK to support plugin configration page
class MyUI_Hack:
    def __init__(self):
        print('--MyUI_Hack __init__', self)
        # self.setup_prefs()
        pass

    ## HACK: should not change this func, just implement .show_my_ui()
    def setup_prefs(self):
        ## HACK: override PrefsEditor class, inject custom UI
        prefseditor = sys.modules.get('terminatorlib.prefseditor')
        # print('--plugin:', prefseditor, prefseditor.PrefsEditor.set_plugin)
        
        ## reg ui handle
        prefs = prefseditor.PrefsEditor
        if not hasattr(prefs, 'my_ui_handles'):
            setattr(prefs, 'my_ui_handles', {})
        print('---reg ui:', self.__class__.__name__, self)
        prefs.my_ui_handles[self.__class__.__name__] = self

        ## call ui handle
        def _set_plugin(prefs, plugin):
            if not hasattr(prefs, 'orig_ui'):
                pluginpanelabel = prefs.builder.get_object('pluginpanelabel')
                # pluginconfig = _self.config.plugin_get_config(plugin)
                setattr(prefs, 'orig_ui', pluginpanelabel)
                # print('--set_plugin:', plugin)

                parent_ui = prefs.orig_ui.get_parent()
                # print('--show_my_ui:', parent_ui)
                setattr(prefs, 'parent_ui', parent_ui)

            ## hide preview ui
            prefs.parent_ui.remove(prefs.parent_ui.get_children()[1])
            
            ## show current ui
            if plugin in prefs.my_ui_handles:
                vbox = prefs.my_ui_handles.get(plugin).show_my_ui()
                prefs.parent_ui.add2(vbox)
                prefs.parent_ui.show_all()
            else:
                if prefs.parent_ui:
                    prefs.parent_ui.add2(prefs.orig_ui)
                prefs.orig_ui.set_text('world: ' + plugin)

        ## override PrefsEditor
        prefseditor.PrefsEditor.set_plugin = _set_plugin

    def show_my_ui(self):
        # ------ new ui
        label = Gtk.Label(label="prefs for " + self.__class__.__name__)
        return label
