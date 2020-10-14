*** Settings ***
Library   CalculatorLibrary

*** Test Cases ***
กดที่ละปุ่ม 1+2
    CalculatorLibrary.Push button  1
    CalculatorLibrary.Push button  +
    CalculatorLibrary.Push button  2
    CalculatorLibrary.Push button  =
    CalculatorLibrary.Result should be  3

กด 1+2+3=
    CalculatorLibrary.Push buttons  1+2+3=
    CalculatorLibrary.Result should be  6