[app]
title = cband by keno666
package.name = cbandbykeno666
package.domain = com.keno666.cband
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.exclude_exts = spec
version = 1.0
orientation = portrait
fullscreen = 0
requirements = python3,kivy,requests,certifi,urllib3,charset-normalizer,idna
android.permissions = INTERNET,ACCESS_NETWORK_STATE
p4a.bootstrap = sdl2
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
[buildozer]
log_level = 2
warn_on_root = 1
