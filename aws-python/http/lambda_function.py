# This is the function that will be run. Feel free to extend or replace it!
def lambda_handler(event, context):
    """Handle an HTTP request; the body of the request is in event, and headers are in context.
    """
    message = 'Hello {} {}!'.format(event['first_name'], event['last_name'])  
    return { 
        'message' : message
    }
