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
 'pygments>=2.3,<3.0',
 'ruamel.yaml>=0.15.86,<0.16.0']

entry_points = \
{'console_scripts': ['sysfacts = sysfacts.cli:main']}

setup_kwargs = {
    'name': 'sysfacts',
    'version': '0.1.3',
    'description': 'Collect system information',
    'long_description': "# sysfacts\n\n[![Build Status](https://travis-ci.com/pmav99/sysfacts.svg?branch=master)](https://travis-ci.com/pmav99/sysfacts)\n\n`sysfacts` is a system information collector.\n\nIt can be used standalone or as a library.  In order to achieve its goals, `sysfacts`\ntries to leverage existing cross-platform python libraries.\n\n## Installation\n\n### `pipx`\n\nThe recommended installation method is [pipx](https://github.com/cs01/pipx).  More\nspecifically, if you need to run `sysfacts` just once, you can do it from a *temporary*\nvirtual environment with:\n\n``` shell\npipx run sysfacts\n```\n\nIf you need to actually install `sysfacts` for your user you can do it with:\n\n```\npipx install sysfacts\n```\n\nThis command will create a virtual environment in `~/.local/pipx/venvs/sysfacts` and add\nthe `sysfacts` script in `~/.local/bin`.\n\n### `pip`\n\nAlternatively you can use good old `pip` but this is more fragile than `pipx`.\n\n``` bash\npip install --user sysfacts\n```\n\n### As a dependency for another project\n\nIf you use [poetry](https://github.com/sdispater/poetry), you can use:\n\n``` bash\npoetry add sysfacts\n```\n\n## Usage\n\n### Standalone\n\nOn standalone mode the output format can be either JSON or YAML. You can also choose\nbetween a JSON data blob or colored, pretty-printed output.\n\n``` shell\nsysfacts --help\n# JSON output\nsysfacts\nsysfacts --pretty\nsysfacts --pretty --color\n# YAML output\nsysfacts --yaml\nsysfacts --yaml --color\n```\n\n### API\n\nThe main function is `collect_facts()` which returns a python dictionary.\n\n``` python\nfrom sysfacts import collect_facts\n\nfacts = collect_facts()\n```\n\n## Alternative projects\n\nWell, this is not really unique, since there are several similar projects out there\n\n- puppet's [facter](https://github.com/puppetlabs/facter)\n- chef's [ohai](https://github.com/chef/ohai) is written in ruby.\n- datadog's [gohai]() is written in go.\n- if you have ansible installed you can also use `ansible local -m setup`.\n",
    'author': 'Panos Mavrogiorgos',
    'author_email': 'pmav99@gmail.com',
    'url': 'https://github.com/pmav99/sysfacts',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
