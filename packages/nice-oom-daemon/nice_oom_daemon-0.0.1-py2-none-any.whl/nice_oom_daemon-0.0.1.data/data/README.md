

# Use

`nice-oom-daemon --stop-signal sigint=50 sigterm=50 sigkill=5 --grace-period 5`

# Use in Docker

```
docker build -t nice-oom-daemon .
docker run -v /var/run/docker.sock:/var/run/docker.sock nice-oom-daemon
```