-- creates an index idx_name_first_score on table names, 1st letter & score.
CREATE INDEX idx_name_first_score ON names(name(1), score);
