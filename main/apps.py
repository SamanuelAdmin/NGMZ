from django.apps import AppConfig

import asyncio
import os
import multiprocessing


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        if os.environ.get('RUN_MAIN') != 'true':
            return

        from .models import Info
        from .modules.tg_bot import SingletonBot

        def botProcess():
            token = Info.objects.get(tag="notifications_bot").getData('token')
            if not token: return

            asyncio.run(
                SingletonBot( token ).start()
            )

        multiprocessing.Process(
            target=botProcess, daemon=True
        ).start()