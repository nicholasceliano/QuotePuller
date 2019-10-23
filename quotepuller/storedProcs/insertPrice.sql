CREATE PROCEDURE `insertPrice` (IN guid varchar(32), IN commodity_guid varchar(32), IN currency_guid varchar(32), IN date timestamp,
IN source varchar(2048), IN type varchar(2048), IN value_num bigint(20), IN value_denom bigint(20))
BEGIN
    INSERT INTO prices (guid, commodity_guid, currency_guid, date, source, type, value_num, value_denom) 
    VALUES (guid, commodity_guid, currency_guid, date, source, type, value_num, value_denom);
END