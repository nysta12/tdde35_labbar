import socket


def modify_data(data):
    """
    function in charge of modifying the data according to the assignment.
    """
    print("Now modifying the following data: ", data)

    data = data.replace(b'Smiley', b'Trolly').replace(b'Stockholm', b'Link\xc3\xb6ping').replace(b'smiley.jpg', b'trolly.jpg')
    data = data.replace(b'Link\xc3\xb6ping-spring.jpg', b'Stockholm-spring.jpg')

    return data


def get_data(connection):
    """
    Collects and gathers all the data in the variable all_data.
    """
    all_data = b''

    # run and collect data indefinietly until the condition is met
    while 1:
        try:
            
            # recieve data up to 1024 bytes at a time
            packet_data = connection.recv(1024)

        except socket.error:
            packet_data = b''

        # append the packet data to all_data variable
        all_data += packet_data

        # end condition
        if not packet_data or packet_data.endswith(b'\r\n\r\n') or packet_data.endswith(b'\x00\x00'):

            return all_data


def extract_http_information(data):
    """
    Extracts the host from the data.
    """
    host_index = data.index(b'Host: ') + len(b'Host: ')
    host = data[host_index:].split(b'\r\n')[0]

    return host


def run(data, client_part, connection):
    """
    The function that runs and handles the data being sent
    and recieved over the connection. 
    """
    while data:
        # send all the data over the connection
        print("Sending data...")
        client_part.sendall(data)

        # recieve all the data
        host_data = get_data(client_part)

        if not host_data:
            break

        # modify the host data according to instructions
        host_data = modify_data(host_data)
        # send all the data over the connection
        connection.sendall(host_data)

        # retrieve all the data that has been sent over the connection
        data = get_data(connection)


def main():
    """
    This is the main function and it is run when the file runs. The function
    initiates the start of the proxy and then lets the function run handle the
    data being sent and recieved over the connection.
    """

    # set up server part of proxy, sets it up as a stream socket which is 
    # a reliable, sequenced, two way, connection based byte stream connection.
    # And AF_INET specifies the communication is done by addresses of IPv4 
    server_part = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # allows the socket to be reused with the same combination of address and port 
    server_part.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # binds socket to specific host and port
    server_part.bind((HOST, PORT))

    try:

        while 1:

            print("Listening for connections...")
            # listen for connections and only accept one pending connection at a time.
            server_part.listen(1)

            # accepts incoming request, returns socket object representing connection
            #to the client and address of the client
            connection, address = server_part.accept()
            print("Now connected to: ", address)

            # get the information over the connection
            data = get_data(connection)

            if data:
                # extract information of the web host
                web_host = extract_http_information(data)

                print("The host: ", web_host)

                # set up client part of proxy
                client_part = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_part.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

                # connects to the web_host and http port 80
                client_part.connect((web_host, HTTP_PORT))

            # run the connection
            run(data, client_part, connection)

            # close the connection and client part
            connection.close()
            client_part.close()

    finally:
        server_part.close()



if __name__== "__main__":
    print("----- Proxy server is staring -----")

    HOST = '127.0.0.1'
    PORT = 1212
    HTTP_PORT = 80

    main()
