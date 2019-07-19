#!/usr/bin/env bash


database/flyway/flyway clean -url=jdbc:mysql://localhost:3306/sredb -user=root -password=p@ssw0rd -locations=filesystem:./database/sql/

database/flyway/flyway migrate -url=jdbc:mysql://localhost:3306/sredb -user=root -password=p@ssw0rd -locations=filesystem:./database/sql/

database/flyway/flyway info -url=jdbc:mysql://localhost:3306/sredb -user=root -password=p@ssw0rd -locations=filesystem:./database/sql/




