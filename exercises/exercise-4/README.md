# Exercise Four

Now that you've seen containers that are quite ephemeral, how about long running or everlasting processes?

Take a webserver for instance.

```shell
docker pull nginx
docker run --rm nginx
```

As you can see, based on the output, the webserver starts, but it stops as soon as you close your terminal or press Control-C. In a previous example we used the ampersand (&) to direct the job to the background. Docker has an option for running containers 'detached'.

```shell
docker run --name ididitmyweb --rm --detach nginx
docker ps
```

## Logs

So the container is running, but where's my output?

Docker captures the output of a container in a logfile, which is readable through the API.

```shell
docker logs ididitmyweb
```

or show the last 10 lines

```shell
docker logs --tail 10 ididitmyweb
```

or if you want to follow the log stream

```shell
docker logs --follow ididitmyweb
```

Press Control-C to quit the stream.

## Break out of isolation

Now spinning up a webserver only makes sense if you can access it from outside the container. Depending on how the image was created one or more ports may be exposed.

If you look at the output of `docker ps` under **PORTS** you see _80/tcp_ as an indication that port 80 is exposed. There's a more extensive way to 'inspect' a container:

```shell
docker container inspect --format="{{ json .Config.ExposedPorts }}" ididitmyweb
```

The result is a JSON that shows that port 80 is indeed exposed. And that means we can 'bind' it to the 'outside'.

```shell
# First stop the container
docker stop ididitmyweb
# Run again but with an accessible port 80
docker run --name ididitmyweb --rm --detach --publish 80:80 nginx
# List the container processes and notice the difference in the PORTS column
docker ps
# And check access
curl localhost
```

Instead of `curl` you can of course also open up a browser to http://localhost.

The binding is set to `0.0.0.0:80` which means that every IP address can access this container on port 80. Of course more granular control can be configured, but Docker Networking is not for the faint of heart and definitely no stuff for beginners.

Now networking is in place how about files? Checkout the next section.
