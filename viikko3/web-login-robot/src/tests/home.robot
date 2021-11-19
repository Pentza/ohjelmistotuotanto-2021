*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Test Cases ***
Click Login Link
    Click Link  Login
    Click Login Should Succeed

Click Register Link
    Click Link  Register new user
    Click Register Should Succeed

*** Keywords ***
Click Login Should Succeed
    Login Page Should Be Open

Click Register Should Succeed
    Register Page Should Be Open