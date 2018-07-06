# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     __init__.py
   Description :
   Author :       潘晓华
   date：          2018/3/1
-------------------------------------------------
"""

import os


def load_config():
    """加载配置类"""
    env = os.environ.get('APP_ENV')
    try:
        if env == 'PRODUCTION':
            from .production import ProductionConfig
            return ProductionConfig

        elif env == 'TESTING':
            from .testing import TestingConfig
            return TestingConfig
        elif env == 'DOCKER':
            from .docker import DockerConfig
            return DockerConfig
        else:
            from .development import DevelopmentConfig
            return DevelopmentConfig

    except ImportError:
        from .default import Config
        return Config
