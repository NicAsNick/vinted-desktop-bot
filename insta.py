



def http_status(status):
    match status:
        case 400:
            return "Bad request"
        case 401:
            return "Unauthorized"
        case 403:
            return "Forbidden"
        case 404:
            return "Not found"
        case _:
            return "unknown request"



def http_status(status):
    if status == 400:
        return "Bad request"
    elif status == 401:
        return "Unauthorized"
    elif status == 403:
        return "Forbidden"
    elif status == 404:
        return "Not found"



