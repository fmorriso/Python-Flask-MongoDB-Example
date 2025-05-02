import sys
from importlib.metadata import version

from flask import Flask

from routes import bp




def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def get_package_version(package_name: str) -> str:
    return version(package_name)

app = Flask(__name__)
print(f'Python version: {get_python_version()}')
print(f'pymongo version: {get_package_version("pymongo")}')
print(f'python-dotenv version: {get_package_version("python-dotenv")}')
print(f'pathlib version: {get_package_version("pathlib")}')


def main():
    # route information is separate, so use Blueprint feature of Flask
    app.register_blueprint(bp)
    app.run(debug = True)


if __name__ == '__main__':
    main()
