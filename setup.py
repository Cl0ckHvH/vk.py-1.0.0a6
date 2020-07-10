# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['vk',
 'vk.bot_framework',
 'vk.bot_framework.addons',
 'vk.bot_framework.addons.caching',
 'vk.bot_framework.addons.validators',
 'vk.bot_framework.dispatcher',
 'vk.bot_framework.extensions',
 'vk.bot_framework.middlewares',
 'vk.bot_framework.rules',
 'vk.bot_framework.storages',
 'vk.exceptions',
 'vk.keyboards',
 'vk.longpoll',
 'vk.longpoll.bot',
 'vk.longpoll.user',
 'vk.methods',
 'vk.streaming_api',
 'vk.types',
 'vk.types.additional',
 'vk.types.attachments',
 'vk.types.events',
 'vk.types.events.community',
 'vk.types.responses',
 'vk.utils',
 'vk.utils.vkscript']

package_data = \
{'': ['*'], 'vk.utils.vkscript': ['handlers/*']}

install_requires = \
['aiohttp>=3.6,<4.0', 'pydantic', 'watchgod>=0.5.0,<0.6.0']

extras_require = \
{':python_version == "3.6"': ['async-generator>=1.10,<2.0',
                              'contextvars>=2.4,<3.0'],
 'vbml': ['vbml>=0.5.0,<0.6.0']}

setup_kwargs = {
    'name': 'vk.py-1.0.0a6',
    'version': '1.0.0',
    'description': 'Extremely-fast, easy-to-use, ready for production. The asyncio based library for Python and Humans written to be efficient and reliable.',
    'long_description': 'Reupload vk.py, which the deleted on pypi and github',
    'author': 'Cl0ckHvH',
    'author_email': None,
    'url': 'https://github.com/Cl0ckHvH/vk.py-1.0.0a6',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
