from app import create_app

app = create_app()

if __name__ == '__main__':                  # Startup stuff
    app.run(host='127.0.0.1', port=5000)    # Specify the port and url

    # from waitress import serve                # Waitress is a production server. It can serve multiple simultaneous requests
    # serve(app, host='0.0.0.0', port=80)       # Serve on the public IP address of the host computer

