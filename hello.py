
def just_function(first,second):
    return

def simple_app(environ, start_response):
    """
    (dict, callable( status: str,
                     headers: list[(header_name: str, header_value: str)]))
                  -> body: iterable of strings
    """
    data = ("\n".join(environ['QUERY_STRING'].strip("/?").split("&"))).encode()
    start_response( "200 OK",[
           ("Content-Type","text/plain"),
           ("Content-Lenght", str(len(data)))
        ])
    return iter([data])

if __name__ == "__main__":
    print("For test")
    print(simple_app({"QUERY_STRING":"/?a=1&b=2"},just_function))