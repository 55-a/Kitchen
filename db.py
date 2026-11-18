import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def get_db_connection():
    """Получить подключение к PostgreSQL"""
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    return conn

def init_db():
    """Создать таблицы, если их нет"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id SERIAL PRIMARY KEY,
            name TEXT UNIQUE NOT NULL,
            telegram_id INTEGER UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stock (
            id SERIAL PRIMARY KEY,
            name TEXT UNIQUE NOT NULL,
            unit TEXT NOT NULL,
            quantity FLOAT DEFAULT 0,
            price_per_unit FLOAT DEFAULT 0,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recipes (
            id SERIAL PRIMARY KEY,
            name TEXT UNIQUE NOT NULL,
            base_yield INTEGER DEFAULT 100,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recipe_ingredients (
            id SERIAL PRIMARY KEY,
            recipe_id INTEGER REFERENCES recipes(id) ON DELETE CASCADE,
            product_id INTEGER REFERENCES stock(id) ON DELETE CASCADE,
            quantity FLOAT NOT NULL,
            unit TEXT NOT NULL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS client_deliveries (
            id SERIAL PRIMARY KEY,
            client_name TEXT NOT NULL,
            dish_name TEXT NOT NULL,
            portions INTEGER NOT NULL,
            amount FLOAT NOT NULL,
            cost FLOAT NOT NULL,
            date DATE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS payments (
            id SERIAL PRIMARY KEY,
            client_name TEXT NOT NULL,
            amount FLOAT NOT NULL,
            payment_type TEXT DEFAULT 'payment',
            date DATE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS purchases (
            id SERIAL PRIMARY KEY,
            product_name TEXT NOT NULL,
            quantity FLOAT NOT NULL,
            unit TEXT NOT NULL,
            total_price FLOAT NOT NULL,
            payment_method TEXT DEFAULT 'cash',
            date DATE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS batches (
            id SERIAL PRIMARY KEY,
            recipe_id INTEGER REFERENCES recipes(id),
            planned_yield INTEGER NOT NULL,
            actual_yield INTEGER NOT NULL,
            date DATE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    print("✅ База данных инициализирована")
