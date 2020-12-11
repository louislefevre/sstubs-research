import json


class JsonWriter:
    def __init__(self, file_name):
        self._file = open(file_name, 'a')

    def write_object(self, obj):
        self._write(obj.__dict__)

    def write_dictionary(self, dictionary):
        self._write(dictionary)

    def _write(self, data):
        with self._file as json_file:
            json.dump(data, json_file, indent=4)
        json_file.close()

    def close(self):
        self._file.close()


class JsonReader:
    def __init__(self, path):
        self._file = open(path)

    def read(self):
        return json.load(self._file)

    def close(self):
        self._file.close()
