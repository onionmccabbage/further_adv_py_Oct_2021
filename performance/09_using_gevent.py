# gevent is a green event runner (spawn new threads for us)
import gevent # may need to pip install gevent
from gevent import socket

# get a list of host addresses from a list of URLs (and do it as threads)
hosts = ['www.ericsson.com', 'www.neueda.com', 'www.crappytaxidermy.com']
jobs = [gevent.spawn(gevent.socket.gethostbyname, host) for host in hosts]
# start all the threads then join all the threads
gevent.joinall(jobs, timeout=5)
for job in jobs:
    print(job.value)