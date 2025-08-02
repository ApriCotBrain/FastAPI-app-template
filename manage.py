import typer
import uvicorn

manager = typer.Typer()


@manager.command()
def run_api():
    from app.api import main

    uvicorn.run(
        "app.api.main:app",
        host="0.0.0.0",  # noqa: S104
        port=main.config.server.port,
        loop="uvloop",
        reload=main.config.server.reload,
        workers=main.config.server.workers,
        root_path=main.config.server.root_path,
        use_colors=True,
    )


@manager.command()
def run_workers(): ...


@manager.command()
def run_consumers(): ...


if __name__ == "__main__":
    manager()
