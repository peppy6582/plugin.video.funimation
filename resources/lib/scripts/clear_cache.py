import os
import StorageServer
import CommonFunctions
import xbmc
import xbmcaddon

addon = xbmcaddon.Addon('plugin.video.funimation')
name = addon.getAddonInfo('name')
icon = addon.getAddonInfo('icon')

duration = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10][int(addon.getSetting('notification_length'))]) * 1000
msg = addon.getLocalizedString(30602)

common = CommonFunctions
common.dbg = addon.getSetting('debug') == 'true'
common.dbglevel = 5

common.log('clearing cache')
cache = StorageServer.StorageServer(name).delete('%')

cookie_path = xbmc.translatePath(addon.getAddonInfo('profile'))
cookie_path = os.path.join(cookie_path, 'fun-cookiejar.txt')
if os.path.exists(cookie_path):
    common.log('Deleting cookie')
    os.remove(cookie_path)

xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(name, msg, duration, icon))
