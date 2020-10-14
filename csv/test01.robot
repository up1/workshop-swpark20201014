*** Settings ***
Library   Employee

*** Test Cases ***
List all test data from csv file
    ${datas}=  employee.Read All
    FOR  ${row}  IN  @{datas}
        Log To Console   ${row}[0]-${row}[1]
    END