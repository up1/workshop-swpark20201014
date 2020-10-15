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

Send data to exchange
    Create Rabbitmq Connection  ${SERVER}  15672  5672    
    ...  ${USER}    ${PASSWORD}    alias=rmq   vhost=/
    Publish Message	   exchange_name=amq.topic
    ...  routing_key=send.test.message	  payload=test
    Binding Exchange With Queue	 exchange_name=amq.topic
    ...  queue_name=testQueue	routing_key=send.test.message
    ${msg}=  Get Message	 queue_name=testQueue	
    ...  count=1  requeue=false	  encoding=auto
    ...  truncate=50000  vhost=/
    Log List	${msg}
    Log    ${msg[0]['payload']}
    Should Be Equal   test   ${msg[0]['payload']}
    Close All Rabbitmq Connections