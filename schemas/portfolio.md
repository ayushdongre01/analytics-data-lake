portfolio (analytics view)
-------------------------

Id                          String
Name                        String
DisplayName                 String

ClientVisibility            Bool
RelationshipID              Int64
ExternalRelationshipID      String

IsMasterPortfolio           Bool
ExcludeFromRebalancing      Bool
AdminOnly                   Bool
DemoPortfolio               Bool
HistoryLoaded               Bool

AccountIds                  Array(String)

Address.City                String
Address.Company             String
Address.Line1               String
Address.Line2               String
Address.Line3               String
Address.State               String
Address.Zip                 String
Address.FirstName           String
Address.LastName            String
Address.MiddleInitial       String
Address.OverrideCustodialAddress  String
Address.AddressSource       String

Advisors                    Array / JSON
Goals                       Array / JSON
FeeSchedules                Array / JSON
Tags                        Array / JSON
Targets                     Array / JSON
Teams                       Array / JSON
Reporting                   Array / JSON
Benchmarks                  Array / JSON
PortfolioAccountGoals       Array / JSON
ReferencingRelationships    Array / JSON
OutsideIdentifiers          Array / JSON


Notes:
- This schema represents the flattened analytics view derived from Parquet.
- Nested collections are retained as JSON arrays and can be normalized into
  separate datasets if required.
- Address fields are partially flattened for common filtering and reporting use cases.
