# 10% Docker for beginners

Containers are a way to package, deploy and run an application or a service. This repository contains instructions and exercises to get acquainted with containers.

## Why Docker?

Docker is to containers what Google is to search engines. It's become a verb; like googling the web we also dockerise our applications.

Docker was the first to build an API around a container runtime and uses a CLI to control it and enable the building and running of containers.

Containers are native to the Unix/Linux operating system, so you're in luck if you use that on your machine. But also on Windows or MacOS you can experience the benefits of working with containers. You'll just need to install a virtual machine.

## Container vs. Virtual Machine

Although often mentioned in one breath, containers are different from VMs.

![Difference between virtual machines and containers](assets/images/SWTM-2060_Diagram_Containers_VirtualMachines_v03.png)
<sup>\* Image taken from [Atlassian](https://www.atlassian.com/microservices/cloud-computing/containers-vs-vms)</sup>

VMs require a hypervisor on top of the hardware and the host operating system in order to run. This architecture allows us to run Windows and Linux on a Mac.

Containers require a Container Engine which is native to most Unix/Linux systems.

**Docker Desktop** is in fact a virtual machine that contains a GuestOS with a Container Engine.

## Open Container Initiative

https://opencontainers.org/

> The OCI currently contains three specifications: the Runtime Specification (runtime-spec), the Image Specification (image-spec) and the Distribution Specification (distribution-spec). The Runtime Specification outlines how to run a “filesystem bundle” that is unpacked on disk. At a high-level an OCI implementation would download an OCI Image then unpack that image into an OCI Runtime filesystem bundle. At this point the OCI Runtime Bundle would be run by an OCI Runtime.

Basically the idea behind this is 'build once, run everywhere' (like Java).

## Terminology

Entering the container ecosystem will surround you with a lot of new buzzwords. RedHat has a nice page where they are explained:

https://developers.redhat.com/blog/2018/02/22/container-terminology-practical-introduction

## Excercises

1. [Getting started](exercises/exercise-1/README.md)
2. [Container images](exercises/exercise-2/README.md)
3. [Running containers](exercises/exercise-3/)
4. [Exposing containers](exercises/exercise-4/README.md)
5. [Inside containers](exercises/exercise-5/README.md)
6. [Building images](exercises/exercise-6/README.md)
7. [Building images from scratch](exercises/exercise-7/README.md)
8. [Building images with intermediate steps](exercises/exercise-8/README.md)
9. [Registering images](exercises/exercise-9/README.md)

## Advanced topics

- [Networking](https://docs.docker.com/network/) (ingress/egress)
- [Volumes](https://docs.docker.com/storage/volumes/) (persistant storage)
- [Scout](https://docs.docker.com/scout/) (scan for vulnerabilities)
- [Compose](https://docs.docker.com/compose/) (run multiple containers in one go)
- [Cross Platform Builds](https://docs.docker.com/build/building/multi-platform/) (arm64, aarch64, amd64)
- [Swarm](https://docs.docker.com/engine/swarm/) (manage a hive)
- [Kubernetes](https://kubernetes.io/) (container orchestration)
