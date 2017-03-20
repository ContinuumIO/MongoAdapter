import subprocess
import mongoadapter
import os
import time
import atexit
import sys
import shlex



def start_mongo():
    print('Starting Mongo server...')

    cmd = shlex.split('docker run --name mongo-db --publish 27017:27017 mongo:3.0')
    proc = subprocess.Popen(cmd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT,
                            universal_newlines=True)

    pg_init = False
    while True:
        output_line = proc.stdout.readline()
        print(output_line.rstrip())
        if proc.poll() is not None: # If the process exited
            raise Exception('Mongo server failed to start up properly.')
        if 'waiting for connections on port 27017' in output_line:
            break


def stop_mongo(let_fail=False):
    try:
        print('Stopping Mongo server...')
        subprocess.check_call('docker ps -q --filter "name=mongo-db" | xargs docker rm -vf', shell=True)
    except subprocess.CalledProcessError:
        if not let_fail:
            raise


### Start Mongo
stop_mongo(let_fail=True)
start_mongo()
atexit.register(stop_mongo)

### Run MongoAdapter tests
assert mongoadapter.test()

# Print the version
print('mongoadapter.__version__: %s' % mongoadapter.__version__)

sys.exit(0)
