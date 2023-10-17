from setuptools import setup

from posty.version import __version__


setup(
    name='posty',
    version=__version__,
    description='A CLI API platform',
    url='https://github.com/ignasrum/posty',
    author='Ignas Rumbavicius',
    license='MIT',
    packages=['posty',
              'posty.enum'],
    python_requires='>=3.10',
    install_requires=['argparse',
                      'requests',
                      'pillow',
                      'pytest'],
    entry_points = {
        'console_scripts': ['posty=posty.__main__:main'],
    }
)