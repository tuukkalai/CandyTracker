CREATE TABLE candies (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  size INTEGER,
  sugar INTEGER,
  gtin BIGINT UNIQUE,
  company TEXT,
  category TEXT
);
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  auth TEXT NOT NULL DEFAULT 'user',
  joined TIMESTAMP DEFAULT NOW()
);
CREATE TABLE entries (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users,
  candy_id INTEGER REFERENCES candies,
  entry_time DATE DEFAULT CURRENT_DATE,
  visible BOOLEAN NOT NULL DEFAULT true
);
CREATE TABLE groups (
  id SERIAL PRIMARY KEY,
  name TEXT UNIQUE NOT NULL,
  members INTEGER[],
  open BOOLEAN NOT NULL DEFAULT false,
  visible BOOLEAN NOT NULL DEFAULT true
);