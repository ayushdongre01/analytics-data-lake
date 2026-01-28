relationship (analytics view)
----------------------------

Id                          String
Name                        String
DisplayName                 String

InceptionDate               String
TerminationDate             String

CrmSource                   String
ClientTypeId                Int64

FinancialTeamTemplateId     String
FinancialTeamTemplateName   String

FinancialTeam               Array / JSON
Teams                       Array / JSON
Portfolios                  Array / JSON
Accounts                    Array / JSON
Contacts                    Array / JSON
RelationshipAddresses       Array / JSON
FirmUsers                   Array / JSON
RelationshipOutsideIdentifiers  Array / JSON
RelationshipCustomFields    Array / JSON


Notes:
- This schema represents the flattened analytics view derived from Parquet.
- Nested relationship mappings (Accounts, Portfolios, Contacts) are retained as
  JSON arrays to preserve relationship context and can be normalized further
  if required by analytical use cases.
