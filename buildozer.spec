[app]

# 🔥 ОБЯЗАТЕЛЬНЫЕ ПОЛЯ
title = MyPdfApp
package.name = mypdfapp
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf

version = 1.0

# 🔥 Python / зависимости
requirements = python3,kivy,plyer

# 🔥 Android настройки
orientation = portrait
fullscreen = 0

# 🔥 permissions (если нужны)
android.permissions = INTERNET

# 🔥 SDK настройки
android.api = 34
android.minapi = 24
android.ndk = 27.3.13750724

# 🔥 архитектуры
android.archs = arm64-v8a,armeabi-v7a

# ------------------------

[buildozer]

log_level = 2
warn_on_root = 0
