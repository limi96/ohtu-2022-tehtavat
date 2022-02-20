*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py
Resource  resource.robot

*** Keywords ***


Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    Main Page Should Be Open

Submit Credentials
    Click Button  Login

Login After Registration
    [Arguments]  ${username}  ${password}
    Go To Login Page
    Set Username  ${username}
    Set Password  ${password}
    Submit Credentials

