*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123123

Register With Already Taken Username And Valid Password
# ...
    Input Credentials  kalle  kalle123123
    Input New Command 
    Input Credentials  kalle  kalle123123
    Output Should Contain  Username is already taken

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input Credentials  kalle  kalle
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  password
    Output Should Contain  Password must not contain only letters