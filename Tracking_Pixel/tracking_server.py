# Import the necessary modules from the 'http.server' module
from http.server import BaseHTTPRequestHandler, HTTPServer

# Define a custom class called 'RequestHandler' that inherits from 
# 'BaseHTTPRequestHandler'. This class will handle incoming requests.
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # When a GET request is received (e.g., when the user navigates to 
        # a URL in their browser), this method is called. We use it to log
        # information about the incoming request, such as the client IP address
        # and User-Agent header.
        print(f"Client IP: {self.client_address[0]} User Agent: {self.headers['User-Agent']}")

        # Now that we've logged the request information, let's send a response 
        # back to the client. In this case, we're sending an image (a GIF) 
        # with a status code of 200 (OK).
        self.send_response(200)

        # Add a header to the response indicating the type of content being sent.
        # In this case, it's an image GIF.
        self.send_header('Content-type', 'image/jpg')

        # This line tells the client that we've finished sending the headers and 
        # are ready to send the actual content (the image).
        self.end_headers()

        # Now let's open the 'pixel.gif' file and read its contents. We'll then 
        # write this content directly into the response body.
        with open('pixel.jpg', 'rb') as f:
            # Read the entire contents of the 'pixel.gif' file into memory.
            self.wfile.write(f.read())  # Write the file contents to the response body

# Define a function called 'run_server()' that sets up and starts an HTTP server.
def run_server():
    # Specify the address and port where we want the server to listen for incoming 
    # requests. In this case, it's all IP addresses on port 8000.
    server_address = ('', 8000)

    # Create a new instance of the 'HTTPServer' class, passing in our custom 
    # request handler and the address where we want the server to listen.
    httpd = HTTPServer(server_address, RequestHandler)

    # Print a message to let us know that the server is up and running.
    print("Tracking server running on port 8000...")

    # Start the server's event loop. This will keep the server running indefinitely 
    # until we manually stop it (e.g., by pressing Ctrl+C in the terminal).
    httpd.serve_forever()

# If this script is being run directly (i.e., not being imported as a module), 
# then let's call our 'run_server()' function to start the server.
if __name__ == '__main__':
    # Call the 'run_server()' function to set up and start the HTTP server.
    run_server()