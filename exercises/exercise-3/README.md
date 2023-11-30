# Exercise Three

## Putting the images to work

The previous exercise gave a sneak preview on running a container. Let's try this again with our BusyBox.

> BusyBox: The Swiss Army Knife of Embedded Linux

https://busybox.net/about.html

To see the capabilities of `busybox`:

```shell
docker run busybox busybox
```

To list the contents of the root folder inside a container:

```shell
docker run busybox busybox ls -la
```

It should look different from the root folder on your machine.

You can omit the busybox command, because the container has all the symbolic links inside (https://busybox.net/downloads/BusyBox.html).

```shell
docker run busybox ls -la
```

or list the content of a file

```shell
docker run busybox cat /etc/passwd
```

## Where's the container gone?

Running containers can be shown using

```
docker container ps
```

or `docker ps` for short.

This will probably come up empty, so try this

```shell
docker run busybox sleep 10 &

docker ps
```

The same as with the list of images there's an ID, but where image ID's don't change, container IDs are created on every run. The same applies to the name which uses a funny algorithm. The rest of the attributes speak for themselves.

## Naming things

Container ID's and names that are generated aren't always practical if you want to identify container processes. Fortunately you can specify your own `--name`.

```shell
docker run --name sandman busybox sleep 10 &

docker ps
```

Please note that if you name your containers and try to run it again, you'll see an error:

> docker: Error response from daemon: Conflict. The container name "/sandman" is already in use ...

Use the `container start` (or just `start`) command to tackle this.

```shell
docker container start sandman

docker ps
```

No need to specify the command again!

## What a mess!

Now type

```shell
docker ps --all
```

Chances are that you'll see some stale containers. How to get rid of them?

As with images, containers can also be removed.

```shell
docker container rm sandman
```

or a bit shorter and multiple stale containers

```shell
docker rm ae351f239032 7439b81002cb
```

or if there are a lot of them

```shell
docker container prune
```

Removing active containers will result in a error.

```shell
docker run --name sandman busybox sleep 10 &

docker rm sandman
```

> Error response from daemon: You cannot remove a running container ...

So you'll have to stop them first.

```shell
docker start sandman
docker ps
docker stop sandman
docker ps -a
docker rm sandman
```

Type fast, you only have 10 seconds...

In fact `docker stop` will gracefully shutdown the container and it might even complete the sleep. If you're impatient or the stop fails, there's always `docker kill`.

## Auto clean-up

To remove containers every time after they ran sounds a bit tedious and should be automated. Of course there's an option that takes care of that. Try:

```shell
docker run --rm busybox ls -la
docker ps -a
```

If there's no more rubbish we can start looking into containers that are not that ephemeral.
