class Player:
    def __init__(self, name: str, _id: str):
        self._name = name
        self._id = _id

    def to_dict(self, __exclude: list[str] = None):
        obj_dict = {
            'name': self._name,
            'id': self._id
        }

        if __exclude is not None:
            for key in obj_dict.keys():
                if key in __exclude:
                    del obj_dict[key]

        return obj_dict
