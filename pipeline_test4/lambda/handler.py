from datetime import datetime


def handler(event, context):
    return {
        'body': f'Hello from Lambda pipeline-test4 edit 14! The time is {datetime.now().isoformat()}',
        'statusCode': '200'
    }
