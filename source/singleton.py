
class Borg:
    """ class que faz os atributos serem globais """
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state

class Singleton(Borg):

    def __init__(self,project_dictionary={}):
        Borg.__init__(self)
        self._shared_state.update(project_dictionary)
    
    def __str__(self):
        return str(self._shared_state)
