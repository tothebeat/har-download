from selenium import webdriver
import time

profile = webdriver.FirefoxProfile()
# Get a version of firebug compatible with your version of firefox:
# https://getfirebug.com/releases/firebug/
profile.add_extension('./firefox-extensions/firebug-1.12.5.xpi')
# Get a version of netexport compatible with the above firebug 
# version: https://getfirebug.com/releases/netexport/
profile.add_extension('./firefox-extensions/netExport-0.9b4.xpi')
# Setting firebug preferences
profile.set_preference("extensions.firebug.currentVersion", "2.0")
profile.set_preference("extensions.firebug.addonBarOpened", True)
profile.set_preference("extensions.firebug.console.enableSites", True)
profile.set_preference("extensions.firebug.script.enableSites", True)
profile.set_preference("extensions.firebug.net.enableSites", True)
profile.set_preference("extensions.firebug.previousPlacement", 1)
profile.set_preference("extensions.firebug.allPagesActivation", "on")
profile.set_preference("extensions.firebug.onByDefault", True)
profile.set_preference("extensions.firebug.defaultPanelName", "net")
# Setting netExport preferences
profile.set_preference("extensions.firebug.netexport.alwaysEnableAutoExport", True)
profile.set_preference("extensions.firebug.netexport.autoExportToFile", True)
profile.set_preference("extensions.firebug.netexport.Automation", True)
profile.set_preference("extensions.firebug.netexport.showPreview", False)
profile.set_preference("extensions.firebug.netexport.defaultLogDir", "/home/nick/src/har-download/netexport/")

browser = webdriver.Firefox(profile)
# Wait for firebug and netexport to load
time.sleep(5)
# Scanned book page using OpenSeadragon with Deep Zoom tiled images
# From Polonsky Foundation Digitization Project http://bav.bodleian.ox.ac.uk/
browser.get('http://bav.bodleian.ox.ac.uk/icv/page.php?book=arch._b_b.10&page=3')
# Wait for page to load
time.sleep(5)
zoom_in_button = browser.find_element_by_id('zoom-in')
for i in range(4):
	zoom_in_button.click()
	time.sleep(1)
# Wait for netexport to save the HAR file
time.sleep(20)
browser.quit()
