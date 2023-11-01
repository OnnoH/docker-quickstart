# Exercise Six

## BYOI

Of course it's nice to not have to reinvent the wheel and borrow a cup of images from the neighbours. But there are a lot of reasons for you to want to build your own image...

- Internet restrictions
- Security
- Custom applications
- ...

Some good practices: https://docs.docker.com/develop/develop-images/dockerfile_best-practices/

Checkout the build command:

```shell
docker image build --help
```

## From webserver

Have a look at `Dockerfile.nginx`. Here you see that the base for this image (**FROM**) is `nginx` which we used in the previous exercise. Furthermore it brings over (**COPY**) the content of the _nginx_ folder, which contains a webpage.

To build the image, change to the 'exercises/exercise-6' folder from the root of this repository and issue the following command:

```shell
docker image build --tag ididitmyweb:1.0 --file Dockerfile.nginx nginx
```

After a (short) while you can run a container out of this image:

```shell
docker run --rm --detach --name ididitmyweb --publish 80:80 ididitmyweb:1.0

open http://localhost
```

Note that `:1.0` is added to the image name. Leaving it out would cause an error because then Docker would go look for `ididitmyweb:latest` which (hopefully) does not exist both locally and remote.

Adding the `latest` tag is easy:

```shell
docker image tag ididitmyweb:1.0 ididitmyweb:latest
```

This goes to show that the `latest` tag doesn't have to belong to the latest version of the image.

You can also alias the image name or rename it.

```shell
docker image tag ididitmyweb:1.0 someotherweb:1.0
docker image rm ididitmyweb:1.0
```

Note that the last command only removed the tag. Removing the last tag will in effect remove the image.

> Docker tags are just an alias for an image ID.

## The Nginx image

We used the prepared nginx image as a base.

https://hub.docker.com/_/nginx

And the Dockerfile(s) used to create this are here: https://github.com/nginxinc/docker-nginx

As you can see, image building is hard work and we're going to explore that in more detail in the next exercise.
