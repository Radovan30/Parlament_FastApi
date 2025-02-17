-- Přidání výchozího administrátora (heslo: "admin123", musíš hashovat ručně)
INSERT INTO admin_users (username, password_hash)
VALUES ('admin', '240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9');

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


-- Přidání categorii jídel
INSERT INTO food_categories (name) VALUES
    ('Polévky'),
    ('Pochoutky k pivu'),
    ('Salónková nabídka'),
    ('Bezmasá jídla'),
    ('Jídla z ryb');


-- Přidání jídel s is_special a image_url
INSERT INTO foods (food_name, category_id, weight, price, description, is_special, image_url) VALUES
    -- Polévky
    ('Slezská česnečka s vejcem, sýrem a krutony', 1, 0.33, 44.00, 'Sýrová polévka s česnekem a vejcem', 0, NULL),
    ('Masový vývar s játrovými knedlíčky a nudlemi', 1, 0.33, 44.00, 'Vývar s játrovými knedlíčky a domácími nudlemi', 0, NULL),
    ('Polévka dle denní nabídky', 1, 0.33, 33.00, 'Speciální polévka dle denní nabídky', 0, NULL),

    -- Pochoutky k pivu
    ('Nakládaný hermelín s feferonkou, chléb', 2, 1.00, 78.00, 'Nakládaný hermelín s feferonkou a chlebem', 0, NULL),
    ('Tvarůžkový talíř, máslo, cibule, chléb', 2, 0.10, 78.00, 'Tvarůžky s máslem, cibulí a chlebem', 0, NULL),
    ('Utopence s cibulí, chléb', 2, 1.00, 66.00, 'Utopence s cibulí a chlebem', 0, NULL),

    -- Salónková nabídka
    ('Těstovinový salát', 3, 1.00, 190.00, 'Salát s těstovinami a zeleninou', 0, NULL),
    ('Ovocná mísa', 3, 1.00, 180.00, 'Mísa čerstvého ovoce', 0, NULL),
    ('Zeleninová mísa', 3, 1.00, 180.00, 'Mísa čerstvé zeleniny', 0, NULL),
    ('Salámová mísa (4 druhy salámů s přízdobou)', 3, 1.00, 490.00, 'Výběr salámů s přízdobou', 0, NULL),
    ('Sýrová mísa (4 druhy sýrů s přízdobou)', 3, 1.00, 540.00, 'Sýrová mísa se 4 druhy sýrů', 0, NULL),
    ('Řízková mísa (vepřové a kuřecí s přízdobou)', 3, 1.00, 420.00, 'Řízky s přízdobou', 0, NULL),
    ('Kuřecí pečené špalíčky (s přízdobou)', 3, 1.00, 225.00, 'Pečené kuřecí špalíčky', 0, NULL),
    ('Marinovaná pečená vepřová kýta (cca 6 kg)', 3, 1.00, 280.00, 'Marinovaná kýta', 0, NULL),

    -- Speciální jídlo: Tatarský biftek
    ('Tatarský biftek (hovězí svíčková)', 3, 1.00, 1100.00, 'Tatarský biftek z hovězí svíčkové', 1, 'static/uploads/foods/rizek.jpg'),

    -- Bezmasá jídla
    ('Smažený sýr, hranolky', 4, 0.15, 145.00, 'Smažený sýr s hranolky', 0, NULL),
    ('Smažený hermelín, hranolky', 4, 0.12, 156.00, 'Smažený hermelín s hranolky', 0, NULL),
    ('Smažené tvarůžky, hranolky', 4, 0.10, 156.00, 'Smažené tvarůžky s hranolky', 0, NULL),
    ('Smažené žampiony, hranolky', 4, 0.15, 145.00, 'Smažené žampiony s hranolky', 0, NULL),
    ('Hermelín na bramborovém placku', 4, 0.30, 156.00, 'Hermelín na bramborové placce', 0, NULL),
    ('Zeleninové rizoto sypané sýrem', 4, 0.30, 119.00, 'Zeleninové rizoto se sýrem', 0, NULL),
    ('Halušky s bryndzou a smaženou cibulkou', 4, 0.30, 129.00, 'Halušky s bryndzou', 0, NULL),

    -- Jídla z ryb
    ('Rybí filé na másle, vařené brambory', 5, 0.20, 189.00, 'Rybí filé s máslem a brambory', 0, NULL),
    ('Smažené rybí filé, vařené brambory', 5, 0.20, 189.00, 'Smažené rybí filé s brambory', 0, NULL),
    ('Přírodní rybí filé na grilu se zeleninou, vařené brambory', 5, 0.20, 189.00, 'Grilované rybí filé s brambory', 0, NULL);



-- Přidání allergenů
INSERT INTO allergens (code, name) VALUES
    (1, 'Lepek'),
    (3, 'Vejce'),
    (7, 'Mléko'),
    (9, 'Celer'),
    (10, 'Hořčice'),
    (12, 'Oxid siřičitý a siřičitany');


-- Polévky
INSERT INTO food_allergens (food_id, allergen_id) VALUES
    (1, 1),   -- Slezská česnečka (Lepek)
    (1, 2),   -- Slezská česnečka (Vejce)
    (1, 3),   -- Slezská česnečka (Mléko)
    (2, 1),   -- Masový vývar (Lepek)
    (2, 2),   -- Masový vývar (Vejce)
    (3, 1);   -- Polévka dle denní nabídky (Lepek - závisí na nabídce)

-- Pochoutky k pivu
INSERT INTO food_allergens (food_id, allergen_id) VALUES
    (4, 3),   -- Nakládaný hermelín (Mléko)
    (5, 3),   -- Tvarůžkový talíř (Mléko)
    (6, 1);   -- Utopence (Lepek)

-- Salónková nabídka
INSERT INTO food_allergens (food_id, allergen_id) VALUES
    (7, 1),   -- Těstovinový salát (Lepek)
    (7, 2),   -- Těstovinový salát (Vejce)
    (10, 1),  -- Salámová mísa (Lepek)
    (10, 6),  -- Salámová mísa (Oxid siřičitý)
    (11, 3),  -- Sýrová mísa (Mléko)
    (12, 1),  -- Řízková mísa (Lepek)
    (12, 2),  -- Řízková mísa (Vejce)
    (13, 1),  -- Kuřecí pečené špalíčky (Lepek)
    (14, 1),  -- Marinovaná kýta (Lepek)
    (15, 1),  -- Tatarský biftek (Lepek)
    (15, 2);  -- Tatarský biftek (Vejce)

-- Bezmasá jídla
INSERT INTO food_allergens (food_id, allergen_id) VALUES
    (16, 1),  -- Smažený sýr (Lepek)
    (16, 3),  -- Smažený sýr (Mléko)
    (17, 1),  -- Smažený hermelín (Lepek)
    (17, 2),  -- Smažený hermelín (Vejce)
    (17, 3),  -- Smažený hermelín (Mléko)
    (18, 1),  -- Smažené tvarůžky (Lepek)
    (18, 3),  -- Smažené tvarůžky (Mléko)
    (19, 1),  -- Smažené žampiony (Lepek)
    (19, 2),  -- Smažené žampiony (Vejce)
    (20, 3),  -- Hermelín na bramborovém placku (Mléko)
    (21, 1),  -- Zeleninové rizoto (Lepek)
    (21, 3),  -- Zeleninové rizoto (Mléko)
    (22, 1),  -- Halušky s bryndzou (Lepek)
    (22, 3);  -- Halušky s bryndzou (Mléko)

-- Jídla z ryb
INSERT INTO food_allergens (food_id, allergen_id) VALUES
    (23, 4),  -- Rybí filé na másle (Celer)
    (23, 3),  -- Rybí filé na másle (Mléko)
    (24, 4),  -- Smažené rybí filé (Celer)
    (25, 4);  -- Přírodní rybí filé na grilu (Celer)
