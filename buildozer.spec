[app]

title = MyPdfApp

package.name = mypdfapp
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,pdf

version = 0.1

requirements = python3,kivy,plyer,PyMuPDF

orientation = portrait
fullscreen = 0

icon.filename = icon.png

android.api = 34
android.minapi = 24
android.build_tools_version = 34.0.0

# фикс, чтобы не тянул unstable версии
p4a.branch = stable

android.archs = arm64-v8a, armeabi-v7a

# убираем MANAGE_EXTERNAL_STORAGE (он часто ломает/не проходит сборку/плеймаркет)
android.permissions = READ_EXTERNAL_STORAGE

presplash.color = #FFFFFF


[buildozer]

log_level = 2
warn_on_root = 0
