# T-220-VLN2-Group19

Verklegt Námsekið 2 HR Vor 2022. T-220-VLN2. Hópur 19

## Google Drive

Link: [Verklegt námskeið 2 - Group 19](https://drive.google.com/drive/folders/1XHwv9RL6jLqjCWcG4RrQcmunrCCoBF6o?usp=sharing)

## Hópmeðlimir - [Hópur 19 í T-220-VLN2 á Canvas](https://reykjavik.instructure.com/groups/72331)

+ `HSJ` Helgi Steinarr Júlíusson - helgi21@ru.is
+ `IS` Ingólfur Sigurbjörnsson  - ingolfurs21@ru.is
+ `RAE` Ríkharður Aron Eiríksson - rikhardur21@ru.is

# About

## Extra requirements done (not mentioned in project description)
#### Listed in order of related part in project description
- logout
- notification tab / button in header navbar
- profile dropdown navigation (probably counted with navbar)
- birthday in profile / edit profile
- email in profile / edit profile
- joined date in profile
- saved card info in a section in profile if the profile is yours
- search based not only on name but also includes description
- search also has many additional filters:
  + results ascending or decending   
  + order by: newest/old, alphabetical name, lowest/highest price (newest/old and lowest/highest depending on ascending or decending direction)
  + filter by category, live auctions or old / finished auctions
- more paramaters when creating auction:
  + seller asking price
  + category
  + location (postal-city-province)
- item details shows the extra parameters added in create but also when an auction is finished (has an accepted offer) asking price is made "strike through" (line over it) and the winning offer price is show with the label "went for [WINNING PRICE] kr" and the "make offer" button is disabled and changed to "SOLD".
- at start of payment you can choose to fill out the form with existing saved card info if present
- at end of payment you can chooce to save the data you filled the form with to use later

- In offer page, filter between sent offer and received offers
- send counter offer
- user reviews
  + When buyer has paid he can review the seller
  + When seller has accepted an offer he can review the buyer
  + You can see all reviews made of user on their profile page
  + You can see other users average rating on their profile

## Misc Mentions
- password for user HelgiSt is GoodPassword123

## Disabled buttons (buttons with no functionality)
- if superuser: manage button in user nav
- report button in user nav


## First time setup
+ Create new venv in pycharm (called venv)
+ install dependencies

  + `pip install -r requirements.txt`

+ opening terminal in pycharm should automatically activate the venv but if not, you can activate it by doing the following:
##### If it's not happening automatically, this needs to be done every time the project is opened/new terminal opened

**_Windows_**
>venv\Scripts\activate

**_Windows bash terminal_**
>source venv/Scripts/activate

**_Linux or MacOS_**
>source venv/bin/activate
