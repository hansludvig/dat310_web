from http.server import BaseHTTPRequestHandler
import cgi

class PostHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        # Parse the form data posted
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })

        # Begin the response
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes('Client: %s\n' % str(self.client_address), "utf8"))
        self.wfile.write(bytes('User-agent: %s\n' % str(self.headers['user-agent']), "utf8"))
        self.wfile.write(bytes('Path: %s\n' % self.path, "utf8"))
        self.wfile.write(bytes('Form data:\n', "utf8"))

        # Echo back information about what was posted in the form
        for field in form.keys():
            field_item = form[field]
            if field_item.filename:
                # The field contains an uploaded file
                file_data = field_item.file.read()
                file_len = len(file_data)
                del file_data
                self.wfile.write(bytes('\tUploaded %s as "%s" (%d bytes)\n' % (field, field_item.filename, file_len), "utf8"))
            else:
                # Regular form value
                self.wfile.write(bytes('\t%s=%s\n' % (field, form[field].value), "utf8"))
        return

if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8080), PostHandler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()