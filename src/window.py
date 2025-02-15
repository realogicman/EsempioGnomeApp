# window.py
#
# Copyright 2025 Marco Angeli
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Adw
from gi.repository import Gtk
from gi.repository import Gio

@Gtk.Template(resource_path='/org/altervista/ReaLoGiCMaN/window.ui')
class RealogicmanWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'RealogicmanWindow'

    # Oggetti con i quali c'è interazione (dichiarazione obbligatoria)
    entryInput = Gtk.Template.Child()
    lbOutput = Gtk.Template.Child()
    tvLeggimiBuffer = Gtk.Template.Child()
    mediaVideo = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Questo serve solo per il debug
        self.mostra_testo_label()
        self.mostra_testo_entryInput()
        self.carica_file_leggimi()
        self.apri_file_video()

    # Questo serve solo per il debug
    # Scopro il percorso delle risorse disponibili
    # Decommentare le seguenti righe per attivare - salva in '/home/utente'
    #import os
    #os.system('ls /app/share -alR > ~/ElencoFile.txt')

    # Questo serve solo per il debug
    def mostra_testo_entryInput(self):
        if self.entryInput:
            testo = self.entryInput.get_text()
            print(f"Testo della casella di input: {testo}")

    # Questo serve solo per il debug
    def mostra_testo_label(self):
        if self.lbOutput:
            testo = self.lbOutput.get_text()
            print(f"Testo della label: {testo}")

    # Questo intercetta il segnale "Click" del pulsante
    @Gtk.Template.Callback('btWebbrowser_Cliccato')
    def btWebbrowser_Cliccato(self, *args):
        print('Avvio browser...')
        import subprocess
        subprocess.run(["xdg-open http://realogicman.altervista.org/"], shell=True)

    # Questo intercetta il segnale "Click" del pulsante
    @Gtk.Template.Callback('btInput_Cliccato')
    def btInput_Cliccato(self, *args):
        if self.entryInput:
            testo = self.entryInput.get_text()
            self.lbOutput.set_text(testo)
            print(f"Testo della label modificato in: {testo}")

    # Questo intercetta il tasto INVIO sull' entryInput
    @Gtk.Template.Callback('entryInput_Attivato')
    def entryInput_Attivato(self, *args):
        self.btInput_Cliccato()

    # Questo intercetta il segnale "Click" del pulsante
    @Gtk.Template.Callback('btWBrowserPy_Cliccato')
    def btWBrowserPy_Cliccato(self, *args):
        if self.entryInput:
            print(f"Avvio dello script 'webbrowser.py'...")
            scriptBrowser = ("/app/bin/webbrowser.py")
            urlBersaglio = ("file:///app/share/risorse/Leggimi.txt")
            comando = (scriptBrowser + " " + urlBersaglio + " &")
            #import os
            #os.system(comando)
            import subprocess
            subprocess.run([comando], shell=True)

    # Apre il file video (richiede "Gio")
    def apri_file_video(self):
        if self.mediaVideo:
            file = "file:///app/share/risorse/video.webm"
            gio_file = Gio.File.new_for_uri(file)
            self.mediaVideo.set_file(gio_file)
            print(f"Nome del file video caricato: {file}")

    # Carica il file "Leggimi.txt"
    def carica_file_leggimi(self):
        if self.tvLeggimiBuffer:
            file = open("/app/share/risorse/Leggimi.txt", "r")
            testo = file.read()
            self.tvLeggimiBuffer.set_text(testo)
            print(f"File caricato nel TextView: {file}")
            file.close()
            