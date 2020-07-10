![vk.py](https://user-images.githubusercontent.com/28061158/63603699-cd51b980-c5d2-11e9-8a8f-06e1eef20afe.jpg)



# Welcome to vk.py 👋

> Extremely-fast, easy-to-use, ready for production. The asyncio based library for Python and Humans written to be efficient and reliable.



### 🏠 [Homepage](https://github.com/Cl0ckHvH/vk.py-1.0.0a6)


## Install

Install package from PyPi: (current version is 6 alpha of 1.0.0)

```sh
pip install vk.py==1.0.0a6 -U
```

Warning: this version really unstable and not recommended to use in production.


## Usage

A simple example
```python
from vk import VK
from vk.utils.task_manager import TaskManager
from vk.utils.auth_manager import AuthManager
import logging

logging.basicConfig(level="INFO")
auth = AuthManager("7999123456", "my-password")
vk = VK(access_token=auth.get_token())

async def status_get():
    resp = await vk.api_request("status.get")
    print(resp)

if __name__ == "__main__":
    task_manager = TaskManager(vk.loop)
    task_manager.add_task(status_get)
    task_manager.run()

```

You can find more examples [here](./examples).



## Features

- Rich high-level API.
- Fully asynchronous. Based on asyncio and aiohttp.
- Bot framework out of-the-box.
- Fully typed, thanks to Pydantic.
- Compatible with PyPy.
- Have a lot of tools (in bot framework) out-of-the-box for creating largest and powerful applications [click](./vk/bot_framework/addons):
    * Caching
    * Blueprints
    * Cooldowns
    * FSM (WIP)
- Python -> VKScript converter (WIP). [try it](./vk/utils/vkscript)

## Alternatives

- Kutana. Bot engine for creating Telegram and VK bots
- VK_API. A simple library for accessing VK API.

And many other libraries...


## FAQ

This is only bot library? - No, this library could be used for acessing userapi or botapi without any troubles.

How to use it? - You may check docs or see our [examples](./examples).

Why do you do it? - We are interesting to create the most used and easy-to-use library for Python.

When `1.0.0` will be released? - We don't know. We hope that it's moment will come to us ASAP. However, you can see current issues and help us.

## Author

👤 **Cl0ckHvH**

* Github: [@Cl0ckHvH](https://github.com/Cl0ckHvH)


## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/Cl0ckHvH/vk.py-1.0.0a6/issues).
Also you can check your [contributors guide](./CONTRIBUTING.md).

[Our contributors](./CONTRIBUTORS.txt).

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2020 [Cl0ckHvH](https://github.com/Cl0ckHvH).<br />
This project is [MIT](https://github.com/Cl0ckHvH/vk.py-1.0.0a6/blob/master/LICENSE) licensed.

