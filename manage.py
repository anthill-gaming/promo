#!/usr/bin/env python3
import os

if __name__ == "__main__":
    os.environ.setdefault("ANTHILL_SETTINGS_MODULE", "settings")
    try:
        import anthill.framework
        anthill.framework.setup()
    except ImportError:
        raise ImportError(
            "Couldn't import anthill framework. Are you sure it's installed "
            "and available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?")
    from anthill.framework.apps import app
    from anthill.framework.core.management import Manager

    manager = Manager(app)
    manager.run()
