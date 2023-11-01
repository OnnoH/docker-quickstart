# Exercise Eight

## Intermediates or Slicks?

When creating a containerised application using a runtime language like Python, the images can be built in one step. If you consider a compiled, transpiled or JVM language an additional build step is probably required. Of course this can be done in a CI/CD pipeline where the build results are stored on some shared storage. But it's also possible to let Docker use multiple stages.

When you look at `Dockerfile.react` you'll notice two stages. The first is identified as `builder` and will create the React app. In the second stage the build result is copied over using the `--from` option. Building the image and running the container is business as usual:

```shell
# Create the build context folder
mkdir react
# Build the image
docker build --tag react-app --file Dockerfile.react react
# Run the container
docker run --rm --name my-react-app --detach --publish 80:80 react-app
# Open the application
open http://localhost
```

If you prefer Java, using the `Dockerfile.java` is the way to go.

```shell
# Create the build context folder
mkdir java
# Build the image
docker build --tag java-app --file Dockerfile.java java
# Run the container
docker run --rm --name my-java-app --detach --publish 80:8080 java-app
# Open the application
open http://localhost
```

## Housekeeping

When creating images some intermediate results may be left behind. If you look at the output of `docker images ls`, some entries contain `<none>`. Those so-called 'dangling' images can be removed by issueing the following command:

```shell
docker image prune
```

During the image building Docker created a cache. That's why a second consecutive build runs faster. Specifically when the internet is downloaded getting the NPM packages or Maven dependencies. Sadly using a cache can cause issues. To clean up the build cache:

```shell
docker builder prune
```

All's gone!
