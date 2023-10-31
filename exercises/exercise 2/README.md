# Exercise Two

## Containers vs. Images

Containers are instances of images. You can compare it to a running Spring Boot application which base is the compiled JAR file.

Images can be created out of a definition and they reside in a registry. The most popular registry is the Docker Hub (https://hub.docker.com/). But you can also run a private registry or use the Nexus Repository Manager for instance.

Images are cached on your local machine and instantiated from there. If an images can't be located locally, it is pulled from a registry.

## My first image

When you've just installed Docker Desktop the local image 'cache' is empty. Run `docker image ls` or `docker images` to verify that.

So let's obtain our first image:

```shell
docker pull busybox
```

Depending on your internet connection the image is downloaded and expanded. Compression is used to save space in the registry and speed-up the download. For a faster runtime experience, they're are stored expanded in your Docker Desktop VM.

Run the list image command again

```shell
docker image ls
```

## Image properties

Next to an image ID, you see the size and the creation date. But more important are the **repository** and the **tag**.

The **repository** contains the name of the image and can be prefixed by a registry.

The **tag** is used to indicate a version and/or tell us something about the image specifics.

You'll often find the tag **latest**, which is used as a default. If you don't specify a tag when pulling in an image, latest is used. Remember it's just a tag and doesn't mean that it is actually the latest version.

> Docker tags are just an alias for an image ID.

## Be specific

Let's get a different version of the BusyBox image and list the images again.

```shell
docker pull busybox:1.35.0
docker image ls
```

And from another registry:

```shell
docker pull quay.io/quay/busybox
docker image ls
```

And the latest with the specific tag

```shell
docker pull busybox:1.36.1
docker image ls
```

Notice that the image ID for `busybox:latest` and `busybox:1.36.1` are the same.

## Clean up

We probably don't need that many versions of an image on our machine. Removing an image is easy:

```shell
docker image rm busybox:1.35.0
```

or

```shell
docker image rm cb300da5c300
```

or multiple in one go

```shell
docker image rm 0a2b6b0873db cb300da5c300
```

Note that `docker rmi` can be used as a shortcut and is one of the leftovers of the old API.

## Auto pull

As mentioned before, when you start a container, the local registry is used and if the specified image is not present, it's retrieved from the default registry.

```shell
docker run --rm -it wernight/funbox nyancat
```

Press Control-C to stop the container.
