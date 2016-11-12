
from __future__ import print_function
import json
import click
import aqt
from aqt import query
from botocore.exceptions import ProfileNotFound, NoRegionError



@click.group()
@click.option('--profile', default=None, help='AWS CLI profile name')
@click.option('--key-id', default=None, help='AWS Access Key ID')
@click.option('--secret-key', default=None, help='AWS Secret Key')
@click.option('--region', default=None, help='AWS region name')
@click.option('--debug', is_flag=True, help='Print debug info')
@click.pass_context
def cli(ctx, profile, key_id, secret_key, region, debug):
    """AWS Query Tool"""
    ctx.obj['profile'] = profile
    ctx.obj['key_id'] = key_id
    ctx.obj['secret_key'] = secret_key
    ctx.obj['region'] = region
    ctx.obj['debug'] = debug


@cli.group()
@click.argument('property')
@click.pass_context
def select(ctx, property):
    """Retrieve an ec2 property
    """
    ctx.obj['property'] = property


@select.command()
@click.argument('filters', nargs=-1)
@click.pass_context
def where(ctx, filters):
    """Where a given filter is true
    """
    # need to be able to filter results in the case of tags for instance
    # need to be able to search against self rather than all, easily
    if len(filters) < 2:
        click.echo('A filter must be provided as a key value pair')
        return
    filter_pairs = []
    for i in range(0, len(filters), 2):
        filter_pairs += [(filters[i], filters[i + 1])]
    try:
        collection = query.filter(ctx, filter_pairs)
        results = query.select(collection, ctx.obj.get('property'))
        if results:
            click.secho(json.dumps(results), fg='white')
    except ProfileNotFound:
        click.secho('No profile found', fg='red')
    except NoRegionError:
        click.secho('No region provided', fg='red')

def main():
    cli(obj={})
