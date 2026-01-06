import sqlite3

initial_categories = [
    # (Category ID, Category Name)
    (1, "Weapons and Artifacts"),
    (2, "Transport"),
    (3, "Technology"),
    (4, "Exotic Items"),
    (5, "Services (Disguised as Goods)")
]

initial_items = [
    # 1. Weapons and Artifacts
    ("Captain Hook's hook", 500, "hook_skin_01", 1, 0),
    ("Witcher swords", 2500, "blueprint_swords", 1, 0),
    ("Lightsabers", 4000, "kyber_crystal_pack", 1, 0),
    ("DL-44 Blaster", 1200, "han_shot_first", 1, 0),
    ("Phaser Type-2", 900, "stun_setting_only", 1, 0),
    ("Portal Gun", 9999, "cake_is_a_lie", 1, 0),
    ("Mjölnir", 50000, "odin_enchantment", 1, 0),
    ("One Ring", 100000, "my_precious", 1, 0),
    ("Darkslicer Black Sword", 4500, "darksaber_v1", 1, 0),

    # 2. Transport
    ("TIE Fighter", 150000, "sienar_fleet_sys", 2, 0),
    ("X-Wing", 160000, "red_five_standing_by", 2, 0),
    ("Millennium Falcon", 500000, "hyperdrive_broken", 2, 0),
    ("DeLorean DMC-12", 88000, "1.21_gigawatts", 2, 0),
    ("TARDIS", 1000000, "time_vortex_key", 2, 0),
    ("Batmobile", 300000, "wayne_tech_auth", 2, 0),

    # 3. Technology
    ("Exosuit", 8500, "mimic_defense_sys", 3, 0),
    ("Holographic communicator", 600, "obi_wan_msg", 3, 0),
    ("Tricorder", 1200, "med_scan_results", 3, 0),
    ("Cybernetic implants", 3000, "arasaka_mk1", 3, 0),
    ("Neural interface", 4500, "matrix_jack_in", 3, 0),
    ("Arc Reactor", 15000, "proof_tony_has_heart", 3, 0),
    ("Omnitrix", 7000, "hero_time_10", 3, 0),
    ("Anti-gravity boots", 2100, "zero_g_protocol", 3, 0),
    ("Star Trek Transporter", 6000, "beam_me_up", 3, 0),

    # 4. Exotic Items
    ("Pet Groot", 800, "i_am_groot", 4, 0),
    ("Astromech droid", 3500, "beep_boop_whistle", 4, 0),
    ("Xenomorph egg", 1000, "facehugger_inside", 4, 0),
    ("Covenant Plasma Sword", 1300, "halo_energy_key", 4, 0),
    ("Infinity Stones", 5000, "snap_fingers", 4, 0),
    ("Spice Melange", 2000, "must_flow", 4, 0),

    # 5. Services (Disguised as Goods)
    ("Fake Imperial passport", 600, "chain_code_clear", 5, 0),
    ("Hyperspace route map", 900, "nav_computer_data", 5, 0),
    ("Jedi Library Access", 1500, "jocasta_nu_permit", 5, 0),
    ("Bounty Hunter License", 2200, "this_is_the_way", 5, 0)
]


def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    create_tables(cursor)
    filling_tables(cursor, conn)
    conn.close()

def create_tables(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        ban INTEGER DEFAULT 0 CHECK(ban IN (0,1)),
        reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categories(
        id INTEGER PRIMARY KEY,
        cat_name TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS items(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT NOT NULL,
        price REAL NOT NULL,
        content TEXT NOT NULL,
        cat_id INTEGER NOT NULL,
        is_deleted INTEGER DEFAULT 0 CHECK(is_deleted IN (0,1)),
        FOREIGN KEY (cat_id) REFERENCES categories(id)
    )
    """)

def filling_tables(cursor, conn):
    cursor.execute("SELECT count(*) FROM categories")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("INSERT INTO categories (id, cat_name) VALUES (?, ?)", initial_categories)
        conn.commit()
    
    cursor.execute("SELECT count(*) FROM items")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("INSERT INTO items (item_name, price, content, cat_id, is_deleted) VALUES (?, ?, ?, ?, ?)", initial_items)
        conn.commit()
    print("Add testing categories and items")
