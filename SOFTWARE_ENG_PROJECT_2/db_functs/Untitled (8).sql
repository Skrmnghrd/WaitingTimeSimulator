CREATE TABLE `cashier` (
  `cashier_id` int(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `cashier_uuid` varchar(255) DEFAULT NULL,
  `cashier_people_served` int(11) DEFAULT NULL
);

CREATE TABLE `cashier_queue` (
  `cashier_q_id` int(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `cashier_q_cashier_uuid` varchar(255) DEFAULT NULL,
  `cashier_q_cust_uuid` varchar(255) DEFAULT NULL,
  `cashier_q_service_needed` float(11) DEFAULT NULL
);

CREATE TABLE `customers` (
  `customers_id` int(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `customers_entry_time` int(11) DEFAULT NULL,
  `customers_time_done` float(11) DEFAULT NULL,
  `customers_date` timestamp,
  `customers_served_by` varchar(255) DEFAULT NULL,
  `customer_uuid` varchar(255) DEFAULT NULL,
  `customer_service_needed` float(11) DEFAULT NULL,
  `DO_NOT_TOUCH_FOR_REFERENCE_ONLY_customer_service_needed` float(11) DEFAULT NULL,
  `customers_waiting_time` float(11) DEFAULT NULL
);

ALTER TABLE `cashier_queue` ADD FOREIGN KEY (`cashier_q_cashier_uuid`) REFERENCES `cashier` (`cashier_uuid`);

ALTER TABLE `cashier_queue` ADD FOREIGN KEY (`cashier_q_cust_uuid`) REFERENCES `customers` (`customer_uuid`);

ALTER TABLE `customers` ADD FOREIGN KEY (`customers_served_by`) REFERENCES `cashier` (`cashier_uuid`);

CREATE UNIQUE INDEX `cashier_uuid` ON `cashier` (`cashier_uuid`);

CREATE UNIQUE INDEX `cashier_q_cust_uuid` ON `cashier_queue` (`cashier_q_cust_uuid`);

CREATE INDEX `cashier_q_cashier_uuid` ON `cashier_queue` (`cashier_q_cashier_uuid`);

CREATE UNIQUE INDEX `customer_uuid` ON `customers` (`customer_uuid`);

CREATE INDEX `customers_served_by` ON `customers` (`customers_served_by`);
