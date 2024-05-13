CREATE TABLE ACCOUNT_REJECT_CLAUSE (
    Account_nbr VARCHAR(10) PRIMARY KEY,
    Reject_Clause VARCHAR(255)
);


CREATE TABLE Reject_clause_vs_key_fields (
    Reject_Clause VARCHAR(255),
    Key_Field_Name VARCHAR(50)
);

CREATE TABLE Account_nbr_vs_all_key_fields (
    Account_nbr VARCHAR(10) PRIMARY KEY,
    program_type INT,
	product_cd INT
);