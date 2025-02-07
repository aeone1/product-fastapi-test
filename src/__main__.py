from sys import exit

from alembic import command
from alembic.config import Config
from typer import Typer
from uvicorn import run

from config import Settings

cli = Typer()


@cli.command()
def runapi(
        host: str = Settings.uvicorn.host,
        port: int = Settings.uvicorn.port,
        reload: bool = Settings.uvicorn.reload,
        log_level: str = Settings.uvicorn.log_level,
        use_colors: bool = Settings.uvicorn.use_colors,
        proxy_headers: bool = Settings.uvicorn.proxy_headers
) -> None:
    run(
        host=host,
        port=port,
        reload=reload,
        log_level=log_level,
        use_colors=use_colors,
        app=Settings.uvicorn.app,
        proxy_headers=proxy_headers,
        reload_dirs=["src", ]
    )


@cli.command()
def migratedb(revision: str = 'head') -> None:
    alembic_cfg = Config()
    alembic_cfg.set_main_option('script_location', 'src/db_migrations')
    alembic_cfg.set_main_option('sqlalchemy.url', Settings.db.dsn)
    command.upgrade(alembic_cfg, revision)

@cli.command()
def downgradedb(revision: str = 'base') -> None:
    alembic_cfg = Config()
    alembic_cfg.set_main_option('script_location', 'src/db_migrations')
    alembic_cfg.set_main_option('sqlalchemy.url', Settings.db.dsn)
    command.downgrade(alembic_cfg, revision)


@cli.command()
def makemigrations(message: str = None) -> None:
    alembic_cfg = Config()
    alembic_cfg.set_main_option('script_location', 'src/db_migrations')
    alembic_cfg.set_main_option('sqlalchemy.url', Settings.db.dsn)
    command.revision(alembic_cfg, message=message, autogenerate=True)


if __name__ == "__main__":
    exit(cli())
