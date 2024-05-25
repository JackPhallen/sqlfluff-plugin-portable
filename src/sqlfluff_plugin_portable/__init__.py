"""
A SQLFluff rule to check function portability
"""

from typing import List, Type

from sqlfluff.core.config import ConfigLoader
from sqlfluff.core.plugin import hookimpl
from sqlfluff.core.rules import BaseRule


@hookimpl
def get_rules() -> List[Type[BaseRule]]:
    """Get plugin rules"""
    from sqlfluff_plugin_portable.rules.FN01 import Rule_Portable_FN01

    return [Rule_Portable_FN01,]


@hookimpl
def load_default_config() -> dict:
    """Loads the default configuration for the plugin."""
    return ConfigLoader.get_global().load_config_resource(
        package="sqlfluff_plugin_portable",
        file_name="plugin_default_config.cfg",
    )


@hookimpl
def get_configs_info() -> dict:
    """Get rule config validations and descriptions."""
    return {
        "function_allowlist": {"definition": "Functions on allowlist"},
    }
