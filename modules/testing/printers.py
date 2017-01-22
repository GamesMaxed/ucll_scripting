import testing

class Printer:
    def log(self, verbosity, message, *args, **kwargs):
        if testing.environment.settings.verbosity >= verbosity:
            print(message.format(*args, **kwargs))
