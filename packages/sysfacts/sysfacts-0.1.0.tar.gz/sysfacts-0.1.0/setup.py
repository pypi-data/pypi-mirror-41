# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['sysfacts']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0',
 'distro>=1.3,<2.0',
 'pendulum>=2.0,<3.0',
 'psutil>=5.4,<6.0',
 'py-cpuinfo>=4.0,<5.0',
 'ruamel.yaml>=0.15.86,<0.16.0']

entry_points = \
{'console_scripts': ['sysfacts = sysfacts.cli:main']}

setup_kwargs = {
    'name': 'sysfacts',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Panos Mavrogiorgos',
    'author_email': 'pmav99@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
