# Exercise Seven

## From scratch

Starting with a clean slate, you can create rather small images.

To build the image, change to the 'exercises/exercise-7' of the root of this repository.

Look at the `Dockerfile.scratch` file. It contains a build argument (**ARG**) with a default `arm64`. The jq executable for the given CPU architecture is copied over to the image.

Build it

```shell
docker image build --tag basic \
                   --file Dockerfile.scratch \
                   --build-arg="arm64" \
                   scratch
```

and run it

```shell
docker run --rm basic .bar some.json
```

## Alpine

Sometimes there's a need for an underlying operating system, e.g. because your containerised application requires the use of a different C-library set or requires a process daemon to run multiple tasks simultaneously.

[Alpine Linux](https://alpinelinux.org/) is a popular variant because it is rather small compared to e.g. Ubuntu.

Goto https://alpinelinux.org/downloads/ and fetch the miniroot filesystem archive for your favourite architecture and place it in the `alpine` folder under this exercise.

```shell
docker image build --tag alpine:3.18.4 \
                   --file Dockerfile.alpine \
                   --build-arg="ARCH=aarch64" \
                   alpine
```

And run it

```shell
# Enter the shell
docker run --rm -it alpine:3.18.4

# Run a command to find the architecture
docker run --rm alpine:3.18.4 uname -a
```

> The `Dockerfile.alpine` contains an **ADD** statement. If the first argument is a (compressed) tar, it is expanded automatically. It can also be an URL to fetch a (tar) file from a remote location, but that will not be processed, so some additional commands may be necessary.

## CMD vs ENTRYPOINT

> ENTRYPOINT is the process that’s executed inside the container.

> CMD is the default set of arguments that are supplied to the ENTRYPOINT process.

See: https://spacelift.io/blog/docker-entrypoint-vs-cmd
