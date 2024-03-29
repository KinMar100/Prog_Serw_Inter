# FORUM API

## Zastosowanie:
System stworzony na potrzeby przedmiotu Projektowanie Serwisów Internetowych.
Zawiera kod napisany z pomocą frameworka Django i Django REST (język programowania Python)

## Opis systemu

Forum internetowe

## Aplikacja

### Users

Modele

_User_
- Id
- E-mail
- Name
- Password
- Date added
- Last login
- rank (FK -> Rank)

_Rank_
- id
- name


### Polls

Modele:

_Category_
- id
- Name

_Question_
- id
- Name
- Question text
- Category (FK -> Category)
- Pub date

_Choice_
- id
- Question (FK -> Question)
- Choice text
- Votes

### Posts

Modele:

_Post_
- id
- user (FK -> User)
- title
- description 
- add_date
- edit_date

_Comment_
- id
- user (FK -> User)
- post (FK -> Post)
- description
- add_date
- edit_date

_Reaction_

- id
- user (FK -> User)
- post (FK -> Post)
- type_of_reaction
- add_date


## Funkcjonalności
- dodawanie postów przez użytkowników (ok)
- zarządzanie postami: dodawanie, edycja, usuwanie (CRUD) (ok - admin)
- dodawanie reakcji do postów innych użytkowników (ok)
- formularze do ankiet (ok)
- moderacja komentarzy (ok)
- rangi użytkowników (ok)
- najnowsze wpisy (posty) (ok)
