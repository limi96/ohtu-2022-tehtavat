*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page And Click Register Link

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kallekalle
    Set Password  kalle123123
    Set Password Confirm  kalle123123
    Click Register Button
    Register Welcome Should Be Open

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123123
    Set Password Confirm  kalle123123
    Click Register Button
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  kallekalle
    Set Password  ka
    Set Password Confirm  ka
    Click Register Button
    Register Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Set Username  kallekallekalle
    Set Password  kalle123123444444444444
    Set Password Confirm  kalle123123
    Click Register Button
    Register Should Fail With Message  Passwords do not match

*** Keywords *** 



Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirm
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Click Register Button
    Click Button  Register

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}