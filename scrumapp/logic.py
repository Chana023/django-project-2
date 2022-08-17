from datetime import datetime
from rest_framework.exceptions import PermissionDenied

#Logic tests

def taskComplete(self, data, requestuser):
    data_dict = data
    if requestuser == data_dict['developer']:
            data_dict['status'] = 'C'
            data_dict['completed_at'] = datetime.now()
            return data_dict
    raise PermissionDenied({"message":"You don't have permission to access",
                                "Task": data_dict['name']})
    