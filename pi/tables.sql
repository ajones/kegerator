CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS kegweights (
	id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
	keg_id text NOT NULL,
	weight_lbs real NOT NULL,
	created_at timestamp NOT NULL DEFAULT NOW()
);
CREATE INDEX kegweights_keg_id ON kegweights (keg_id);