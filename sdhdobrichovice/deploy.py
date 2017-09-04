from app import app

if __name__ == '__main__':
    from elsa import cli
    cli(app, base_url='http://www.sdhdobrichovice.cz')
