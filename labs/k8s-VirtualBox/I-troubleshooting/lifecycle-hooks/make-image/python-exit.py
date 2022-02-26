import signal, os, time

print("good-exit-pod starting...", flush=True)

def handler(signum, frame):
    print('OK, heard you...going to exit.', signum,flush=True)

signal.signal(signal.SIGINT, handler)

signal.pause()

print("That's it...I'm going out.",flush=True)
time.sleep(15)