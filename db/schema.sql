-- Vytvoření tabulky admin_users
CREATE TABLE IF NOT EXISTS admin_users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL
);

-- Vytvoření tabulky daily_menu
CREATE TABLE daily_menu (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    soup VARCHAR(255) NOT NULL,
    meal_1 VARCHAR(255) NOT NULL,
    meal_1_price DECIMAL(5,2) NOT NULL,
    meal_2 VARCHAR(255) NOT NULL,
    meal_2_price DECIMAL(5,2) NOT NULL,
    meal_3 VARCHAR(255) NOT NULL,
    meal_3_price DECIMAL(5,2) NOT NULL
);

-- Vytvoření tabulky drink_menu
CREATE TABLE drinks_menu (
    id INT AUTO_INCREMENT PRIMARY KEY,
    drink_name VARCHAR(255) NOT NULL,
    drink_price DECIMAL(5,2) NOT NULL
);

-- Vytvoření tabulky categories (Kategorie nápojů)
CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE
);

-- Vytvoření tabulky drink_types (Typy nápojů)
CREATE TABLE drink_types (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE
);

-- Vytvoření tabulky drinks (Nápoje)
CREATE TABLE drinks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    drink_name VARCHAR(255) NOT NULL,
    category_id INT NOT NULL,
    drink_type_id INT NOT NULL,
    volume DECIMAL(4,2) NOT NULL,
    price DECIMAL(5,2) NOT NULL,
    description TEXT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE,
    FOREIGN KEY (drink_type_id) REFERENCES drink_types(id) ON DELETE CASCADE
)

