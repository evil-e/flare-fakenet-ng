# To read about customizing HTTP responses, see docs/CustomResponse.md
def HandleRequest(req, method, post_data=None):
    """Sample dynamic HTTP response handler.

	Parameters
	----------
	req : BaseHTTPServer.BaseHTTPRequestHandler
		The BaseHTTPRequestHandler that recevied the request
	method: str
		The HTTP method, either 'HEAD', 'GET', 'POST' as of this writing
	post_data: str
		The HTTP post data received by calling `rfile.read()` against the
		BaseHTTPRequestHandler that received the request.
    """
    response = 'Ahoy\r\n'

    if method == 'GET':
        req.send_response(200)
        req.send_header('Content-Length', len(response))
        req.end_headers()
        req.wfile.write(response)

    elif method == 'POST':
        req.send_response(200)
        req.send_header('Content-Length', len(response))
        req.end_headers()
        req.wfile.write(response)

    elif method == 'HEAD':
        req.send_response(200)
        req.end_headers()
