asset (analytics view)
---------------------

AssetId                 Int64
AssetName               String
AssetNameShort          String
Ticker                  String
Cusip                   String
DisplayCusip            String
AlternateId             String

SuperClassId            Int64
SuperclassName          String
SuperClassOrdinal       Int64

ClassName               String
ClassId                 Int64
ClassOrdinal            Int64

SectorSegment            String
SectorSegmentId          Int64
SectorSegmentOrdinal     Int64

SegmentName             String
CapSegmentid            Int64
CapSegmentOrdinal       Int64

ProviderIssueType       String

Cash                    Bool
IsCashEquivalent        Bool
MoneyMarket             Bool
Archived                Bool

OriginalAssetName       String
SECAssetType            String

CouponRate              String
LastDividend            String
MaturityDate            String
FirstPaymentDate        String
IssueDate               String
CallDate                String

TaxStatus               String
PayDownFactor           String
PriceFactor             Float64
MuniState               String
Yield                   Float64

Billable                Bool
Supervised              Bool
Discretionary           Bool

Exchange                String

AssetTags               Array / JSON

Notes:
- This schema represents the flattened analytics view derived from Parquet.
- Nested or semi-structured fields such as AssetTags are retained as JSON for flexibility.
- Date fields are currently stored as strings and can be cast during query time if required.
