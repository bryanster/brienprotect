import watchdog.events
import watchdog.observers
import time
import sys
import os
import clamd
from tkinter.messagebox import showwarning


class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        # Set the patterns for PatternMatchingEventHandler
        watchdog.events.PatternMatchingEventHandler.__init__(
            self,
            ignore_directories=True,
            case_sensitive=False,
        )

    def on_created(self, event):
        filename = event.src_path
        filepath = filename.replace("/", "\\")
        result = cd.scan(filepath)
        showwarning(title="match found",
        message=result.get(f"{filepath}")
        )
    def on_modified(self, event):
        filename = event.src_path
        filepath = filename.replace("/", "\\")
        result = cd.scan(filepath)
        showwarning(title="match found",
        message=result.get(f"{filepath}")
        )

    


if __name__ == "__main__":
    cd = clamd.ClamdNetworkSocket(host="127.0.0.1" , port=3311, timeout=None)
    path = f"C:\\Users\\{os.getenv('username')}\\Downloads" 
    # "C:\Users\bryan\Downloads"
    event_handler = Handler()
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, path=path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()