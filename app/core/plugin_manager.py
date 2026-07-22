import importlib
import pkgutil

import app.plugins


class PluginManager:

    def __init__(self):
        self.plugins = {}
        self.load_plugins()

    def load_plugins(self):

        package = app.plugins

        for _, module_name, _ in pkgutil.iter_modules(package.__path__):

            module = importlib.import_module(
                f"app.plugins.{module_name}"
            )

            if hasattr(module, "INTENT"):
                self.plugins[module.INTENT] = module

    def get_plugin(self, intent):
        return self.plugins.get(intent)