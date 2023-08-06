import click
import dateparser
import requests
from joule.cli.config import pass_config


@click.command(name="remove")
@click.option("--from", "start", help="timestamp or descriptive string")
@click.option("--to", "end", help="timestamp or descriptive string")
@click.argument("stream")
@pass_config
def data_remove(config, start, end, stream):
    params = {"path": stream}
    if start is not None:
        params['start'] = int(dateparser.parse(start).timestamp() * 1e6)
    if end is not None:
        params['end'] = int(dateparser.parse(end).timestamp() * 1e6)
    try:
        resp = requests.delete(config.url+"/data", params=params)
    except requests.ConnectionError:
        raise click.ClickException("Error contacting Joule server at [%s]" % config.url)
    if resp.status_code != 200:
        raise click.ClickException("Error [%d]: %s" % (resp.status_code, resp.text))
    else:
        click.echo("OK")
