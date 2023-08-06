"""Simple async worker"""

__version__ = "2.6"

import asyncio
import os

import click

from . import utils
from .worker import JobRunner

global script
global run
global create_table


@click.group()
def script():
    pass


@click.command()
@click.option(
    "--queue-table",
    help='Queue table name (Default: os.getenv("DBTABLE", "public.modngarn_job"))',
    default=os.getenv("DBTABLE", "public.modngarn_job"),
)
@click.option("--limit", default=300, help="Limit jobs (Default: 300)")
def run(queue_table, limit):
    table_name = utils.sql_table_name(queue_table)
    job_runner = JobRunner()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(job_runner.run(table_name, limit=limit))


@click.command()
@click.option(
    "--queue-table",
    help='Queue table name (Default: os.getenv("DBTABLE", "public.modngarn_job"))',
    default=os.getenv("DBTABLE", "public.modngarn_job"),
)
def create_table(queue_table):
    table_name = utils.sql_table_name(queue_table)
    asyncio.run(utils.create_table(table_name))


script.add_command(run)
script.add_command(create_table)
