-- creates an index idx_name_first on the table names and the first letter of a name.
CREATE INDEX idx_name_first on names(name(1));
