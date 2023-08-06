# AMY Plugin

[Amy Assistant](http://amy-assistant.at)

Just import amy to write your plugin.

```py
from amy import Plugin

class Telegram(TelethonClient, Plugin):
    def __init__(username, *args, **kwargs):
        self.username = username
        super().__init(*args, **kwargs)

Telegram._Plugin__connect()

client = Telegram('<number>')

```
