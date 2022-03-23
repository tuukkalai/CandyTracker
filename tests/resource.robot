*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  chrome
${DELAY}  0.2 seconds
${HOME URL}  http://${SERVER}
${REGISTER URL}  http://${SERVER}/register

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Home Page Should Be Open
    Title Should Be  CandyTracker

Go To Sign Up Page
    Go To  ${REGISTER URL}

Sign Up Page Should Be Open
    Page Should Contain     Create new user
