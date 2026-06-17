"""CLI for ws-gateway"""
import click
from rich.console import Console
from rich.table import Table
from .core import Engine
console = Console()
@click.group()
@click.option("--verbose","-v",is_flag=True)
@click.pass_context
def main(ctx, verbose):
    """High-performance WebSocket API gateway with rate limiting and pub/sub"""
    ctx.ensure_object(dict)
    ctx.obj["verbose"] = verbose
@main.command()
@click.argument("target")
@click.option("--output","-o",default=None)
@click.pass_context
def run(ctx, target, output):
    """Run ws-gateway"""
    engine = Engine()
    result = engine.process(target)
    console.print("[green]Done:[/green] " + str(result))
@main.command()
def status():
    """Show status"""
    console.print("[green]ws-gateway v1.0.0 ready[/green]")
if __name__ == "__main__":
    main()
