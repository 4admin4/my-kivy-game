[app]
title = GuessNumber
package.name = guessgame
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy

# Налаштування Android
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# КРИТИЧНІ НАЛАШТУВАННЯ ДЛЯ ГІТХАБУ
android.api = 31
android.minapi = 21
android.sdk = 31
android.build_tools_version = 33.0.0
android.accept_sdk_license = True
android.skip_update = True
