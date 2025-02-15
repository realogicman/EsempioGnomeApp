application_id = 'org.altervista.ReaLoGiCMaN'

# Copia l'intera directory 'risorse' nella destinazione finale 'share'
install_subdir('risorse', install_dir: join_paths(get_option('prefix'), 'share'))

# Copia altri file dalla cartella '../src'

# File sorgente della finestra 'window.ui' (tanto per...)
window_cmb = '../src'
install_data(
  window_cmb / ('window.cmb'),
  install_dir: get_option('datadir') / 'risorse'
)

# Rendo lo script 'webbrowser.py' eseguibile
configure_file(
  input: 'webbrowser.py',
  output: 'webbrowser.py',
  #configuration: conf,
  copy: true,
  install: true,
  install_dir: get_option('prefix') / 'bin',
  install_mode: 'r-xr-xr-x'
)
