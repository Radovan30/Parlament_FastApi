-- Přidání výchozího administrátora (heslo: "admin123", musíš hashovat ručně)
INSERT INTO admin_users (username, password_hash)
VALUES ('admin', '$2b$12$3bqcH9QHqfz8AeIVsU1FO.5zV1aCtOs3NQ.YzAVdRQ2G6mVJdwWxK');

-- Přidání testovacího denního menu
INSERT INTO daily_menu (date, soup, meal_1, meal_1_price, meal_2, meal_2_price, meal_3, meal_3_price)
VALUES
    ('2025-02-7', 'Hovězí vývar', 'Vepřo knedlo zelo', 139.99, 'Losos s bramborami', 149.99, 'Těstoviny s pestem', 119.99),
    ('2025-02-8', 'Čočková polévka', 'Pečená kachna s červeným zelím', 149.99, 'Smažený sýr s hranolkami', 119.99, 'Salát Caesar s kuřecím masem', 109.99),
    ('2025-02-9', 'Bramborová polévka', 'Vepřová panenka s omáčkou', 139.99, 'Losos na grilu s bylinkovým máslem', 159.99, 'Špagety Carbonara', 119.99),
    ('2025-02-10', 'Gulášová', 'Svíčková na smetaně', 129.99, 'Kuřecí steak', 119.99, 'Vegetariánská pizza', 109.99),
    ('2025-02-11', 'Rajská polévka', 'Hovězí guláš s houskovým knedlíkem', 129.99, 'Grilovaný hermelín s brusinkami', 109.99, 'Rizoto se zeleninou', 99.99);

-- Přidání testovacích nápojů
INSERT INTO drinks_menu (drink_name, drink_price)
VALUES
    ('Pivo 0.5l', 39.99),
    ('Víno červené 2dcl', 49.99),
    ('Káva Espresso', 29.99),
    ('Cola 0.33l', 35.99);

-- Přidání kategorií nápojů
INSERT INTO categories (name) VALUES
    ('Pivo čepované'),
    ('Lahvové a plechovkové pivo'),
    ('Pivo nealkoholické'),
    ('Nealkoholické osvěžení'),
    ('Vína, sekty, aperitivy'),
    ('Lihoviny, likéry a whiskey'),
    ('Nealkoholické nápoje'),
    ('Teplé nápoje');

-- Přidání typů nápojů
INSERT INTO drink_types (name) VALUES
    ('Světlý ležák'),
    ('Světlé výčepní pivo'),
    ('Nealkoholické pivo'),
    ('Limonáda'),
    ('Víno červené'),
    ('Víno bílé'),
    ('Rum'),
    ('Vodka'),
    ('Káva'),
    ('Čaj');

-- Přidání nápojů
INSERT INTO drinks (drink_name, category_id, drink_type_id, volume, price, description)
VALUES
    -- Pivo čepované
    ('Pilsner Urquell', 1, 1, 0.5, 46.00, 'Čepované pivo'),
    ('Radegast Ryze Hořká 12', 1, 1, 0.5, 37.00, 'Čepované tankové pivo'),

    -- Lahvové a plechovkové pivo
    ('Pilsner Urquell - plechovka', 2, 1, 0.5, 46.00, 'Lahvové pivo'),
    ('Velkopopovický Kozel Černý', 2, 2, 0.5, 34.00, 'Černé pivo'),

    -- Pivo nealkoholické
    ('Birell světlý - čepovaný', 3, 3, 0.5, 35.00, 'Světlé nealkoholické pivo'),
    ('Birell polotmavý - láhev', 3, 3, 0.5, 34.00, 'Polotmavé nealkoholické pivo'),

    -- Nealkoholické osvěžení
    ('Birell pomelo & grep', 4, 4, 0.5, 37.00, 'Míchaný nápoj z nealkoholického piva'),

    -- Vína, sekty, aperitivy
    ('Vino rozlévané - červené', 5, 5, 0.2, 28.00, 'Dle nabídky'),
    ('Bohemia sekt', 5, 6, 0.7, 220.00, 'Šumivé víno'),

    -- Lihoviny, likéry a whiskey
    ('Božkov Tuzemský', 6, 7, 0.04, 25.00, 'Rum'),
    ('Finlandia - Vodka', 6, 8, 0.04, 28.00, 'Vodka'),

    -- Nealkoholické nápoje
    ('Coca Cola original', 7, 4, 0.33, 36.00, 'Nealkoholický nápoj'),
    ('Sprite', 7, 4, 0.33, 36.00, 'Nealkoholický nápoj'),
    ('Rauch juice', 7, 4, 0.25, 29.00, 'Ovocný džus'),

    -- Teplé nápoje
    ('Espresso', 8, 9, 0.07, 25.00, 'Káva Grande Cuvée'),
    ('Čaj "DILMAH"', 8, 10, 0.3, 31.00, 'S citronem a medem');
