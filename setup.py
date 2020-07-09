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
    'name': 'vk.py',
    'version': '1.0.0a6',
    'description': 'Extremely-fast, easy-to-use, ready for production. The asyncio based library for Python and Humans written to be efficient and reliable.',
    'long_description': '![vk.py](https://user-images.githubusercontent.com/28061158/63603699-cd51b980-c5d2-11e9-8a8f-06e1eef20afe.jpg)\n\n\n\n# Welcome to vk.py 👋\n\n![Version](https://img.shields.io/badge/version-0.6.0-blue.svg?cacheSeconds=2592000) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg) ](https://github.com/prostomarkeloff/vk.py/blob/master/LICENSE) [![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fprostomarkeloff%2Fvk.py.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fprostomarkeloff%2Fvk.py?ref=badge_shield)\n[![Codacy Badge](https://api.codacy.com/project/badge/Grade/cac2f27aab0a41f993660a525c054bb5)](https://app.codacy.com/app/prostomarkeloff/vk.py?utm_source=github.com&utm_medium=referral&utm_content=prostomarkeloff/vk.py&utm_campaign=Badge_Grade_Dashboard)\n[![Build Status](https://travis-ci.org/prostomarkeloff/vk.py.svg?branch=master)](https://travis-ci.org/prostomarkeloff/vk.py)\n\n> Extremely-fast, easy-to-use, ready for production. The asyncio based library for Python and Humans written to be efficient and reliable.\n\n\n\n### 🏠 [Homepage](github.com/prostomarkeloff/vk.py)\n\n\n## Install\n\nInstall package from PyPi: (current version is 6 alpha of 1.0.0)\n\n```sh\npip install vk.py==1.0.0a6 -U\n```\n\nWarning: this version really unstable and not recommended to use in production.\n\n\n## Usage\n\nA simple example\n```python\nfrom vk import VK\nfrom vk.utils.task_manager import TaskManager\nfrom vk.utils.auth_manager import AuthManager\nimport logging\n\nlogging.basicConfig(level="INFO")\nauth = AuthManager("7999123456", "my-password")\nvk = VK(access_token=auth.get_token())\n\nasync def status_get():\n    resp = await vk.api_request("status.get")\n    print(resp)\n\nif __name__ == "__main__":\n    task_manager = TaskManager(vk.loop)\n    task_manager.add_task(status_get)\n    task_manager.run()\n\n```\n\nYou can find more examples [here](./examples).\n\n\n\n## Features\n\n- Rich high-level API.\n- Fully asynchronous. Based on asyncio and aiohttp.\n- Bot framework out of-the-box.\n- Fully typed, thanks to Pydantic.\n- Compatible with PyPy.\n- Have a lot of tools (in bot framework) out-of-the-box for creating largest and powerful applications [click](./vk/bot_framework/addons):\n    * Caching\n    * Blueprints\n    * Cooldowns\n    * FSM (WIP)\n- Python -> VKScript converter (WIP). [try it](./vk/utils/vkscript)\n\n## Alternatives\n\n- Kutana. Bot engine for creating Telegram and VK bots\n- VK_API. A simple library for accessing VK API.\n\nAnd many other libraries...\n\n\n## FAQ\n\nThis is only bot library? - No, this library could be used for acessing userapi or botapi without any troubles.\n\nWhere i can find the docs? - [Check it](https://prostomarkeloff.github.io/vk.py).\n\nHow to use it? - You may check docs or see our [examples](./examples).\n\nWhy do you do it? - We are interesting to create the most used and easy-to-use library for Python.\n\nWhen `1.0.0` will be released? - We don\'t know. We hope that it\'s moment will come to us ASAP. However, you can see current issues and help us.\n\n## Author\n\n👤 **prostomarkeloff**\n\n* Github: [@prostomarkeloff](https://github.com/prostomarkeloff)\n\n\n## 🤝 Contributing\n\nContributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/prostomarkeloff/vk.py/issues).\nAlso you can check your [contributors guide](./CONTRIBUTING.md).\n\n[Our contributors](./CONTRIBUTORS.txt).\n\n## Show your support\n\nGive a ⭐️ if this project helped you!\n\n## 📝 License\n\nCopyright © 2019 [prostomarkeloff](https://github.com/prostomarkeloff).<br />\nThis project is [MIT](https://github.com/prostomarkeloff/vk.py/blob/master/LICENSE) licensed.\n\n',
    'author': 'prostomarkeloff',
    'author_email': None,
    'url': 'https://github.com/Cl0ckHvH/vk.py-1.0.0a6',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
