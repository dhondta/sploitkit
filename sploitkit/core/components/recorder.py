from __future__ import unicode_literals

from sploitkit.utils.path import Path


__all__ = ["Recorder"]


class Recorder(object):
    """ Simple text recording class. """
    def __init__(self):
        self.stop()
    
    @property
    def enabled(self):
        return self.__file is not None
    
    def save(self, text):
        """ Save the given text to the record file. """
        if self.enabled:
            self.__file.append_line(text)
    
    def start(self, filename, overwrite=False):
        """ Start the recorder, creating the record file. """
        self.__file = f = Path(filename)
        if f.suffix != ".rc":
            self.__file = f = Path(filename + ".rc")
        if not overwrite and f.exists():
            raise OSError("File already exists")
        f.reset()
    
    def stop(self):
        """ Stop the recorder by removing the record file reference. """
        self.__file = None
