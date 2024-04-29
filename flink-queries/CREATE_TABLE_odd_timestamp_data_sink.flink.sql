CREATE TABLE odd_timestamp_data_sink (
        id STRING,
        payment_timestamp TIMESTAMP,
        account_number STRING,
        account_holder STRING,
        payment_amount FLOAT 
) WITH (
    'connector' = 'kafka',
    'properties.bootstrap.servers' = 'sa-kafka-homework-carlsongould-2cdd.l.aivencloud.com:10358',
    'scan.startup.mode' = 'earliest-offset',
    'topic' = 'odd_timestamp_data_sink',
    'value.format' = 'json')