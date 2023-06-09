TRAIN_DATA = [
    # LOGIN examples
    ("Please log me into my account", {"entities": [(7, 13, "LOGIN"), (22, 29, "ACCOUNT")]}),
    ("Log me in", {"entities": [(0, 6, "LOGIN")]}),
    ("I'd like to login", {"entities": [(12, 17, "LOGIN")]}),
    ("Can you log me in?", {"entities": [(8, 14, "LOGIN")]}),
    ("I want to sign in", {"entities": [(10, 17, "LOGIN")]}),
    ("Sign me in, please", {"entities": [(0, 7, "LOGIN")]}),
    ("I'd like to sign in to my account", {"entities": [(12, 19, "LOGIN"), (26, 33, "ACCOUNT")]}),
    ("Please let me access my account", {"entities": [(14, 20, "LOGIN"), (24, 31, "ACCOUNT")]}),
    ("Authenticate me", {"entities": [(0, 12, "LOGIN")]}),
    ("Can I sign in?", {"entities": [(6, 13, "LOGIN")]}),
    ("I want to log into my account", {"entities": [(10, 18, "LOGIN"), (22, 29, "ACCOUNT")]}),
    ("Let me log in", {"entities": [(7, 13, "LOGIN")]}),
    ("I'd like to access my account", {"entities": [(12, 18, "LOGIN"), (22, 29, "ACCOUNT")]}),

    # OPEN JOURNAL examples
    ("Open me my fourth journal", {"entities": [(0, 4, "OPEN"), (18, 25, "JOURNAL")]}),
    ("Please open my journal called My Journal", {"entities": [(7, 11, "OPEN"), (15, 22, "JOURNAL")]}),
    ("Could you open my 1st journal", {"entities": [(10, 14, "OPEN"), (22, 29, "JOURNAL")]}),
    ("I'd like to open my second journal", {"entities": [(12, 16, "OPEN"), (27, 34, "JOURNAL")]}),
    ("Can you open the journal named New Journal?", {"entities": [(8, 12, "OPEN"), (17, 24, "JOURNAL")]}),
    ("I want to access my fifth journal", {"entities": [(10, 16, "OPEN"), (26, 33, "JOURNAL")]}),
    ("Show me my third journal", {"entities": [(0, 4, "OPEN"), (17, 24, "JOURNAL")]}),
    ("Display my first journal, please", {"entities": [(0, 7, "OPEN"), (17, 24, "JOURNAL")]}),
    ("Can I view my journal titled Crypto Journal?", {"entities": [(6, 10, "OPEN"), (14, 21, "JOURNAL")]}),
    ("Open my journal called Daily Entries", {"entities": [(0, 4, "OPEN"), (8, 15, "JOURNAL")]}),

    # OPEN ASSET examples
    ("Please enter Ethereum", {"entities": [(7, 12, "OPEN"), (13, 21, "ASSET_NAME")]}),
    ("Open Bitcoin", {"entities": [(0, 4, "OPEN"), (5, 12, "ASSET_NAME")]}),
    ("Show me Ripple", {"entities": [(0, 4, "OPEN"), (8, 14, "ASSET_NAME")]}),
    ("Display Polygon", {"entities": [(0, 7, "OPEN"), (8, 15, "ASSET_NAME")]}),
    ("View Cardano", {"entities": [(0, 4, "OPEN"), (5, 12, "ASSET_NAME")]}),
    ("Can you open Ethereum?", {"entities": [(8, 12, "OPEN"), (13, 21, "ASSET_NAME")]}),
    ("I'd like to access Bitcoin", {"entities": [(12, 18, "OPEN"), (19, 26, "ASSET_NAME")]}),
    ("Can I view Ripple?", {"entities": [(6, 10, "OPEN"), (11, 17, "ASSET_NAME")]}),
    ("Could you show me Polygon?", {"entities": [(10, 14, "OPEN"), (18, 25, "ASSET_NAME")]}),
    ("Please open XRP", {"entities": [(7, 11, "OPEN"), (12, 15, "ASSET_NAME")]}),
    ("Open ETH", {"entities": [(0, 4, "OPEN"), (5, 8, "ASSET_NAME")]}),
    ("Access BTC", {"entities": [(0, 6, "OPEN"), (7, 10, "ASSET_NAME")]}),
    ("I want to see ADA", {"entities": [(10, 13, "OPEN"), (14, 17, "ASSET_NAME")]}),
    ("Display MATIC", {"entities": [(0, 7, "OPEN"), (8, 13, "ASSET_NAME")]}),

    # TRADE examples
    ("Shorted 12 Bitcoin at $28,000 on 30 March 2023", {"entities": [(0, 7, "TRADE"), (8, 10, "AMOUNT"), (11, 18, "ASSET_NAME"), (22, 29, "PRICE"), (33, 46, "DATE")]}),
    ("Longed 1000 ADA for 0.38 dollar each", {"entities": [(0, 6, "TRADE"), (7, 11, "AMOUNT"), (12, 15, "ASSET_NAME"), (20, 24, "PRICE")]}),
    ("Bought 5 Ethereum for $1500 apiece", {"entities": [(0, 6, "TRADE"), (7, 8, "AMOUNT"), (9, 17, "ASSET_NAME"), (22, 27, "PRICE")]}),
    ("Sold 50 Ripple at $0.85 on April 20, 2023", {"entities": [(0, 4, "TRADE"), (5, 7, "AMOUNT"), (8, 14, "ASSET_NAME"), (18, 23, "PRICE"), (27, 41, "DATE")]}),
    ("I went long on 100 MATIC at $1.20", {"entities": [(7, 11, "TRADE"), (15, 18, "AMOUNT"), (19, 24, "ASSET_NAME"), (28, 33, "PRICE")]}),
    ("Went short on 20 Cardano for $0.9", {"entities": [(5, 10, "TRADE"), (14, 16, "AMOUNT"), (17, 24, "ASSET_NAME"), (29, 33, "PRICE")]}),
    ("Short 3 BTC at $45,000 on May 15, 2023", {"entities": [(0, 5, "TRADE"), (6, 7, "AMOUNT"), (8, 11, "ASSET_NAME"), (15, 22, "PRICE"), (26, 38, "DATE")]}),
    ("Long 15 XRP for $0.5 each", {"entities": [(0, 4, "TRADE"), (5, 7, "AMOUNT"), (8, 11, "ASSET_NAME"), (16, 20, "PRICE")]}),
]
