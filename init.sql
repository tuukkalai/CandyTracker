CREATE TABLE polls (
  id SERIAL PRIMARY KEY,
  topic TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE choices (
  id SERIAL PRIMARY KEY,
  poll_id INTEGER REFERENCES polls,
  choice TEXT
);
CREATE TABLE answers (
  id SERIAL PRIMARY KEY,
  choice_id INTEGER REFERENCES choices,
  sent_at TIMESTAMP
);
CREATE TABLE candies (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  size INTEGER,
  sugar INTEGER,
  gtin BIGINT,
  company TEXT,
  category TEXT
);
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username TEXT NOT NULL,
  password TEXT NOT NULL,
  auth TEXT NOT NULL DEFAULT 'admin'
);
CREATE TABLE entries (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users,
  candy_id INTEGER REFERENCES candies,
  entry_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE messages (
  id SERIAL PRIMARY KEY,
  content TEXT
);

INSERT INTO users (username, password, auth) VALUES ('tuukkala','pbkdf2:sha256:150000$yRBgegD3$3fe8c0556671f2be8980adb133a7164db21531f7f8c4011bb55f3db4f77714ee','admin');
INSERT INTO candies (name, size, sugar, gtin, company, category) VALUES ('Karl Fazer Maitosuklaa', 200, 96, 6411401015090, 'Fazer', 'Chocolate'), ('Remix Mad', 350, 210, 6416453034945, 'Fazer', 'Candy bag');