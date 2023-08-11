# botch

quick botch to convert some csv data into output, which can be copy and pasted into JSON

## background

We were faced with manually adding entities to our chatbot agent in Dialog Flow CX. This would have meant one manual entry through a web-interface for each car brand available for purchase in the UK.

Setting up a solution via API would have taken too long to implement and get sign-off for, and we had a deadline of a POC; so I wrote this python script to convert the entries of a CSV file into a plain txt output that we could me copy & paste into a JSON backup of our agent, without the need for further editing.
