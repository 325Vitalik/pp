CREATE DATABASE Pharmacy;

CREATE TABLE Pharmacy.user (
  first_name LONGTEXT NOT NULL,
  last_name LONGTEXT,
  id NVARCHAR(36) PRIMARY KEY NOT NULL,
  birthday DATE,
  email NVARCHAR(365) NOT NULL,
  phone_number NVARCHAR(50),
  role NVARCHAR(30) NOT NULL
);

CREATE TABLE Pharmacy.medicine (
  id NVARCHAR(36) PRIMARY KEY NOT NULL,
  name LONGTEXT NOT NULL,
  price DECIMAL(18,0) NOT NULL,
  amount INT NOT NULL
);

CREATE TABLE Pharmacy.buy (
  amount INT DEFAULT 1,
  id NVARCHAR(36) PRIMARY KEY NOT NULL,
  user_id NVARCHAR(36) NOT NULL,
  medicine_id NVARCHAR(36) NOT NULL,
  FOREIGN KEY (user_id) REFERENCES Pharmacy.user(id),
  FOREIGN KEY (medicine_id) REFERENCES Pharmacy.medicine(id)
);

CREATE TABLE Pharmacy.demand (
  amount INT DEFAULT 1,
  id NVARCHAR(36) PRIMARY KEY NOT NULL,
  user_id NVARCHAR(36) NOT NULL,
  medicine_id NVARCHAR(36) NOT NULL,
  FOREIGN KEY (user_id) REFERENCES Pharmacy.user(id),
  FOREIGN KEY (medicine_id) REFERENCES Pharmacy.medicine(id)
);