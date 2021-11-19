*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***

Register With Valid Username And password
    Input Credentials  testi  validPass1
    Output Should Contain  New user registered

Register With Already Taken Usermane And Valid Password
    Input Credentials  kalle  validPass1
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kahdeksan8
    Output Should Contain  Username is too short (3 or longer)

Register With Valid Username And Too Short Password
    Input Credentials  jolle  moi1
    Output Should Contain  Password is too short (8 or longer)

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kahdeksaN
    Output Should Contain  Password cant contain only letters

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command