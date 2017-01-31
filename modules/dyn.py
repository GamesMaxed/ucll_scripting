class DynamicScopeError(Exception):
    pass

    
class _Frame:
    def __init__(self, parent, **kwargs):
        # Needs to be written using __dict__, otherwise infinite recusion ensues
        self.__dict__["parent"] = parent
        self.__dict__["_map"] = kwargs

    def __getattr__(self, id):
        if id in self._map:
            return self._map[id]
        else:
            return self.parent.__getattr__(id)

    def keys(self):
        return set(self._map).union(self.parent.keys())

    def is_bound(self, id): ## TODO Remove
        return id in self._map or self.parent.is_bound(id)

    def __contains__(self, id):
        return id in self._map or self.parent.is_bound(id)

    def __iter__(self):
        yield from self.keys()


class _RootFrame:
    def __getattr__(self, id):
        raise DynamicScopeError( "Unbound dynamic variable '{}'".format(id) )

    def __setattr__(self, id, val):
        raise DynamicScopeError( "Cannot write to root frame" )

    def is_bound(self, id): ## TODO Remove
        return False

    def __contains__(self, id):
        return False

    def keys(self):
        return set()
    
    def __iter__(self):
        yield from self.keys()


class _DynamicEnvironmentContextManager:
    def __init__(self, environment, **kwargs):
        self._environment = environment
        self._bindings = kwargs
        
    def __enter__(self):
        """Pushes a new frame with all bindings onto the stack"""
        self._environment.push(**self._bindings)

    def __exit__(self, type, value, traceback):
        """Pops last frame from the stack"""
        self._environment.pop()
    

class _DynamicEnvironment:
    def __init__(self, top = _RootFrame()):
        self.__dict__["_top"] = top

    def push(self, **kwargs):
        """Pushes a fresh frame"""
        frame = _Frame(self._top, **kwargs)
        self.__dict__["_top"] = frame

    def pop(self):
        """Pops a frame"""
        self.__dict__["_top"] = self._top.parent

    def let(self, **kwargs):
        """To be used in conjunction with the with-statement"""
        return _DynamicEnvironmentContextManager(self, **kwargs)

    def is_bound(self, id): ## TODO Remove this
        return self._top.is_bound(id)

    def __contains__(self, id):
        return self._top.is_bound(id)

    def __getattr__(self, id):
        return self._top.__getattr__(id)

    def __setattr__(self, id, val):
        self._top.__setattr__(id, val)

    def __iter__(self):
        yield from self._top

    def __str__(self):
        return ", ".join([ "{} => {}".format(id, getattr(self, id)) for id in self.__iter__() ])


_global_environment = _DynamicEnvironment()

def let(**kwargs):
    """To be used in conjunction with the with-statement"""
    return _global_environment.let(**kwargs)


def create():
    """Creates a new dynamic environment"""
    return _DynamicEnvironment()
