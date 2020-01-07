-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/ZbbUo6
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

CREATE TABLE "User" (
    "UserID" int   NOT NULL,
    "Name" string   NOT NULL,
    "Address1" string   NOT NULL,
    "Address2" string   NULL,
    "Address3" string   NULL,
    CONSTRAINT "pk_User" PRIMARY KEY (
        "UserID"
     )
);

CREATE TABLE "Order" (
    "OrderID" int   NOT NULL,
    -- fiels documentation
    "UserID" int   NOT NULL,
    "TotalAmount" money   NOT NULL,
    "OrderStatusID" int   NOT NULL,
    CONSTRAINT "pk_Order" PRIMARY KEY (
        "OrderID"
     )
);

-- Table des transactions
CREATE TABLE "OrderLine" (
    "OrderLineID" int   NOT NULL,
    -- Date de l
    "OrderID" int   NOT NULL,
    "ActionID" int   NOT NULL,
    "Quantity" int   NOT NULL,
    "Date" date   NOT NULL,
    CONSTRAINT "pk_OrderLine" PRIMARY KEY (
        "OrderLineID"
     )
);

-- Table Action
CREATE TABLE "Action" (
    "ActionID" int   NOT NULL,
    -- name
    -- symbol
    -- Michelin
    "Name" varchar(20)   NOT NULL,
    -- ML.PA
    "Symbol" varchar(10)   NOT NULL,
    CONSTRAINT "pk_Action" PRIMARY KEY (
        "ActionID"
     ),
    CONSTRAINT "uc_Action_Name" UNIQUE (
        "Name"
    )
);

CREATE TABLE "OrderStatus" (
    "OrderStatusID" int   NOT NULL,
    "Name" string   NOT NULL,
    CONSTRAINT "pk_OrderStatus" PRIMARY KEY (
        "OrderStatusID"
     ),
    CONSTRAINT "uc_OrderStatus_Name" UNIQUE (
        "Name"
    )
);

-- Table type de compte
CREATE TABLE "Cpt" (
    "CptID" int   NOT NULL,
    CONSTRAINT "pk_Cpt" PRIMARY KEY (
        "CptID"
     )
);

-- name
-- Table listes des comptes d'un user
CREATE TABLE "CptLine" (
    "CptLineID" int   NOT NULL,
    "CptID" int   NOT NULL,
    "UserID" int   NOT NULL,
    CONSTRAINT "pk_CptLine" PRIMARY KEY (
        "CptLineID"
     )
);

ALTER TABLE "Order" ADD CONSTRAINT "fk_Order_UserID" FOREIGN KEY("UserID")
REFERENCES "User" ("UserID");

ALTER TABLE "Order" ADD CONSTRAINT "fk_Order_OrderStatusID" FOREIGN KEY("OrderStatusID")
REFERENCES "OrderStatus" ("OrderStatusID");

ALTER TABLE "OrderLine" ADD CONSTRAINT "fk_OrderLine_OrderID" FOREIGN KEY("OrderID")
REFERENCES "Order" ("OrderID");

ALTER TABLE "OrderLine" ADD CONSTRAINT "fk_OrderLine_ActionID" FOREIGN KEY("ActionID")
REFERENCES "Action" ("ActionID");

ALTER TABLE "CptLine" ADD CONSTRAINT "fk_CptLine_CptID" FOREIGN KEY("CptID")
REFERENCES "Cpt" ("CptID");

ALTER TABLE "CptLine" ADD CONSTRAINT "fk_CptLine_UserID" FOREIGN KEY("UserID")
REFERENCES "User" ("UserID");

CREATE INDEX "idx_User_Name"
ON "User" ("Name");

