[app]

title = MyPdfApp

package.name = mypdfapp

package.domain = org.example

source.dir = .

source.include_exts = py,png,jpg,kv,pdf

version = 0.1

requirements = python3,kivy,plyer,pymupdf

orientation = portrait

fullscreen = 0

icon.filename = icon.png

android.api = 34
android.minapi = 24

android.archs = arm64-v8a, armeabi-v7a

android.permissions = READ_EXTERNAL_STORAGE

presplash.color = #FFFFFF


[buildozer]

log_level = 2

warn_on_root = 1