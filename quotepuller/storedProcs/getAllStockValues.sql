CREATE PROCEDURE `getAllStockValues`()
BEGIN
	SELECT 
		c.mnemonic as stockName,
        c.guid as commodity_guid,
		IF(c.namespace = 'Commodity', 1, 0 ) as isCommodity,
		SUM(s.quantity_num / quantity_denom) as stockQty,
		SUM(s.quantity_num / quantity_denom) * p.recentPrice as stockVal,
		p.date as lastPriceDate, 
		p.recentPrice as lastPriceVal
	FROM accounts a
		JOIN (SELECT p.commodity_guid, p.date, (value_num / value_denom) as recentPrice
			FROM prices p
			JOIN (SELECT commodity_guid, MAX(date) as MaxDate
					FROM prices p 
					GROUP BY commodity_guid) p2 ON p.commodity_guid = p2.commodity_guid AND p.date = p2.MaxDate
		) p ON a.commodity_guid = p.commodity_guid
		JOIN commodities c on a.commodity_guid = c.guid
		JOIN splits s on s.account_guid = a.guid
	WHERE account_type = 'STOCK' AND (c.namespace = 'NYSE' OR c.namespace = 'Commodity')
	GROUP BY a.commodity_guid
	HAVING stockQty > 0;
END