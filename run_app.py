import threading
import time
import webbrowser

from werkzeug.serving import make_server

from assets.PY.app import app


def main():
    server = make_server("127.0.0.1", 0, app)
    port = server.server_port
    server_thread = threading.Thread(target=server.serve_forever, daemon=True)
    server_thread.start()

    url = f"http://127.0.0.1:{port}/"
    print(f"Buggy Fun Facts is running at {url}")
    webbrowser.open(url)

    try:
        while server_thread.is_alive():
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down Buggy Fun Facts...")
    finally:
        server.shutdown()


if __name__ == "__main__":
    main()
