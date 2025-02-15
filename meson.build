project('realogicman',
          version: '0.1.0',
    meson_version: '>= 1.0.0',
  default_options: [ 'warning_level=2', 'werror=false', ],
)

i18n = import('i18n')
gnome = import('gnome')

subdir('data')
subdir('src')
subdir('po')

# Aggiungo al progetto una directory 'risorse_dir'
subdir('risorse_app')

gnome.post_install(
     glib_compile_schemas: true,
    gtk_update_icon_cache: true,
  update_desktop_database: true,
)
