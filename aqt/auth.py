
import click
import boto3


def get_session(context):
    args = context.obj
    if args.get('debug'):
        click.secho('Auth args:', fg='cyan')
        click.secho(str(args), fg='cyan')

    if args.get('profile', None):
        if args.get('debug'):
            click.secho('Attempting to use profile', fg='cyan')
        return boto3.Session(
            profile_name=args.get('profile')
        )
    elif args.get('key_id', None) and args.get('secret_key', None):
        click.secho('Attempting to use secret key', fg='cyan')
        return boto3.Session(
            aws_access_key_id=args.get('key_id'),
            aws_secret_access_key=args.get('secret_key'),
            aws_session_token=''
        )
    else:
        click.secho('Attempting to use IAM role', fg='cyan')
        return None
