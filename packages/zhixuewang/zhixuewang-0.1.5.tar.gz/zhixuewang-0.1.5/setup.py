import sys
from shutil import rmtree
from setuptools import setup, Command
import os

version = "0.1.5"
class UploadCommand(Command):
    """Support setup.py upload."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass
    def run(self):
        try:
            print('Removing previous builds…')
            rmtree('dist')
        except OSError:
            pass

        print('Building Source and Wheel (universal) distribution…')
        os.system(f'{ sys.executable} setup.py sdist bdist_wheel --universal')

        print('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        print('Pushing git tags…')
        os.system(f'git tag v{version}')
        os.system('git push --tags')

        sys.exit()


setup(
    name="zhixuewang",
    version=version,
    keywords=["test", "xxx"],
    description="关于智学网的api",
    license="GPLv3",

    author="anwenhu",
    author_email="anemailpocket@163.com",

    packages=["zhixuewang"],
    include_package_data=True,
    platforms="any",
    install_requires=["requests", 'PyExecJs'],

    cmdclass={
        'upload': UploadCommand,
    },
)
