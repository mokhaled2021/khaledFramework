*** Settings ***
Library         SeleniumLibrary
Variables       ../Locators/locators.py
Resource        ../commons/LoginPage.robot


*** Variables ***
${site_url}     https://sis.medadstg.com
${login}        /#login
${browser}      Chrome
#read from json file
${json} =       Get file    ${EXECDIR}\\PageObjects\\TestData\\testdata.json
${object} =     Evaluate    json.loads('''${json}''')    json


*** Keywords ***
Opening Browser
    [Arguments]    ${site_url}    ${browser}
    Open Browser    ${site_url}    ${browser}
    Wait Until Page Contains Element    ${Username_Locator}

Open the AcademicStructure page
    Click Element    ${Academic_Structure}

Open the Admission page
    Click Element    ${Admission_Link}

closing Browser
    close Browser