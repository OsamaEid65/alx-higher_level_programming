SELECT column_name, column_type
FROM information_schema.columns
WHERE table_schema = DATABASE() AND table_name = 'first_table';

