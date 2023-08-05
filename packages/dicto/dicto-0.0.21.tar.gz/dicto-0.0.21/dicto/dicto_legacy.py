import os
import json
import collections

yaml = None
xmltodict = None

class dicto(dict):

    def __init__(self, *args, **kwargs):
        super(dicto, self).__init__(*args, **kwargs)

        for key, value in self.items():
            if isinstance(value, dict):
                self[key] = dicto(value)

            elif isinstance(value, str):
                pass

            elif hasattr(value, "__iter__"):
                self[key] = [ dicto(e) if isinstance(e, dict) else e for e in value ]


    def __getattr__(self, attr):
        if attr in self:
            return self[attr]
        else:
            raise AttributeError(attr)

    def __setattr__(self, attr, value):
        self[attr] = value

    
    def dict_(self):
        d = dict(self)

        for key, value in d.items():
            if isinstance(value, dicto):
                d[key] = value.dict_()

            elif isinstance(value, str):
                pass

            elif isinstance(value, dict):
                pass

            elif hasattr(value, "__iter__"):
                d[key] = [ e.dict_() if isinstance(e, dicto) else e for e in value ]

        return d



    def merge_(self, merge_dct):
        """ Recursive dict merge. Inspired by :meth:``dict.update()``, instead of
        updating only top-level keys, dict_merge recurses down into dicts nested
        to an arbitrary depth, updating keys. The ``merge_dct`` is merged into
        ``self``.
        :param self: dict onto which the merge is executed
        :param merge_dct: self merged into self
        :return: None
        """

        for k, v in merge_dct.items():
            if (k in self and isinstance(self[k], dict) and isinstance(merge_dct[k], collections.Mapping)):
                self[k].merge_(dicto(merge_dct[k]))
            else:
                self[k] = merge_dct[k]
        
        return self

    def merge(self, *args, **kwargs):
        return self.merge_(*args, **kwargs)

    @classmethod
    def load_(cls, filepath):
        filepath = os.path.realpath(filepath)

        if filepath.endswith(".yaml") or filepath.endswith(".yml"):
            global yaml

            if yaml is None:
                import yaml as mod
                yaml = mod

            with open(filepath, 'r') as stream:
                dict_ = yaml.load(stream)
        elif filepath.endswith(".json"):
            with open(filepath, 'r') as stream:
                dict_ = json.load(stream)
        elif filepath.endswith(".xml"):
            global xmltodict

            if xmltodict is None:
                import xmltodict as mod
                xmltodict = mod
            
            with open(filepath, 'r') as stream:
                dict_ = xmltodict.parse(stream.read())
        else:
            raise Exception("File type not supported.")

        return cls(dict_)

    def dump_(self, filepath):
        
        filepath = os.path.realpath(filepath)
        obj = self.dict_()

        if filepath.endswith(".yaml") or filepath.endswith(".yml"):
            global yaml

            if yaml is None:
                import yaml as mod
                yaml = mod

            with open(filepath, 'w') as stream:
                yaml.safe_dump(obj, stream, default_flow_style=False)
        elif filepath.endswith(".json"):
            with open(filepath, 'w') as stream:
                json.dump(obj, stream)
        else:
            raise Exception("File type not supported.")
