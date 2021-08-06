
def just_function(first,second):
    return

def simple_app(environ, start_response):
    """
    (dict, callable( status: str,
                     headers: list[(header_name: str, header_value: str)]))
                  -> body: iterable of strings
    """
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ("\n".join(environ['QUERY_STRING'].strip("/?").split("&"))).encode()

if __name__ == "__main__":
    print("For test")
    print(simple_app({"QUERY_STRING":"/?a=1&b=2"},just_function))