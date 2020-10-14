*** Settings ***
Library   RequestsLibrary
Library   OperatingSystem
Library   Collections

*** Test Cases ***
Post Request With File
    Create Session    httpbin    http://httpbin.org    debug=2    max_retries=10
    ${file_data}=    Get Binary File    ${CURDIR}${/}data.json
    ${files}=    Create Dictionary    file    ${file_data}
    ${resp}=    Post Request    httpbin    /post    files=${files}
    Log To Console   ${resp.json()}
    ${file}=    To Json    ${resp.json()['files']['file']}
    Dictionary Should Contain Key    ${file}    data1
    Dictionary Should Contain Key    ${file}    data2