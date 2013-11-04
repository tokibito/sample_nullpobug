CREATE SEQUENCE item_seq;
CREATE TABLE item (
  id INTEGER PRIMARY KEY DEFAULT NEXTVAL('item_seq'),
  code VARCHAR(10) UNIQUE,
  name VARCHAR(100),
  price INTEGER,
  category VARCHAR(20)
);

CREATE SEQUENCE bundle_seq;
CREATE TABLE bundle (
  id INTEGER PRIMARY KEY DEFAULT NEXTVAL('bundle_seq'),
  bundle_name VARCHAR(100)
);

CREATE SEQUENCE bundle_item_seq;
CREATE TABLE bundle_item (
  id INTEGER PRIMARY KEY DEFAULT NEXTVAL('bundle_item_seq'),
  bundle_id INTEGER,
  item_id INTEGER
);

INSERT INTO item (code, name, price, category) VALUES (
  '001',
  'りんご',
  100,
  'fruit'
);

INSERT INTO item (code, name, price, category) VALUES (
  '002',
  'みかん',
  50,
  'fruit'
);

INSERT INTO item (code, name, price, category) VALUES (
  '003',
  'じゃがいも',
  80,
  'vegetable'
);

INSERT INTO item (code, name, price, category) VALUES (
  '004',
  'にんじん',
  90,
  'vegetable'
);

INSERT INTO item (code, name, price, category) VALUES (
  '005',
  'たまねぎ',
  60,
  'vegetable'
);
