*** Settings ***
Library   HelloLibrary

*** Test Cases ***
Try to say hi all
    HelloLibrary.Say hi all   id=1   name=somkiat  age=30

Hello with default value and age
    HelloLibrary.Try To Send Data With   age=50   name=joe
    HelloLibrary.Result Should Be   Hi, joe

Hello with default value
    HelloLibrary.Try To Send Data With
    HelloLibrary.Result Should Be   Hi, demo

Hello with somkiat
    HelloLibrary.Try To Send Data With   somkiat
    HelloLibrary.Result Should Be   Hi, somkiat