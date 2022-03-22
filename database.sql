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
  joined TIMESTAMP DEFAULT NOW(),
  visible BOOLEAN NOT NULL DEFAULT true
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
  visible BOOLEAN NOT NULL DEFAULT true,
  requests INTEGER[]
);
CREATE TABLE messages (
  id SERIAL PRIMARY KEY,
  content TEXT NOT NULL,
  user_id INTEGER NOT NULL REFERENCES users,
  timestamp TIMESTAMP DEFAULT NOW(),
  group_id INTEGER NOT NULL REFERENCES groups
);
CREATE TABLE challenges (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  max INTEGER NOT NULL DEFAULT 0,
  max_days INTEGER NOT NULL DEFAULT 0,
  start_date DATE DEFAULT CURRENT_DATE,
  end_date DATE DEFAULT CURRENT_DATE
);
CREATE TABLE group_challenges (
  id SERIAL PRIMARY KEY,
  challenge_id INTEGER NOT NULL REFERENCES challenges,
  group_id INTEGER NOT NULL REFERENCES groups,
  date_completed DATE,
  date_started DATE
);
