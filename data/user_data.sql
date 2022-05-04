INSERT INTO user_User (name, password, birthday, is_admin)
VALUES
    ('Ingó', 'ingo123', '1997-12-26', True),
    ('Helgi', 'helgi123', '01-01-2011', False);

INSERT INTO user_report(reporter_user_id, title, description, report_type)
VALUES
    (1, 'Site does not work', 'Just says TemplateSyntaxError at /', 2)
INSERT INTO user_report(reporter_user_id, reported_user_id, title, description, report_type)
VALUES
    (1, 2, 'Hacker', 'Hacked my computer', 1);

INSERT INTO user_cardinfo(user_id, first_name, last_name, card_number, cvc, expires, street, city, region, zip, country)
VALUES
    (2, 'Helgi', 'Júlíusson', 1234123412341234, 123, '2024-01-01','Laugavegur 1', 'Reykjavík', 'Capital Region','101', 'Iceland');

SELECT * FROM user_auction_tag