*** Settings ***
Library         SeleniumLibrary
Variables       ../Locators/locators.py
Resource        ../commons/LoginPage.robot
Library         RequestsLibrary
Library         Collections
Library         OperatingSystem


*** Variables ***
${site_url}     https://cmp-test.medadstg.com
${login}        /#login
${browser}      Chrome

#read from json file
${json}         Get file    ${EXECDIR}\\PageObjects\\TestData\\testdata.json
${object}       Evaluate    json.loads('''${json}''')    json


*** Keywords ***
Opening Browser
    [Arguments]    ${site_url}    ${browser}
    Open Browser    ${site_url}    ${browser}
    Wait Until Page Contains Element    ${Username_Locator}

Open the AcademicStructure page
    Click Element    ${Academic_Structure}

Open the Admission page
    Click Element    ${Admission_Link}

Successfully Messages Appears After Submitting
    Sleep    2
    Wait Until Page Contains Element    ${Successfully_Saved}
    Sleep    1

Delete Doctype By Name
    [Arguments]    ${doctype}    ${doctypevalue}
    ${authorization}=    Create List    d969e59bcd0761b    30c81a805de0ef7
    Create Session    DeleteDoctype    ${site_url}    auth=${authorization}
    ${response}=    DELETE On Session    DeleteDoctype    /api/resource/${doctype}/${doctypevalue}
    ${status}=    Convert To String    ${response.status_code}
    Should Be Equal    ${status}    202

closing Browser
    close Browser
