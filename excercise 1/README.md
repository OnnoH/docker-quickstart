# Exercise One

## Getting started

### Prerequisites

- Docker Desktop installed
  https://docs.docker.com/get-docker/
- Access to a terminal/command prompt

Docker is free for personal use, but if you want to keep things private or use it in a commercial fashion then a license is needed (https://www.docker.com/pricing/).

Alternatively you can use Podman (https://podman.io/docs/installation). In theory you can replace `docker` with `podman`, but in practice ymmv.

The excercises in this repository target Docker.

### Docker Desktop

**Docker Desktop** is a virtual machine that contains a GuestOS with a Container Engine.

Checkout the **Settings** and in particular the **Resources** section on your machine.

### Litmus test

Open up a terminal or a command prompt and type

```shell
docker version
```

If all is working as it should, some version information is visible on the screen.

Pay attention to the **OS/Arch** properties in the output. Although you can probably use Docker on every Unix/Linux machine, the hardware underneath determines which images can be used. Not every CPU architecture is supported, because you need to build those images for ever

### Docker CLI

Issuing the Docker commands is done via a CLI that comes with the Docker Desktop and is available if you passed the litmus test.

Just run the `docker` command without any parameters and your screen will be flooded.

The most common commands are listed on top. To get more information on a specific command, just type `docker <command>` followed by `--help`. E.g.

```shell
docker pull --help
```
