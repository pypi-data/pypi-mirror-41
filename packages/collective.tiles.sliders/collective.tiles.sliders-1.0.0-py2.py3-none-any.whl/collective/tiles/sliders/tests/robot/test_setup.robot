*** Settings *****************************************************************
Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot
Resource  Selenium2Screenshots/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Keywords *****************************************************************
Crop page screenshot
    [Documentation]  Crops the given ``filename`` to
    ...              match the combined bounding box of the
    ...              elements matching the given ``locators``.
    ...
    ...              !!! can be removed when Crop page screenshot is
    ...              !!! updated to recognize devicepixelratio.
    ...
    ...              Requires at least two arguments
    ...              (``filename`` and at least one ``locator``).
    [Arguments]  ${filename}  @{locators}
    @{selectors} =  Create list
    :FOR  ${locator}  IN  @{locators}
    \  ${selector} =  Normalize annotation locator  ${locator}
    \  Append to list  ${selectors}  ${selector}
    ${selectors} =  Evaluate  "['%s']" % "', '".join(@{selectors})
    @{dimensions} =  Execute Javascript
    ...    return (function(){
    ...        var selectors = ${selectors}, i, target, offset;
    ...        var left = null, top = null, width = null, height = null;
    ...        var ratio = window.devicePixelRatio;
    ...        for (i = 0; i < selectors.length; i++) {
    ...            target = jQuery(selectors[i]);
    ...            if (target.length === 0) {
    ...                return [selectors[i], '', '', ''];
    ...            }
    ...            offset = target.offset();
    ...            if (left === null || width === null) {
    ...                width = target.outerWidth();
    ...            } else {
    ...                width = Math.max(
    ...                    left + width, offset.left + target.outerWidth()
    ...                ) - Math.min(left, offset.left);
    ...            }
    ...            if (top === null || height === null) {
    ...                height = target.outerHeight();
    ...            } else {
    ...                height = Math.max(
    ...                    top + height, offset.top + target.outerHeight()
    ...                ) - Math.min(top, offset.top);
    ...            }
    ...            if (left === null) { left = offset.left; }
    ...            else { left = Math.min(left, offset.left); }
    ...            if (top === null) { top = offset.top - jQuery(window).scrollTop(); }
    ...            else { top = Math.min(top, offset.top); }
    ...        }
    ...        return [Math.max(0, (left - ${CROP_MARGIN})*ratio),
    ...                Math.max(0, (top - ${CROP_MARGIN})*ratio),
    ...                Math.min(window.outerWidth*ratio, (width + ${CROP_MARGIN} * 2)*ratio),
    ...                (height + ${CROP_MARGIN} * 2)*ratio];
    ...    })();
    ${first} =  Evaluate  '@{dimensions}[0]'
    Should match regexp  ${first}  ^[\\d\\.]+$
    ...    msg=${first} was not found and no image was cropped
    Crop image  ${OUTPUT_DIR}  ${filename}  @{dimensions}


*** Test Cases ***************************************************************
Show how to activate the add-on
    Set window size  1024  768
    Enable autologin as  Manager
    Go to  ${PLONE_URL}/prefs_install_products_form

    Page should contain element  xpath=//*[@value='collective.tiles.sliders']

    Assign id to element
    ...     xpath=//*[@value='collective.tiles.sliders']/ancestor::section
    ...     addons-list

    Assign id to element
    ...     xpath=//*[@value='collective.tiles.sliders']/ancestor::li
    ...     addon

    Click Element  addons-list
    Highlight  addon

    Capture and crop page screenshot  addon_installed.png  addons-list

    Click button  xpath=//*[@value='collective.tiles.sliders']/ancestor::form//input[@type='submit']

    Page should contain element  xpath=//*[@value='collective.tiles.sliders']

    Assign id to element
    ...     xpath=//*[@value='collective.tiles.sliders']/ancestor::section
    ...     addons-list

    Assign id to element
    ...  xpath=//*[@value='collective.tiles.sliders']/ancestor::li
    ...  addon

    Click Element  addons-list
    Highlight  addon

    Capture and crop page screenshot  addon_installable.png  addons-list
