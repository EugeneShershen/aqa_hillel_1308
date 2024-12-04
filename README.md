# aqa_hillel_1308
Automation QA Course Repository 13_08_2024

# Lesson_29: Docker
## Build the docker images for Database and Tests

### Database
```bash
docker build -t lesson29_db -f lesson_29/Dockerfile_db .
```

### Tests
```bash
docker build -t lesson29_test -f lesson_29/Dockerfile_test .
```

## Creating network for connecting Tests to Database

```bash
docker network create lesson_29
```

## Run the Database and Tests

### Database
```bash
docker run --network lesson_29 -p 5432:5432 -d lesson29_db
```

### Tests
```bash
docker run --network lesson_29 lesson29_test
```

# Lesson_30: Allure
## Create allure-report in one html-file
```bash
allure generate --single-file --clean
```