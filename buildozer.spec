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

# ⚠️ лучше убрать принудительную версию build-tools
# android.build_tools_version = 34.0.0

p4a.branch = master
android.release_artifact = apk

android.archs = arm64-v8a, armeabi-v7a

android.permissions = READ_EXTERNAL_STORAGE

presplash.color = #FFFFFF

# 🔥 ДОБАВЛЕНО ТЕБЕ
android.accept_sdk_license = True
android.skip_update = False


[buildozer]

log_level = 2
warn_on_root = 0
