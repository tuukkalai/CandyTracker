*** Settings ***
Resource        resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close All Browsers

*** Test Cases ***
Test Should Run And Pass
    Should Be True      1 < 2

User Can Open Home Page
    Go To   ${HOME URL}
    Home Page Should Be Open