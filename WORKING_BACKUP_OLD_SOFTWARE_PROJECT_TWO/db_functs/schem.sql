Table "cashier" {
  "cashier_id" int(11) [pk, not null, increment]
  "cashier_uuid" varchar(255) [default: NULL]
  "cashier_people_served" int(11) [default: NULL]

        
Indexes {
  cashier_uuid [unique, name: "cashier_uuid"]
}
}

Table "cashier_queue" {
  "cashier_q_id" int(11) [pk, not null, increment]
  "cashier_q_cashier_uuid" varchar(255) [default: NULL]
  "cashier_q_cust_uuid" varchar(255) [default: NULL]
  "cashier_q_service_needed" float(11) [default: NULL]

        
Indexes {
  cashier_q_cust_uuid [unique, name: "cashier_q_cust_uuid"]
  cashier_q_cashier_uuid [name: "cashier_q_cashier_uuid"]
}
}

Table "customers" {
  "customers_id" int(11) [pk, not null, increment]
  "customers_entry_time" int(11) [default: NULL]
  "customers_time_done" float(11) [default: NULL]
  "customers_date" timestamp
  "customers_served_by" varchar(255) [default: NULL]
  "customer_uuid" varchar(255) [default: NULL]
  "customer_service_needed" float(11) [default: NULL]
  "DO_NOT_TOUCH_FOR_REFERENCE_ONLY_customer_service_needed" int(11) [default: NULL]
  "customers_waiting_time" float(11) [default: NULL]

        
Indexes {
  customer_uuid [unique, name: "customer_uuid"]
  customers_served_by [name: "customers_served_by"]
}
}

Ref:"cashier"."cashier_uuid" < "cashier_queue"."cashier_q_cashier_uuid"

Ref:"customers"."customer_uuid" < "cashier_queue"."cashier_q_cust_uuid"

Ref:"cashier"."cashier_uuid" < "customers"."customers_served_by"
