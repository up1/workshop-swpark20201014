*** Settings ***
Library    RabbitMq
Library    Collections

*** Variables ***
${SERVER}    139.59.246.17
${USER}      admin
${PASSWORD}  xitgmLwmp


*** Test Cases ***
Simple Test
    Create Rabbitmq Connection  ${SERVER}  15672  5672    
    ...  ${USER}    ${PASSWORD}    alias=rmq   vhost=/
    ${overview}=    Overview
    Log Dictionary    ${overview} 
    Close All Rabbitmq Connections