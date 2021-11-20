*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  notkalle
    Set Password  password123
    Set Password Confirmation  password123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  mo
    Set Password  password123
    Set Password Confirmation  password123
    Submit Credentials
    Register Should Fail With Message  Username is too short (3 or longer)

Register With Valid Username And Too Short Password
    Set Username  testaaja
    Set Password  pass
    Set Password Confirmation  pass
    Submit Credentials
    Register Should Fail With Message  Password is too short (8 or longer)

Register With Nonmatching Password And Password Confirmation
    Set Username  testaaja
    Set Password  password123
    Set Password Confirmation  password12
    Submit Credentials
    Register Should Fail With Message  Password and confirmation doesn't match

Login After Successful Registration
    Set Username  notkalle
    Set Password  password123
    Set Password Confirmation  password123
    Submit Credentials
    Register Should Succeed
    Click Link  Continue to main page
    Main Page Should Be Open
    Click Button  Logout
    Login Page Should Be Open
    Set Username  notkalle
    Set Password  password123
    Click Button  Login
    Login Should Succeed

Login After Failed Registration
    Set Username  kalle
    Set Password  password123
    Set Password Confirmation  password123
    Submit Credentials
    Register Should Fail With Message  User with username kalle already exists
    Go To Login Page
    Login Page Should Be Open
    Set Username  notkalle
    Set Password  password123
    Click Button  Login
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${passwordConfirmation}
    Input Password  password_confirmation  ${passwordConfirmation}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open