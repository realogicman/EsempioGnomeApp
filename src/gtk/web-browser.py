#!/usr/bin/env python

# Portions and Adaptations Copyright 2023-2024 Hin-Tak Leung
# - Ported to GTK4

# This was originally written by Julita Inca AFAIK, first posted in
# https://lleksah.wordpress.com/2017/07/31/writing-my-first-web-browser-in-python-with-gtk/

# Marco Angeli, Febbraio 2025 - Adattamenti per integrazione su altro progetto
# Scaricato da: https://github.com/HinTak/minimal-web-browsers/blob/main/WebKitGTK4-example.py

import gi
gi.require_version('Gtk', '4.0')
gi.require_version('WebKit', '6.0')
gi.require_version("Adw", "1")

from gi.repository import Gtk, WebKit, GLib, Adw

Adw.init()

import sys, os
pathname = os.path.dirname(sys.argv[0])
HOME_PAGE = ("file://" + os.path.abspath(pathname) + "/")

webview = WebKit.WebView()
entry = Gtk.Entry()

def open_page(url):
    entry.set_text(url)
    webview.load_uri(url)

def on_load_changed(webview, event):
    url = webview.get_uri ()
    entry.set_text(url)

def on_enter(entry):
    url = entry.get_text()
    webview.load_uri(url)
    open_page(url)

def on_go_back(button):
    webview.go_back()

def on_go_forward(button):
    webview.go_forward()

import sys
if len(sys.argv) > 1:
    open_page(sys.argv[1])
else:
    open_page(HOME_PAGE)

webview.connect("load-changed", on_load_changed)

headerbar = Gtk.HeaderBar()
headerbar.set_show_title_buttons(True)

go_back_button = Gtk.Button.new_from_icon_name("go-previous")
go_back_button.connect("clicked", on_go_back)

go_forward_button = Gtk.Button.new_from_icon_name("go-next")
go_forward_button.connect("clicked", on_go_forward)

headerbar.pack_start(go_back_button)
headerbar.pack_start(go_forward_button)

entry.connect("activate", on_enter)
headerbar.set_title_widget(entry)

def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)
    win.set_title("GTK Browser")
    win.set_default_size(800,500)
    win.set_titlebar(headerbar)
    win.set_child(webview)
    entry.set_width_chars(40)
    #entry.set_editable(0)
    #entry.set_visible(0)
    win.present()

app = Gtk.Application()
app.connect('activate', on_activate)

app.run(None)
