# -*- coding: utf-8 -*-
import sys
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
import urllib, urllib2, urlparse
import NFLGame, NFLYear
from selenium import webdriver


driver = webdriver.PhantomJS()
listing = []
update = True

def login():
    element = driver.find_element_by_name("Email")
    element.send_keys("erk3452@gmail.com")
    element = driver.find_element_by_id("Password")
    element.send_keys("Elc@28946")

    driver.find_element_by_tag_name("button").click()

def endListing():
    """
    Signals the end of the menu listing
    """
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def makeLink(params, baseUrl=sys.argv[0]):
    """
    Build a link with the specified base URL and parameters

    Parameters:
    params: the params to be added to the URL
    BaseURL: the base URL, sys.argv[0] by default
    """
    return baseUrl + '?' + urllib.urlencode(unicode(0).encode(params))


def getYears():
    year = NFLYear()

    years = []
    years[0] = year

    return years
    #Use built in JS functions to grab all the years from nfl2go
    #

def getGames():
    games = []
    game = NFLGame()
    game[0] = game
    return games


def showError(addonId, errorMessage):
    """
    Shows an error to the user and logs it

    Parameters:
    addonId: the current addon id
    message: the message to be shown
    """
    xbmc.log(errorMessage, xbmc.LOGERROR)


def parseParameters(inputString=sys.argv[2]):
    """Parses a parameter string starting at the first ? found in inputString

    Argument:
    inputString: the string to be parsed, sys.argv[2] by default

    Returns a dictionary with parameter names as keys and parameter values as values
    """



def playVideo():
    pass


def addMenuItem(title, link, icon=None, thumbnail=None, folder=False):
    """
    Add a menu item to the xbmc GUI

    Parameters:
    caption: the caption for the menu item
    icon: the icon for the menu item, displayed if the thumbnail is not accessible
    thumbail: the thumbnail for the menu item
    link: the link for the menu item
    folder: True if the menu item is a folder, false if it is a terminal menu item

    Returns True if the item is successfully added, False otherwise
    """
    listItem = xbmcgui.ListItem(unicode(title), iconImage=icon, thumbnailImage=thumbnail)
    listItem.setInfo(type="Video", infoLabels={"Title": title})
    return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=link, listitem=listItem, isFolder=folder)


def buildMenu():

    """
    Get the years in an array
    Get the games in an array

    Iterate through each your and build a folder with a menu item for each game containing the link

    ONLY ADD GAMES WHEN THE PLUGIN IS INVOCATED WITHIN A SUBFOLDER

    Use addMenuItem and change
    :return:
    """

    # list("years")
    #
    # parameters = parseParameters("test?t=")
    # if update:
    #     for list1 in listing:
    #         link = makeLink(list1)
    #         addMenuItem(list, link, 'DefaultVideo.png', None, True)
    #
    #     endListing()





def main():

    addon_base = sys.argv[0]
    addon_handle = int(sys.argv[1])
    args = urlparse.parse_qs(sys.argv[2][1:]
    driver.get("http://app.nfl2go.com/Account/Login?ReturnUrl=%2F")

    login()

    while True:
        parameters = parseParameters()

        if 'play' in parameters:
            playVideo()
        else:
            buildMenu()


if __name__ == "__main__":
    main()
