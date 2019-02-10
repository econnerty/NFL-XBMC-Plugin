import sys
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
import urllib, urllib2

import addon
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def login(driver):

    element = driver.find_element_by_name("Email")
    element.send_keys("erk3452@gmail.com")

    element = driver.find_element_by_id("Password")
    element.send_keys("Elc@28946")

    driver.find_element_by_tag_name("button").click()


def makeLink(params, baseUrl=sys.argv[0]):
    """
    Build a link with the specified base URL and parameters

    Parameters:
    params: the params to be added to the URL
    BaseURL: the base URL, sys.argv[0] by default
    """
    return baseUrl + '?' + urllib.urlencode(
        dict([k.encode('utf-8'), unicode(v).encode('utf-8')] for k, v in params.items()))


def listOldGame(driver):

    driver


    elements = .find_elements_by_tag_name("option")
    for element in elements:
        xbmcgui.Dialog().ok('ELements', elements.)
    return elements

    # for i in range(0,3):
    #
    #     liz = xbmcgui.ListItem(elements[i].text, iconImage="DefaultFolder.png")
    #     liz.setInfo(type="Video", infoLabels={"Title": elements[i].text})
    #     xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url="", listitem=liz, isFolder=True)
    #     xbmcplugin.endOfDirectory(int(sys.argv[1]))


def showError(addonId, errorMessage):
    """
    Shows an error to the user and logs it

    Parameters:
    addonId: the current addon id
    message: the message to be shown
    """
    xbmc.log(errorMessage, xbmc.LOGERROR)


def parseParameters(listings, inputString=sys.argv[2]):
    """Parses a parameter string starting at the first ? found in inputString

    Argument:
    inputString: the string to be parsed, sys.argv[2] by default

    Returns a dictionary with parameter names as keys and parameter values as values
    """
    xbmcgui.Dialog().ok('PARSEPARAMS', sys.argv[2])
    parameters = {}
    p1 = inputString.find('?')
    if p1 >= 0:
        splitParameters = inputString[p1 + 1:].split('&')
        for nameValuePair in splitParameters:
            if (len(nameValuePair) > 0):
                pair = nameValuePair.split('=')
                key = pair[0]
                value = listings
                parameters[key] = value
    return parameters
