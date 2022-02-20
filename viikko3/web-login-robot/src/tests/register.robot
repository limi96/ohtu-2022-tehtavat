*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page And Click Register Link

*** Test Cases ***
Register With Valid Username And Password
    Register New Account  kallekalle  kalle123123  kalle123123
    Register Welcome Should Be Open

Register With Too Short Username And Valid Password
    Register New Account  ka  kalle123123  kalle123123
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Register New Account  kallekalle  ka  ka
    Register Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Register New Account  kallekallekalle  kalle123123444444444444  kalle123123
    Register Should Fail With Message  Passwords do not match

Login After Successful Registration
    Register New Account  omenapuu  kalle123123  kalle123123
    Login After Registration  omenapuu  kalle123123
    Login Should Succeed
    
Login After Failed Registration
    Register New Account  kallekallekalle123  kalle123123444444444444  kalle123123
    Login After Registration  kallekallekalle123  kalle123123444444444444
    Login Should Fail With Message  Invalid username or password

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

Register New Account
    [Arguments]  ${username}  ${password}  ${password_confirmation}

    Set Username  ${username}
    Set Password  ${password}
    Set Password Confirm  ${password_confirmation}
    Click Register Button


Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

