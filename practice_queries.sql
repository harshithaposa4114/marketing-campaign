-- Campaign metrics
SELECT CampaignID, Channel,
       100.0*Clicks/NULLIF(Impressions,0) AS CTR_pct,
       100.0*Conversions/NULLIF(Clicks,0) AS ConversionRate_pct,
       Spend/NULLIF(Conversions,0) AS CostPerConversion
FROM campaigns;
