from setuptools import setup, find_packages

VERSION = 1.0

setup(
    name='faded-parsons',
    version=VERSION,
    author='Tommy Joseph, Akshit Dewan',
    # author_email='',
    description=('faded-parsons implements a frontend for faded parsons '
                 'problems that interfaces with OKPy. It reuses much of '
                 'Nate Weinman\'s work, and you can find the original paper'
                 ' at https://dl.acm.org/doi/abs/10.1145/3328778.3372639'),
    # long_description=long_description,
    url='https://github.com/Cal-CS-61A-Staff/faded-parsons',
    # license='Apache License, Version 2.0',
    keywords=['education', 'parsons'],
    packages=find_packages(include=[
        'parsons',
        'parsons.*',
    ]),
    entry_points={
        # 'console_scripts': [
        #     'ok=client.cli.ok:main',
        #     'ok-publish=client.cli.publish:main',
        #     'ok-lock=client.cli.lock:main',
        #     'ok-test=client.cli.test:main',
        # ],
    },
    # classifiers=[
    #     'Programming Language :: Python :: 3.4',
    #     'Programming Language :: Python :: 3.5',
    #     'Programming Language :: Python :: 3.6',
    # ],
    install_requires=[
        # 'requests==2.22.0',
        # 'certifi==2019.11.28',
        # 'urllib3==1.25.7',
        # 'chardet==3.0.4',
        # 'idna==2.8',
        # 'coverage==4.4',
        # 'pytutor==1.0.0',
        # 'ast-scope==0.3.1',
        # 'attrs==19.3.0',
        # 'pyaes==1.6.1',
        # 'colorama==0.4.3',
        # 'display-timedelta==1.1',
        # 'filelock==3.0.12',
        'pyyaml==6.0',
        'flask==2.0.2'
    ],
)
