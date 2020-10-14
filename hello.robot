*** Settings ***
Library   hello.py

*** Test Cases ***
Hello with somkiat
    ${result}=  hello.Say Hi   somkiat
    Should Be Equal   Hi, somkiat    ${result}