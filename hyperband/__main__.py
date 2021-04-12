import warnings

import click

warnings.simplefilter("ignore", UserWarning)

from hyperband.services import Hyperband
from hyperband.services.xgboost import get_params, try_params


@click.group()
def cli():
    """Description about the project."""


@click.command()
def run():
    """Run project."""
    print("El proceso ha comenzado.")

    hb = Hyperband(get_params, try_params)

    hb.run()

    print("El proceso ha finalizado.")


cli.add_command(run)

if __name__ == "__main__":
    cli()
