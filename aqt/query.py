
import boto3
import click
from aqt import auth
from botocore.exceptions import ClientError


def filter(context, filters):
    page = ''
    instances = []
    session = auth.get_session(context)
    client = session.client('ec2') if session else boto3.client('ec2')
    query = [
        {
            'Name': n,
            'Values': [v]
        }
        for n, v in filters
    ]
    try:
        res = client.describe_instances(Filters=query)
        for reservation in res.get('Reservations'):
            instances += reservation.get('Instances')
    except ClientError as e:
        click.secho(str(e), fg='red')
    return instances


def select(collection, property):
    properties = property.split('.')
    values = []
    try:
        for item in collection:
            val = item
            for prop in properties:
                if prop.isdigit():
                    prop = int(prop)
                val = val[prop]
            values.append(val)
        return values
    except KeyError as e:
        click.secho('Unable to find: {}'.format(str(e)), fg='red')
