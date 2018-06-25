import gi

gi.require_version("Gtk", "2.0")
from gi.repository import Gtk

win = Gtk.Window()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
