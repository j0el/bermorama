import http.server
import socketserver
import os


def serve(port):
    gallery = os.path.join(os.getcwd(), "build")
    if not os.path.isdir(gallery):
        print("The gallery has not been built yet.")
        print("Generate it first with `mikula build`")
        return

    class Handler(http.server.SimpleHTTPRequestHandler):
        extensions_map = {
            '.manifest': 'text/cache-manifest',
            '.html': 'text/html',
            '.png': 'image/png',
            '.jpg': 'image/jpg',
            '.svg': 'image/svg+xml',
            '.css': 'text/css',
            '.js': 'application/x-javascript',
            '': 'text/html'
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=gallery, **kwargs)

    with socketserver.TCPServer(("", port), Handler) as httpd:
        print(f"Serving on 'http://localhost:{port}'")
        print("Ctrl + C to exit")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\ndone")
