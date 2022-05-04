INSERT INTO auction_province (name)
VALUES
    ('Capital Region'),
    ('Southern Peninsula'),
    ('Western Region'),
    ('Westfjords'),
    ('Northeastern Region'),
    ('Eastern Region'),
    ('Southern Region'),
    ('Northwestern Region');

INSERT INTO auction_location (postal_code, name, provID)
VALUES
    ('101', 'Reykjavik', 1),
    ('102', 'Reykjavik', 1),
    ('103', 'Reykjavik', 1),
    ('104', 'Reykjavik', 1),
    ('105', 'Reykjavik', 1),
    ('107', 'Reykjavik', 1),
    ('108', 'Reykjavik', 1),
    ('109', 'Reykjavik', 1),
    ('110', 'Reykjavik', 1),
    ('111', 'Reykjavik', 1),
    ('112', 'Reykjavik', 1),
    ('113', 'Reykjavik', 1),
    ('116', 'Reykjavik', 1),
    ('170', 'Seltjarnarnes', 1),
    ('190', 'Vogar', 2),
    ('200', 'Kópavogur', 1),
    ('201', 'Kópavogur', 1),
    ('203', 'Kópavogur', 1),
    ('210', 'Garðabær', 1),
    ('220', 'Hafnarfjörður', 1),
    ('221', 'Hafnarfjörður', 1),
    ('225', 'Garðabær', 1),
    ('230', 'Reykjanesbær', 2),
    ('233', 'Reykjanesbær', 2),
    ('240', 'Grindavík', 2),
    ('245', 'Sandgerði', 2),
    ('250', 'Garður', 2),
    ('260', 'Reykjanesbær', 2),
    ('262', 'Reykjanesbær', 2),
    ('270', 'Mosfellsbær', 1),
    ('300', 'Akranes', 3),
    ('310', 'Borgarnes', 3),
    ('340', 'Stykkishólmur', 3),
    ('350', 'Grundarfjörður', 3),
    ('355', 'Ólafsvík', 3),
    ('360', 'Hellissandur', 3),
    ('370', 'Búðardalur', 3),
    ('380', 'Reykhólahreppur', 4),
    ('400', 'Ísafjörður', 4),
    ('410', 'Hnífsdalur', 4),
    ('415', 'Bolungarvík', 4),
    ('420', 'Súðavík', 4),
    ('425', 'Flateyri', 4),
    ('430', 'Suðureyri', 4),
    ('450', 'Patreksfjörður', 4),
    ('460', 'Tálknafjörður', 4),
    ('465', 'Bíldudalur', 4),
    ('470', 'Thingeyri', 4),
    ('510', 'Hólmavík', 4),
    ('520', 'Drangsnes', 4),
    ('530', 'Hvammstangi', 8),
    ('540', 'Blönduós', 8),
    ('545', 'Skagaströnd', 8),
    ('550', 'Sauðárkrókur', 8),
    ('560', 'Varmahlíð', 8),
    ('565', 'Hofsós', 8),
    ('580', 'Siglufjörður', 5),
    ('600', 'Akureyri', 5),
    ('620', 'Dalvík', 5),
    ('625', 'Ólafsfjörður', 5),
    ('630', 'Hrísey', 5),
    ('640', 'Húsavík', 5),
    ('650', 'Þingeyjarsveit', 5),
    ('660', 'Mývatn', 5),
    ('670', 'Kópasker', 5),
    ('675', 'Raufarhöfn', 5),
    ('680', 'Þórshöfn', 5),
    ('685', 'Bakkafjörður', 5),
    ('690', 'Vopnafjörður', 6),
    ('700', 'Egilsstaðir', 6),
    ('710', 'Seyðisfjörður', 6),
    ('730', 'Reyðarfjörður', 6),
    ('735', 'Eskifjörður', 6),
    ('740', 'Neskaupstaður', 6),
    ('750', 'Fáskrúðsfjörður', 6),
    ('755', 'Stöðvarfjörður', 6),
    ('760', 'Breiðdalsvík', 6),
    ('765', 'Djúpivogur', 6),
    ('780', 'Höfn', 6),
    ('800', 'Selfoss', 7),
    ('810', 'Hveragerði', 7),
    ('815', 'Þorlákshöfn', 7),
    ('820', 'Eyrarbakki', 7),
    ('825', 'Stokkseyri', 7),
    ('840', 'Laugarvatn', 7),
    ('845', 'Flúðir', 7),
    ('850', 'Hella, Iceland', 7),
    ('860', 'Hvolsvöllur', 7),
    ('870', 'Vík í Mýrdal', 7),
    ('880', 'Kirkjubæjarklaustur', 7),
    ('900', 'Vestmannaeyjar', 7);

INSERT INTO auction_Category (name)
VALUES
    ('Automobiles'),
    ('Electronics'),
    ('Home'),
    ('Clothing');

INSERT INTO auction_Tag (name)
VALUES
    ('used'),
    ('new'),
    ('stolen');

INSERT INTO auction_auction (user_id, title, description, price, loc_ID, cat_ID)
VALUES
    (1, 'Item', 'Item for sale, legit stuff', 10000, 1, 3),
    (1, 'Another item', 'Item for sale', 100, 1, 3),
    (1, 'Third item', 'Cool item for sale found it behind MiniMarket', 400, 1, 4);

INSERT INTO auciton_auction_tag(auction_id, tag_id)
VALUES
    (1, 1),
    (1, 3),
    (2, 1),
    (3, 3);

INSERT INTO auction_offer(user_id, auction_id, price, status)
VALUES
    (2, 1, 500, 1),
    (2, 1, 9999, 2),
    (2, 1, 1000, 3),
    (2, 2, 50, 4),
    (2, 3, 400, 5);

INSERT INTO auction_review(reviewed_user_id, reviewer_user_id, description, rating, type)
VALUES
    (1, 2, 'Great', 5, 2),
    (2, 1, 'Good', 4, 1);

INSERT INTO auction_image(link, auction_id)
VALUES
    ('https://post.medicalnewstoday.com/wp-content/uploads/sites/3/2020/03/Silverback-gorilla-800x1200.jpg', 1),
    ('https://post.medicalnewstoday.com/wp-content/uploads/sites/3/2020/03/Silverback-gorilla-800x1200.jpg', 2),
    ('https://post.medicalnewstoday.com/wp-content/uploads/sites/3/2020/03/Silverback-gorilla-800x1200.jpg', 3);

