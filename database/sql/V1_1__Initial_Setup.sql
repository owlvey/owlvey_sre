create table Users(
    user_id int not null AUTO_INCREMENT,
    email varchar(512),
    PRIMARY KEY(user_id)
);

insert into Users(email) values('test@hotmail.com');

create table Customers(
    customer_id int,
    name varchar(256),
    PRIMARY KEY(customer_id)
);

create table CustomersUsers(
    customer_user_id int,
    customer_id int,
    user_id int,
    PRIMARY KEY(customer_user_id)
);

create table Products(
    product_id int,
    customer_id int,
    name varchar(256),
    PRIMARY KEY(product_id),
    FOREIGN KEY(customer_id) REFERENCES Customers(customer_id)
);

create table Services(
    service_id int,
    product_id int,
    name varchar(256),
    PRIMARY KEY(service_id),
    FOREIGN KEY(product_id)REFERENCES Products(product_id)
);

create table Squads(
    squad_id int,
    customer_id int,
    name varchar(256),
    PRIMARY KEY(squad_id),
    FOREIGN KEY(customer_id) REFERENCES Customers(customer_id)
);

create table Features(
    feature_id int,
    name varchar(256),
    PRIMARY KEY(feature_id)
);

create table Sources(
    source_id int,
    name varchar(256),
    good_definition varchar(2024),
    total_definition varchar(2024),
    PRIMARY KEY(source_id)
);

create table Events(
    event_id int,
    source_id int,
    good int,
    total int,
    start_date DATE,
    end_date DATE,
    PRIMARY KEY(event_id),
    FOREIGN KEY(source_id) REFERENCES Sources(source_id)
);