import json
class GetKeyValue(object):
    def __init__(self, o, mode):
        self.json_object = None
        if mode == 'j':
            self.json_object = o
        elif mode == 's':
            self.json_object = json.loads(o)
        else:
            raise Exception('Unexpected mode argument.Choose "j" or "s".')
        self.key_list = []
        self.value_list = []

    def search_key(self):
        (keys,value) = self.__search(self.json_object)
        return keys,value

    def __search(self, json_object):
        for k in json_object:
            if isinstance(json_object[k], dict):
                self.__search(json_object[k])
            elif isinstance(json_object[k], list):
                for item in json_object[k]:
                    #如果嵌套的list的item是dict格式，执行该代码
                    if isinstance(item, dict):
                        self.__search(item)
            else:
                self.key_list.append(k)
                self.value_list.append(json_object[k])
        return self.key_list, self.value_list










