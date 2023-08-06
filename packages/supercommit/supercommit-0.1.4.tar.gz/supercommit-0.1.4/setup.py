from setuptools import setup

setup(
    name='supercommit',
    version='0.1.4',
    author='zhangbinhui',
    author_email="maru-zhang@foxmail.com",
    packages=['supercommit'],
    install_requires=['Click', 'inquirer', 'terminaltables', 'configparser', 'translate'],
    entry_points='''
        [console_scripts]
        git-sc=supercommit.index:cli
    '''
)