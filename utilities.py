import cisco
from functools import wraps

class RollBack(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print "Creating checkpoint: %s" % self.name
        cisco.cli('checkpoint %s' % self.name)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
             print "Caught an error inside critical section"
             print "Rolling back to checkpoint %s" % self.name
             cisco.cli('rollback running-config checkpoint %s' % self.name)
        else:
             print "Exited critical section without error"


def saves(func):
    'Call copy running-config startup-config after execution'
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        print 'Calling original function'
        result = func(*args, **kwargs)

        print 'Saving running config'
        cisco.cli('copy r s')
        
        return result
    
    return wrapper


def saves_improved(vdc_all=False):
    'Improve the @saves decorator by supplying an option for vdc-all'

    def saves(func):
        'Call copy running-config startup-config after execution'
    
        @wraps(func)
        def wrapper(*args, **kwargs):
            print 'Calling original function'
            result = func(*args, **kwargs)

            print 'Saving running config with vdc all: %r' % vdc_all
            if vdc_all:
                cisco.cli('copy r s vdc-all')
            else:
                cisco.cli('copy r s vdc-all')
            return result

        return wrapper
    
    return saves
