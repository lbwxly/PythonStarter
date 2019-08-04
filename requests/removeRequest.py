from requests import request 

class RemoveRequest(request.Request):
    def __init__(self, requestId, needHelp):
        super().__init__(requestId)
        self.needHelp = needHelp

    def display(self):
        return "remove request, need help:" + self.needHelp;