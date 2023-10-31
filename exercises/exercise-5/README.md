# Exercise Five

## Entering the container

First make sure our webserver container is running and accessible.

```shell
docker run --name ididitmyweb --rm --detach --publish 80:80 nginx
curl localhost
```

Then we `exec` a shell to get into our running container.

```shell
docker container exec --interactive --tty ididitmyweb bash
# But probably you'll prefer the short version
docker exec -it ididitmyweb bash
```

> The shell that can be started depends on the image. Some images don't have a shell installed.

Roam around inside the container. Try to break it ;-)

Or change some web content (still inside a container).

```shell
echo "<html><body><h1>Hello World.</h1></body></html>" > /usr/share/nginx/html/index.html
```

Exit the container (Control-D) and again `curl localhost` or refresh the browser to see the change.

## Volumes

In this case it would be more convenient to access a file from the host file system. Mounting files or folders is done via Docker Volumes.

Stop the container ()`docker stop ididitmyweb`) and change into the folder `exercises/exercise-5` from the root of this repository. You're going to the `index.html` is this folder to the container using `--volume`.

```shell
docker run --name ididitmyweb \
    --rm --detach \
    --publish 80:80 \
    --volume ./index.html:/usr/share/nginx/html/index.html \
    nginx
```

For the last time (this exercise) use `curl localhost` or refresh the browser to see the change ;-)

Like Docker Networking is Docker Volumes extensive matter. Too much to deal with in a beginners course.
