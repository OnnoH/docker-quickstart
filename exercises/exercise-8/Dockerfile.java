# Stage 1
FROM maven:3.8.3-openjdk-17 as builder

WORKDIR /pet-clinic

RUN git clone https://github.com/spring-projects/spring-petclinic.git && \
    cd spring-petclinic && \
    mvn clean package -DskipTests

# Stage 2
FROM openjdk:17

COPY --from=builder /pet-clinic/spring-petclinic/target/spring-petclinic-3.2.0-SNAPSHOT.jar /petclinic.jar

CMD ["java", "-jar", "petclinic.jar"]