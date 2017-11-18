import logmet

lm = logmet.Logmet(
    logmet_host='logs.ng.bluemix.net',
    logmet_port=9091,
    space_id='45c44221-e724-4591-81d3-4a36a4994e37',
    token='YGOba3BzMiWN'
)

# Emitting a string will map the string to the "message" field in Logmet Kibana
lm.emit_log('This is a log message')

# You can also emit a dictionary with additional fields.
# These can be searched and filtered on in Logmet Kibana.
lm.emit_log(
    {'app_name': 'myApp',
     'type': 'myType',
     'message': 'This is a log message'}
)

