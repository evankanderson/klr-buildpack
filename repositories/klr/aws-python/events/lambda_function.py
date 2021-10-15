# This is the function that will be run. Feel free to extend or replace it!
def lambda_handler(event, context):
    """Handle event, which should be a CloudEvent with a JSON payload with 'first_name' and 'last_name' parameters.
    """
    message = 'Hello {} {}!'.format(event['data']['first_name'], event['data']['last_name'])  
    return { 
        'type': 'com.example.echo',
        'id': event['id'],
        'timestamp': event['timestamp'],
        'specversion': '1.0',
        'message' : message
    }
