
import io

import eccodes

class Message:
    def __init__(self, handle):
        self.handle = handle

    def __del__(self):
        try:
            eccodes.codes_release(self.handle)
        except Exception:
            pass

    def copy(self):
        return Message(eccodes.codes_clone(self.handle))

    def __copy__(self):
        return self.copy()

    def get(self, name):
        if eccodes.codes_get_size(self.handle, name) > 1:
            return eccodes.codes_get_array(self.handle, name)
        return eccodes.codes_get(self.handle, name)

    def set(self, name, value):
        return eccodes.codes_set(self.handle, name, value)

    def get_array(self, name):
        return eccodes.codes_get_array(self.handle, name)

    def get_size(self, name):
        return eccodes.codes_get_size(self.handle, name)

    def get_data(self):
        return eccodes.codes_grib_get_data(self.handle)

    def set_array(self, name, value):
        return eccodes.codes_set_array(self.handle, name, value)

    def write_to(self, fileobj):
        assert isinstance(fileobj, io.IOBase)
        eccodes.codes_write(self.handle, fileobj)

    def get_buffer(self):
        return eccodes.codes_get_message(self.handle)

    @classmethod
    def from_samples(cls, name):
        return cls(eccodes.codes_grib_new_from_samples(name))