from requests import request 

class AddRequest(request.Request):
    def __init__(self, requestId,currentServiceProvider):
        super().__init__(requestId)
        self.currentServiceProvider = currentServiceProvider

    def display(self):
        return "add request,service provider:"+self.currentServiceProvider