# Exercise Nine

## Keep pushing

If you want to keep your images it's better to store them in a supported registry. For Docker the Docker Hub is the place to go, but you'll need an account: https://hub.docker.com/signup

Once created you can login.

```shell
docker login
```

Make sure your images are tagged with your Docker Hub username.

```shell
docker tag java-app onnoh/java-app
```

Then upload the image to the registry.

```shell
docker push onnoh/java-app
```
