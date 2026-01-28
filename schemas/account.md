account (analytics view)
------------------------
Id                          String
Name                        String
CustodialAccountName        String
AccountNumber               String
Custodian                   String
AccountType                 String
Discretionary               Bool
Billable                    Bool
Supervised                  Bool
PositionOnly                Bool
CreateDate                  DateTime

CostBasis.AssetId           UInt32
CostBasis.EMV               Float64
CostBasis.Units             Float64
CostBasis.CostBasis         Float64

Details.TotalEmv            Float64
Details.SupervisedEmv       Float64
Details.UnsupervisedEmv     Float64


Note:
Nested collections such as Holdings, Transactions, Tags, and Team
are retained in raw form or modeled separately and are not part of
the primary analytics schema.
