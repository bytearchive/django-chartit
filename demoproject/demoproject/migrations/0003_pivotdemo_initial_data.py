# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def initial_data(apps, schema_editor):
    data = [
        # authors first b/c of foreign keys
        {"fields": {"first_name": "Seth",
                    "last_name": "Godin"
                    },
         "model": "Author",
         "pk": 1
         },
        {"fields": {"first_name": "Guy",
                    "last_name": "Kawasaki"
                    },
         "model": "Author",
         "pk": 2
         },
        {"fields": {"first_name": "Geoffrey",
                    "last_name": "Colvin"
                    },
         "model": "Author",
         "pk": 3
         },
        {"fields": {"first_name": "Malcolm",
                    "last_name": "Gladwell"
                    },
         "model": "Author",
         "pk": 4
         },
        {"fields": {"first_name": "Daniel",
                    "last_name": "Pink"
                    },
         "model": "Author",
         "pk": 5
         },
        {"fields": {"first_name": "Dan",
                    "last_name": "Ariely"
                    },
         "model": "Author",
         "pk": 6
         },
        {"fields": {"first_name": "Charles",
                    "last_name": "Wheelan"
                    },
         "model": "Author",
         "pk": 7
         },
        {"fields": {"first_name": "Burton",
                    "last_name": "Malkiel"
                    },
         "model": "Author",
         "pk": 8
         },
        {"fields": {"first_name": "William",
                    "last_name": "Dunham"
                    },
         "model": "Author",
         "pk": 9
         },
        {"fields": {"first_name": "Stephen",
                    "last_name": "Covey"
                    },
         "model": "Author",
         "pk": 10
         },
        {"fields": {"first_name": "Patrick",
                    "last_name": "Lencioni"
                    },
         "model": "Author",
         "pk": 11
         },
        {"fields": {"first_name": "Richard",
                    "last_name": "Feynman"
                    },
         "model": "Author",
         "pk": 12
         },
        {"fields": {"first_name": "Steven",
                    "last_name": "Blank"
                    },
         "model": "Author",
         "pk": 13
         },
        {"fields": {"first_name": "Steven",
                    "last_name": "Levitt"
                    },
         "model": "Author",
         "pk": 14
         },
        {"fields": {"first_name": "Stephen",
                    "last_name": "Dubner"
                    },
         "model": "Author",
         "pk": 15
         },
        {"fields": {"first_name": "Raghuram",
                    "last_name": "Rajan"
                    },
         "model": "Author",
         "pk": 16
         },
        {"fields": {"first_name": "Keith",
                    "last_name": "Devlin"
                    },
         "model": "Author",
         "pk": 17
         },
        {"fields": {"first_name": "Edward",
                    "last_name": "Burger"
                    },
         "model": "Author",
         "pk": 18
         },
        {"fields": {"first_name": "Michael",
                    "last_name": "Starbird"
                    },
         "model": "Author",
         "pk": 19
         },
        {"fields": {"first_name": "John",
                    "last_name": "Paulos"
                    },
         "model": "Author",
         "pk": 20
         },
        {"fields": {"first_name": "Darrell",
                    "last_name": "Huff"
                    },
         "model": "Author",
         "pk": 21
         },
        {"fields": {"first_name": "Stephen",
                    "last_name": "Hawking"
                    },
         "model": "Author",
         "pk": 22
         },
        {"fields": {"first_name": "Leonard",
                    "last_name": "Mlodinow"
                    },
         "model": "Author",
         "pk": 23
         },
        {"fields": {"first_name": "Michio",
                    "last_name": "Okaku"
                    },
         "model": "Author",
         "pk": 24
         },
        {"fields": {"first_name": "Brian",
                    "last_name": "Greene"
                    },
         "model": "Author",
         "pk": 25
         },
        {"fields": {"first_name": "Irving",
                    "last_name": "Gells"
                    },
         "model": "Author",
         "pk": 27
         },
        {"fields": {"first_name": "Gregory",
                    "last_name": "Mankiw"
                    },
         "model": "Author",
         "pk": 28
         },

        # publisher second b/c of foreign keys
        {"fields": {"name": "Portfolio"},
         "model": "Publisher",
         "pk": 1
         },
        {"fields": {"name": "Back Bay"},
         "model": "Publisher",
         "pk": 2
         },
        {"fields": {"name": "Harper"},
         "model": "Publisher",
         "pk": 3
         },
        {"fields": {"name": "W. W. Norton"},
         "model": "Publisher",
         "pk": 4
         },
        {"fields": {"name": "South-Western College"},
         "model": "Publisher",
         "pk": 5
         },
        {"fields": {"name": "Princeton University"},
         "model": "Publisher",
         "pk": 6
         },
        {"fields": {"name": "Penguin"},
         "model": "Publisher",
         "pk": 7
         },
        {"fields": {"name": "Holt"},
         "model": "Publisher",
         "pk": 8
         },
        {"fields": {"name": "Anchor "},
         "model": "Publisher",
         "pk": 9
         },
        {"fields": {"name": "Hill and Wang"},
         "model": "Publisher",
         "pk": 10
         },
        {"fields": {"name": "Bantam"},
         "model": "Publisher",
         "pk": 11
         },
        {"fields": {"name": "Vintage"},
         "model": "Publisher",
         "pk": 12
         },

        # genre third b/c of foreign keys
        {"fields": {"name": "Mathematics"},
         "model": "Genre",
         "pk": 3
         },
        {"fields": {"name": "Economics"},
         "model": "Genre",
         "pk": 4
         },
        {"fields": {"name": "Business"},
         "model": "Genre",
         "pk": 1
         },
        {"fields": {"name": "Personal Development"},
         "model": "Genre",
         "pk": 2
         },
        {"fields": {"name": "Science"},
         "model": "Genre",
         "pk": 5
         },

        # city fourht b/c of foreign keys
        {"fields": {"city": "Los Angeles",
                    "state": "CA"
                    },
         "model": "City",
         "pk": 1
         },
        {"fields": {"city": "San Diego",
                    "state": "CA"
                    },
         "model": "City",
         "pk": 2
         },
        {"fields": {"city": "San Francisco",
                    "state": "CA"
                    },
         "model": "City",
         "pk": 3
         },
        {"fields": {"city": "New York",
                    "state": "NY"
                    },
         "model": "City",
         "pk": 4
         },
        {"fields": {"city": "Buffalo",
                    "state": "NY"
                    },
         "model": "City",
         "pk": 5
         },
        {"fields": {"city": "Rochester",
                    "state": "NY"
                    },
         "model": "City",
         "pk": 6
         },
        {"fields": {"city": "Boston",
                    "state": "MA"
                    },
         "model": "City",
         "pk": 7
         },
        {"fields": {"city": "Cambridge",
                    "state": "MA"
                    },
         "model": "City",
         "pk": 8
         },
        {"fields": {"city": "Austin",
                    "state": "TX"
                    },
         "model": "City",
         "pk": 9
         },
        {"fields": {"city": "Houston",
                    "state": "TX"
                    },
         "model": "City",
         "pk": 10
         },

        # book sixth b/c it has FKs on Publisher and Author
        # note: books order by dependency of the related field
        {"fields": {"authors": [],
                    "genre_id": 4,
                    "publisher_id": 3,
                    "rating": 3.8999999999999999,
                    "rating_count": 1869,
                    "related": [10],
                    "title": "Freakonomics"
                    },
            "model": "Book",
            "pk": 9
         },
        # TODO: book 9 and 10 have circular dependency
        {"fields": {"authors": [6],
                    "genre_id": 4,
                    "publisher_id": 3,
                    "rating": 4.2000000000000002,
                    "rating_count": 126,
                    "related": [9],
                    "title": "Predictably irrational"
                    },
            "model": "Book",
            "pk": 10
         },

        {"fields": {"authors": [24],
                    "genre_id": 5,
                    "publisher_id": 9,
                    "rating": 4.4000000000000004,
                    "rating_count": 222,
                    "related": [23, 21],
                    "title": "Hyperspace"
                    },
            "model": "Book",
            "pk": 24
         },
        {"fields": {"authors": [25],
                    "genre_id": 5,
                    "publisher_id": 12,
                    "rating": 4.4000000000000004,
                    "rating_count": 556,
                    "related": [24,
                                22,
                                21
                                ],
                    "title": "The Elegant Universe"
                    },
            "model": "Book",
            "pk": 23
         },
        {"fields": {"authors": [22],
                    "genre_id": 5,
                    "publisher_id": 11,
                    "rating": 4.2999999999999998,
                    "rating_count": 343,
                    "related": [23],
                    "title": "A Brief History of Time"
                    },
            "model": "Book",
            "pk": 22
         },
        {"fields": {"authors": [22,
                                23
                                ],
                    "genre_id": 5,
                    "publisher_id": 11,
                    "rating": 3.5,
                    "rating_count": 417,
                    "related": [24,
                                23
                                ],
                    "title": "The Grand Design"
                    },
            "model": "Book",
            "pk": 21
         },
        {"fields": {"authors": [12],
                    "genre_id": 5,
                    "publisher_id": 6,
                    "rating": 4.7999999999999998,
                    "rating_count": 37,
                    "related": [],
                    "title": "QED"
                    },
            "model": "Book",
            "pk": 20
         },
        {"fields": {"authors": [21,
                                27
                                ],
                    "genre_id": 3,
                    "publisher_id": 4,
                    "rating": 4.5999999999999996,
                    "rating_count": 117,
                    "related": [17],
                    "title": "How to lie with statistics"
                    },
            "model": "Book",
            "pk": 19
         },
        {"fields": {"authors": [20],
                    "genre_id": 3,
                    "publisher_id": 10,
                    "rating": 4.0,
                    "rating_count": 101,
                    "related": [16,
                                15
                                ],
                    "title": "Innumeracy"
                    },
            "model": "Book",
            "pk": 18
         },
        {"fields": {"authors": [20],
                    "genre_id": 3,
                    "publisher_id": 9,
                    "rating": 4.0999999999999996,
                    "rating_count": 34,
                    "related": [19,
                                16
                                ],
                    "title": "A Mathematician Reads the Newspaper"
                    },
            "model": "Book",
            "pk": 17
         },
        {"fields": {"authors": [18,
                                19
                                ],
                    "genre_id": 3,
                    "publisher_id": 4,
                    "rating": 4.7000000000000002,
                    "rating_count": 21,
                    "related": [18,
                                17
                                ],
                    "title": "Coincidences, Chaos, and All That Math Jazz"
                    },
            "model": "Book",
            "pk": 16
         },
        {"fields": {"authors": [17],
                    "genre_id": 3,
                    "publisher_id": 8,
                    "rating": 4.7000000000000002,
                    "rating_count": 26,
                    "related": [18,
                                14
                                ],
                    "title": "The Language of Mathematics"
                    },
            "model": "Book",
            "pk": 15
         },
        {"fields": {"authors": [9],
                    "genre_id": 3,
                    "publisher_id": 7,
                    "rating": 4.9000000000000004,
                    "rating_count": 87,
                    "related": [15],
                    "title": "Journey through Genius"
                    },
            "model": "Book",
            "pk": 14
         },
        {"fields": {"authors": [16],
                    "genre_id": 4,
                    "publisher_id": 6,
                    "rating": 4.5,
                    "rating_count": 55,
                    "related": [12],
                    "title": "Fault Lines"
                    },
            "model": "Book",
            "pk": 13
         },
        {"fields": {"authors": [28],
                    "genre_id": 4,
                    "publisher_id": 5,
                    "rating": 4.0999999999999996,
                    "rating_count": 90,
                    "related": [13,
                                11
                                ],
                    "title": "Principles of Economics"
                    },
            "model": "Book",
            "pk": 12
         },
        {"fields": {"authors": [7,
                                8
                                ],
                    "genre_id": 4,
                    "publisher_id": 4,
                    "rating": 4.5999999999999996,
                    "rating_count": 198,
                    "related": [12],
                    "title": "Naked Economics"
                    },
            "model": "Book",
            "pk": 11
         },

        {"fields": {"authors": [4],
                    "genre_id": 1,
                    "publisher_id": 2,
                    "rating": 3.7000000000000002,
                    "rating_count": 1239,
                    "related": [7],
                    "title": "Blink"
                    },
            "model": "Book",
            "pk": 8
         },
        {"fields": {"authors": [4],
                    "genre_id": 1,
                    "publisher_id": 2,
                    "rating": 4.0999999999999996,
                    "rating_count": 1169,
                    "related": [8],
                    "title": "Outliers"
                    },
            "model": "Book",
            "pk": 7
         },
        {"fields": {"authors": [3],
                    "genre_id": 1,
                    "publisher_id": 1,
                    "rating": 4.0,
                    "rating_count": 125,
                    "related": [],
                    "title": "Talent is overrated"
                    },
            "model": "Book",
            "pk": 6
         },
        {"fields": {"authors": [2],
                    "genre_id": 1,
                    "publisher_id": 1,
                    "rating": 4.5999999999999996,
                    "rating_count": 196,
                    "related": [5],
                    "title": "Enchantment"
                    },
            "model": "Book",
            "pk": 4
         },
        {"fields": {"authors": [2],
                    "genre_id": 1,
                    "publisher_id": 1,
                    "rating": 4.5,
                    "rating_count": 231,
                    "related": [4,
                                2
                                ],
                    "title": "The Art of the start"
                    },
            "model": "Book",
            "pk": 5
         },
        {"fields": {"authors": [1],
                    "genre_id": 1,
                    "publisher_id": 1,
                    "rating": 4.0,
                    "rating_count": 226,
                    "related": [],
                    "title": "Purple Cow"
                    },
            "model": "Book",
            "pk": 3
         },
        {"fields": {"authors": [1],
                    "genre_id": 1,
                    "publisher_id": 1,
                    "rating": 4.0999999999999996,
                    "rating_count": 217,
                    "related": [5,
                                1
                                ],
                    "title": "Tribes"
                    },
            "model": "Book",
            "pk": 2
         },
        {"fields": {"authors": [1],
                    "genre_id": 1,
                    "publisher_id": 1,
                    "rating": 4.4000000000000004,
                    "rating_count": 322,
                    "related": [2],
                    "title": "Linchpin"
                    },
            "model": "Book",
            "pk": 1
         },

        # bookstore seventh b/c it has FK on City
        {"fields": {"city_id": 1,
                    "name": "B&N"
                    },
         "model": "BookStore",
         "pk": 1
         },
        {"fields": {"city_id": 2,
                    "name": "B&N"
                    },
         "model": "BookStore",
         "pk": 2
         },
        {"fields": {"city_id": 3,
                    "name": "B&N"
                    },
         "model": "BookStore",
         "pk": 3
         },
        {"fields": {"city_id": 4,
                    "name": "B&N"
                    },
         "model": "BookStore",
         "pk": 4
         },
        {"fields": {"city_id": 5,
                    "name": "B&N"
                    },
         "model": "BookStore",
         "pk": 5
         },
        {"fields": {"city_id": 6,
                    "name": "B&N"
                    },
         "model": "BookStore",
         "pk": 6
         },
        {"fields": {"city_id": 7,
                    "name": "B&N"
                    },
         "model": "BookStore",
         "pk": 7
         },
        {"fields": {"city_id": 8,
                    "name": "B&N"
                    },
         "model": "BookStore",
         "pk": 8
         },
        {"fields": {"city_id": 9,
                    "name": "B&N"
                    },
         "model": "BookStore",
         "pk": 9
         },
        {"fields": {"city_id": 10,
                    "name": "B&N"
                    },
         "model": "BookStore",
         "pk": 10
         },
        {"fields": {"city_id": 1,
                    "name": "Borders"
                    },
         "model": "BookStore",
         "pk": 11
         },
        {"fields": {"city_id": 2,
                    "name": "Borders"
                    },
         "model": "BookStore",
         "pk": 12
         },
        {"fields": {"city_id": 3,
                    "name": "Borders"
                    },
         "model": "BookStore",
         "pk": 13
         },
        {"fields": {"city_id": 4,
                    "name": "Borders"
                    },
         "model": "BookStore",
         "pk": 14
         },
        {"fields": {"city_id": 5,
                    "name": "Borders"
                    },
         "model": "BookStore",
         "pk": 15
         },
        {"fields": {"city_id": 6,
                    "name": "Borders"
                    },
         "model": "BookStore",
         "pk": 16
         },
        {"fields": {"city_id": 7,
                    "name": "Borders"
                    },
         "model": "BookStore",
         "pk": 17
         },
        {"fields": {"city_id": 8,
                    "name": "Borders"
                    },
         "model": "BookStore",
         "pk": 18
         },
        {"fields": {"city_id": 9,
                    "name": "Borders"
                    },
         "model": "BookStore",
         "pk": 19
         },
        {"fields": {"city_id": 10,
                    "name": "Borders"
                    },
         "model": "BookStore",
         "pk": 20
         },
        {"fields": {"city_id": 1,
                    "name": "Books-a-Million"
                    },
         "model": "BookStore",
         "pk": 21
         },
        {"fields": {"city_id": 2,
                    "name": "Books-a-Million"
                    },
         "model": "BookStore",
         "pk": 22
         },
        {"fields": {"city_id": 3,
                    "name": "Books-a-Million"
                    },
         "model": "BookStore",
         "pk": 23
         },
        {"fields": {"city_id": 4,
                    "name": "Books-a-Million"
                    },
         "model": "BookStore",
         "pk": 24
         },
        {"fields": {"city_id": 5,
                    "name": "Books-a-Million"
                    },
         "model": "BookStore",
         "pk": 25
         },
        {"fields": {"city_id": 6,
                    "name": "Metropolis"
                    },
         "model": "BookStore",
         "pk": 26
         },
        {"fields": {"city_id": 7,
                    "name": "Metropolis"
                    },
         "model": "BookStore",
         "pk": 27
         },
        {"fields": {"city_id": 8,
                    "name": "Metropolis"
                    },
         "model": "BookStore",
         "pk": 28
         },
        {"fields": {"city_id": 9,
                    "name": "Metropolis"
                    },
         "model": "BookStore",
         "pk": 29
         },
        {"fields": {"city_id": 10,
                    "name": "Metropolis"
                    },
         "model": "BookStore",
         "pk": 30
         },
        {"fields": {"city_id": 1,
                    "name": "East West"
                    },
         "model": "BookStore",
         "pk": 31
         },
        {"fields": {"city_id": 2,
                    "name": "East West"
                    },
         "model": "BookStore",
         "pk": 32
         },
        {"fields": {"city_id": 3,
                    "name": "East West"
                    },
         "model": "BookStore",
         "pk": 33
         },
        {"fields": {"city_id": 9,
                    "name": "East West"
                    },
         "model": "BookStore",
         "pk": 34
         },
        {"fields": {"city_id": 10,
                    "name": "East West"
                    },
         "model": "BookStore",
         "pk": 35
         },
        {"fields": {"city_id": 7,
                    "name": "Rodneys"
                    },
         "model": "BookStore",
         "pk": 36
         },
        {"fields": {"city_id": 8,
                    "name": "Rodneys"
                    },
         "model": "BookStore",
         "pk": 37
         },
        {"fields": {"city_id": 9,
                    "name": "Rodneys"
                    },
         "model": "BookStore",
         "pk": 38
         },
        {"fields": {"city_id": 10,
                    "name": "Rodneys"
                    },
         "model": "BookStore",
         "pk": 39
         },

        # SalesHistory eight b/c it has FKs on Book and BookStore
        {"fields": {"book_id": 9,
                    "bookstore_id": 1,
                    "sale_date": "2010-07-01",
                    "price": "12.24",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 18,
                    "sale_date": "2010-07-01",
                    "price": "28.12",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 2
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 9,
                    "sale_date": "2010-07-01",
                    "price": "16.35",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 3
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 39,
                    "sale_date": "2010-07-01",
                    "price": "20.95",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 4
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 21,
                    "sale_date": "2010-07-01",
                    "price": "15.21",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 5
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 35,
                    "sale_date": "2010-07-01",
                    "price": "21.26",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 6
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 27,
                    "sale_date": "2010-07-02",
                    "price": "24.51",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 7
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 26,
                    "sale_date": "2010-07-02",
                    "price": "19.38",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 8
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 35,
                    "sale_date": "2010-07-02",
                    "price": "12.38",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 9
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 1,
                    "sale_date": "2010-07-02",
                    "price": "11.16",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 10
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 15,
                    "sale_date": "2010-07-02",
                    "price": "13.75",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 11
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 15,
                    "sale_date": "2010-07-02",
                    "price": "20.64",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 12
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 26,
                    "sale_date": "2010-07-02",
                    "price": "12.35",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 13
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 35,
                    "sale_date": "2010-07-03",
                    "price": "14.51",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 14
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 21,
                    "sale_date": "2010-07-03",
                    "price": "23.36",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 15
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 17,
                    "sale_date": "2010-07-03",
                    "price": "8.34",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 16
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 22,
                    "sale_date": "2010-07-04",
                    "price": "12.80",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 17
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 12,
                    "sale_date": "2010-07-04",
                    "price": "12.39",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 18
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 36,
                    "sale_date": "2010-07-04",
                    "price": "14.95",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 19
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 24,
                    "sale_date": "2010-07-04",
                    "price": "16.83",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 20
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 34,
                    "sale_date": "2010-07-04",
                    "price": "24.35",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 21
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 30,
                    "sale_date": "2010-07-05",
                    "price": "16.95",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 22
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 23,
                    "sale_date": "2010-07-05",
                    "price": "15.31",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 23
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 34,
                    "sale_date": "2010-07-05",
                    "price": "11.59",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 24
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 8,
                    "sale_date": "2010-07-05",
                    "price": "14.58",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 25
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 6,
                    "sale_date": "2010-07-05",
                    "price": "19.12",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 26
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 2,
                    "sale_date": "2010-07-05",
                    "price": "11.76",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 27
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 19,
                    "sale_date": "2010-07-06",
                    "price": "12.20",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 28
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 5,
                    "sale_date": "2010-07-06",
                    "price": "16.37",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 29
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 12,
                    "sale_date": "2010-07-06",
                    "price": "12.36",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 30
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 13,
                    "sale_date": "2010-07-06",
                    "price": "20.04",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 31
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 15,
                    "sale_date": "2010-07-06",
                    "price": "15.25",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 32
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 35,
                    "sale_date": "2010-07-06",
                    "price": "18.41",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 33
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 37,
                    "sale_date": "2010-07-06",
                    "price": "10.94",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 34
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 34,
                    "sale_date": "2010-07-07",
                    "price": "26.40",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 35
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 7,
                    "sale_date": "2010-07-07",
                    "price": "19.92",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 36
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 14,
                    "sale_date": "2010-07-07",
                    "price": "12.07",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 37
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 2,
                    "sale_date": "2010-07-08",
                    "price": "11.85",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 38
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 24,
                    "sale_date": "2010-07-08",
                    "price": "11.47",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 39
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 2,
                    "sale_date": "2010-07-08",
                    "price": "15.82",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 40
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 17,
                    "sale_date": "2010-07-08",
                    "price": "14.90",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 41
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 32,
                    "sale_date": "2010-07-09",
                    "price": "9.53",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 42
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 4,
                    "sale_date": "2010-07-09",
                    "price": "17.23",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 43
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 13,
                    "sale_date": "2010-07-09",
                    "price": "15.55",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 44
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 6,
                    "sale_date": "2010-07-10",
                    "price": "15.98",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 45
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 5,
                    "sale_date": "2010-07-10",
                    "price": "27.02",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 46
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 19,
                    "sale_date": "2010-07-10",
                    "price": "9.58",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 47
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 6,
                    "sale_date": "2010-07-10",
                    "price": "15.11",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 48
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 34,
                    "sale_date": "2010-07-10",
                    "price": "15.37",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 49
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 34,
                    "sale_date": "2010-07-10",
                    "price": "20.80",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 50
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 39,
                    "sale_date": "2010-07-11",
                    "price": "11.24",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 51
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 14,
                    "sale_date": "2010-07-11",
                    "price": "12.35",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 52
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 1,
                    "sale_date": "2010-07-11",
                    "price": "12.23",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 53
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 13,
                    "sale_date": "2010-07-11",
                    "price": "9.31",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 54
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 17,
                    "sale_date": "2010-07-11",
                    "price": "16.39",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 55
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 29,
                    "sale_date": "2010-07-11",
                    "price": "29.31",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 56
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 4,
                    "sale_date": "2010-07-11",
                    "price": "25.23",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 57
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 36,
                    "sale_date": "2010-07-12",
                    "price": "14.85",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 58
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 16,
                    "sale_date": "2010-07-12",
                    "price": "14.10",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 59
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 39,
                    "sale_date": "2010-07-13",
                    "price": "16.43",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 60
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 14,
                    "sale_date": "2010-07-13",
                    "price": "21.46",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 61
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 33,
                    "sale_date": "2010-07-13",
                    "price": "11.92",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 62
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 10,
                    "sale_date": "2010-07-13",
                    "price": "13.57",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 63
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 23,
                    "sale_date": "2010-07-14",
                    "price": "15.60",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 64
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 21,
                    "sale_date": "2010-07-15",
                    "price": "26.10",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 65
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 35,
                    "sale_date": "2010-07-15",
                    "price": "14.48",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 66
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 13,
                    "sale_date": "2010-07-15",
                    "price": "13.61",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 67
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 35,
                    "sale_date": "2010-07-15",
                    "price": "14.71",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 68
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 38,
                    "sale_date": "2010-07-15",
                    "price": "27.25",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 69
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 38,
                    "sale_date": "2010-07-15",
                    "price": "13.41",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 70
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 15,
                    "sale_date": "2010-07-15",
                    "price": "15.72",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 71
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 28,
                    "sale_date": "2010-07-15",
                    "price": "22.39",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 72
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 1,
                    "sale_date": "2010-07-16",
                    "price": "15.02",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 73
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 34,
                    "sale_date": "2010-07-16",
                    "price": "10.21",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 74
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 23,
                    "sale_date": "2010-07-16",
                    "price": "11.21",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 75
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 38,
                    "sale_date": "2010-07-16",
                    "price": "12.74",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 76
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 17,
                    "sale_date": "2010-07-16",
                    "price": "18.68",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 77
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 8,
                    "sale_date": "2010-07-17",
                    "price": "19.94",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 78
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 15,
                    "sale_date": "2010-07-17",
                    "price": "14.96",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 79
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 18,
                    "sale_date": "2010-07-17",
                    "price": "14.70",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 80
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 23,
                    "sale_date": "2010-07-17",
                    "price": "18.51",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 81
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 23,
                    "sale_date": "2010-07-17",
                    "price": "9.14",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 82
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 5,
                    "sale_date": "2010-07-17",
                    "price": "22.02",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 83
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 18,
                    "sale_date": "2010-07-18",
                    "price": "24.37",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 84
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 9,
                    "sale_date": "2010-07-18",
                    "price": "17.26",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 85
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 39,
                    "sale_date": "2010-07-18",
                    "price": "16.64",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 86
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 14,
                    "sale_date": "2010-07-18",
                    "price": "14.09",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 87
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 12,
                    "sale_date": "2010-07-18",
                    "price": "26.63",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 88
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 35,
                    "sale_date": "2010-07-18",
                    "price": "14.92",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 89
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 4,
                    "sale_date": "2010-07-18",
                    "price": "12.47",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 90
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 5,
                    "sale_date": "2010-07-19",
                    "price": "16.53",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 91
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 27,
                    "sale_date": "2010-07-19",
                    "price": "26.53",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 92
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 22,
                    "sale_date": "2010-07-19",
                    "price": "24.92",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 93
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 20,
                    "sale_date": "2010-07-19",
                    "price": "20.98",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 94
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 26,
                    "sale_date": "2010-07-19",
                    "price": "13.18",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 95
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 32,
                    "sale_date": "2010-07-19",
                    "price": "24.73",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 96
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 30,
                    "sale_date": "2010-07-19",
                    "price": "16.67",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 97
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 33,
                    "sale_date": "2010-07-19",
                    "price": "12.02",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 98
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 14,
                    "sale_date": "2010-07-20",
                    "price": "14.02",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 99
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 25,
                    "sale_date": "2010-07-20",
                    "price": "21.96",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 100
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 6,
                    "sale_date": "2010-07-20",
                    "price": "16.56",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 101
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 9,
                    "sale_date": "2010-07-20",
                    "price": "27.34",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 102
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 19,
                    "sale_date": "2010-07-20",
                    "price": "12.64",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 103
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 4,
                    "sale_date": "2010-07-20",
                    "price": "17.37",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 104
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 21,
                    "sale_date": "2010-07-20",
                    "price": "15.64",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 105
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 20,
                    "sale_date": "2010-07-20",
                    "price": "19.67",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 106
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 20,
                    "sale_date": "2010-07-20",
                    "price": "15.08",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 107
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 25,
                    "sale_date": "2010-07-21",
                    "price": "19.32",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 108
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 35,
                    "sale_date": "2010-07-21",
                    "price": "14.85",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 109
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 36,
                    "sale_date": "2010-07-21",
                    "price": "13.90",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 110
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 22,
                    "sale_date": "2010-07-21",
                    "price": "16.19",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 111
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 12,
                    "sale_date": "2010-07-22",
                    "price": "15.10",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 112
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 6,
                    "sale_date": "2010-07-22",
                    "price": "13.64",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 113
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 28,
                    "sale_date": "2010-07-22",
                    "price": "14.60",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 114
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 30,
                    "sale_date": "2010-07-22",
                    "price": "12.44",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 115
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 35,
                    "sale_date": "2010-07-23",
                    "price": "15.95",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 116
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 11,
                    "sale_date": "2010-07-23",
                    "price": "12.21",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 117
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 28,
                    "sale_date": "2010-07-23",
                    "price": "12.38",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 118
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 23,
                    "sale_date": "2010-07-23",
                    "price": "11.47",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 119
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 19,
                    "sale_date": "2010-07-23",
                    "price": "16.19",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 120
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 4,
                    "sale_date": "2010-07-23",
                    "price": "13.50",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 121
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 2,
                    "sale_date": "2010-07-23",
                    "price": "11.45",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 122
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 38,
                    "sale_date": "2010-07-24",
                    "price": "11.90",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 123
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 17,
                    "sale_date": "2010-07-24",
                    "price": "11.22",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 124
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 27,
                    "sale_date": "2010-07-24",
                    "price": "21.30",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 125
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 28,
                    "sale_date": "2010-07-24",
                    "price": "24.50",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 126
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 15,
                    "sale_date": "2010-07-24",
                    "price": "15.14",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 127
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 24,
                    "sale_date": "2010-07-25",
                    "price": "14.93",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 128
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 8,
                    "sale_date": "2010-07-26",
                    "price": "9.15",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 129
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 36,
                    "sale_date": "2010-07-26",
                    "price": "16.05",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 130
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 15,
                    "sale_date": "2010-07-26",
                    "price": "12.63",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 131
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 23,
                    "sale_date": "2010-07-26",
                    "price": "9.20",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 132
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 7,
                    "sale_date": "2010-07-27",
                    "price": "9.13",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 133
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 38,
                    "sale_date": "2010-07-27",
                    "price": "13.34",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 134
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 17,
                    "sale_date": "2010-07-27",
                    "price": "21.09",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 135
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 23,
                    "sale_date": "2010-07-27",
                    "price": "14.82",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 136
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 23,
                    "sale_date": "2010-07-27",
                    "price": "10.68",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 137
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 35,
                    "sale_date": "2010-07-27",
                    "price": "15.64",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 138
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 38,
                    "sale_date": "2010-07-27",
                    "price": "13.51",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 139
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 23,
                    "sale_date": "2010-07-27",
                    "price": "11.67",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 140
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 33,
                    "sale_date": "2010-07-28",
                    "price": "20.74",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 141
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 8,
                    "sale_date": "2010-07-28",
                    "price": "11.86",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 142
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 15,
                    "sale_date": "2010-07-28",
                    "price": "16.21",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 143
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 33,
                    "sale_date": "2010-07-28",
                    "price": "14.06",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 144
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 2,
                    "sale_date": "2010-07-28",
                    "price": "17.81",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 145
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 39,
                    "sale_date": "2010-07-28",
                    "price": "20.57",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 146
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 14,
                    "sale_date": "2010-07-28",
                    "price": "15.92",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 147
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 22,
                    "sale_date": "2010-07-29",
                    "price": "15.65",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 148
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 37,
                    "sale_date": "2010-07-29",
                    "price": "28.10",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 149
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 18,
                    "sale_date": "2010-07-29",
                    "price": "12.07",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 150
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 9,
                    "sale_date": "2010-07-29",
                    "price": "19.55",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 151
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 25,
                    "sale_date": "2010-07-29",
                    "price": "12.49",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 152
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 7,
                    "sale_date": "2010-07-30",
                    "price": "12.57",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 153
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 9,
                    "sale_date": "2010-07-30",
                    "price": "14.23",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 154
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 39,
                    "sale_date": "2010-07-30",
                    "price": "14.57",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 155
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 14,
                    "sale_date": "2010-07-30",
                    "price": "17.62",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 156
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 11,
                    "sale_date": "2010-07-30",
                    "price": "15.39",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 157
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 1,
                    "sale_date": "2010-07-30",
                    "price": "26.06",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 158
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 28,
                    "sale_date": "2010-07-30",
                    "price": "18.25",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 159
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 31,
                    "sale_date": "2010-07-30",
                    "price": "13.37",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 160
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 12,
                    "sale_date": "2010-07-31",
                    "price": "14.44",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 161
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 17,
                    "sale_date": "2010-07-31",
                    "price": "14.77",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 162
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 16,
                    "sale_date": "2010-07-31",
                    "price": "15.82",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 163
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 39,
                    "sale_date": "2010-07-31",
                    "price": "15.75",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 164
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 11,
                    "sale_date": "2010-07-31",
                    "price": "11.04",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 165
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 30,
                    "sale_date": "2010-07-31",
                    "price": "13.43",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 166
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 1,
                    "sale_date": "2010-07-31",
                    "price": "12.68",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 167
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 25,
                    "sale_date": "2010-07-31",
                    "price": "15.31",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 168
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 5,
                    "sale_date": "2010-07-31",
                    "price": "12.15",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 169
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 9,
                    "sale_date": "2010-08-01",
                    "price": "12.88",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 170
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 11,
                    "sale_date": "2010-08-01",
                    "price": "14.43",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 171
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 19,
                    "sale_date": "2010-08-01",
                    "price": "17.41",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 172
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 11,
                    "sale_date": "2010-08-01",
                    "price": "17.00",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 173
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 27,
                    "sale_date": "2010-08-01",
                    "price": "13.55",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 174
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 18,
                    "sale_date": "2010-08-01",
                    "price": "13.42",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 175
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 1,
                    "sale_date": "2010-08-01",
                    "price": "12.15",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 176
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 5,
                    "sale_date": "2010-08-02",
                    "price": "19.82",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 177
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 35,
                    "sale_date": "2010-08-02",
                    "price": "12.91",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 178
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 18,
                    "sale_date": "2010-08-02",
                    "price": "11.05",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 179
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 34,
                    "sale_date": "2010-08-02",
                    "price": "16.90",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 180
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 29,
                    "sale_date": "2010-08-02",
                    "price": "12.02",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 181
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 10,
                    "sale_date": "2010-08-03",
                    "price": "28.18",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 182
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 30,
                    "sale_date": "2010-08-03",
                    "price": "17.41",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 183
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 38,
                    "sale_date": "2010-08-03",
                    "price": "18.98",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 184
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 31,
                    "sale_date": "2010-08-04",
                    "price": "10.65",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 185
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 34,
                    "sale_date": "2010-08-04",
                    "price": "12.28",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 186
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 9,
                    "sale_date": "2010-08-04",
                    "price": "16.52",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 187
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 15,
                    "sale_date": "2010-08-05",
                    "price": "20.15",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 188
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 21,
                    "sale_date": "2010-08-05",
                    "price": "15.69",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 189
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 8,
                    "sale_date": "2010-08-05",
                    "price": "12.27",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 190
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 27,
                    "sale_date": "2010-08-05",
                    "price": "16.83",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 191
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 29,
                    "sale_date": "2010-08-06",
                    "price": "26.11",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 192
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 25,
                    "sale_date": "2010-08-06",
                    "price": "21.24",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 193
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 27,
                    "sale_date": "2010-08-06",
                    "price": "12.52",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 194
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 5,
                    "sale_date": "2010-08-06",
                    "price": "22.82",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 195
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 13,
                    "sale_date": "2010-08-06",
                    "price": "17.74",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 196
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 34,
                    "sale_date": "2010-08-07",
                    "price": "9.90",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 197
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 20,
                    "sale_date": "2010-08-07",
                    "price": "14.48",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 198
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 26,
                    "sale_date": "2010-08-07",
                    "price": "20.09",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 199
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 31,
                    "sale_date": "2010-08-07",
                    "price": "13.25",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 200
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 28,
                    "sale_date": "2010-08-07",
                    "price": "15.56",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 201
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 10,
                    "sale_date": "2010-08-07",
                    "price": "13.87",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 202
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 21,
                    "sale_date": "2010-08-08",
                    "price": "13.16",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 203
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 4,
                    "sale_date": "2010-08-08",
                    "price": "14.62",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 204
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 31,
                    "sale_date": "2010-08-08",
                    "price": "16.67",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 205
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 24,
                    "sale_date": "2010-08-08",
                    "price": "24.50",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 206
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 20,
                    "sale_date": "2010-08-08",
                    "price": "12.70",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 207
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 28,
                    "sale_date": "2010-08-08",
                    "price": "14.43",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 208
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 32,
                    "sale_date": "2010-08-08",
                    "price": "18.44",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 209
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 11,
                    "sale_date": "2010-08-08",
                    "price": "10.94",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 210
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 20,
                    "sale_date": "2010-08-09",
                    "price": "17.97",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 211
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 31,
                    "sale_date": "2010-08-09",
                    "price": "18.71",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 212
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 29,
                    "sale_date": "2010-08-09",
                    "price": "15.29",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 213
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 3,
                    "sale_date": "2010-08-09",
                    "price": "12.22",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 214
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 18,
                    "sale_date": "2010-08-09",
                    "price": "16.17",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 215
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 23,
                    "sale_date": "2010-08-09",
                    "price": "10.38",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 216
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 13,
                    "sale_date": "2010-08-09",
                    "price": "13.96",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 217
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 29,
                    "sale_date": "2010-08-09",
                    "price": "16.28",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 218
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 20,
                    "sale_date": "2010-08-10",
                    "price": "10.61",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 219
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 32,
                    "sale_date": "2010-08-10",
                    "price": "12.03",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 220
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 10,
                    "sale_date": "2010-08-10",
                    "price": "17.88",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 221
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 19,
                    "sale_date": "2010-08-11",
                    "price": "13.50",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 222
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 39,
                    "sale_date": "2010-08-11",
                    "price": "13.27",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 223
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 6,
                    "sale_date": "2010-08-11",
                    "price": "10.98",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 224
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 9,
                    "sale_date": "2010-08-11",
                    "price": "15.11",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 225
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 39,
                    "sale_date": "2010-08-11",
                    "price": "13.42",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 226
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 33,
                    "sale_date": "2010-08-11",
                    "price": "15.87",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 227
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 6,
                    "sale_date": "2010-08-11",
                    "price": "26.53",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 228
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 7,
                    "sale_date": "2010-08-12",
                    "price": "14.86",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 229
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 1,
                    "sale_date": "2010-08-12",
                    "price": "26.59",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 230
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 4,
                    "sale_date": "2010-08-12",
                    "price": "14.17",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 231
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 29,
                    "sale_date": "2010-08-12",
                    "price": "11.80",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 232
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 14,
                    "sale_date": "2010-08-12",
                    "price": "22.86",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 233
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 36,
                    "sale_date": "2010-08-12",
                    "price": "16.08",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 234
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 12,
                    "sale_date": "2010-08-12",
                    "price": "12.22",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 235
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 22,
                    "sale_date": "2010-08-13",
                    "price": "14.15",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 236
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 15,
                    "sale_date": "2010-08-13",
                    "price": "10.98",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 237
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 9,
                    "sale_date": "2010-08-13",
                    "price": "15.41",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 238
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 24,
                    "sale_date": "2010-08-13",
                    "price": "16.91",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 239
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 18,
                    "sale_date": "2010-08-13",
                    "price": "10.62",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 240
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 7,
                    "sale_date": "2010-08-13",
                    "price": "12.53",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 241
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 10,
                    "sale_date": "2010-08-13",
                    "price": "21.75",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 242
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 7,
                    "sale_date": "2010-08-13",
                    "price": "12.95",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 243
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 18,
                    "sale_date": "2010-08-13",
                    "price": "8.42",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 244
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 32,
                    "sale_date": "2010-08-13",
                    "price": "26.66",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 245
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 24,
                    "sale_date": "2010-08-13",
                    "price": "26.24",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 246
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 5,
                    "sale_date": "2010-08-14",
                    "price": "13.76",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 247
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 34,
                    "sale_date": "2010-08-14",
                    "price": "24.18",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 248
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 15,
                    "sale_date": "2010-08-14",
                    "price": "12.02",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 249
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 34,
                    "sale_date": "2010-08-14",
                    "price": "23.47",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 250
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 16,
                    "sale_date": "2010-08-14",
                    "price": "13.13",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 251
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 32,
                    "sale_date": "2010-08-14",
                    "price": "12.81",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 252
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 2,
                    "sale_date": "2010-08-15",
                    "price": "13.79",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 253
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 5,
                    "sale_date": "2010-08-15",
                    "price": "15.60",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 254
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 19,
                    "sale_date": "2010-08-15",
                    "price": "11.91",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 255
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 39,
                    "sale_date": "2010-08-16",
                    "price": "19.08",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 256
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 17,
                    "sale_date": "2010-08-16",
                    "price": "18.53",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 257
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 30,
                    "sale_date": "2010-08-16",
                    "price": "17.22",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 258
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 6,
                    "sale_date": "2010-08-16",
                    "price": "13.22",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 259
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 2,
                    "sale_date": "2010-08-16",
                    "price": "13.52",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 260
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 30,
                    "sale_date": "2010-08-16",
                    "price": "26.17",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 261
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 4,
                    "sale_date": "2010-08-16",
                    "price": "13.09",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 262
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 9,
                    "sale_date": "2010-08-17",
                    "price": "26.52",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 263
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 1,
                    "sale_date": "2010-08-17",
                    "price": "29.79",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 264
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 6,
                    "sale_date": "2010-08-17",
                    "price": "15.76",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 265
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 33,
                    "sale_date": "2010-08-17",
                    "price": "13.16",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 266
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 4,
                    "sale_date": "2010-08-17",
                    "price": "17.25",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 267
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 14,
                    "sale_date": "2010-08-18",
                    "price": "10.63",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 268
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 35,
                    "sale_date": "2010-08-18",
                    "price": "15.69",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 269
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 19,
                    "sale_date": "2010-08-18",
                    "price": "21.38",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 270
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 18,
                    "sale_date": "2010-08-18",
                    "price": "20.44",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 271
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 22,
                    "sale_date": "2010-08-18",
                    "price": "18.70",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 272
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 19,
                    "sale_date": "2010-08-18",
                    "price": "16.80",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 273
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 25,
                    "sale_date": "2010-08-18",
                    "price": "13.45",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 274
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 9,
                    "sale_date": "2010-08-19",
                    "price": "11.39",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 275
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 26,
                    "sale_date": "2010-08-19",
                    "price": "11.82",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 276
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 5,
                    "sale_date": "2010-08-19",
                    "price": "13.94",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 277
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 28,
                    "sale_date": "2010-08-19",
                    "price": "13.37",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 278
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 20,
                    "sale_date": "2010-08-19",
                    "price": "20.07",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 279
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 20,
                    "sale_date": "2010-08-19",
                    "price": "12.43",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 280
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 15,
                    "sale_date": "2010-08-19",
                    "price": "15.91",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 281
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 30,
                    "sale_date": "2010-08-19",
                    "price": "26.19",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 282
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 39,
                    "sale_date": "2010-08-20",
                    "price": "23.22",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 283
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 38,
                    "sale_date": "2010-08-21",
                    "price": "14.14",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 284
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 17,
                    "sale_date": "2010-08-21",
                    "price": "10.40",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 285
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 33,
                    "sale_date": "2010-08-21",
                    "price": "17.44",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 286
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 6,
                    "sale_date": "2010-08-21",
                    "price": "15.18",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 287
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 2,
                    "sale_date": "2010-08-21",
                    "price": "13.35",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 288
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 23,
                    "sale_date": "2010-08-21",
                    "price": "14.40",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 289
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 20,
                    "sale_date": "2010-08-21",
                    "price": "12.29",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 290
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 32,
                    "sale_date": "2010-08-22",
                    "price": "13.71",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 291
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 30,
                    "sale_date": "2010-08-22",
                    "price": "13.05",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 292
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 17,
                    "sale_date": "2010-08-22",
                    "price": "12.59",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 293
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 2,
                    "sale_date": "2010-08-22",
                    "price": "14.90",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 294
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 34,
                    "sale_date": "2010-08-22",
                    "price": "28.20",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 295
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 23,
                    "sale_date": "2010-08-22",
                    "price": "18.77",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 296
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 19,
                    "sale_date": "2010-08-22",
                    "price": "13.76",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 297
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 19,
                    "sale_date": "2010-08-22",
                    "price": "17.90",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 298
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 15,
                    "sale_date": "2010-08-22",
                    "price": "11.69",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 299
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 25,
                    "sale_date": "2010-08-23",
                    "price": "11.71",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 300
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 31,
                    "sale_date": "2010-08-23",
                    "price": "27.80",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 301
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 22,
                    "sale_date": "2010-08-23",
                    "price": "15.14",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 302
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 33,
                    "sale_date": "2010-08-23",
                    "price": "19.75",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 303
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 18,
                    "sale_date": "2010-08-23",
                    "price": "27.03",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 304
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 11,
                    "sale_date": "2010-08-23",
                    "price": "20.59",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 305
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 33,
                    "sale_date": "2010-08-23",
                    "price": "23.44",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 306
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 17,
                    "sale_date": "2010-08-23",
                    "price": "23.91",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 307
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 24,
                    "sale_date": "2010-08-24",
                    "price": "19.45",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 308
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 16,
                    "sale_date": "2010-08-24",
                    "price": "11.27",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 309
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 32,
                    "sale_date": "2010-08-24",
                    "price": "13.45",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 310
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 20,
                    "sale_date": "2010-08-24",
                    "price": "13.81",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 311
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 11,
                    "sale_date": "2010-08-24",
                    "price": "22.45",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 312
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 33,
                    "sale_date": "2010-08-24",
                    "price": "13.68",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 313
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 8,
                    "sale_date": "2010-08-24",
                    "price": "14.96",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 314
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 13,
                    "sale_date": "2010-08-25",
                    "price": "12.40",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 315
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 19,
                    "sale_date": "2010-08-25",
                    "price": "12.68",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 316
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 30,
                    "sale_date": "2010-08-25",
                    "price": "16.68",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 317
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 7,
                    "sale_date": "2010-08-26",
                    "price": "12.58",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 318
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 24,
                    "sale_date": "2010-08-26",
                    "price": "15.38",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 319
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 14,
                    "sale_date": "2010-08-26",
                    "price": "10.72",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 320
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 26,
                    "sale_date": "2010-08-26",
                    "price": "9.59",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 321
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 6,
                    "sale_date": "2010-08-26",
                    "price": "15.64",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 322
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 18,
                    "sale_date": "2010-08-26",
                    "price": "13.09",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 323
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 39,
                    "sale_date": "2010-08-26",
                    "price": "13.65",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 324
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 38,
                    "sale_date": "2010-08-27",
                    "price": "27.65",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 325
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 2,
                    "sale_date": "2010-08-27",
                    "price": "16.49",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 326
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 19,
                    "sale_date": "2010-08-27",
                    "price": "15.64",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 327
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 19,
                    "sale_date": "2010-08-28",
                    "price": "14.42",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 328
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 17,
                    "sale_date": "2010-08-28",
                    "price": "12.58",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 329
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 20,
                    "sale_date": "2010-08-28",
                    "price": "18.44",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 330
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 8,
                    "sale_date": "2010-08-28",
                    "price": "16.28",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 331
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 36,
                    "sale_date": "2010-08-28",
                    "price": "11.94",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 332
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 8,
                    "sale_date": "2010-08-28",
                    "price": "16.90",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 333
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 31,
                    "sale_date": "2010-08-28",
                    "price": "14.15",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 334
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 17,
                    "sale_date": "2010-08-29",
                    "price": "14.71",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 335
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 9,
                    "sale_date": "2010-08-29",
                    "price": "26.65",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 336
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 24,
                    "sale_date": "2010-08-29",
                    "price": "22.21",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 337
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 35,
                    "sale_date": "2010-08-29",
                    "price": "10.46",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 338
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 32,
                    "sale_date": "2010-08-30",
                    "price": "19.34",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 339
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 19,
                    "sale_date": "2010-08-30",
                    "price": "14.33",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 340
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 29,
                    "sale_date": "2010-08-30",
                    "price": "29.73",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 341
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 32,
                    "sale_date": "2010-08-30",
                    "price": "16.79",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 342
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 2,
                    "sale_date": "2010-08-30",
                    "price": "13.62",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 343
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 10,
                    "sale_date": "2010-08-30",
                    "price": "14.71",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 344
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 1,
                    "sale_date": "2010-08-30",
                    "price": "12.22",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 345
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 9,
                    "sale_date": "2010-08-31",
                    "price": "23.92",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 346
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 11,
                    "sale_date": "2010-08-31",
                    "price": "16.13",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 347
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 20,
                    "sale_date": "2010-08-31",
                    "price": "13.41",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 348
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 29,
                    "sale_date": "2010-08-31",
                    "price": "9.41",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 349
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 12,
                    "sale_date": "2010-08-31",
                    "price": "20.91",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 350
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 30,
                    "sale_date": "2010-08-31",
                    "price": "19.17",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 351
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 39,
                    "sale_date": "2010-08-31",
                    "price": "10.44",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 352
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 6,
                    "sale_date": "2010-09-01",
                    "price": "12.45",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 353
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 31,
                    "sale_date": "2010-09-01",
                    "price": "17.20",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 354
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 8,
                    "sale_date": "2010-09-01",
                    "price": "15.06",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 355
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 34,
                    "sale_date": "2010-09-01",
                    "price": "11.74",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 356
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 13,
                    "sale_date": "2010-09-01",
                    "price": "30.81",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 357
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 14,
                    "sale_date": "2010-09-01",
                    "price": "10.23",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 358
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 33,
                    "sale_date": "2010-09-02",
                    "price": "16.55",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 359
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 3,
                    "sale_date": "2010-09-02",
                    "price": "12.43",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 360
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 29,
                    "sale_date": "2010-09-02",
                    "price": "12.38",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 361
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 3,
                    "sale_date": "2010-09-02",
                    "price": "17.98",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 362
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 14,
                    "sale_date": "2010-09-02",
                    "price": "13.85",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 363
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 6,
                    "sale_date": "2010-09-02",
                    "price": "10.20",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 364
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 31,
                    "sale_date": "2010-09-03",
                    "price": "26.38",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 365
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 25,
                    "sale_date": "2010-09-03",
                    "price": "24.94",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 366
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 1,
                    "sale_date": "2010-09-03",
                    "price": "19.33",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 367
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 26,
                    "sale_date": "2010-09-03",
                    "price": "22.53",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 368
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 1,
                    "sale_date": "2010-09-03",
                    "price": "26.00",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 369
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 26,
                    "sale_date": "2010-09-03",
                    "price": "14.64",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 370
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 17,
                    "sale_date": "2010-09-03",
                    "price": "20.21",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 371
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 18,
                    "sale_date": "2010-09-03",
                    "price": "25.88",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 372
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 35,
                    "sale_date": "2010-09-03",
                    "price": "13.09",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 373
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 31,
                    "sale_date": "2010-09-04",
                    "price": "16.86",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 374
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 1,
                    "sale_date": "2010-09-04",
                    "price": "30.88",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 375
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 20,
                    "sale_date": "2010-09-04",
                    "price": "12.97",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 376
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 24,
                    "sale_date": "2010-09-04",
                    "price": "13.00",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 377
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 30,
                    "sale_date": "2010-09-04",
                    "price": "28.14",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 378
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 15,
                    "sale_date": "2010-09-04",
                    "price": "17.05",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 379
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 13,
                    "sale_date": "2010-09-04",
                    "price": "12.65",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 380
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 5,
                    "sale_date": "2010-09-04",
                    "price": "15.28",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 381
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 13,
                    "sale_date": "2010-09-04",
                    "price": "19.66",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 382
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 6,
                    "sale_date": "2010-09-05",
                    "price": "21.12",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 383
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 12,
                    "sale_date": "2010-09-05",
                    "price": "20.72",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 384
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 9,
                    "sale_date": "2010-09-05",
                    "price": "12.31",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 385
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 13,
                    "sale_date": "2010-09-05",
                    "price": "13.26",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 386
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 5,
                    "sale_date": "2010-09-05",
                    "price": "27.79",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 387
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 36,
                    "sale_date": "2010-09-05",
                    "price": "12.37",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 388
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 1,
                    "sale_date": "2010-09-05",
                    "price": "10.00",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 389
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 2,
                    "sale_date": "2010-09-05",
                    "price": "18.88",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 390
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 12,
                    "sale_date": "2010-09-05",
                    "price": "24.42",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 391
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 15,
                    "sale_date": "2010-09-06",
                    "price": "15.83",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 392
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 7,
                    "sale_date": "2010-09-06",
                    "price": "18.65",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 393
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 6,
                    "sale_date": "2010-09-07",
                    "price": "13.68",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 394
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 17,
                    "sale_date": "2010-09-07",
                    "price": "13.69",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 395
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 35,
                    "sale_date": "2010-09-07",
                    "price": "19.97",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 396
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 10,
                    "sale_date": "2010-09-07",
                    "price": "29.54",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 397
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 11,
                    "sale_date": "2010-09-07",
                    "price": "17.22",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 398
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 32,
                    "sale_date": "2010-09-07",
                    "price": "15.38",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 399
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 39,
                    "sale_date": "2010-09-07",
                    "price": "13.44",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 400
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 10,
                    "sale_date": "2010-09-07",
                    "price": "12.74",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 401
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 5,
                    "sale_date": "2010-09-08",
                    "price": "17.76",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 402
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 37,
                    "sale_date": "2010-09-08",
                    "price": "13.04",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 403
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 39,
                    "sale_date": "2010-09-08",
                    "price": "22.93",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 404
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 12,
                    "sale_date": "2010-09-08",
                    "price": "28.21",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 405
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 26,
                    "sale_date": "2010-09-08",
                    "price": "13.22",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 406
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 34,
                    "sale_date": "2010-09-08",
                    "price": "13.32",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 407
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 1,
                    "sale_date": "2010-09-08",
                    "price": "13.42",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 408
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 39,
                    "sale_date": "2010-09-08",
                    "price": "14.95",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 409
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 39,
                    "sale_date": "2010-09-08",
                    "price": "9.97",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 410
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 24,
                    "sale_date": "2010-09-09",
                    "price": "26.02",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 411
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 27,
                    "sale_date": "2010-09-09",
                    "price": "14.79",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 412
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 17,
                    "sale_date": "2010-09-09",
                    "price": "12.85",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 413
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 31,
                    "sale_date": "2010-09-09",
                    "price": "22.62",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 414
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 35,
                    "sale_date": "2010-09-09",
                    "price": "12.50",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 415
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 27,
                    "sale_date": "2010-09-10",
                    "price": "15.92",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 416
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 29,
                    "sale_date": "2010-09-10",
                    "price": "10.75",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 417
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 33,
                    "sale_date": "2010-09-10",
                    "price": "13.27",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 418
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 36,
                    "sale_date": "2010-09-10",
                    "price": "16.78",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 419
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 15,
                    "sale_date": "2010-09-10",
                    "price": "12.36",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 420
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 29,
                    "sale_date": "2010-09-10",
                    "price": "11.72",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 421
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 14,
                    "sale_date": "2010-09-10",
                    "price": "13.86",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 422
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 31,
                    "sale_date": "2010-09-10",
                    "price": "27.88",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 423
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 13,
                    "sale_date": "2010-09-10",
                    "price": "14.61",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 424
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 9,
                    "sale_date": "2010-09-10",
                    "price": "10.70",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 425
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 30,
                    "sale_date": "2010-09-11",
                    "price": "24.73",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 426
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 20,
                    "sale_date": "2010-09-11",
                    "price": "14.38",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 427
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 2,
                    "sale_date": "2010-09-11",
                    "price": "21.14",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 428
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 37,
                    "sale_date": "2010-09-12",
                    "price": "11.42",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 429
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 16,
                    "sale_date": "2010-09-12",
                    "price": "15.19",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 430
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 11,
                    "sale_date": "2010-09-12",
                    "price": "25.05",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 431
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 22,
                    "sale_date": "2010-09-12",
                    "price": "17.66",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 432
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 33,
                    "sale_date": "2010-09-12",
                    "price": "10.68",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 433
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 30,
                    "sale_date": "2010-09-12",
                    "price": "9.68",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 434
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 13,
                    "sale_date": "2010-09-12",
                    "price": "15.73",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 435
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 24,
                    "sale_date": "2010-09-12",
                    "price": "10.94",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 436
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 14,
                    "sale_date": "2010-09-12",
                    "price": "10.99",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 437
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 12,
                    "sale_date": "2010-09-13",
                    "price": "22.60",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 438
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 6,
                    "sale_date": "2010-09-13",
                    "price": "20.76",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 439
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 1,
                    "sale_date": "2010-09-13",
                    "price": "14.75",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 440
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 35,
                    "sale_date": "2010-09-14",
                    "price": "14.36",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 441
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 15,
                    "sale_date": "2010-09-14",
                    "price": "15.88",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 442
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 26,
                    "sale_date": "2010-09-14",
                    "price": "27.59",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 443
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 3,
                    "sale_date": "2010-09-14",
                    "price": "10.20",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 444
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 12,
                    "sale_date": "2010-09-14",
                    "price": "11.29",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 445
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 18,
                    "sale_date": "2010-09-14",
                    "price": "9.70",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 446
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 20,
                    "sale_date": "2010-09-15",
                    "price": "11.15",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 447
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 17,
                    "sale_date": "2010-09-15",
                    "price": "26.43",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 448
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 9,
                    "sale_date": "2010-09-15",
                    "price": "10.81",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 449
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 23,
                    "sale_date": "2010-09-15",
                    "price": "20.60",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 450
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 17,
                    "sale_date": "2010-09-15",
                    "price": "19.07",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 451
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 20,
                    "sale_date": "2010-09-16",
                    "price": "16.39",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 452
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 20,
                    "sale_date": "2010-09-17",
                    "price": "11.50",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 453
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 35,
                    "sale_date": "2010-09-17",
                    "price": "12.19",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 454
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 39,
                    "sale_date": "2010-09-17",
                    "price": "14.74",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 455
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 23,
                    "sale_date": "2010-09-17",
                    "price": "12.93",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 456
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 25,
                    "sale_date": "2010-09-17",
                    "price": "17.32",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 457
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 25,
                    "sale_date": "2010-09-17",
                    "price": "10.35",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 458
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 23,
                    "sale_date": "2010-09-17",
                    "price": "18.35",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 459
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 9,
                    "sale_date": "2010-09-18",
                    "price": "16.96",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 460
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 30,
                    "sale_date": "2010-09-18",
                    "price": "24.47",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 461
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 14,
                    "sale_date": "2010-09-18",
                    "price": "11.65",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 462
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 11,
                    "sale_date": "2010-09-18",
                    "price": "14.08",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 463
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 14,
                    "sale_date": "2010-09-18",
                    "price": "24.86",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 464
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 38,
                    "sale_date": "2010-09-18",
                    "price": "13.65",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 465
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 22,
                    "sale_date": "2010-09-19",
                    "price": "15.19",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 466
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 10,
                    "sale_date": "2010-09-19",
                    "price": "14.18",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 467
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 8,
                    "sale_date": "2010-09-19",
                    "price": "12.14",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 468
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 12,
                    "sale_date": "2010-09-19",
                    "price": "14.60",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 469
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 5,
                    "sale_date": "2010-09-19",
                    "price": "22.78",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 470
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 23,
                    "sale_date": "2010-09-19",
                    "price": "13.24",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 471
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 25,
                    "sale_date": "2010-09-19",
                    "price": "12.54",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 472
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 26,
                    "sale_date": "2010-09-19",
                    "price": "28.40",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 473
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 14,
                    "sale_date": "2010-09-19",
                    "price": "14.97",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 474
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 22,
                    "sale_date": "2010-09-20",
                    "price": "15.44",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 475
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 30,
                    "sale_date": "2010-09-20",
                    "price": "13.91",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 476
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 29,
                    "sale_date": "2010-09-20",
                    "price": "21.43",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 477
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 27,
                    "sale_date": "2010-09-20",
                    "price": "20.33",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 478
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 33,
                    "sale_date": "2010-09-20",
                    "price": "14.10",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 479
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 27,
                    "sale_date": "2010-09-21",
                    "price": "9.42",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 480
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 11,
                    "sale_date": "2010-09-21",
                    "price": "14.56",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 481
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 15,
                    "sale_date": "2010-09-21",
                    "price": "30.56",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 482
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 37,
                    "sale_date": "2010-09-21",
                    "price": "13.13",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 483
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 4,
                    "sale_date": "2010-09-22",
                    "price": "19.93",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 484
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 26,
                    "sale_date": "2010-09-22",
                    "price": "14.50",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 485
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 2,
                    "sale_date": "2010-09-22",
                    "price": "23.08",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 486
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 10,
                    "sale_date": "2010-09-22",
                    "price": "15.00",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 487
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 33,
                    "sale_date": "2010-09-22",
                    "price": "16.59",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 488
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 31,
                    "sale_date": "2010-09-22",
                    "price": "16.02",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 489
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 31,
                    "sale_date": "2010-09-22",
                    "price": "12.45",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 490
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 18,
                    "sale_date": "2010-09-23",
                    "price": "16.06",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 491
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 16,
                    "sale_date": "2010-09-23",
                    "price": "14.17",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 492
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 26,
                    "sale_date": "2010-09-23",
                    "price": "14.23",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 493
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 32,
                    "sale_date": "2010-09-23",
                    "price": "12.62",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 494
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 10,
                    "sale_date": "2010-09-23",
                    "price": "13.55",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 495
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 18,
                    "sale_date": "2010-09-23",
                    "price": "20.93",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 496
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 3,
                    "sale_date": "2010-09-24",
                    "price": "25.14",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 497
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 24,
                    "sale_date": "2010-09-24",
                    "price": "14.54",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 498
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 25,
                    "sale_date": "2010-09-24",
                    "price": "12.97",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 499
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 26,
                    "sale_date": "2010-09-24",
                    "price": "16.65",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 500
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 34,
                    "sale_date": "2010-09-24",
                    "price": "15.89",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 501
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 34,
                    "sale_date": "2010-09-24",
                    "price": "16.70",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 502
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 8,
                    "sale_date": "2010-09-24",
                    "price": "18.94",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 503
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 11,
                    "sale_date": "2010-09-25",
                    "price": "16.08",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 504
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 23,
                    "sale_date": "2010-09-25",
                    "price": "17.38",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 505
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 24,
                    "sale_date": "2010-09-25",
                    "price": "11.68",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 506
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 6,
                    "sale_date": "2010-09-25",
                    "price": "21.47",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 507
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 34,
                    "sale_date": "2010-09-25",
                    "price": "13.17",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 508
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 39,
                    "sale_date": "2010-09-25",
                    "price": "15.57",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 509
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 19,
                    "sale_date": "2010-09-26",
                    "price": "14.89",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 510
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 7,
                    "sale_date": "2010-09-26",
                    "price": "8.50",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 511
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 25,
                    "sale_date": "2010-09-27",
                    "price": "15.15",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 512
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 18,
                    "sale_date": "2010-09-27",
                    "price": "13.25",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 513
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 29,
                    "sale_date": "2010-09-27",
                    "price": "12.53",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 514
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 23,
                    "sale_date": "2010-09-27",
                    "price": "15.37",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 515
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 37,
                    "sale_date": "2010-09-27",
                    "price": "12.18",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 516
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 5,
                    "sale_date": "2010-09-27",
                    "price": "17.17",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 517
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 19,
                    "sale_date": "2010-09-27",
                    "price": "13.04",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 518
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 15,
                    "sale_date": "2010-09-28",
                    "price": "11.58",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 519
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 25,
                    "sale_date": "2010-09-28",
                    "price": "11.33",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 520
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 22,
                    "sale_date": "2010-09-28",
                    "price": "25.60",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 521
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 6,
                    "sale_date": "2010-09-28",
                    "price": "14.34",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 522
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 21,
                    "sale_date": "2010-09-29",
                    "price": "18.79",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 523
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 16,
                    "sale_date": "2010-09-29",
                    "price": "14.73",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 524
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 35,
                    "sale_date": "2010-09-29",
                    "price": "13.50",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 525
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 30,
                    "sale_date": "2010-09-29",
                    "price": "17.77",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 526
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 18,
                    "sale_date": "2010-09-29",
                    "price": "10.92",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 527
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 26,
                    "sale_date": "2010-09-29",
                    "price": "15.15",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 528
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 11,
                    "sale_date": "2010-09-29",
                    "price": "19.66",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 529
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 26,
                    "sale_date": "2010-09-30",
                    "price": "12.33",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 530
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 3,
                    "sale_date": "2010-09-30",
                    "price": "14.96",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 531
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 37,
                    "sale_date": "2010-09-30",
                    "price": "10.64",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 532
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 2,
                    "sale_date": "2010-09-30",
                    "price": "10.04",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 533
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 28,
                    "sale_date": "2010-10-01",
                    "price": "18.64",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 534
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 12,
                    "sale_date": "2010-10-01",
                    "price": "25.34",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 535
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 7,
                    "sale_date": "2010-10-02",
                    "price": "11.72",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 536
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 28,
                    "sale_date": "2010-10-02",
                    "price": "15.84",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 537
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 12,
                    "sale_date": "2010-10-02",
                    "price": "16.26",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 538
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 9,
                    "sale_date": "2010-10-02",
                    "price": "13.14",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 539
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 39,
                    "sale_date": "2010-10-02",
                    "price": "18.81",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 540
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 21,
                    "sale_date": "2010-10-03",
                    "price": "16.91",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 541
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 19,
                    "sale_date": "2010-10-03",
                    "price": "12.34",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 542
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 36,
                    "sale_date": "2010-10-03",
                    "price": "10.36",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 543
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 29,
                    "sale_date": "2010-10-03",
                    "price": "13.36",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 544
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 20,
                    "sale_date": "2010-10-03",
                    "price": "14.20",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 545
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 9,
                    "sale_date": "2010-10-03",
                    "price": "15.52",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 546
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 36,
                    "sale_date": "2010-10-03",
                    "price": "13.08",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 547
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 5,
                    "sale_date": "2010-10-04",
                    "price": "11.15",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 548
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 3,
                    "sale_date": "2010-10-04",
                    "price": "17.89",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 549
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 17,
                    "sale_date": "2010-10-05",
                    "price": "11.94",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 550
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 28,
                    "sale_date": "2010-10-05",
                    "price": "20.94",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 551
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 24,
                    "sale_date": "2010-10-05",
                    "price": "13.51",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 552
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 8,
                    "sale_date": "2010-10-05",
                    "price": "13.59",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 553
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 38,
                    "sale_date": "2010-10-05",
                    "price": "15.88",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 554
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 34,
                    "sale_date": "2010-10-05",
                    "price": "16.70",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 555
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 33,
                    "sale_date": "2010-10-06",
                    "price": "12.63",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 556
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 9,
                    "sale_date": "2010-10-06",
                    "price": "20.39",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 557
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 24,
                    "sale_date": "2010-10-06",
                    "price": "25.66",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 558
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 39,
                    "sale_date": "2010-10-06",
                    "price": "14.23",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 559
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 17,
                    "sale_date": "2010-10-06",
                    "price": "12.27",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 560
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 4,
                    "sale_date": "2010-10-07",
                    "price": "15.45",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 561
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 33,
                    "sale_date": "2010-10-07",
                    "price": "16.21",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 562
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 11,
                    "sale_date": "2010-10-07",
                    "price": "20.84",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 563
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 14,
                    "sale_date": "2010-10-07",
                    "price": "14.62",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 564
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 17,
                    "sale_date": "2010-10-07",
                    "price": "17.92",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 565
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 25,
                    "sale_date": "2010-10-07",
                    "price": "10.35",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 566
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 37,
                    "sale_date": "2010-10-08",
                    "price": "11.47",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 567
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 8,
                    "sale_date": "2010-10-08",
                    "price": "11.33",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 568
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 9,
                    "sale_date": "2010-10-08",
                    "price": "13.08",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 569
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 37,
                    "sale_date": "2010-10-08",
                    "price": "27.83",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 570
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 34,
                    "sale_date": "2010-10-08",
                    "price": "10.70",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 571
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 22,
                    "sale_date": "2010-10-08",
                    "price": "21.23",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 572
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 35,
                    "sale_date": "2010-10-08",
                    "price": "9.65",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 573
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 13,
                    "sale_date": "2010-10-09",
                    "price": "9.29",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 574
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 28,
                    "sale_date": "2010-10-09",
                    "price": "13.40",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 575
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 16,
                    "sale_date": "2010-10-09",
                    "price": "13.96",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 576
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 22,
                    "sale_date": "2010-10-09",
                    "price": "16.15",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 577
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 23,
                    "sale_date": "2010-10-09",
                    "price": "13.63",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 578
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 4,
                    "sale_date": "2010-10-10",
                    "price": "13.60",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 579
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 36,
                    "sale_date": "2010-10-10",
                    "price": "17.51",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 580
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 39,
                    "sale_date": "2010-10-10",
                    "price": "13.71",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 581
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 21,
                    "sale_date": "2010-10-10",
                    "price": "16.27",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 582
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 18,
                    "sale_date": "2010-10-10",
                    "price": "15.02",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 583
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 36,
                    "sale_date": "2010-10-10",
                    "price": "16.31",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 584
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 10,
                    "sale_date": "2010-10-10",
                    "price": "24.50",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 585
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 31,
                    "sale_date": "2010-10-10",
                    "price": "13.56",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 586
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 5,
                    "sale_date": "2010-10-10",
                    "price": "12.20",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 587
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 34,
                    "sale_date": "2010-10-11",
                    "price": "15.94",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 588
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 18,
                    "sale_date": "2010-10-11",
                    "price": "16.25",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 589
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 15,
                    "sale_date": "2010-10-11",
                    "price": "13.86",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 590
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 36,
                    "sale_date": "2010-10-12",
                    "price": "16.74",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 591
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 3,
                    "sale_date": "2010-10-12",
                    "price": "15.05",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 592
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 34,
                    "sale_date": "2010-10-12",
                    "price": "17.78",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 593
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 21,
                    "sale_date": "2010-10-12",
                    "price": "26.11",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 594
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 21,
                    "sale_date": "2010-10-12",
                    "price": "15.50",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 595
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 34,
                    "sale_date": "2010-10-12",
                    "price": "14.91",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 596
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 11,
                    "sale_date": "2010-10-12",
                    "price": "15.48",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 597
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 6,
                    "sale_date": "2010-10-13",
                    "price": "11.68",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 598
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 9,
                    "sale_date": "2010-10-13",
                    "price": "21.96",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 599
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 17,
                    "sale_date": "2010-10-13",
                    "price": "25.97",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 600
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 30,
                    "sale_date": "2010-10-13",
                    "price": "15.01",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 601
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 4,
                    "sale_date": "2010-10-13",
                    "price": "11.83",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 602
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 3,
                    "sale_date": "2010-10-14",
                    "price": "11.84",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 603
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 36,
                    "sale_date": "2010-10-14",
                    "price": "20.03",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 604
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 34,
                    "sale_date": "2010-10-14",
                    "price": "23.82",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 605
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 4,
                    "sale_date": "2010-10-14",
                    "price": "28.51",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 606
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 7,
                    "sale_date": "2010-10-15",
                    "price": "27.00",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 607
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 20,
                    "sale_date": "2010-10-15",
                    "price": "15.15",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 608
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 20,
                    "sale_date": "2010-10-16",
                    "price": "15.26",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 609
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 10,
                    "sale_date": "2010-10-16",
                    "price": "25.77",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 610
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 35,
                    "sale_date": "2010-10-16",
                    "price": "13.24",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 611
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 32,
                    "sale_date": "2010-10-17",
                    "price": "10.17",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 612
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 28,
                    "sale_date": "2010-10-17",
                    "price": "26.68",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 613
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 21,
                    "sale_date": "2010-10-17",
                    "price": "12.17",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 614
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 37,
                    "sale_date": "2010-10-17",
                    "price": "11.31",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 615
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 6,
                    "sale_date": "2010-10-17",
                    "price": "30.42",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 616
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 18,
                    "sale_date": "2010-10-17",
                    "price": "19.40",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 617
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 27,
                    "sale_date": "2010-10-17",
                    "price": "20.12",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 618
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 15,
                    "sale_date": "2010-10-17",
                    "price": "14.22",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 619
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 8,
                    "sale_date": "2010-10-17",
                    "price": "24.73",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 620
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 15,
                    "sale_date": "2010-10-17",
                    "price": "14.29",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 621
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 35,
                    "sale_date": "2010-10-17",
                    "price": "14.00",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 622
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 9,
                    "sale_date": "2010-10-18",
                    "price": "16.39",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 623
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 29,
                    "sale_date": "2010-10-18",
                    "price": "14.87",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 624
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 9,
                    "sale_date": "2010-10-18",
                    "price": "15.15",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 625
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 32,
                    "sale_date": "2010-10-18",
                    "price": "16.73",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 626
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 25,
                    "sale_date": "2010-10-18",
                    "price": "12.06",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 627
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 23,
                    "sale_date": "2010-10-18",
                    "price": "16.76",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 628
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 7,
                    "sale_date": "2010-10-18",
                    "price": "12.08",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 629
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 20,
                    "sale_date": "2010-10-18",
                    "price": "13.05",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 630
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 29,
                    "sale_date": "2010-10-18",
                    "price": "23.13",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 631
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 4,
                    "sale_date": "2010-10-19",
                    "price": "14.57",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 632
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 35,
                    "sale_date": "2010-10-19",
                    "price": "14.19",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 633
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 28,
                    "sale_date": "2010-10-19",
                    "price": "12.34",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 634
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 3,
                    "sale_date": "2010-10-19",
                    "price": "21.13",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 635
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 17,
                    "sale_date": "2010-10-19",
                    "price": "14.03",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 636
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 31,
                    "sale_date": "2010-10-19",
                    "price": "25.56",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 637
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 19,
                    "sale_date": "2010-10-20",
                    "price": "15.14",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 638
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 33,
                    "sale_date": "2010-10-20",
                    "price": "13.93",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 639
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 8,
                    "sale_date": "2010-10-20",
                    "price": "23.28",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 640
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 29,
                    "sale_date": "2010-10-20",
                    "price": "14.54",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 641
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 14,
                    "sale_date": "2010-10-20",
                    "price": "16.30",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 642
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 29,
                    "sale_date": "2010-10-20",
                    "price": "16.51",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 643
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 20,
                    "sale_date": "2010-10-20",
                    "price": "22.54",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 644
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 11,
                    "sale_date": "2010-10-20",
                    "price": "22.10",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 645
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 35,
                    "sale_date": "2010-10-20",
                    "price": "10.16",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 646
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 7,
                    "sale_date": "2010-10-20",
                    "price": "15.30",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 647
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 34,
                    "sale_date": "2010-10-21",
                    "price": "20.75",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 648
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 24,
                    "sale_date": "2010-10-21",
                    "price": "10.85",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 649
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 17,
                    "sale_date": "2010-10-21",
                    "price": "18.96",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 650
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 7,
                    "sale_date": "2010-10-21",
                    "price": "10.50",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 651
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 39,
                    "sale_date": "2010-10-21",
                    "price": "27.46",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 652
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 23,
                    "sale_date": "2010-10-21",
                    "price": "8.60",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 653
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 25,
                    "sale_date": "2010-10-21",
                    "price": "14.21",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 654
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 32,
                    "sale_date": "2010-10-21",
                    "price": "22.85",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 655
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 28,
                    "sale_date": "2010-10-21",
                    "price": "16.47",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 656
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 21,
                    "sale_date": "2010-10-21",
                    "price": "13.72",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 657
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 6,
                    "sale_date": "2010-10-21",
                    "price": "12.74",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 658
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 2,
                    "sale_date": "2010-10-21",
                    "price": "19.29",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 659
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 17,
                    "sale_date": "2010-10-21",
                    "price": "10.98",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 660
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 25,
                    "sale_date": "2010-10-21",
                    "price": "30.36",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 661
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 23,
                    "sale_date": "2010-10-22",
                    "price": "22.84",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 662
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 8,
                    "sale_date": "2010-10-22",
                    "price": "13.77",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 663
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 16,
                    "sale_date": "2010-10-22",
                    "price": "12.70",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 664
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 3,
                    "sale_date": "2010-10-22",
                    "price": "15.56",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 665
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 22,
                    "sale_date": "2010-10-23",
                    "price": "11.28",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 666
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 7,
                    "sale_date": "2010-10-23",
                    "price": "26.68",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 667
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 8,
                    "sale_date": "2010-10-23",
                    "price": "11.83",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 668
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 15,
                    "sale_date": "2010-10-23",
                    "price": "13.65",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 669
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 20,
                    "sale_date": "2010-10-24",
                    "price": "28.26",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 670
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 39,
                    "sale_date": "2010-10-24",
                    "price": "17.94",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 671
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 34,
                    "sale_date": "2010-10-24",
                    "price": "11.31",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 672
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 1,
                    "sale_date": "2010-10-24",
                    "price": "16.75",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 673
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 9,
                    "sale_date": "2010-10-24",
                    "price": "17.00",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 674
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 26,
                    "sale_date": "2010-10-24",
                    "price": "14.43",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 675
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 1,
                    "sale_date": "2010-10-25",
                    "price": "13.58",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 676
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 1,
                    "sale_date": "2010-10-26",
                    "price": "10.58",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 677
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 3,
                    "sale_date": "2010-10-26",
                    "price": "13.41",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 678
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 38,
                    "sale_date": "2010-10-26",
                    "price": "18.79",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 679
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 24,
                    "sale_date": "2010-10-26",
                    "price": "19.24",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 680
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 16,
                    "sale_date": "2010-10-26",
                    "price": "21.28",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 681
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 35,
                    "sale_date": "2010-10-26",
                    "price": "15.65",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 682
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 27,
                    "sale_date": "2010-10-26",
                    "price": "14.55",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 683
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 18,
                    "sale_date": "2010-10-27",
                    "price": "15.95",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 684
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 19,
                    "sale_date": "2010-10-27",
                    "price": "22.67",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 685
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 9,
                    "sale_date": "2010-10-27",
                    "price": "10.08",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 686
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 7,
                    "sale_date": "2010-10-27",
                    "price": "12.68",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 687
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 10,
                    "sale_date": "2010-10-27",
                    "price": "22.37",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 688
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 18,
                    "sale_date": "2010-10-28",
                    "price": "16.59",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 689
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 15,
                    "sale_date": "2010-10-28",
                    "price": "11.69",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 690
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 28,
                    "sale_date": "2010-10-28",
                    "price": "11.55",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 691
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 38,
                    "sale_date": "2010-10-28",
                    "price": "15.35",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 692
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 5,
                    "sale_date": "2010-10-28",
                    "price": "24.37",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 693
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 19,
                    "sale_date": "2010-10-28",
                    "price": "28.49",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 694
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 29,
                    "sale_date": "2010-10-28",
                    "price": "15.06",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 695
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 10,
                    "sale_date": "2010-10-28",
                    "price": "26.54",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 696
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 32,
                    "sale_date": "2010-10-29",
                    "price": "12.95",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 697
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 6,
                    "sale_date": "2010-10-29",
                    "price": "13.97",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 698
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 28,
                    "sale_date": "2010-10-29",
                    "price": "20.47",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 699
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 2,
                    "sale_date": "2010-10-29",
                    "price": "13.66",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 700
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 37,
                    "sale_date": "2010-10-29",
                    "price": "21.80",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 701
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 22,
                    "sale_date": "2010-10-29",
                    "price": "12.73",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 702
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 14,
                    "sale_date": "2010-10-29",
                    "price": "17.38",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 703
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 7,
                    "sale_date": "2010-10-29",
                    "price": "19.48",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 704
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 37,
                    "sale_date": "2010-10-29",
                    "price": "11.13",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 705
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 27,
                    "sale_date": "2010-10-29",
                    "price": "7.16",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 706
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 33,
                    "sale_date": "2010-10-30",
                    "price": "12.40",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 707
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 17,
                    "sale_date": "2010-10-30",
                    "price": "15.17",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 708
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 8,
                    "sale_date": "2010-10-30",
                    "price": "15.86",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 709
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 4,
                    "sale_date": "2010-10-30",
                    "price": "17.75",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 710
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 28,
                    "sale_date": "2010-10-30",
                    "price": "11.68",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 711
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 29,
                    "sale_date": "2010-10-31",
                    "price": "22.28",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 712
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 37,
                    "sale_date": "2010-10-31",
                    "price": "22.76",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 713
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 33,
                    "sale_date": "2010-10-31",
                    "price": "15.41",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 714
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 9,
                    "sale_date": "2010-10-31",
                    "price": "15.40",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 715
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 3,
                    "sale_date": "2010-10-31",
                    "price": "11.08",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 716
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 33,
                    "sale_date": "2010-10-31",
                    "price": "14.35",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 717
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 13,
                    "sale_date": "2010-10-31",
                    "price": "12.90",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 718
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 36,
                    "sale_date": "2010-11-01",
                    "price": "12.45",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 719
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 28,
                    "sale_date": "2010-11-01",
                    "price": "13.61",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 720
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 21,
                    "sale_date": "2010-11-01",
                    "price": "28.30",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 721
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 11,
                    "sale_date": "2010-11-01",
                    "price": "20.64",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 722
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 24,
                    "sale_date": "2010-11-01",
                    "price": "26.36",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 723
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 36,
                    "sale_date": "2010-11-01",
                    "price": "12.96",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 724
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 29,
                    "sale_date": "2010-11-01",
                    "price": "13.13",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 725
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 25,
                    "sale_date": "2010-11-01",
                    "price": "18.35",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 726
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 10,
                    "sale_date": "2010-11-02",
                    "price": "27.62",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 727
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 5,
                    "sale_date": "2010-11-02",
                    "price": "11.33",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 728
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 26,
                    "sale_date": "2010-11-02",
                    "price": "30.22",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 729
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 19,
                    "sale_date": "2010-11-03",
                    "price": "16.92",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 730
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 34,
                    "sale_date": "2010-11-03",
                    "price": "23.76",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 731
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 32,
                    "sale_date": "2010-11-03",
                    "price": "12.95",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 732
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 21,
                    "sale_date": "2010-11-03",
                    "price": "22.91",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 733
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 1,
                    "sale_date": "2010-11-03",
                    "price": "15.92",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 734
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 6,
                    "sale_date": "2010-11-04",
                    "price": "10.77",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 735
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 30,
                    "sale_date": "2010-11-04",
                    "price": "14.79",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 736
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 17,
                    "sale_date": "2010-11-04",
                    "price": "21.91",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 737
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 15,
                    "sale_date": "2010-11-04",
                    "price": "15.88",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 738
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 34,
                    "sale_date": "2010-11-04",
                    "price": "12.03",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 739
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 39,
                    "sale_date": "2010-11-04",
                    "price": "18.22",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 740
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 38,
                    "sale_date": "2010-11-04",
                    "price": "10.43",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 741
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 1,
                    "sale_date": "2010-11-05",
                    "price": "10.15",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 742
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 11,
                    "sale_date": "2010-11-05",
                    "price": "13.20",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 743
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 17,
                    "sale_date": "2010-11-05",
                    "price": "21.98",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 744
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 39,
                    "sale_date": "2010-11-05",
                    "price": "11.18",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 745
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 12,
                    "sale_date": "2010-11-06",
                    "price": "17.19",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 746
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 9,
                    "sale_date": "2010-11-06",
                    "price": "13.15",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 747
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 22,
                    "sale_date": "2010-11-06",
                    "price": "15.58",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 748
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 32,
                    "sale_date": "2010-11-06",
                    "price": "22.64",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 749
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 26,
                    "sale_date": "2010-11-06",
                    "price": "22.60",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 750
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 11,
                    "sale_date": "2010-11-06",
                    "price": "23.79",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 751
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 8,
                    "sale_date": "2010-11-07",
                    "price": "15.56",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 752
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 22,
                    "sale_date": "2010-11-07",
                    "price": "19.73",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 753
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 25,
                    "sale_date": "2010-11-07",
                    "price": "13.36",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 754
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 10,
                    "sale_date": "2010-11-07",
                    "price": "18.91",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 755
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 12,
                    "sale_date": "2010-11-07",
                    "price": "10.71",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 756
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 33,
                    "sale_date": "2010-11-07",
                    "price": "19.62",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 757
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 17,
                    "sale_date": "2010-11-08",
                    "price": "19.95",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 758
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 7,
                    "sale_date": "2010-11-08",
                    "price": "14.89",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 759
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 8,
                    "sale_date": "2010-11-08",
                    "price": "19.96",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 760
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 23,
                    "sale_date": "2010-11-08",
                    "price": "18.57",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 761
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 12,
                    "sale_date": "2010-11-09",
                    "price": "18.75",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 762
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 15,
                    "sale_date": "2010-11-09",
                    "price": "25.00",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 763
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 2,
                    "sale_date": "2010-11-09",
                    "price": "16.75",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 764
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 10,
                    "sale_date": "2010-11-09",
                    "price": "12.59",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 765
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 21,
                    "sale_date": "2010-11-09",
                    "price": "14.08",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 766
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 34,
                    "sale_date": "2010-11-09",
                    "price": "18.06",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 767
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 2,
                    "sale_date": "2010-11-09",
                    "price": "11.14",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 768
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 28,
                    "sale_date": "2010-11-10",
                    "price": "11.86",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 769
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 21,
                    "sale_date": "2010-11-10",
                    "price": "13.89",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 770
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 17,
                    "sale_date": "2010-11-10",
                    "price": "21.24",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 771
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 1,
                    "sale_date": "2010-11-11",
                    "price": "11.61",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 772
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 12,
                    "sale_date": "2010-11-11",
                    "price": "22.69",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 773
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 10,
                    "sale_date": "2010-11-11",
                    "price": "16.31",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 774
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 18,
                    "sale_date": "2010-11-11",
                    "price": "14.77",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 775
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 4,
                    "sale_date": "2010-11-11",
                    "price": "14.45",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 776
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 9,
                    "sale_date": "2010-11-11",
                    "price": "16.27",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 777
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 27,
                    "sale_date": "2010-11-12",
                    "price": "14.49",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 778
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 6,
                    "sale_date": "2010-11-12",
                    "price": "24.06",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 779
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 31,
                    "sale_date": "2010-11-12",
                    "price": "12.70",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 780
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 35,
                    "sale_date": "2010-11-12",
                    "price": "11.43",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 781
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 18,
                    "sale_date": "2010-11-12",
                    "price": "19.43",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 782
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 3,
                    "sale_date": "2010-11-12",
                    "price": "12.63",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 783
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 8,
                    "sale_date": "2010-11-12",
                    "price": "11.07",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 784
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 33,
                    "sale_date": "2010-11-13",
                    "price": "29.53",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 785
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 26,
                    "sale_date": "2010-11-13",
                    "price": "28.77",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 786
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 27,
                    "sale_date": "2010-11-13",
                    "price": "14.07",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 787
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 1,
                    "sale_date": "2010-11-13",
                    "price": "13.49",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 788
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 22,
                    "sale_date": "2010-11-13",
                    "price": "19.03",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 789
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 38,
                    "sale_date": "2010-11-13",
                    "price": "9.62",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 790
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 31,
                    "sale_date": "2010-11-13",
                    "price": "18.26",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 791
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 32,
                    "sale_date": "2010-11-13",
                    "price": "12.87",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 792
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 8,
                    "sale_date": "2010-11-14",
                    "price": "14.82",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 793
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 35,
                    "sale_date": "2010-11-14",
                    "price": "17.94",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 794
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 9,
                    "sale_date": "2010-11-14",
                    "price": "11.47",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 795
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 38,
                    "sale_date": "2010-11-15",
                    "price": "15.64",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 796
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 3,
                    "sale_date": "2010-11-15",
                    "price": "14.32",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 797
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 13,
                    "sale_date": "2010-11-15",
                    "price": "26.22",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 798
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 26,
                    "sale_date": "2010-11-16",
                    "price": "13.86",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 799
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 16,
                    "sale_date": "2010-11-16",
                    "price": "14.13",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 800
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 31,
                    "sale_date": "2010-11-16",
                    "price": "23.25",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 801
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 33,
                    "sale_date": "2010-11-16",
                    "price": "13.51",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 802
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 34,
                    "sale_date": "2010-11-16",
                    "price": "15.85",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 803
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 38,
                    "sale_date": "2010-11-16",
                    "price": "28.23",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 804
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 9,
                    "sale_date": "2010-11-16",
                    "price": "23.01",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 805
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 21,
                    "sale_date": "2010-11-17",
                    "price": "24.97",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 806
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 17,
                    "sale_date": "2010-11-17",
                    "price": "14.47",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 807
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 9,
                    "sale_date": "2010-11-17",
                    "price": "16.84",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 808
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 16,
                    "sale_date": "2010-11-17",
                    "price": "14.76",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 809
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 31,
                    "sale_date": "2010-11-17",
                    "price": "13.16",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 810
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 31,
                    "sale_date": "2010-11-17",
                    "price": "11.96",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 811
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 29,
                    "sale_date": "2010-11-17",
                    "price": "22.29",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 812
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 22,
                    "sale_date": "2010-11-18",
                    "price": "28.84",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 813
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 29,
                    "sale_date": "2010-11-18",
                    "price": "14.64",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 814
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 13,
                    "sale_date": "2010-11-18",
                    "price": "19.12",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 815
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 30,
                    "sale_date": "2010-11-18",
                    "price": "16.27",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 816
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 38,
                    "sale_date": "2010-11-18",
                    "price": "16.25",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 817
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 1,
                    "sale_date": "2010-11-19",
                    "price": "9.63",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 818
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 18,
                    "sale_date": "2010-11-19",
                    "price": "16.48",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 819
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 1,
                    "sale_date": "2010-11-19",
                    "price": "18.31",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 820
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 27,
                    "sale_date": "2010-11-19",
                    "price": "12.55",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 821
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 15,
                    "sale_date": "2010-11-20",
                    "price": "13.26",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 822
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 31,
                    "sale_date": "2010-11-20",
                    "price": "13.25",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 823
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 29,
                    "sale_date": "2010-11-20",
                    "price": "12.65",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 824
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 24,
                    "sale_date": "2010-11-20",
                    "price": "19.68",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 825
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 32,
                    "sale_date": "2010-11-20",
                    "price": "10.49",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 826
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 12,
                    "sale_date": "2010-11-20",
                    "price": "25.75",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 827
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 20,
                    "sale_date": "2010-11-20",
                    "price": "23.66",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 828
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 19,
                    "sale_date": "2010-11-21",
                    "price": "24.09",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 829
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 26,
                    "sale_date": "2010-11-21",
                    "price": "12.38",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 830
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 6,
                    "sale_date": "2010-11-21",
                    "price": "14.62",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 831
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 3,
                    "sale_date": "2010-11-21",
                    "price": "15.94",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 832
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 11,
                    "sale_date": "2010-11-21",
                    "price": "14.68",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 833
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 5,
                    "sale_date": "2010-11-21",
                    "price": "20.02",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 834
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 14,
                    "sale_date": "2010-11-22",
                    "price": "17.08",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 835
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 27,
                    "sale_date": "2010-11-22",
                    "price": "28.79",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 836
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 17,
                    "sale_date": "2010-11-22",
                    "price": "20.81",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 837
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 37,
                    "sale_date": "2010-11-23",
                    "price": "28.59",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 838
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 33,
                    "sale_date": "2010-11-23",
                    "price": "15.94",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 839
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 27,
                    "sale_date": "2010-11-23",
                    "price": "9.84",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 840
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 30,
                    "sale_date": "2010-11-23",
                    "price": "13.54",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 841
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 18,
                    "sale_date": "2010-11-23",
                    "price": "18.68",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 842
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 26,
                    "sale_date": "2010-11-23",
                    "price": "18.97",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 843
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 18,
                    "sale_date": "2010-11-23",
                    "price": "15.39",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 844
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 3,
                    "sale_date": "2010-11-23",
                    "price": "21.07",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 845
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 9,
                    "sale_date": "2010-11-23",
                    "price": "19.05",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 846
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 17,
                    "sale_date": "2010-11-24",
                    "price": "14.53",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 847
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 37,
                    "sale_date": "2010-11-24",
                    "price": "15.93",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 848
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 30,
                    "sale_date": "2010-11-24",
                    "price": "16.30",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 849
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 9,
                    "sale_date": "2010-11-24",
                    "price": "16.34",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 850
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 7,
                    "sale_date": "2010-11-24",
                    "price": "15.47",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 851
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 29,
                    "sale_date": "2010-11-24",
                    "price": "14.13",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 852
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 10,
                    "sale_date": "2010-11-25",
                    "price": "11.91",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 853
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 35,
                    "sale_date": "2010-11-25",
                    "price": "16.24",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 854
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 21,
                    "sale_date": "2010-11-25",
                    "price": "25.41",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 855
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 37,
                    "sale_date": "2010-11-25",
                    "price": "23.48",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 856
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 21,
                    "sale_date": "2010-11-25",
                    "price": "16.60",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 857
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 21,
                    "sale_date": "2010-11-25",
                    "price": "17.76",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 858
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 6,
                    "sale_date": "2010-11-25",
                    "price": "15.18",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 859
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 26,
                    "sale_date": "2010-11-26",
                    "price": "14.66",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 860
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 30,
                    "sale_date": "2010-11-26",
                    "price": "12.88",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 861
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 25,
                    "sale_date": "2010-11-26",
                    "price": "26.84",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 862
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 29,
                    "sale_date": "2010-11-26",
                    "price": "13.07",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 863
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 11,
                    "sale_date": "2010-11-26",
                    "price": "11.80",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 864
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 34,
                    "sale_date": "2010-11-26",
                    "price": "19.68",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 865
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 15,
                    "sale_date": "2010-11-26",
                    "price": "16.15",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 866
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 6,
                    "sale_date": "2010-11-26",
                    "price": "14.61",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 867
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 37,
                    "sale_date": "2010-11-26",
                    "price": "20.16",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 868
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 14,
                    "sale_date": "2010-11-27",
                    "price": "26.32",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 869
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 11,
                    "sale_date": "2010-11-27",
                    "price": "27.36",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 870
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 22,
                    "sale_date": "2010-11-27",
                    "price": "27.65",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 871
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 15,
                    "sale_date": "2010-11-27",
                    "price": "11.44",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 872
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 10,
                    "sale_date": "2010-11-27",
                    "price": "18.08",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 873
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 24,
                    "sale_date": "2010-11-27",
                    "price": "18.67",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 874
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 17,
                    "sale_date": "2010-11-28",
                    "price": "12.54",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 875
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 34,
                    "sale_date": "2010-11-28",
                    "price": "21.99",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 876
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 26,
                    "sale_date": "2010-11-28",
                    "price": "12.89",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 877
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 24,
                    "sale_date": "2010-11-28",
                    "price": "14.67",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 878
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 15,
                    "sale_date": "2010-11-28",
                    "price": "19.69",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 879
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 39,
                    "sale_date": "2010-11-28",
                    "price": "21.89",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 880
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 5,
                    "sale_date": "2010-11-29",
                    "price": "12.21",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 881
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 21,
                    "sale_date": "2010-11-29",
                    "price": "11.29",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 882
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 25,
                    "sale_date": "2010-11-29",
                    "price": "16.89",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 883
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 5,
                    "sale_date": "2010-11-29",
                    "price": "11.36",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 884
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 33,
                    "sale_date": "2010-11-30",
                    "price": "18.74",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 885
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 26,
                    "sale_date": "2010-11-30",
                    "price": "15.45",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 886
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 39,
                    "sale_date": "2010-11-30",
                    "price": "11.41",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 887
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 38,
                    "sale_date": "2010-11-30",
                    "price": "10.60",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 888
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 37,
                    "sale_date": "2010-11-30",
                    "price": "15.93",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 889
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 12,
                    "sale_date": "2010-12-01",
                    "price": "22.76",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 890
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 28,
                    "sale_date": "2010-12-02",
                    "price": "10.52",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 891
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 29,
                    "sale_date": "2010-12-02",
                    "price": "17.19",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 892
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 38,
                    "sale_date": "2010-12-02",
                    "price": "15.10",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 893
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 7,
                    "sale_date": "2010-12-02",
                    "price": "12.10",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 894
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 34,
                    "sale_date": "2010-12-02",
                    "price": "13.82",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 895
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 16,
                    "sale_date": "2010-12-02",
                    "price": "18.70",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 896
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 31,
                    "sale_date": "2010-12-02",
                    "price": "16.12",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 897
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 9,
                    "sale_date": "2010-12-02",
                    "price": "21.86",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 898
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 3,
                    "sale_date": "2010-12-02",
                    "price": "15.03",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 899
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 16,
                    "sale_date": "2010-12-03",
                    "price": "28.21",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 900
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 32,
                    "sale_date": "2010-12-03",
                    "price": "18.28",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 901
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 34,
                    "sale_date": "2010-12-03",
                    "price": "13.81",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 902
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 5,
                    "sale_date": "2010-12-04",
                    "price": "15.88",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 903
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 29,
                    "sale_date": "2010-12-04",
                    "price": "21.93",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 904
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 10,
                    "sale_date": "2010-12-04",
                    "price": "19.02",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 905
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 36,
                    "sale_date": "2010-12-04",
                    "price": "10.02",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 906
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 16,
                    "sale_date": "2010-12-04",
                    "price": "9.11",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 907
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 5,
                    "sale_date": "2010-12-04",
                    "price": "10.51",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 908
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 31,
                    "sale_date": "2010-12-05",
                    "price": "18.61",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 909
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 24,
                    "sale_date": "2010-12-05",
                    "price": "11.19",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 910
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 24,
                    "sale_date": "2010-12-05",
                    "price": "11.75",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 911
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 34,
                    "sale_date": "2010-12-05",
                    "price": "15.74",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 912
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 2,
                    "sale_date": "2010-12-05",
                    "price": "9.10",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 913
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 4,
                    "sale_date": "2010-12-05",
                    "price": "11.73",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 914
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 30,
                    "sale_date": "2010-12-05",
                    "price": "17.20",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 915
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 36,
                    "sale_date": "2010-12-05",
                    "price": "9.99",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 916
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 9,
                    "sale_date": "2010-12-05",
                    "price": "19.08",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 917
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 26,
                    "sale_date": "2010-12-05",
                    "price": "14.77",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 918
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 9,
                    "sale_date": "2010-12-06",
                    "price": "20.71",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 919
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 7,
                    "sale_date": "2010-12-06",
                    "price": "16.45",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 920
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 14,
                    "sale_date": "2010-12-06",
                    "price": "10.06",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 921
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 37,
                    "sale_date": "2010-12-06",
                    "price": "17.04",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 922
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 24,
                    "sale_date": "2010-12-06",
                    "price": "24.70",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 923
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 35,
                    "sale_date": "2010-12-06",
                    "price": "23.67",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 924
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 9,
                    "sale_date": "2010-12-07",
                    "price": "20.27",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 925
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 8,
                    "sale_date": "2010-12-07",
                    "price": "15.39",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 926
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 7,
                    "sale_date": "2010-12-07",
                    "price": "14.04",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 927
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 34,
                    "sale_date": "2010-12-07",
                    "price": "26.33",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 928
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 17,
                    "sale_date": "2010-12-07",
                    "price": "15.32",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 929
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 14,
                    "sale_date": "2010-12-07",
                    "price": "12.09",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 930
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 26,
                    "sale_date": "2010-12-07",
                    "price": "14.49",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 931
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 14,
                    "sale_date": "2010-12-08",
                    "price": "13.28",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 932
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 16,
                    "sale_date": "2010-12-08",
                    "price": "25.69",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 933
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 17,
                    "sale_date": "2010-12-08",
                    "price": "15.79",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 934
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 36,
                    "sale_date": "2010-12-08",
                    "price": "11.72",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 935
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 14,
                    "sale_date": "2010-12-08",
                    "price": "13.13",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 936
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 4,
                    "sale_date": "2010-12-09",
                    "price": "25.39",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 937
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 39,
                    "sale_date": "2010-12-09",
                    "price": "9.30",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 938
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 7,
                    "sale_date": "2010-12-09",
                    "price": "16.06",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 939
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 30,
                    "sale_date": "2010-12-09",
                    "price": "8.52",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 940
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 15,
                    "sale_date": "2010-12-10",
                    "price": "11.05",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 941
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 31,
                    "sale_date": "2010-12-10",
                    "price": "10.99",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 942
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 23,
                    "sale_date": "2010-12-10",
                    "price": "11.90",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 943
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 29,
                    "sale_date": "2010-12-10",
                    "price": "16.48",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 944
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 10,
                    "sale_date": "2010-12-10",
                    "price": "16.46",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 945
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 32,
                    "sale_date": "2010-12-10",
                    "price": "15.04",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 946
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 8,
                    "sale_date": "2010-12-10",
                    "price": "10.12",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 947
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 26,
                    "sale_date": "2010-12-10",
                    "price": "12.81",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 948
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 20,
                    "sale_date": "2010-12-11",
                    "price": "12.64",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 949
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 35,
                    "sale_date": "2010-12-11",
                    "price": "21.66",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 950
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 39,
                    "sale_date": "2010-12-11",
                    "price": "22.58",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 951
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 33,
                    "sale_date": "2010-12-11",
                    "price": "11.51",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 952
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 9,
                    "sale_date": "2010-12-11",
                    "price": "17.35",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 953
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 16,
                    "sale_date": "2010-12-12",
                    "price": "17.03",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 954
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 12,
                    "sale_date": "2010-12-12",
                    "price": "26.43",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 955
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 30,
                    "sale_date": "2010-12-12",
                    "price": "15.53",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 956
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 18,
                    "sale_date": "2010-12-12",
                    "price": "20.38",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 957
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 29,
                    "sale_date": "2010-12-12",
                    "price": "14.50",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 958
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 17,
                    "sale_date": "2010-12-12",
                    "price": "16.30",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 959
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 29,
                    "sale_date": "2010-12-12",
                    "price": "15.19",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 960
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 15,
                    "sale_date": "2010-12-12",
                    "price": "13.09",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 961
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 10,
                    "sale_date": "2010-12-12",
                    "price": "23.53",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 962
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 24,
                    "sale_date": "2010-12-12",
                    "price": "30.71",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 963
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 11,
                    "sale_date": "2010-12-13",
                    "price": "25.87",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 964
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 23,
                    "sale_date": "2010-12-13",
                    "price": "13.02",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 965
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 25,
                    "sale_date": "2010-12-13",
                    "price": "12.70",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 966
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 34,
                    "sale_date": "2010-12-13",
                    "price": "15.23",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 967
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 1,
                    "sale_date": "2010-12-13",
                    "price": "26.98",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 968
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 8,
                    "sale_date": "2010-12-13",
                    "price": "12.86",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 969
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 32,
                    "sale_date": "2010-12-13",
                    "price": "14.87",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 970
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 10,
                    "sale_date": "2010-12-14",
                    "price": "9.09",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 971
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 33,
                    "sale_date": "2010-12-14",
                    "price": "17.64",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 972
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 24,
                    "sale_date": "2010-12-14",
                    "price": "14.05",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 973
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 31,
                    "sale_date": "2010-12-14",
                    "price": "13.35",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 974
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 30,
                    "sale_date": "2010-12-14",
                    "price": "15.15",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 975
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 19,
                    "sale_date": "2010-12-14",
                    "price": "15.50",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 976
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 14,
                    "sale_date": "2010-12-14",
                    "price": "25.46",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 977
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 28,
                    "sale_date": "2010-12-14",
                    "price": "19.98",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 978
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 20,
                    "sale_date": "2010-12-14",
                    "price": "10.39",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 979
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 15,
                    "sale_date": "2010-12-15",
                    "price": "18.70",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 980
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 7,
                    "sale_date": "2010-12-15",
                    "price": "18.56",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 981
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 15,
                    "sale_date": "2010-12-15",
                    "price": "13.75",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 982
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 9,
                    "sale_date": "2010-12-15",
                    "price": "12.02",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 983
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 16,
                    "sale_date": "2010-12-15",
                    "price": "18.69",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 984
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 23,
                    "sale_date": "2010-12-16",
                    "price": "11.67",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 985
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 7,
                    "sale_date": "2010-12-16",
                    "price": "16.07",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 986
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 24,
                    "sale_date": "2010-12-16",
                    "price": "23.77",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 987
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 9,
                    "sale_date": "2010-12-16",
                    "price": "17.17",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 988
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 2,
                    "sale_date": "2010-12-16",
                    "price": "19.00",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 989
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 12,
                    "sale_date": "2010-12-17",
                    "price": "20.73",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 990
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 1,
                    "sale_date": "2010-12-17",
                    "price": "13.08",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 991
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 1,
                    "sale_date": "2010-12-17",
                    "price": "17.12",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 992
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 4,
                    "sale_date": "2010-12-17",
                    "price": "15.29",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 993
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 15,
                    "sale_date": "2010-12-17",
                    "price": "14.88",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 994
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 36,
                    "sale_date": "2010-12-17",
                    "price": "11.25",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 995
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 12,
                    "sale_date": "2010-12-17",
                    "price": "13.76",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 996
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 7,
                    "sale_date": "2010-12-17",
                    "price": "16.82",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 997
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 17,
                    "sale_date": "2010-12-17",
                    "price": "14.36",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 998
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 36,
                    "sale_date": "2010-12-17",
                    "price": "24.00",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 999
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 14,
                    "sale_date": "2010-12-17",
                    "price": "29.50",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 1000
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 14,
                    "sale_date": "2010-12-17",
                    "price": "14.17",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 1001
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 38,
                    "sale_date": "2010-12-17",
                    "price": "12.00",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1002
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 2,
                    "sale_date": "2010-12-18",
                    "price": "20.32",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1003
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 22,
                    "sale_date": "2010-12-18",
                    "price": "11.84",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1004
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 19,
                    "sale_date": "2010-12-19",
                    "price": "21.33",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 1005
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 10,
                    "sale_date": "2010-12-20",
                    "price": "14.04",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 1006
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 22,
                    "sale_date": "2010-12-20",
                    "price": "14.99",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1007
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 3,
                    "sale_date": "2010-12-20",
                    "price": "12.84",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 1008
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 2,
                    "sale_date": "2010-12-20",
                    "price": "12.70",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1009
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 1,
                    "sale_date": "2010-12-20",
                    "price": "9.51",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 1010
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 4,
                    "sale_date": "2010-12-20",
                    "price": "11.25",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1011
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 36,
                    "sale_date": "2010-12-20",
                    "price": "9.93",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 1012
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 25,
                    "sale_date": "2010-12-20",
                    "price": "20.55",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 1013
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 1,
                    "sale_date": "2010-12-20",
                    "price": "13.61",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1014
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 35,
                    "sale_date": "2010-12-20",
                    "price": "13.39",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1015
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 1,
                    "sale_date": "2010-12-20",
                    "price": "13.36",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1016
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 16,
                    "sale_date": "2010-12-20",
                    "price": "14.48",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 1017
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 29,
                    "sale_date": "2010-12-20",
                    "price": "13.94",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 1018
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 37,
                    "sale_date": "2010-12-20",
                    "price": "13.94",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1019
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 33,
                    "sale_date": "2010-12-21",
                    "price": "19.78",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1020
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 5,
                    "sale_date": "2010-12-21",
                    "price": "16.59",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 1021
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 11,
                    "sale_date": "2010-12-21",
                    "price": "28.55",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1022
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 33,
                    "sale_date": "2010-12-21",
                    "price": "9.35",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1023
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 3,
                    "sale_date": "2010-12-21",
                    "price": "13.83",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1024
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 2,
                    "sale_date": "2010-12-21",
                    "price": "11.39",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1025
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 13,
                    "sale_date": "2010-12-21",
                    "price": "19.51",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 1026
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 3,
                    "sale_date": "2010-12-22",
                    "price": "10.08",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 1027
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 15,
                    "sale_date": "2010-12-22",
                    "price": "22.53",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 1028
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 20,
                    "sale_date": "2010-12-22",
                    "price": "10.15",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1029
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 38,
                    "sale_date": "2010-12-22",
                    "price": "13.85",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 1030
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 1,
                    "sale_date": "2010-12-22",
                    "price": "14.58",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1031
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 36,
                    "sale_date": "2010-12-22",
                    "price": "16.17",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1032
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 25,
                    "sale_date": "2010-12-22",
                    "price": "19.52",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 1033
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 17,
                    "sale_date": "2010-12-23",
                    "price": "19.86",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 1034
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 12,
                    "sale_date": "2010-12-23",
                    "price": "24.94",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1035
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 5,
                    "sale_date": "2010-12-23",
                    "price": "11.03",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1036
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 27,
                    "sale_date": "2010-12-23",
                    "price": "14.37",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1037
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 15,
                    "sale_date": "2010-12-23",
                    "price": "12.32",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1038
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 36,
                    "sale_date": "2010-12-23",
                    "price": "26.29",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1039
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 20,
                    "sale_date": "2010-12-24",
                    "price": "13.50",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1040
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 1,
                    "sale_date": "2010-12-24",
                    "price": "15.91",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1041
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 12,
                    "sale_date": "2010-12-24",
                    "price": "20.70",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1042
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 11,
                    "sale_date": "2010-12-24",
                    "price": "15.82",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 1043
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 7,
                    "sale_date": "2010-12-24",
                    "price": "26.36",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 1044
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 10,
                    "sale_date": "2010-12-24",
                    "price": "23.18",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1045
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 39,
                    "sale_date": "2010-12-24",
                    "price": "12.68",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1046
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 8,
                    "sale_date": "2010-12-24",
                    "price": "10.76",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1047
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 23,
                    "sale_date": "2010-12-25",
                    "price": "14.59",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 1048
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 14,
                    "sale_date": "2010-12-25",
                    "price": "16.24",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1049
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 12,
                    "sale_date": "2010-12-25",
                    "price": "10.80",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1050
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 23,
                    "sale_date": "2010-12-25",
                    "price": "15.34",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 1051
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 4,
                    "sale_date": "2010-12-25",
                    "price": "12.89",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 1052
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 10,
                    "sale_date": "2010-12-25",
                    "price": "10.18",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 1053
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 11,
                    "sale_date": "2010-12-26",
                    "price": "24.50",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1054
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 38,
                    "sale_date": "2010-12-27",
                    "price": "14.40",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1055
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 36,
                    "sale_date": "2010-12-27",
                    "price": "12.93",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1056
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 6,
                    "sale_date": "2010-12-27",
                    "price": "9.23",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1057
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 1,
                    "sale_date": "2010-12-27",
                    "price": "16.35",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1058
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 8,
                    "sale_date": "2010-12-27",
                    "price": "10.96",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1059
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 14,
                    "sale_date": "2010-12-28",
                    "price": "26.87",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 1060
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 38,
                    "sale_date": "2010-12-28",
                    "price": "13.27",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 1061
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 37,
                    "sale_date": "2010-12-28",
                    "price": "14.75",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1062
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 39,
                    "sale_date": "2010-12-28",
                    "price": "18.18",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1063
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 8,
                    "sale_date": "2010-12-28",
                    "price": "14.70",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1064
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 22,
                    "sale_date": "2010-12-28",
                    "price": "26.89",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1065
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 22,
                    "sale_date": "2010-12-28",
                    "price": "12.05",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 1066
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 6,
                    "sale_date": "2010-12-28",
                    "price": "12.23",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1067
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 9,
                    "sale_date": "2010-12-29",
                    "price": "16.29",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1068
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 10,
                    "sale_date": "2010-12-29",
                    "price": "12.52",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 1069
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 35,
                    "sale_date": "2010-12-29",
                    "price": "14.23",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1070
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 27,
                    "sale_date": "2010-12-29",
                    "price": "11.29",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1071
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 3,
                    "sale_date": "2010-12-29",
                    "price": "18.48",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 1072
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 38,
                    "sale_date": "2010-12-30",
                    "price": "12.56",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1073
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 10,
                    "sale_date": "2010-12-30",
                    "price": "11.31",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 1074
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 30,
                    "sale_date": "2010-12-30",
                    "price": "27.43",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1075
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 6,
                    "sale_date": "2010-12-30",
                    "price": "11.04",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 1076
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 24,
                    "sale_date": "2010-12-30",
                    "price": "18.35",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1077
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 39,
                    "sale_date": "2010-12-30",
                    "price": "18.25",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 1078
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 10,
                    "sale_date": "2010-12-30",
                    "price": "11.20",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1079
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 35,
                    "sale_date": "2010-12-30",
                    "price": "15.34",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1080
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 18,
                    "sale_date": "2010-12-31",
                    "price": "19.83",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 1081
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 14,
                    "sale_date": "2010-12-31",
                    "price": "12.56",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 1082
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 39,
                    "sale_date": "2010-12-31",
                    "price": "26.59",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1083
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 3,
                    "sale_date": "2010-12-31",
                    "price": "9.54",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1084
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 24,
                    "sale_date": "2010-12-31",
                    "price": "11.69",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 1085
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 2,
                    "sale_date": "2011-01-01",
                    "price": "13.90",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1086
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 39,
                    "sale_date": "2011-01-01",
                    "price": "9.80",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1087
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 26,
                    "sale_date": "2011-01-01",
                    "price": "29.89",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 1088
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 13,
                    "sale_date": "2011-01-01",
                    "price": "19.51",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 1089
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 33,
                    "sale_date": "2011-01-01",
                    "price": "21.74",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1090
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 4,
                    "sale_date": "2011-01-02",
                    "price": "13.09",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1091
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 18,
                    "sale_date": "2011-01-02",
                    "price": "27.74",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1092
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 32,
                    "sale_date": "2011-01-02",
                    "price": "22.75",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1093
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 13,
                    "sale_date": "2011-01-02",
                    "price": "13.15",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 1094
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 21,
                    "sale_date": "2011-01-02",
                    "price": "13.33",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1095
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 10,
                    "sale_date": "2011-01-02",
                    "price": "11.77",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 1096
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 15,
                    "sale_date": "2011-01-02",
                    "price": "30.40",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1097
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 25,
                    "sale_date": "2011-01-02",
                    "price": "21.77",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1098
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 10,
                    "sale_date": "2011-01-03",
                    "price": "11.29",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 1099
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 11,
                    "sale_date": "2011-01-03",
                    "price": "20.91",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 1100
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 17,
                    "sale_date": "2011-01-03",
                    "price": "12.05",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 1101
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 8,
                    "sale_date": "2011-01-03",
                    "price": "12.88",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 1102
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 10,
                    "sale_date": "2011-01-03",
                    "price": "13.04",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1103
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 34,
                    "sale_date": "2011-01-03",
                    "price": "19.73",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 1104
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 1,
                    "sale_date": "2011-01-03",
                    "price": "10.32",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 1105
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 34,
                    "sale_date": "2011-01-04",
                    "price": "12.93",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 1106
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 20,
                    "sale_date": "2011-01-04",
                    "price": "19.92",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1107
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 1,
                    "sale_date": "2011-01-04",
                    "price": "18.18",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1108
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 17,
                    "sale_date": "2011-01-04",
                    "price": "11.37",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1109
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 29,
                    "sale_date": "2011-01-05",
                    "price": "21.54",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 1110
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 15,
                    "sale_date": "2011-01-05",
                    "price": "30.45",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1111
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 20,
                    "sale_date": "2011-01-05",
                    "price": "18.51",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1112
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 5,
                    "sale_date": "2011-01-05",
                    "price": "11.21",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1113
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 35,
                    "sale_date": "2011-01-05",
                    "price": "17.07",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1114
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 8,
                    "sale_date": "2011-01-05",
                    "price": "16.53",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 1115
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 39,
                    "sale_date": "2011-01-05",
                    "price": "15.95",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 1116
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 39,
                    "sale_date": "2011-01-06",
                    "price": "15.92",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1117
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 10,
                    "sale_date": "2011-01-06",
                    "price": "19.61",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 1118
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 22,
                    "sale_date": "2011-01-06",
                    "price": "30.64",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1119
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 18,
                    "sale_date": "2011-01-06",
                    "price": "14.36",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1120
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 2,
                    "sale_date": "2011-01-06",
                    "price": "28.44",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1121
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 7,
                    "sale_date": "2011-01-07",
                    "price": "15.11",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1122
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 21,
                    "sale_date": "2011-01-07",
                    "price": "27.00",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 1123
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 3,
                    "sale_date": "2011-01-07",
                    "price": "14.23",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1124
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 29,
                    "sale_date": "2011-01-07",
                    "price": "25.79",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1125
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 28,
                    "sale_date": "2011-01-08",
                    "price": "11.84",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 1126
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 21,
                    "sale_date": "2011-01-08",
                    "price": "13.23",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 1127
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 38,
                    "sale_date": "2011-01-08",
                    "price": "10.93",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 1128
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 21,
                    "sale_date": "2011-01-08",
                    "price": "12.06",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 1129
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 6,
                    "sale_date": "2011-01-08",
                    "price": "20.91",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1130
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 20,
                    "sale_date": "2011-01-08",
                    "price": "16.45",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 1131
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 17,
                    "sale_date": "2011-01-08",
                    "price": "14.92",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 1132
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 26,
                    "sale_date": "2011-01-08",
                    "price": "12.02",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1133
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 24,
                    "sale_date": "2011-01-09",
                    "price": "19.82",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1134
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 26,
                    "sale_date": "2011-01-09",
                    "price": "22.03",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 1135
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 3,
                    "sale_date": "2011-01-09",
                    "price": "13.58",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1136
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 11,
                    "sale_date": "2011-01-09",
                    "price": "11.36",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 1137
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 18,
                    "sale_date": "2011-01-09",
                    "price": "17.53",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1138
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 4,
                    "sale_date": "2011-01-09",
                    "price": "26.68",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1139
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 34,
                    "sale_date": "2011-01-09",
                    "price": "12.43",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 1140
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 22,
                    "sale_date": "2011-01-10",
                    "price": "17.20",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1141
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 19,
                    "sale_date": "2011-01-10",
                    "price": "16.00",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1142
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 21,
                    "sale_date": "2011-01-10",
                    "price": "18.13",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1143
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 19,
                    "sale_date": "2011-01-10",
                    "price": "11.09",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1144
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 21,
                    "sale_date": "2011-01-10",
                    "price": "11.97",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1145
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 30,
                    "sale_date": "2011-01-10",
                    "price": "20.93",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1146
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 21,
                    "sale_date": "2011-01-11",
                    "price": "14.84",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 1147
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 32,
                    "sale_date": "2011-01-11",
                    "price": "13.59",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1148
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 9,
                    "sale_date": "2011-01-12",
                    "price": "15.44",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 1149
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 29,
                    "sale_date": "2011-01-12",
                    "price": "12.29",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1150
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 15,
                    "sale_date": "2011-01-12",
                    "price": "11.81",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1151
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 12,
                    "sale_date": "2011-01-12",
                    "price": "12.42",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 1152
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 23,
                    "sale_date": "2011-01-12",
                    "price": "13.44",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1153
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 21,
                    "sale_date": "2011-01-12",
                    "price": "14.57",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1154
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 19,
                    "sale_date": "2011-01-13",
                    "price": "16.67",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 1155
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 11,
                    "sale_date": "2011-01-13",
                    "price": "24.36",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1156
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 23,
                    "sale_date": "2011-01-13",
                    "price": "20.16",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1157
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 22,
                    "sale_date": "2011-01-14",
                    "price": "24.75",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1158
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 27,
                    "sale_date": "2011-01-14",
                    "price": "15.65",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1159
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 8,
                    "sale_date": "2011-01-14",
                    "price": "23.53",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 1160
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 9,
                    "sale_date": "2011-01-15",
                    "price": "21.45",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1161
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 9,
                    "sale_date": "2011-01-15",
                    "price": "9.87",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1162
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 33,
                    "sale_date": "2011-01-15",
                    "price": "10.78",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1163
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 9,
                    "sale_date": "2011-01-15",
                    "price": "12.18",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1164
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 15,
                    "sale_date": "2011-01-15",
                    "price": "10.64",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1165
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 36,
                    "sale_date": "2011-01-15",
                    "price": "10.99",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 1166
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 18,
                    "sale_date": "2011-01-15",
                    "price": "14.52",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 1167
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 18,
                    "sale_date": "2011-01-16",
                    "price": "10.56",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 1168
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 9,
                    "sale_date": "2011-01-16",
                    "price": "15.12",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1169
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 38,
                    "sale_date": "2011-01-16",
                    "price": "12.33",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1170
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 21,
                    "sale_date": "2011-01-16",
                    "price": "11.89",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1171
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 22,
                    "sale_date": "2011-01-16",
                    "price": "12.72",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1172
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 30,
                    "sale_date": "2011-01-16",
                    "price": "17.56",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1173
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 32,
                    "sale_date": "2011-01-16",
                    "price": "14.46",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 1174
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 25,
                    "sale_date": "2011-01-16",
                    "price": "15.34",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 1175
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 22,
                    "sale_date": "2011-01-16",
                    "price": "13.56",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1176
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 31,
                    "sale_date": "2011-01-16",
                    "price": "24.90",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1177
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 34,
                    "sale_date": "2011-01-17",
                    "price": "22.18",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1178
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 10,
                    "sale_date": "2011-01-17",
                    "price": "20.94",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1179
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 21,
                    "sale_date": "2011-01-17",
                    "price": "10.73",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 1180
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 29,
                    "sale_date": "2011-01-17",
                    "price": "13.19",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1181
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 26,
                    "sale_date": "2011-01-17",
                    "price": "16.03",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 1182
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 38,
                    "sale_date": "2011-01-17",
                    "price": "15.61",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1183
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 31,
                    "sale_date": "2011-01-17",
                    "price": "12.69",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 1184
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 17,
                    "sale_date": "2011-01-17",
                    "price": "13.25",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 1185
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 31,
                    "sale_date": "2011-01-17",
                    "price": "15.96",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 1186
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 21,
                    "sale_date": "2011-01-18",
                    "price": "16.06",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1187
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 8,
                    "sale_date": "2011-01-18",
                    "price": "9.65",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1188
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 7,
                    "sale_date": "2011-01-18",
                    "price": "26.44",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1189
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 28,
                    "sale_date": "2011-01-19",
                    "price": "10.92",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 1190
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 4,
                    "sale_date": "2011-01-19",
                    "price": "17.93",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1191
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 14,
                    "sale_date": "2011-01-19",
                    "price": "19.88",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1192
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 37,
                    "sale_date": "2011-01-19",
                    "price": "15.17",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 1193
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 36,
                    "sale_date": "2011-01-20",
                    "price": "16.75",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1194
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 31,
                    "sale_date": "2011-01-20",
                    "price": "27.27",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 1195
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 36,
                    "sale_date": "2011-01-20",
                    "price": "16.28",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 1196
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 16,
                    "sale_date": "2011-01-20",
                    "price": "25.40",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1197
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 23,
                    "sale_date": "2011-01-20",
                    "price": "7.21",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1198
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 18,
                    "sale_date": "2011-01-20",
                    "price": "15.86",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1199
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 10,
                    "sale_date": "2011-01-20",
                    "price": "15.51",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 1200
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 28,
                    "sale_date": "2011-01-21",
                    "price": "20.11",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 1201
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 11,
                    "sale_date": "2011-01-21",
                    "price": "11.42",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 1202
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 32,
                    "sale_date": "2011-01-21",
                    "price": "9.14",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1203
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 5,
                    "sale_date": "2011-01-21",
                    "price": "14.57",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 1204
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 33,
                    "sale_date": "2011-01-21",
                    "price": "19.06",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1205
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 7,
                    "sale_date": "2011-01-22",
                    "price": "13.37",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 1206
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 18,
                    "sale_date": "2011-01-22",
                    "price": "14.97",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1207
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 37,
                    "sale_date": "2011-01-22",
                    "price": "20.10",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1208
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 11,
                    "sale_date": "2011-01-23",
                    "price": "14.36",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 1209
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 20,
                    "sale_date": "2011-01-23",
                    "price": "22.96",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 1210
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 25,
                    "sale_date": "2011-01-23",
                    "price": "15.83",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1211
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 14,
                    "sale_date": "2011-01-23",
                    "price": "16.21",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 1212
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 15,
                    "sale_date": "2011-01-23",
                    "price": "21.04",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 1213
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 17,
                    "sale_date": "2011-01-24",
                    "price": "12.88",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 1214
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 16,
                    "sale_date": "2011-01-24",
                    "price": "18.44",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1215
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 24,
                    "sale_date": "2011-01-24",
                    "price": "10.37",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1216
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 10,
                    "sale_date": "2011-01-24",
                    "price": "22.04",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 1217
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 28,
                    "sale_date": "2011-01-24",
                    "price": "15.84",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1218
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 29,
                    "sale_date": "2011-01-25",
                    "price": "14.84",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1219
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 37,
                    "sale_date": "2011-01-26",
                    "price": "15.01",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1220
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 15,
                    "sale_date": "2011-01-26",
                    "price": "10.24",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 1221
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 39,
                    "sale_date": "2011-01-26",
                    "price": "10.28",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1222
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 22,
                    "sale_date": "2011-01-26",
                    "price": "12.41",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1223
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 25,
                    "sale_date": "2011-01-27",
                    "price": "27.46",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1224
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 1,
                    "sale_date": "2011-01-27",
                    "price": "28.65",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1225
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 13,
                    "sale_date": "2011-01-27",
                    "price": "13.98",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1226
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 27,
                    "sale_date": "2011-01-28",
                    "price": "21.96",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 1227
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 20,
                    "sale_date": "2011-01-28",
                    "price": "18.03",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1228
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 18,
                    "sale_date": "2011-01-28",
                    "price": "16.22",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1229
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 1,
                    "sale_date": "2011-01-29",
                    "price": "13.01",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 1230
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 3,
                    "sale_date": "2011-01-29",
                    "price": "25.22",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 1231
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 30,
                    "sale_date": "2011-01-29",
                    "price": "19.08",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 1232
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 34,
                    "sale_date": "2011-01-30",
                    "price": "13.95",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1233
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 18,
                    "sale_date": "2011-01-30",
                    "price": "10.67",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1234
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 15,
                    "sale_date": "2011-01-30",
                    "price": "13.68",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1235
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 19,
                    "sale_date": "2011-01-30",
                    "price": "12.43",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1236
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 38,
                    "sale_date": "2011-01-31",
                    "price": "15.62",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1237
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 10,
                    "sale_date": "2011-01-31",
                    "price": "18.96",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1238
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 18,
                    "sale_date": "2011-01-31",
                    "price": "17.01",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 1239
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 36,
                    "sale_date": "2011-01-31",
                    "price": "16.66",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 1240
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 19,
                    "sale_date": "2011-01-31",
                    "price": "16.09",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1241
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 9,
                    "sale_date": "2011-02-01",
                    "price": "18.35",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1242
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 8,
                    "sale_date": "2011-02-02",
                    "price": "15.80",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 1243
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 14,
                    "sale_date": "2011-02-02",
                    "price": "11.74",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1244
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 6,
                    "sale_date": "2011-02-02",
                    "price": "15.35",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1245
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 22,
                    "sale_date": "2011-02-03",
                    "price": "11.14",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1246
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 17,
                    "sale_date": "2011-02-03",
                    "price": "14.20",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1247
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 1,
                    "sale_date": "2011-02-03",
                    "price": "11.06",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1248
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 32,
                    "sale_date": "2011-02-03",
                    "price": "17.15",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1249
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 15,
                    "sale_date": "2011-02-04",
                    "price": "12.16",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1250
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 36,
                    "sale_date": "2011-02-04",
                    "price": "16.04",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 1251
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 8,
                    "sale_date": "2011-02-04",
                    "price": "12.64",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 1252
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 24,
                    "sale_date": "2011-02-04",
                    "price": "12.65",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1253
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 15,
                    "sale_date": "2011-02-04",
                    "price": "14.91",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1254
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 14,
                    "sale_date": "2011-02-04",
                    "price": "27.10",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1255
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 30,
                    "sale_date": "2011-02-04",
                    "price": "12.20",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1256
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 17,
                    "sale_date": "2011-02-04",
                    "price": "14.58",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 1257
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 11,
                    "sale_date": "2011-02-04",
                    "price": "10.01",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 1258
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 20,
                    "sale_date": "2011-02-05",
                    "price": "16.15",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1259
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 18,
                    "sale_date": "2011-02-05",
                    "price": "11.41",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1260
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 17,
                    "sale_date": "2011-02-05",
                    "price": "16.68",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 1261
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 23,
                    "sale_date": "2011-02-05",
                    "price": "10.57",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 1262
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 13,
                    "sale_date": "2011-02-05",
                    "price": "13.55",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1263
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 26,
                    "sale_date": "2011-02-06",
                    "price": "14.53",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1264
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 34,
                    "sale_date": "2011-02-06",
                    "price": "15.84",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1265
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 26,
                    "sale_date": "2011-02-07",
                    "price": "14.34",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 1266
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 17,
                    "sale_date": "2011-02-07",
                    "price": "13.72",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1267
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 4,
                    "sale_date": "2011-02-07",
                    "price": "21.17",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 1268
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 31,
                    "sale_date": "2011-02-07",
                    "price": "18.89",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1269
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 26,
                    "sale_date": "2011-02-07",
                    "price": "26.33",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1270
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 17,
                    "sale_date": "2011-02-07",
                    "price": "19.03",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1271
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 6,
                    "sale_date": "2011-02-07",
                    "price": "9.35",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 1272
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 35,
                    "sale_date": "2011-02-07",
                    "price": "11.79",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 1273
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 39,
                    "sale_date": "2011-02-08",
                    "price": "14.38",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 1274
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 33,
                    "sale_date": "2011-02-08",
                    "price": "14.41",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1275
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 13,
                    "sale_date": "2011-02-09",
                    "price": "14.06",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1276
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 33,
                    "sale_date": "2011-02-09",
                    "price": "15.79",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 1277
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 30,
                    "sale_date": "2011-02-09",
                    "price": "13.22",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1278
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 28,
                    "sale_date": "2011-02-10",
                    "price": "22.11",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1279
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 24,
                    "sale_date": "2011-02-10",
                    "price": "18.62",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1280
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 2,
                    "sale_date": "2011-02-10",
                    "price": "15.36",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1281
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 32,
                    "sale_date": "2011-02-10",
                    "price": "12.37",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1282
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 19,
                    "sale_date": "2011-02-10",
                    "price": "21.34",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1283
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 37,
                    "sale_date": "2011-02-10",
                    "price": "13.27",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 1284
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 27,
                    "sale_date": "2011-02-10",
                    "price": "11.07",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 1285
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 29,
                    "sale_date": "2011-02-11",
                    "price": "14.66",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 1286
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 16,
                    "sale_date": "2011-02-11",
                    "price": "19.48",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 1287
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 33,
                    "sale_date": "2011-02-11",
                    "price": "12.71",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 1288
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 25,
                    "sale_date": "2011-02-11",
                    "price": "13.01",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1289
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 26,
                    "sale_date": "2011-02-11",
                    "price": "13.36",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1290
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 33,
                    "sale_date": "2011-02-11",
                    "price": "15.94",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1291
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 25,
                    "sale_date": "2011-02-11",
                    "price": "16.11",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1292
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 9,
                    "sale_date": "2011-02-11",
                    "price": "15.16",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1293
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 35,
                    "sale_date": "2011-02-11",
                    "price": "14.14",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1294
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 1,
                    "sale_date": "2011-02-12",
                    "price": "18.69",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 1295
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 37,
                    "sale_date": "2011-02-12",
                    "price": "22.04",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1296
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 35,
                    "sale_date": "2011-02-12",
                    "price": "18.80",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1297
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 35,
                    "sale_date": "2011-02-13",
                    "price": "14.65",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1298
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 4,
                    "sale_date": "2011-02-13",
                    "price": "11.93",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1299
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 16,
                    "sale_date": "2011-02-13",
                    "price": "13.72",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1300
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 2,
                    "sale_date": "2011-02-13",
                    "price": "12.94",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 1301
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 35,
                    "sale_date": "2011-02-13",
                    "price": "17.66",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1302
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 27,
                    "sale_date": "2011-02-13",
                    "price": "24.46",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1303
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 32,
                    "sale_date": "2011-02-13",
                    "price": "17.32",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1304
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 17,
                    "sale_date": "2011-02-13",
                    "price": "14.46",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1305
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 36,
                    "sale_date": "2011-02-13",
                    "price": "15.95",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 1306
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 35,
                    "sale_date": "2011-02-14",
                    "price": "12.08",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 1307
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 37,
                    "sale_date": "2011-02-14",
                    "price": "30.34",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1308
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 23,
                    "sale_date": "2011-02-14",
                    "price": "16.67",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 1309
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 5,
                    "sale_date": "2011-02-15",
                    "price": "13.79",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1310
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 5,
                    "sale_date": "2011-02-15",
                    "price": "13.46",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 1311
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 39,
                    "sale_date": "2011-02-15",
                    "price": "8.72",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 1312
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 34,
                    "sale_date": "2011-02-15",
                    "price": "16.06",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1313
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 27,
                    "sale_date": "2011-02-16",
                    "price": "18.00",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 1314
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 19,
                    "sale_date": "2011-02-16",
                    "price": "11.99",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1315
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 12,
                    "sale_date": "2011-02-16",
                    "price": "17.15",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1316
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 38,
                    "sale_date": "2011-02-16",
                    "price": "25.26",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1317
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 23,
                    "sale_date": "2011-02-17",
                    "price": "14.91",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1318
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 5,
                    "sale_date": "2011-02-17",
                    "price": "9.63",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 1319
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 6,
                    "sale_date": "2011-02-17",
                    "price": "22.48",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1320
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 22,
                    "sale_date": "2011-02-18",
                    "price": "17.50",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 1321
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 7,
                    "sale_date": "2011-02-18",
                    "price": "10.08",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 1322
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 10,
                    "sale_date": "2011-02-18",
                    "price": "13.43",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1323
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 31,
                    "sale_date": "2011-02-18",
                    "price": "21.27",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1324
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 20,
                    "sale_date": "2011-02-19",
                    "price": "13.64",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1325
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 32,
                    "sale_date": "2011-02-19",
                    "price": "18.62",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1326
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 20,
                    "sale_date": "2011-02-19",
                    "price": "14.45",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1327
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 22,
                    "sale_date": "2011-02-20",
                    "price": "26.49",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1328
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 7,
                    "sale_date": "2011-02-20",
                    "price": "17.18",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 1329
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 25,
                    "sale_date": "2011-02-20",
                    "price": "15.77",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1330
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 33,
                    "sale_date": "2011-02-20",
                    "price": "22.92",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1331
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 2,
                    "sale_date": "2011-02-20",
                    "price": "19.16",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1332
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 15,
                    "sale_date": "2011-02-20",
                    "price": "25.29",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 1333
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 16,
                    "sale_date": "2011-02-20",
                    "price": "16.89",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 1334
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 21,
                    "sale_date": "2011-02-20",
                    "price": "14.00",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 1335
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 1,
                    "sale_date": "2011-02-21",
                    "price": "14.76",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 1336
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 34,
                    "sale_date": "2011-02-21",
                    "price": "11.74",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1337
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 29,
                    "sale_date": "2011-02-21",
                    "price": "12.59",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 1338
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 17,
                    "sale_date": "2011-02-21",
                    "price": "13.49",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 1339
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 36,
                    "sale_date": "2011-02-21",
                    "price": "13.97",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1340
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 39,
                    "sale_date": "2011-02-21",
                    "price": "22.18",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1341
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 12,
                    "sale_date": "2011-02-21",
                    "price": "25.58",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 1342
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 2,
                    "sale_date": "2011-02-21",
                    "price": "13.83",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1343
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 29,
                    "sale_date": "2011-02-21",
                    "price": "13.66",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1344
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 30,
                    "sale_date": "2011-02-22",
                    "price": "15.90",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1345
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 14,
                    "sale_date": "2011-02-22",
                    "price": "16.85",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 1346
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 26,
                    "sale_date": "2011-02-22",
                    "price": "16.74",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1347
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 17,
                    "sale_date": "2011-02-22",
                    "price": "15.83",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1348
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 39,
                    "sale_date": "2011-02-22",
                    "price": "21.08",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1349
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 5,
                    "sale_date": "2011-02-22",
                    "price": "11.26",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 1350
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 6,
                    "sale_date": "2011-02-22",
                    "price": "17.35",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1351
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 4,
                    "sale_date": "2011-02-23",
                    "price": "15.33",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1352
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 1,
                    "sale_date": "2011-02-23",
                    "price": "14.33",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1353
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 36,
                    "sale_date": "2011-02-23",
                    "price": "13.56",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1354
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 30,
                    "sale_date": "2011-02-23",
                    "price": "10.80",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 1355
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 36,
                    "sale_date": "2011-02-23",
                    "price": "16.17",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1356
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 2,
                    "sale_date": "2011-02-23",
                    "price": "13.44",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 1357
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 3,
                    "sale_date": "2011-02-23",
                    "price": "26.86",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1358
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 1,
                    "sale_date": "2011-02-23",
                    "price": "11.02",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1359
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 18,
                    "sale_date": "2011-02-23",
                    "price": "17.14",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1360
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 16,
                    "sale_date": "2011-02-24",
                    "price": "16.29",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1361
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 29,
                    "sale_date": "2011-02-24",
                    "price": "20.89",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 1362
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 16,
                    "sale_date": "2011-02-24",
                    "price": "29.40",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 1363
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 12,
                    "sale_date": "2011-02-24",
                    "price": "13.83",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 1364
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 19,
                    "sale_date": "2011-02-24",
                    "price": "12.99",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1365
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 24,
                    "sale_date": "2011-02-24",
                    "price": "25.31",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 1366
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 4,
                    "sale_date": "2011-02-25",
                    "price": "25.86",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1367
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 19,
                    "sale_date": "2011-02-25",
                    "price": "14.84",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 1368
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 23,
                    "sale_date": "2011-02-25",
                    "price": "12.35",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 1369
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 11,
                    "sale_date": "2011-02-25",
                    "price": "27.26",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1370
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 24,
                    "sale_date": "2011-02-26",
                    "price": "27.99",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1371
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 4,
                    "sale_date": "2011-02-26",
                    "price": "13.13",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 1372
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 10,
                    "sale_date": "2011-02-26",
                    "price": "24.17",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1373
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 19,
                    "sale_date": "2011-02-26",
                    "price": "29.23",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1374
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 27,
                    "sale_date": "2011-02-26",
                    "price": "26.59",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 1375
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 26,
                    "sale_date": "2011-02-27",
                    "price": "15.73",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1376
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 33,
                    "sale_date": "2011-02-27",
                    "price": "14.71",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1377
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 37,
                    "sale_date": "2011-02-27",
                    "price": "20.91",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 1378
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 14,
                    "sale_date": "2011-02-28",
                    "price": "11.72",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1379
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 10,
                    "sale_date": "2011-02-28",
                    "price": "13.31",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1380
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 16,
                    "sale_date": "2011-02-28",
                    "price": "19.61",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1381
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 35,
                    "sale_date": "2011-02-28",
                    "price": "16.09",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 1382
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 12,
                    "sale_date": "2011-02-28",
                    "price": "13.86",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1383
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 21,
                    "sale_date": "2011-03-01",
                    "price": "11.57",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1384
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 12,
                    "sale_date": "2011-03-01",
                    "price": "18.22",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 1385
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 18,
                    "sale_date": "2011-03-02",
                    "price": "21.06",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 1386
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 27,
                    "sale_date": "2011-03-02",
                    "price": "25.48",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1387
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 5,
                    "sale_date": "2011-03-02",
                    "price": "15.83",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 1388
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 31,
                    "sale_date": "2011-03-03",
                    "price": "12.67",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 1389
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 13,
                    "sale_date": "2011-03-03",
                    "price": "18.60",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1390
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 28,
                    "sale_date": "2011-03-04",
                    "price": "15.47",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1391
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 34,
                    "sale_date": "2011-03-04",
                    "price": "26.23",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1392
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 9,
                    "sale_date": "2011-03-04",
                    "price": "17.79",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 1393
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 3,
                    "sale_date": "2011-03-04",
                    "price": "19.31",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1394
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 33,
                    "sale_date": "2011-03-04",
                    "price": "12.66",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 1395
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 37,
                    "sale_date": "2011-03-04",
                    "price": "16.24",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 1396
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 28,
                    "sale_date": "2011-03-05",
                    "price": "28.32",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 1397
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 23,
                    "sale_date": "2011-03-05",
                    "price": "13.72",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1398
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 16,
                    "sale_date": "2011-03-05",
                    "price": "14.17",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 1399
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 38,
                    "sale_date": "2011-03-05",
                    "price": "26.96",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 1400
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 29,
                    "sale_date": "2011-03-05",
                    "price": "15.18",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1401
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 2,
                    "sale_date": "2011-03-05",
                    "price": "18.31",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 1402
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 22,
                    "sale_date": "2011-03-05",
                    "price": "22.46",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1403
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 30,
                    "sale_date": "2011-03-05",
                    "price": "19.28",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1404
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 13,
                    "sale_date": "2011-03-05",
                    "price": "13.40",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 1405
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 9,
                    "sale_date": "2011-03-06",
                    "price": "15.45",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1406
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 15,
                    "sale_date": "2011-03-06",
                    "price": "22.08",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1407
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 2,
                    "sale_date": "2011-03-06",
                    "price": "12.89",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 1408
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 2,
                    "sale_date": "2011-03-07",
                    "price": "18.49",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 1409
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 22,
                    "sale_date": "2011-03-07",
                    "price": "12.34",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1410
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 21,
                    "sale_date": "2011-03-07",
                    "price": "30.22",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 1411
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 34,
                    "sale_date": "2011-03-07",
                    "price": "15.50",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 1412
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 17,
                    "sale_date": "2011-03-07",
                    "price": "25.49",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1413
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 37,
                    "sale_date": "2011-03-07",
                    "price": "11.86",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1414
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 18,
                    "sale_date": "2011-03-08",
                    "price": "14.87",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1415
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 36,
                    "sale_date": "2011-03-08",
                    "price": "29.35",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1416
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 18,
                    "sale_date": "2011-03-08",
                    "price": "22.19",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 1417
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 5,
                    "sale_date": "2011-03-08",
                    "price": "23.42",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 1418
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 35,
                    "sale_date": "2011-03-09",
                    "price": "26.51",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1419
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 17,
                    "sale_date": "2011-03-09",
                    "price": "16.24",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 1420
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 3,
                    "sale_date": "2011-03-09",
                    "price": "15.19",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 1421
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 20,
                    "sale_date": "2011-03-09",
                    "price": "16.93",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1422
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 33,
                    "sale_date": "2011-03-09",
                    "price": "22.75",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 1423
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 21,
                    "sale_date": "2011-03-10",
                    "price": "13.04",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1424
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 31,
                    "sale_date": "2011-03-10",
                    "price": "15.19",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 1425
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 10,
                    "sale_date": "2011-03-10",
                    "price": "16.70",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1426
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 12,
                    "sale_date": "2011-03-10",
                    "price": "9.92",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1427
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 39,
                    "sale_date": "2011-03-10",
                    "price": "18.79",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 1428
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 13,
                    "sale_date": "2011-03-10",
                    "price": "15.48",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1429
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 36,
                    "sale_date": "2011-03-10",
                    "price": "21.45",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1430
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 14,
                    "sale_date": "2011-03-10",
                    "price": "12.31",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1431
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 13,
                    "sale_date": "2011-03-10",
                    "price": "11.07",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1432
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 15,
                    "sale_date": "2011-03-10",
                    "price": "13.61",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1433
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 14,
                    "sale_date": "2011-03-11",
                    "price": "17.71",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1434
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 16,
                    "sale_date": "2011-03-11",
                    "price": "21.08",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1435
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 2,
                    "sale_date": "2011-03-11",
                    "price": "19.19",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 1436
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 8,
                    "sale_date": "2011-03-11",
                    "price": "19.73",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 1437
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 6,
                    "sale_date": "2011-03-11",
                    "price": "19.93",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1438
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 12,
                    "sale_date": "2011-03-11",
                    "price": "26.82",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1439
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 1,
                    "sale_date": "2011-03-12",
                    "price": "12.16",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1440
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 7,
                    "sale_date": "2011-03-12",
                    "price": "18.82",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1441
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 31,
                    "sale_date": "2011-03-12",
                    "price": "12.48",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 1442
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 39,
                    "sale_date": "2011-03-12",
                    "price": "25.42",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 1443
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 20,
                    "sale_date": "2011-03-12",
                    "price": "15.94",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1444
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 14,
                    "sale_date": "2011-03-12",
                    "price": "15.63",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1445
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 37,
                    "sale_date": "2011-03-13",
                    "price": "19.89",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 1446
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 33,
                    "sale_date": "2011-03-13",
                    "price": "25.14",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 1447
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 26,
                    "sale_date": "2011-03-13",
                    "price": "14.58",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1448
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 18,
                    "sale_date": "2011-03-13",
                    "price": "15.32",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1449
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 18,
                    "sale_date": "2011-03-13",
                    "price": "9.32",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 1450
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 4,
                    "sale_date": "2011-03-14",
                    "price": "13.05",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 1451
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 23,
                    "sale_date": "2011-03-14",
                    "price": "29.62",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1452
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 23,
                    "sale_date": "2011-03-14",
                    "price": "15.24",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 1453
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 31,
                    "sale_date": "2011-03-14",
                    "price": "11.55",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1454
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 19,
                    "sale_date": "2011-03-17",
                    "price": "13.58",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1455
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 6,
                    "sale_date": "2011-03-17",
                    "price": "28.90",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 1456
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 11,
                    "sale_date": "2011-03-17",
                    "price": "28.24",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1457
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 38,
                    "sale_date": "2011-03-17",
                    "price": "11.49",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1458
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 2,
                    "sale_date": "2011-03-17",
                    "price": "14.89",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 1459
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 32,
                    "sale_date": "2011-03-18",
                    "price": "12.27",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1460
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 20,
                    "sale_date": "2011-03-18",
                    "price": "16.46",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 1461
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 31,
                    "sale_date": "2011-03-18",
                    "price": "11.08",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1462
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 8,
                    "sale_date": "2011-03-18",
                    "price": "27.34",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 1463
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 16,
                    "sale_date": "2011-03-18",
                    "price": "16.61",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 1464
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 27,
                    "sale_date": "2011-03-18",
                    "price": "10.78",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 1465
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 33,
                    "sale_date": "2011-03-19",
                    "price": "9.22",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1466
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 27,
                    "sale_date": "2011-03-19",
                    "price": "15.47",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1467
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 22,
                    "sale_date": "2011-03-19",
                    "price": "12.80",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 1468
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 28,
                    "sale_date": "2011-03-19",
                    "price": "10.80",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1469
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 38,
                    "sale_date": "2011-03-19",
                    "price": "26.94",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1470
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 1,
                    "sale_date": "2011-03-19",
                    "price": "14.36",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 1471
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 16,
                    "sale_date": "2011-03-20",
                    "price": "10.48",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1472
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 1,
                    "sale_date": "2011-03-20",
                    "price": "16.50",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1473
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 33,
                    "sale_date": "2011-03-20",
                    "price": "16.10",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 1474
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 26,
                    "sale_date": "2011-03-20",
                    "price": "8.45",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1475
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 30,
                    "sale_date": "2011-03-20",
                    "price": "29.94",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1476
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 39,
                    "sale_date": "2011-03-20",
                    "price": "22.28",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 1477
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 9,
                    "sale_date": "2011-03-21",
                    "price": "23.62",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1478
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 17,
                    "sale_date": "2011-03-21",
                    "price": "8.90",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 1479
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 35,
                    "sale_date": "2011-03-21",
                    "price": "26.91",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 1480
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 24,
                    "sale_date": "2011-03-21",
                    "price": "23.29",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 1481
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 24,
                    "sale_date": "2011-03-21",
                    "price": "19.22",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1482
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 13,
                    "sale_date": "2011-03-21",
                    "price": "21.61",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 1483
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 17,
                    "sale_date": "2011-03-22",
                    "price": "11.10",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 1484
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 7,
                    "sale_date": "2011-03-22",
                    "price": "9.83",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 1485
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 9,
                    "sale_date": "2011-03-22",
                    "price": "12.69",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 1486
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 35,
                    "sale_date": "2011-03-22",
                    "price": "13.80",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 1487
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 7,
                    "sale_date": "2011-03-22",
                    "price": "11.29",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1488
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 19,
                    "sale_date": "2011-03-23",
                    "price": "13.62",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 1489
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 30,
                    "sale_date": "2011-03-23",
                    "price": "12.83",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1490
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 6,
                    "sale_date": "2011-03-23",
                    "price": "30.98",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 1491
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 21,
                    "sale_date": "2011-03-23",
                    "price": "25.07",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1492
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 24,
                    "sale_date": "2011-03-23",
                    "price": "12.42",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 1493
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 31,
                    "sale_date": "2011-03-24",
                    "price": "20.64",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1494
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 24,
                    "sale_date": "2011-03-24",
                    "price": "11.65",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1495
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 17,
                    "sale_date": "2011-03-24",
                    "price": "14.52",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1496
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 20,
                    "sale_date": "2011-03-24",
                    "price": "20.01",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 1497
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 19,
                    "sale_date": "2011-03-24",
                    "price": "17.83",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1498
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 7,
                    "sale_date": "2011-03-24",
                    "price": "11.95",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1499
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 21,
                    "sale_date": "2011-03-25",
                    "price": "11.51",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 1500
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 22,
                    "sale_date": "2011-03-25",
                    "price": "27.05",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1501
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 18,
                    "sale_date": "2011-03-25",
                    "price": "10.44",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 1502
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 7,
                    "sale_date": "2011-03-25",
                    "price": "9.33",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1503
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 21,
                    "sale_date": "2011-03-25",
                    "price": "19.49",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1504
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 4,
                    "sale_date": "2011-03-25",
                    "price": "19.10",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1505
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 13,
                    "sale_date": "2011-03-25",
                    "price": "16.33",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1506
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 3,
                    "sale_date": "2011-03-25",
                    "price": "17.50",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1507
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 29,
                    "sale_date": "2011-03-25",
                    "price": "14.36",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 1508
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 21,
                    "sale_date": "2011-03-25",
                    "price": "10.75",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1509
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 35,
                    "sale_date": "2011-03-25",
                    "price": "26.38",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1510
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 7,
                    "sale_date": "2011-03-26",
                    "price": "12.86",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1511
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 15,
                    "sale_date": "2011-03-26",
                    "price": "20.38",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 1512
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 37,
                    "sale_date": "2011-03-27",
                    "price": "24.61",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 1513
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 1,
                    "sale_date": "2011-03-27",
                    "price": "21.27",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 1514
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 13,
                    "sale_date": "2011-03-28",
                    "price": "26.55",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1515
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 30,
                    "sale_date": "2011-03-28",
                    "price": "20.09",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1516
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 21,
                    "sale_date": "2011-03-28",
                    "price": "19.30",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1517
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 20,
                    "sale_date": "2011-03-28",
                    "price": "16.01",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1518
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 9,
                    "sale_date": "2011-03-28",
                    "price": "19.87",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 1519
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 12,
                    "sale_date": "2011-03-28",
                    "price": "14.42",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 1520
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 1,
                    "sale_date": "2011-03-28",
                    "price": "16.45",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 1521
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 29,
                    "sale_date": "2011-03-28",
                    "price": "18.00",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1522
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 36,
                    "sale_date": "2011-03-28",
                    "price": "14.66",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1523
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 31,
                    "sale_date": "2011-03-28",
                    "price": "29.93",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 1524
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 27,
                    "sale_date": "2011-03-28",
                    "price": "12.73",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1525
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 7,
                    "sale_date": "2011-03-29",
                    "price": "10.37",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 1526
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 9,
                    "sale_date": "2011-03-29",
                    "price": "10.04",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 1527
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 20,
                    "sale_date": "2011-03-29",
                    "price": "12.69",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 1528
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 33,
                    "sale_date": "2011-03-29",
                    "price": "15.55",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1529
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 22,
                    "sale_date": "2011-03-29",
                    "price": "11.12",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1530
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 30,
                    "sale_date": "2011-03-29",
                    "price": "14.88",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1531
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 38,
                    "sale_date": "2011-03-30",
                    "price": "11.43",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 1532
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 24,
                    "sale_date": "2011-03-30",
                    "price": "15.05",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1533
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 33,
                    "sale_date": "2011-03-30",
                    "price": "19.46",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1534
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 39,
                    "sale_date": "2011-03-30",
                    "price": "15.50",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1535
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 20,
                    "sale_date": "2011-03-30",
                    "price": "19.71",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1536
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 9,
                    "sale_date": "2011-03-30",
                    "price": "14.40",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1537
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 26,
                    "sale_date": "2011-03-31",
                    "price": "15.54",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1538
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 20,
                    "sale_date": "2011-03-31",
                    "price": "15.27",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 1539
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 32,
                    "sale_date": "2011-03-31",
                    "price": "13.86",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1540
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 37,
                    "sale_date": "2011-03-31",
                    "price": "10.06",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1541
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 5,
                    "sale_date": "2011-03-31",
                    "price": "24.63",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 1542
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 24,
                    "sale_date": "2011-03-31",
                    "price": "22.44",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 1543
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 39,
                    "sale_date": "2011-03-31",
                    "price": "10.13",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1544
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 33,
                    "sale_date": "2011-04-01",
                    "price": "17.94",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 1545
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 32,
                    "sale_date": "2011-04-01",
                    "price": "28.16",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 1546
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 18,
                    "sale_date": "2011-04-01",
                    "price": "11.00",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1547
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 27,
                    "sale_date": "2011-04-01",
                    "price": "15.59",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 1548
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 14,
                    "sale_date": "2011-04-01",
                    "price": "22.11",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 1549
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 14,
                    "sale_date": "2011-04-01",
                    "price": "15.21",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1550
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 13,
                    "sale_date": "2011-04-02",
                    "price": "18.40",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1551
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 8,
                    "sale_date": "2011-04-02",
                    "price": "15.57",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1552
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 8,
                    "sale_date": "2011-04-02",
                    "price": "15.93",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1553
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 10,
                    "sale_date": "2011-04-02",
                    "price": "17.01",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 1554
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 24,
                    "sale_date": "2011-04-02",
                    "price": "12.26",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1555
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 13,
                    "sale_date": "2011-04-03",
                    "price": "14.76",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1556
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 28,
                    "sale_date": "2011-04-03",
                    "price": "14.82",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 1557
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 23,
                    "sale_date": "2011-04-03",
                    "price": "19.11",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1558
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 12,
                    "sale_date": "2011-04-03",
                    "price": "10.70",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1559
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 37,
                    "sale_date": "2011-04-04",
                    "price": "11.38",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1560
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 11,
                    "sale_date": "2011-04-04",
                    "price": "11.83",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1561
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 4,
                    "sale_date": "2011-04-04",
                    "price": "7.05",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1562
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 16,
                    "sale_date": "2011-04-04",
                    "price": "10.62",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1563
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 22,
                    "sale_date": "2011-04-04",
                    "price": "16.73",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 1564
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 17,
                    "sale_date": "2011-04-04",
                    "price": "19.57",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1565
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 30,
                    "sale_date": "2011-04-05",
                    "price": "14.49",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1566
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 12,
                    "sale_date": "2011-04-05",
                    "price": "8.73",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 1567
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 20,
                    "sale_date": "2011-04-05",
                    "price": "13.37",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 1568
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 27,
                    "sale_date": "2011-04-05",
                    "price": "26.93",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1569
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 39,
                    "sale_date": "2011-04-05",
                    "price": "15.54",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 1570
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 17,
                    "sale_date": "2011-04-05",
                    "price": "27.25",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1571
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 5,
                    "sale_date": "2011-04-05",
                    "price": "13.04",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1572
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 9,
                    "sale_date": "2011-04-06",
                    "price": "23.28",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 1573
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 2,
                    "sale_date": "2011-04-06",
                    "price": "30.09",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1574
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 14,
                    "sale_date": "2011-04-06",
                    "price": "19.80",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1575
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 1,
                    "sale_date": "2011-04-06",
                    "price": "26.20",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 1576
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 15,
                    "sale_date": "2011-04-07",
                    "price": "26.09",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1577
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 5,
                    "sale_date": "2011-04-07",
                    "price": "17.99",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 1578
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 8,
                    "sale_date": "2011-04-07",
                    "price": "15.60",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1579
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 20,
                    "sale_date": "2011-04-07",
                    "price": "13.60",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1580
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 34,
                    "sale_date": "2011-04-07",
                    "price": "13.95",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1581
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 20,
                    "sale_date": "2011-04-07",
                    "price": "11.62",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1582
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 7,
                    "sale_date": "2011-04-08",
                    "price": "15.69",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1583
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 4,
                    "sale_date": "2011-04-08",
                    "price": "14.13",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 1584
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 4,
                    "sale_date": "2011-04-08",
                    "price": "17.16",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 1585
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 21,
                    "sale_date": "2011-04-08",
                    "price": "15.52",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 1586
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 35,
                    "sale_date": "2011-04-08",
                    "price": "12.57",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1587
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 14,
                    "sale_date": "2011-04-09",
                    "price": "14.43",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 1588
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 20,
                    "sale_date": "2011-04-09",
                    "price": "10.57",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 1589
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 35,
                    "sale_date": "2011-04-09",
                    "price": "15.18",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 1590
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 3,
                    "sale_date": "2011-04-09",
                    "price": "27.10",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1591
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 4,
                    "sale_date": "2011-04-09",
                    "price": "13.22",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1592
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 37,
                    "sale_date": "2011-04-09",
                    "price": "21.20",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 1593
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 32,
                    "sale_date": "2011-04-10",
                    "price": "12.83",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 1594
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 14,
                    "sale_date": "2011-04-10",
                    "price": "15.53",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 1595
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 1,
                    "sale_date": "2011-04-10",
                    "price": "15.28",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 1596
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 11,
                    "sale_date": "2011-04-10",
                    "price": "15.74",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 1597
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 19,
                    "sale_date": "2011-04-10",
                    "price": "28.65",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1598
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 10,
                    "sale_date": "2011-04-11",
                    "price": "12.73",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1599
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 20,
                    "sale_date": "2011-04-11",
                    "price": "12.56",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1600
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 22,
                    "sale_date": "2011-04-11",
                    "price": "27.60",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1601
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 39,
                    "sale_date": "2011-04-11",
                    "price": "10.65",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1602
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 4,
                    "sale_date": "2011-04-11",
                    "price": "25.76",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 1603
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 5,
                    "sale_date": "2011-04-11",
                    "price": "20.10",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1604
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 36,
                    "sale_date": "2011-04-11",
                    "price": "15.52",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 1605
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 25,
                    "sale_date": "2011-04-11",
                    "price": "15.01",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 1606
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 19,
                    "sale_date": "2011-04-11",
                    "price": "26.49",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 1607
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 15,
                    "sale_date": "2011-04-11",
                    "price": "16.05",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1608
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 32,
                    "sale_date": "2011-04-11",
                    "price": "24.38",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1609
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 33,
                    "sale_date": "2011-04-12",
                    "price": "16.41",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 1610
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 22,
                    "sale_date": "2011-04-12",
                    "price": "13.85",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 1611
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 8,
                    "sale_date": "2011-04-12",
                    "price": "13.67",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 1612
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 13,
                    "sale_date": "2011-04-12",
                    "price": "12.03",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1613
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 32,
                    "sale_date": "2011-04-12",
                    "price": "13.03",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 1614
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 22,
                    "sale_date": "2011-04-13",
                    "price": "29.46",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 1615
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 10,
                    "sale_date": "2011-04-13",
                    "price": "26.84",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1616
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 33,
                    "sale_date": "2011-04-13",
                    "price": "16.24",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1617
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 38,
                    "sale_date": "2011-04-13",
                    "price": "11.58",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 1618
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 36,
                    "sale_date": "2011-04-13",
                    "price": "13.98",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 1619
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 13,
                    "sale_date": "2011-04-13",
                    "price": "22.38",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1620
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 3,
                    "sale_date": "2011-04-13",
                    "price": "24.92",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1621
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 33,
                    "sale_date": "2011-04-13",
                    "price": "11.08",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1622
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 13,
                    "sale_date": "2011-04-13",
                    "price": "14.63",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 1623
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 6,
                    "sale_date": "2011-04-14",
                    "price": "26.72",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1624
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 2,
                    "sale_date": "2011-04-14",
                    "price": "10.69",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 1625
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 18,
                    "sale_date": "2011-04-14",
                    "price": "30.01",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1626
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 33,
                    "sale_date": "2011-04-15",
                    "price": "13.44",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 1627
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 32,
                    "sale_date": "2011-04-15",
                    "price": "20.72",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 1628
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 26,
                    "sale_date": "2011-04-15",
                    "price": "13.69",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 1629
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 16,
                    "sale_date": "2011-04-15",
                    "price": "9.12",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 1630
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 26,
                    "sale_date": "2011-04-15",
                    "price": "23.80",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 1631
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 11,
                    "sale_date": "2011-04-16",
                    "price": "29.34",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 1632
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 15,
                    "sale_date": "2011-04-16",
                    "price": "16.33",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 1633
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 21,
                    "sale_date": "2011-04-16",
                    "price": "22.83",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 1634
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 29,
                    "sale_date": "2011-04-16",
                    "price": "10.49",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1635
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 6,
                    "sale_date": "2011-04-16",
                    "price": "10.11",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1636
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 24,
                    "sale_date": "2011-04-16",
                    "price": "22.84",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 1637
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 34,
                    "sale_date": "2011-04-16",
                    "price": "11.60",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1638
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 33,
                    "sale_date": "2011-04-16",
                    "price": "14.64",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 1639
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 14,
                    "sale_date": "2011-04-16",
                    "price": "16.44",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 1640
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 25,
                    "sale_date": "2011-04-16",
                    "price": "21.72",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 1641
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 29,
                    "sale_date": "2011-04-16",
                    "price": "18.89",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 1642
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 14,
                    "sale_date": "2011-04-17",
                    "price": "22.93",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1643
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 5,
                    "sale_date": "2011-04-17",
                    "price": "10.98",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 1644
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 34,
                    "sale_date": "2011-04-17",
                    "price": "26.30",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1645
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 6,
                    "sale_date": "2011-04-17",
                    "price": "24.56",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 1646
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 30,
                    "sale_date": "2011-04-18",
                    "price": "14.18",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1647
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 38,
                    "sale_date": "2011-04-18",
                    "price": "14.92",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1648
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 15,
                    "sale_date": "2011-04-18",
                    "price": "16.06",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1649
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 25,
                    "sale_date": "2011-04-18",
                    "price": "29.51",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 1650
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 28,
                    "sale_date": "2011-04-19",
                    "price": "15.99",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 1651
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 19,
                    "sale_date": "2011-04-19",
                    "price": "15.40",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 1652
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 5,
                    "sale_date": "2011-04-19",
                    "price": "10.19",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 1653
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 8,
                    "sale_date": "2011-04-19",
                    "price": "17.49",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1654
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 23,
                    "sale_date": "2011-04-19",
                    "price": "15.06",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 1655
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 24,
                    "sale_date": "2011-04-19",
                    "price": "18.54",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1656
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 33,
                    "sale_date": "2011-04-20",
                    "price": "24.78",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 1657
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 25,
                    "sale_date": "2011-04-20",
                    "price": "10.37",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1658
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 25,
                    "sale_date": "2011-04-20",
                    "price": "10.50",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 1659
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 26,
                    "sale_date": "2011-04-20",
                    "price": "12.31",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 1660
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 37,
                    "sale_date": "2011-04-20",
                    "price": "15.86",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1661
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 39,
                    "sale_date": "2011-04-20",
                    "price": "11.36",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1662
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 37,
                    "sale_date": "2011-04-20",
                    "price": "15.85",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1663
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 18,
                    "sale_date": "2011-04-21",
                    "price": "19.73",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 1664
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 25,
                    "sale_date": "2011-04-21",
                    "price": "11.22",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1665
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 22,
                    "sale_date": "2011-04-21",
                    "price": "11.95",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 1666
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 36,
                    "sale_date": "2011-04-21",
                    "price": "12.63",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1667
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 24,
                    "sale_date": "2011-04-21",
                    "price": "12.87",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1668
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 32,
                    "sale_date": "2011-04-22",
                    "price": "23.76",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1669
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 12,
                    "sale_date": "2011-04-22",
                    "price": "14.11",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 1670
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 6,
                    "sale_date": "2011-04-22",
                    "price": "10.73",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1671
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 34,
                    "sale_date": "2011-04-22",
                    "price": "18.81",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 1672
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 9,
                    "sale_date": "2011-04-22",
                    "price": "11.78",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1673
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 7,
                    "sale_date": "2011-04-22",
                    "price": "10.40",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1674
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 25,
                    "sale_date": "2011-04-23",
                    "price": "11.72",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1675
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 1,
                    "sale_date": "2011-04-23",
                    "price": "27.88",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1676
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 37,
                    "sale_date": "2011-04-23",
                    "price": "14.79",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1677
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 36,
                    "sale_date": "2011-04-23",
                    "price": "24.85",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 1678
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 8,
                    "sale_date": "2011-04-23",
                    "price": "13.09",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 1679
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 36,
                    "sale_date": "2011-04-24",
                    "price": "22.09",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 1680
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 14,
                    "sale_date": "2011-04-24",
                    "price": "15.88",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 1681
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 19,
                    "sale_date": "2011-04-24",
                    "price": "18.31",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 1682
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 3,
                    "sale_date": "2011-04-25",
                    "price": "30.83",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 1683
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 10,
                    "sale_date": "2011-04-25",
                    "price": "13.58",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1684
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 31,
                    "sale_date": "2011-04-25",
                    "price": "13.99",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1685
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 2,
                    "sale_date": "2011-04-25",
                    "price": "13.66",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 1686
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 3,
                    "sale_date": "2011-04-26",
                    "price": "20.89",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 1687
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 27,
                    "sale_date": "2011-04-26",
                    "price": "11.20",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1688
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 9,
                    "sale_date": "2011-04-26",
                    "price": "14.32",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 1689
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 18,
                    "sale_date": "2011-04-26",
                    "price": "13.51",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1690
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 25,
                    "sale_date": "2011-04-27",
                    "price": "10.88",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1691
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 10,
                    "sale_date": "2011-04-27",
                    "price": "25.22",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1692
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 7,
                    "sale_date": "2011-04-27",
                    "price": "15.51",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1693
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 35,
                    "sale_date": "2011-04-28",
                    "price": "17.68",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1694
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 9,
                    "sale_date": "2011-04-28",
                    "price": "11.85",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 1695
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 33,
                    "sale_date": "2011-04-28",
                    "price": "9.62",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1696
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 8,
                    "sale_date": "2011-04-28",
                    "price": "23.05",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1697
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 26,
                    "sale_date": "2011-04-28",
                    "price": "18.00",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 1698
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 16,
                    "sale_date": "2011-04-29",
                    "price": "14.96",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 1699
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 18,
                    "sale_date": "2011-04-29",
                    "price": "19.04",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 1700
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 21,
                    "sale_date": "2011-04-29",
                    "price": "21.68",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1701
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 33,
                    "sale_date": "2011-04-30",
                    "price": "20.35",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 1702
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 33,
                    "sale_date": "2011-04-30",
                    "price": "22.40",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1703
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 5,
                    "sale_date": "2011-04-30",
                    "price": "15.98",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1704
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 6,
                    "sale_date": "2011-04-30",
                    "price": "22.87",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 1705
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 24,
                    "sale_date": "2011-05-01",
                    "price": "20.59",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1706
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 10,
                    "sale_date": "2011-05-01",
                    "price": "15.34",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1707
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 8,
                    "sale_date": "2011-05-01",
                    "price": "10.27",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1708
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 4,
                    "sale_date": "2011-05-02",
                    "price": "22.68",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1709
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 32,
                    "sale_date": "2011-05-02",
                    "price": "10.49",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1710
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 20,
                    "sale_date": "2011-05-02",
                    "price": "20.99",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1711
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 24,
                    "sale_date": "2011-05-02",
                    "price": "7.40",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 1712
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 23,
                    "sale_date": "2011-05-02",
                    "price": "14.28",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1713
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 27,
                    "sale_date": "2011-05-02",
                    "price": "19.66",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1714
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 20,
                    "sale_date": "2011-05-02",
                    "price": "11.97",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 1715
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 36,
                    "sale_date": "2011-05-02",
                    "price": "11.92",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1716
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 38,
                    "sale_date": "2011-05-02",
                    "price": "12.05",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 1717
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 36,
                    "sale_date": "2011-05-02",
                    "price": "19.92",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 1718
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 37,
                    "sale_date": "2011-05-02",
                    "price": "15.64",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1719
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 25,
                    "sale_date": "2011-05-02",
                    "price": "14.80",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1720
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 20,
                    "sale_date": "2011-05-03",
                    "price": "23.85",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1721
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 21,
                    "sale_date": "2011-05-03",
                    "price": "21.73",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 1722
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 38,
                    "sale_date": "2011-05-03",
                    "price": "16.89",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 1723
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 6,
                    "sale_date": "2011-05-03",
                    "price": "26.07",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1724
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 36,
                    "sale_date": "2011-05-03",
                    "price": "12.36",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1725
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 5,
                    "sale_date": "2011-05-04",
                    "price": "15.56",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 1726
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 27,
                    "sale_date": "2011-05-04",
                    "price": "15.80",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 1727
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 39,
                    "sale_date": "2011-05-04",
                    "price": "14.93",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1728
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 2,
                    "sale_date": "2011-05-05",
                    "price": "13.90",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1729
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 38,
                    "sale_date": "2011-05-05",
                    "price": "14.41",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 1730
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 25,
                    "sale_date": "2011-05-05",
                    "price": "13.24",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 1731
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 9,
                    "sale_date": "2011-05-05",
                    "price": "26.79",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 1732
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 38,
                    "sale_date": "2011-05-05",
                    "price": "13.80",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1733
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 29,
                    "sale_date": "2011-05-05",
                    "price": "12.57",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 1734
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 24,
                    "sale_date": "2011-05-05",
                    "price": "28.99",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 1735
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 31,
                    "sale_date": "2011-05-06",
                    "price": "10.38",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1736
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 32,
                    "sale_date": "2011-05-06",
                    "price": "15.87",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 1737
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 18,
                    "sale_date": "2011-05-07",
                    "price": "19.12",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 1738
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 7,
                    "sale_date": "2011-05-07",
                    "price": "12.09",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1739
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 6,
                    "sale_date": "2011-05-07",
                    "price": "15.13",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1740
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 9,
                    "sale_date": "2011-05-07",
                    "price": "13.46",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 1741
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 37,
                    "sale_date": "2011-05-07",
                    "price": "13.07",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1742
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 34,
                    "sale_date": "2011-05-07",
                    "price": "8.79",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 1743
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 23,
                    "sale_date": "2011-05-07",
                    "price": "14.48",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1744
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 38,
                    "sale_date": "2011-05-07",
                    "price": "26.55",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 1745
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 29,
                    "sale_date": "2011-05-07",
                    "price": "22.85",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1746
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 5,
                    "sale_date": "2011-05-08",
                    "price": "26.34",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 1747
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 18,
                    "sale_date": "2011-05-08",
                    "price": "14.15",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 1748
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 1,
                    "sale_date": "2011-05-08",
                    "price": "22.43",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1749
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 3,
                    "sale_date": "2011-05-08",
                    "price": "15.48",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 1750
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 34,
                    "sale_date": "2011-05-08",
                    "price": "14.23",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1751
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 35,
                    "sale_date": "2011-05-09",
                    "price": "16.83",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1752
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 18,
                    "sale_date": "2011-05-09",
                    "price": "14.53",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 1753
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 36,
                    "sale_date": "2011-05-09",
                    "price": "17.49",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1754
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 4,
                    "sale_date": "2011-05-09",
                    "price": "26.32",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 1755
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 1,
                    "sale_date": "2011-05-10",
                    "price": "11.01",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1756
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 12,
                    "sale_date": "2011-05-10",
                    "price": "13.52",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 1757
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 12,
                    "sale_date": "2011-05-10",
                    "price": "10.28",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1758
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 12,
                    "sale_date": "2011-05-10",
                    "price": "16.63",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1759
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 37,
                    "sale_date": "2011-05-10",
                    "price": "24.59",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 1760
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 3,
                    "sale_date": "2011-05-12",
                    "price": "14.11",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1761
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 19,
                    "sale_date": "2011-05-12",
                    "price": "30.64",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 1762
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 13,
                    "sale_date": "2011-05-12",
                    "price": "22.60",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 1763
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 22,
                    "sale_date": "2011-05-12",
                    "price": "13.62",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1764
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 32,
                    "sale_date": "2011-05-13",
                    "price": "7.69",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1765
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 19,
                    "sale_date": "2011-05-13",
                    "price": "21.86",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1766
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 16,
                    "sale_date": "2011-05-13",
                    "price": "14.32",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 1767
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 12,
                    "sale_date": "2011-05-13",
                    "price": "11.83",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 1768
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 25,
                    "sale_date": "2011-05-13",
                    "price": "23.37",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1769
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 36,
                    "sale_date": "2011-05-13",
                    "price": "16.62",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 1770
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 4,
                    "sale_date": "2011-05-13",
                    "price": "12.62",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1771
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 30,
                    "sale_date": "2011-05-13",
                    "price": "14.08",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 1772
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 11,
                    "sale_date": "2011-05-13",
                    "price": "19.87",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1773
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 3,
                    "sale_date": "2011-05-14",
                    "price": "20.11",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 1774
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 16,
                    "sale_date": "2011-05-14",
                    "price": "9.14",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 1775
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 22,
                    "sale_date": "2011-05-15",
                    "price": "19.23",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1776
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 17,
                    "sale_date": "2011-05-15",
                    "price": "14.84",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1777
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 34,
                    "sale_date": "2011-05-16",
                    "price": "15.78",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1778
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 17,
                    "sale_date": "2011-05-16",
                    "price": "13.00",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1779
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 24,
                    "sale_date": "2011-05-16",
                    "price": "14.43",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 1780
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 39,
                    "sale_date": "2011-05-16",
                    "price": "15.68",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 1781
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 17,
                    "sale_date": "2011-05-16",
                    "price": "14.44",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1782
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 11,
                    "sale_date": "2011-05-16",
                    "price": "24.25",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 1783
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 34,
                    "sale_date": "2011-05-16",
                    "price": "13.53",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1784
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 28,
                    "sale_date": "2011-05-16",
                    "price": "11.88",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1785
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 35,
                    "sale_date": "2011-05-17",
                    "price": "26.70",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1786
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 31,
                    "sale_date": "2011-05-17",
                    "price": "17.88",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1787
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 33,
                    "sale_date": "2011-05-17",
                    "price": "16.42",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 1788
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 31,
                    "sale_date": "2011-05-17",
                    "price": "11.57",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 1789
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 6,
                    "sale_date": "2011-05-17",
                    "price": "13.73",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 1790
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 6,
                    "sale_date": "2011-05-17",
                    "price": "11.82",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 1791
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 30,
                    "sale_date": "2011-05-18",
                    "price": "21.00",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1792
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 7,
                    "sale_date": "2011-05-18",
                    "price": "11.99",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1793
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 24,
                    "sale_date": "2011-05-18",
                    "price": "18.86",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1794
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 32,
                    "sale_date": "2011-05-19",
                    "price": "18.72",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1795
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 38,
                    "sale_date": "2011-05-19",
                    "price": "15.91",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1796
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 18,
                    "sale_date": "2011-05-19",
                    "price": "18.47",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 1797
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 38,
                    "sale_date": "2011-05-19",
                    "price": "11.90",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1798
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 2,
                    "sale_date": "2011-05-20",
                    "price": "16.08",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1799
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 35,
                    "sale_date": "2011-05-20",
                    "price": "11.15",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 1800
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 2,
                    "sale_date": "2011-05-20",
                    "price": "12.40",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1801
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 34,
                    "sale_date": "2011-05-20",
                    "price": "15.71",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1802
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 30,
                    "sale_date": "2011-05-20",
                    "price": "23.68",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1803
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 31,
                    "sale_date": "2011-05-21",
                    "price": "15.25",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1804
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 15,
                    "sale_date": "2011-05-21",
                    "price": "12.61",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 1805
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 38,
                    "sale_date": "2011-05-21",
                    "price": "15.02",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1806
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 4,
                    "sale_date": "2011-05-21",
                    "price": "24.35",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 1807
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 6,
                    "sale_date": "2011-05-22",
                    "price": "14.96",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1808
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 12,
                    "sale_date": "2011-05-22",
                    "price": "11.42",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1809
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 24,
                    "sale_date": "2011-05-22",
                    "price": "20.80",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 1810
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 18,
                    "sale_date": "2011-05-22",
                    "price": "14.35",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 1811
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 35,
                    "sale_date": "2011-05-22",
                    "price": "26.32",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1812
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 11,
                    "sale_date": "2011-05-22",
                    "price": "15.20",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 1813
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 36,
                    "sale_date": "2011-05-22",
                    "price": "11.80",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 1814
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 30,
                    "sale_date": "2011-05-22",
                    "price": "8.75",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 1815
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 13,
                    "sale_date": "2011-05-23",
                    "price": "29.30",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 1816
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 2,
                    "sale_date": "2011-05-24",
                    "price": "11.70",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1817
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 33,
                    "sale_date": "2011-05-24",
                    "price": "14.58",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1818
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 8,
                    "sale_date": "2011-05-24",
                    "price": "16.43",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 1819
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 30,
                    "sale_date": "2011-05-25",
                    "price": "12.56",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1820
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 26,
                    "sale_date": "2011-05-25",
                    "price": "13.11",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1821
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 38,
                    "sale_date": "2011-05-25",
                    "price": "9.18",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1822
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 5,
                    "sale_date": "2011-05-26",
                    "price": "26.36",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1823
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 1,
                    "sale_date": "2011-05-26",
                    "price": "13.31",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1824
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 6,
                    "sale_date": "2011-05-26",
                    "price": "14.99",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 1825
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 23,
                    "sale_date": "2011-05-26",
                    "price": "21.19",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1826
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 8,
                    "sale_date": "2011-05-26",
                    "price": "15.17",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 1827
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 1,
                    "sale_date": "2011-05-26",
                    "price": "27.77",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1828
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 9,
                    "sale_date": "2011-05-26",
                    "price": "17.94",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1829
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 26,
                    "sale_date": "2011-05-27",
                    "price": "15.96",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1830
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 23,
                    "sale_date": "2011-05-27",
                    "price": "13.05",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 1831
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 8,
                    "sale_date": "2011-05-27",
                    "price": "16.61",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1832
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 4,
                    "sale_date": "2011-05-27",
                    "price": "13.99",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1833
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 18,
                    "sale_date": "2011-05-27",
                    "price": "7.79",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 1834
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 31,
                    "sale_date": "2011-05-27",
                    "price": "18.79",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1835
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 6,
                    "sale_date": "2011-05-28",
                    "price": "13.84",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1836
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 27,
                    "sale_date": "2011-05-28",
                    "price": "8.98",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1837
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 8,
                    "sale_date": "2011-05-28",
                    "price": "28.70",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 1838
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 23,
                    "sale_date": "2011-05-29",
                    "price": "11.69",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1839
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 9,
                    "sale_date": "2011-05-29",
                    "price": "9.36",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 1840
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 36,
                    "sale_date": "2011-05-29",
                    "price": "18.95",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1841
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 24,
                    "sale_date": "2011-05-30",
                    "price": "17.00",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1842
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 27,
                    "sale_date": "2011-05-30",
                    "price": "24.14",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1843
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 23,
                    "sale_date": "2011-05-30",
                    "price": "12.46",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 1844
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 9,
                    "sale_date": "2011-05-30",
                    "price": "13.94",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 1845
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 37,
                    "sale_date": "2011-05-30",
                    "price": "16.51",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1846
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 25,
                    "sale_date": "2011-05-30",
                    "price": "10.86",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1847
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 3,
                    "sale_date": "2011-05-31",
                    "price": "15.47",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1848
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 11,
                    "sale_date": "2011-05-31",
                    "price": "13.71",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 1849
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 38,
                    "sale_date": "2011-05-31",
                    "price": "13.07",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 1850
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 12,
                    "sale_date": "2011-06-01",
                    "price": "13.49",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 1851
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 13,
                    "sale_date": "2011-06-01",
                    "price": "18.99",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1852
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 36,
                    "sale_date": "2011-06-01",
                    "price": "15.29",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 1853
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 1,
                    "sale_date": "2011-06-01",
                    "price": "13.90",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 1854
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 10,
                    "sale_date": "2011-06-01",
                    "price": "15.58",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1855
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 33,
                    "sale_date": "2011-06-02",
                    "price": "30.85",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1856
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 29,
                    "sale_date": "2011-06-02",
                    "price": "11.52",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1857
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 36,
                    "sale_date": "2011-06-02",
                    "price": "13.50",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1858
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 30,
                    "sale_date": "2011-06-02",
                    "price": "11.31",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 1859
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 25,
                    "sale_date": "2011-06-02",
                    "price": "27.00",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 1860
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 2,
                    "sale_date": "2011-06-03",
                    "price": "12.50",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1861
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 18,
                    "sale_date": "2011-06-03",
                    "price": "10.19",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1862
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 6,
                    "sale_date": "2011-06-03",
                    "price": "26.07",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 1863
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 2,
                    "sale_date": "2011-06-03",
                    "price": "12.98",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 1864
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 29,
                    "sale_date": "2011-06-03",
                    "price": "18.32",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1865
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 7,
                    "sale_date": "2011-06-03",
                    "price": "13.03",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1866
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 11,
                    "sale_date": "2011-06-04",
                    "price": "15.85",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1867
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 32,
                    "sale_date": "2011-06-04",
                    "price": "12.29",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1868
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 15,
                    "sale_date": "2011-06-05",
                    "price": "18.83",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 1869
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 19,
                    "sale_date": "2011-06-05",
                    "price": "16.28",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1870
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 9,
                    "sale_date": "2011-06-05",
                    "price": "16.52",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1871
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 36,
                    "sale_date": "2011-06-05",
                    "price": "21.36",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 1872
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 39,
                    "sale_date": "2011-06-05",
                    "price": "18.26",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1873
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 13,
                    "sale_date": "2011-06-05",
                    "price": "14.86",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 1874
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 10,
                    "sale_date": "2011-06-05",
                    "price": "17.06",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1875
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 31,
                    "sale_date": "2011-06-05",
                    "price": "22.87",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1876
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 29,
                    "sale_date": "2011-06-06",
                    "price": "13.84",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1877
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 1,
                    "sale_date": "2011-06-06",
                    "price": "20.94",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1878
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 28,
                    "sale_date": "2011-06-06",
                    "price": "22.00",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 1879
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 15,
                    "sale_date": "2011-06-06",
                    "price": "18.61",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1880
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 26,
                    "sale_date": "2011-06-06",
                    "price": "18.97",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 1881
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 38,
                    "sale_date": "2011-06-06",
                    "price": "14.96",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1882
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 24,
                    "sale_date": "2011-06-06",
                    "price": "12.05",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1883
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 10,
                    "sale_date": "2011-06-06",
                    "price": "26.12",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1884
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 3,
                    "sale_date": "2011-06-07",
                    "price": "15.22",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1885
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 36,
                    "sale_date": "2011-06-07",
                    "price": "15.15",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 1886
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 25,
                    "sale_date": "2011-06-07",
                    "price": "13.05",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1887
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 36,
                    "sale_date": "2011-06-07",
                    "price": "11.94",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1888
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 3,
                    "sale_date": "2011-06-07",
                    "price": "10.52",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1889
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 26,
                    "sale_date": "2011-06-07",
                    "price": "26.54",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 1890
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 22,
                    "sale_date": "2011-06-07",
                    "price": "27.55",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1891
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 15,
                    "sale_date": "2011-06-07",
                    "price": "15.75",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1892
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 28,
                    "sale_date": "2011-06-07",
                    "price": "23.69",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1893
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 3,
                    "sale_date": "2011-06-08",
                    "price": "16.30",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1894
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 6,
                    "sale_date": "2011-06-08",
                    "price": "16.96",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1895
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 34,
                    "sale_date": "2011-06-08",
                    "price": "16.21",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 1896
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 23,
                    "sale_date": "2011-06-08",
                    "price": "19.20",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 1897
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 21,
                    "sale_date": "2011-06-08",
                    "price": "16.71",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1898
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 22,
                    "sale_date": "2011-06-08",
                    "price": "19.94",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 1899
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 28,
                    "sale_date": "2011-06-08",
                    "price": "20.01",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 1900
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 17,
                    "sale_date": "2011-06-09",
                    "price": "19.27",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1901
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 39,
                    "sale_date": "2011-06-09",
                    "price": "22.59",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1902
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 19,
                    "sale_date": "2011-06-09",
                    "price": "12.83",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1903
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 2,
                    "sale_date": "2011-06-09",
                    "price": "16.80",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1904
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 37,
                    "sale_date": "2011-06-09",
                    "price": "12.48",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 1905
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 1,
                    "sale_date": "2011-06-10",
                    "price": "12.10",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1906
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 12,
                    "sale_date": "2011-06-10",
                    "price": "14.28",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1907
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 12,
                    "sale_date": "2011-06-10",
                    "price": "15.40",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 1908
         },
        {"fields": {"book_id": 23,
                    "bookstore_id": 19,
                    "sale_date": "2011-06-10",
                    "price": "16.55",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1909
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 18,
                    "sale_date": "2011-06-11",
                    "price": "15.86",
                    "sale_qty": 5
                    },
         "model": "SalesHistory",
         "pk": 1910
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 27,
                    "sale_date": "2011-06-11",
                    "price": "12.86",
                    "sale_qty": 30
                    },
         "model": "SalesHistory",
         "pk": 1911
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 13,
                    "sale_date": "2011-06-11",
                    "price": "17.62",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 1912
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 38,
                    "sale_date": "2011-06-11",
                    "price": "14.80",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1913
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 1,
                    "sale_date": "2011-06-11",
                    "price": "16.02",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 1914
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 39,
                    "sale_date": "2011-06-11",
                    "price": "17.02",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1915
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 10,
                    "sale_date": "2011-06-11",
                    "price": "14.17",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1916
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 38,
                    "sale_date": "2011-06-11",
                    "price": "26.90",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1917
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 24,
                    "sale_date": "2011-06-11",
                    "price": "18.77",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1918
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 27,
                    "sale_date": "2011-06-12",
                    "price": "15.33",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1919
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 12,
                    "sale_date": "2011-06-12",
                    "price": "26.40",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1920
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 37,
                    "sale_date": "2011-06-12",
                    "price": "10.32",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 1921
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 5,
                    "sale_date": "2011-06-12",
                    "price": "27.86",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 1922
         },
        {"fields": {"book_id": 7,
                    "bookstore_id": 38,
                    "sale_date": "2011-06-12",
                    "price": "15.84",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 1923
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 23,
                    "sale_date": "2011-06-12",
                    "price": "10.89",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 1924
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 8,
                    "sale_date": "2011-06-13",
                    "price": "16.39",
                    "sale_qty": 1
                    },
         "model": "SalesHistory",
         "pk": 1925
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 17,
                    "sale_date": "2011-06-13",
                    "price": "11.57",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 1926
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 23,
                    "sale_date": "2011-06-13",
                    "price": "13.24",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1927
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 32,
                    "sale_date": "2011-06-13",
                    "price": "13.20",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1928
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 4,
                    "sale_date": "2011-06-15",
                    "price": "13.95",
                    "sale_qty": 24
                    },
         "model": "SalesHistory",
         "pk": 1929
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 21,
                    "sale_date": "2011-06-16",
                    "price": "15.04",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1930
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 12,
                    "sale_date": "2011-06-16",
                    "price": "12.87",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 1931
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 6,
                    "sale_date": "2011-06-16",
                    "price": "21.57",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1932
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 19,
                    "sale_date": "2011-06-17",
                    "price": "20.28",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1933
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 28,
                    "sale_date": "2011-06-17",
                    "price": "11.48",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 1934
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 22,
                    "sale_date": "2011-06-17",
                    "price": "15.24",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1935
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 39,
                    "sale_date": "2011-06-17",
                    "price": "7.25",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 1936
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 21,
                    "sale_date": "2011-06-17",
                    "price": "13.28",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1937
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 15,
                    "sale_date": "2011-06-18",
                    "price": "12.10",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1938
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 9,
                    "sale_date": "2011-06-18",
                    "price": "11.43",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1939
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 2,
                    "sale_date": "2011-06-18",
                    "price": "19.53",
                    "sale_qty": 7
                    },
         "model": "SalesHistory",
         "pk": 1940
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 21,
                    "sale_date": "2011-06-18",
                    "price": "29.95",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1941
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 34,
                    "sale_date": "2011-06-18",
                    "price": "11.57",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 1942
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 39,
                    "sale_date": "2011-06-18",
                    "price": "13.37",
                    "sale_qty": 13
                    },
         "model": "SalesHistory",
         "pk": 1943
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 16,
                    "sale_date": "2011-06-19",
                    "price": "14.82",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1944
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 27,
                    "sale_date": "2011-06-19",
                    "price": "11.74",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 1945
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 34,
                    "sale_date": "2011-06-19",
                    "price": "14.14",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1946
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 14,
                    "sale_date": "2011-06-19",
                    "price": "14.79",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1947
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 18,
                    "sale_date": "2011-06-19",
                    "price": "12.95",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1948
         },
        {"fields": {"book_id": 13,
                    "bookstore_id": 15,
                    "sale_date": "2011-06-19",
                    "price": "26.16",
                    "sale_qty": 18
                    },
         "model": "SalesHistory",
         "pk": 1949
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 4,
                    "sale_date": "2011-06-19",
                    "price": "23.96",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1950
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 19,
                    "sale_date": "2011-06-20",
                    "price": "22.20",
                    "sale_qty": 14
                    },
         "model": "SalesHistory",
         "pk": 1951
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 39,
                    "sale_date": "2011-06-20",
                    "price": "11.35",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1952
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 21,
                    "sale_date": "2011-06-20",
                    "price": "16.94",
                    "sale_qty": 27
                    },
         "model": "SalesHistory",
         "pk": 1953
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 6,
                    "sale_date": "2011-06-21",
                    "price": "15.25",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1954
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 4,
                    "sale_date": "2011-06-21",
                    "price": "12.02",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1955
         },
        {"fields": {"book_id": 17,
                    "bookstore_id": 7,
                    "sale_date": "2011-06-21",
                    "price": "9.15",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1956
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 5,
                    "sale_date": "2011-06-21",
                    "price": "13.43",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1957
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 20,
                    "sale_date": "2011-06-21",
                    "price": "26.39",
                    "sale_qty": 21
                    },
         "model": "SalesHistory",
         "pk": 1958
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 4,
                    "sale_date": "2011-06-21",
                    "price": "12.92",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1959
         },
        {"fields": {"book_id": 10,
                    "bookstore_id": 23,
                    "sale_date": "2011-06-22",
                    "price": "15.25",
                    "sale_qty": 16
                    },
         "model": "SalesHistory",
         "pk": 1960
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 29,
                    "sale_date": "2011-06-22",
                    "price": "17.61",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1961
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 13,
                    "sale_date": "2011-06-22",
                    "price": "29.55",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1962
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 9,
                    "sale_date": "2011-06-22",
                    "price": "13.41",
                    "sale_qty": 6
                    },
         "model": "SalesHistory",
         "pk": 1963
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 22,
                    "sale_date": "2011-06-22",
                    "price": "18.72",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 1964
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 22,
                    "sale_date": "2011-06-23",
                    "price": "13.74",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1965
         },
        {"fields": {"book_id": 12,
                    "bookstore_id": 1,
                    "sale_date": "2011-06-23",
                    "price": "29.62",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1966
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 4,
                    "sale_date": "2011-06-23",
                    "price": "12.25",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1967
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 37,
                    "sale_date": "2011-06-23",
                    "price": "16.37",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1968
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 31,
                    "sale_date": "2011-06-23",
                    "price": "22.22",
                    "sale_qty": 12
                    },
         "model": "SalesHistory",
         "pk": 1969
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 30,
                    "sale_date": "2011-06-24",
                    "price": "11.82",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1970
         },
        {"fields": {"book_id": 2,
                    "bookstore_id": 7,
                    "sale_date": "2011-06-24",
                    "price": "14.51",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1971
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 35,
                    "sale_date": "2011-06-24",
                    "price": "13.92",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1972
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 6,
                    "sale_date": "2011-06-24",
                    "price": "16.18",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1973
         },
        {"fields": {"book_id": 5,
                    "bookstore_id": 27,
                    "sale_date": "2011-06-24",
                    "price": "24.56",
                    "sale_qty": 28
                    },
         "model": "SalesHistory",
         "pk": 1974
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 9,
                    "sale_date": "2011-06-24",
                    "price": "13.79",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1975
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 18,
                    "sale_date": "2011-06-25",
                    "price": "14.76",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1976
         },
        {"fields": {"book_id": 20,
                    "bookstore_id": 2,
                    "sale_date": "2011-06-25",
                    "price": "16.47",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1977
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 31,
                    "sale_date": "2011-06-25",
                    "price": "15.87",
                    "sale_qty": 17
                    },
         "model": "SalesHistory",
         "pk": 1978
         },
        {"fields": {"book_id": 6,
                    "bookstore_id": 20,
                    "sale_date": "2011-06-25",
                    "price": "15.25",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 1979
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 20,
                    "sale_date": "2011-06-25",
                    "price": "22.42",
                    "sale_qty": 26
                    },
         "model": "SalesHistory",
         "pk": 1980
         },
        {"fields": {"book_id": 18,
                    "bookstore_id": 4,
                    "sale_date": "2011-06-25",
                    "price": "13.89",
                    "sale_qty": 23
                    },
         "model": "SalesHistory",
         "pk": 1981
         },
        {"fields": {"book_id": 16,
                    "bookstore_id": 11,
                    "sale_date": "2011-06-25",
                    "price": "14.91",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1982
         },
        {"fields": {"book_id": 9,
                    "bookstore_id": 25,
                    "sale_date": "2011-06-25",
                    "price": "10.48",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1983
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 36,
                    "sale_date": "2011-06-26",
                    "price": "16.08",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1984
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 17,
                    "sale_date": "2011-06-26",
                    "price": "15.57",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1985
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 2,
                    "sale_date": "2011-06-27",
                    "price": "16.54",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1986
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 1,
                    "sale_date": "2011-06-27",
                    "price": "15.22",
                    "sale_qty": 15
                    },
         "model": "SalesHistory",
         "pk": 1987
         },
        {"fields": {"book_id": 3,
                    "bookstore_id": 13,
                    "sale_date": "2011-06-27",
                    "price": "15.10",
                    "sale_qty": 19
                    },
         "model": "SalesHistory",
         "pk": 1988
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 33,
                    "sale_date": "2011-06-29",
                    "price": "12.66",
                    "sale_qty": 20
                    },
         "model": "SalesHistory",
         "pk": 1989
         },
        {"fields": {"book_id": 24,
                    "bookstore_id": 24,
                    "sale_date": "2011-06-29",
                    "price": "11.04",
                    "sale_qty": 11
                    },
         "model": "SalesHistory",
         "pk": 1990
         },
        {"fields": {"book_id": 15,
                    "bookstore_id": 17,
                    "sale_date": "2011-06-29",
                    "price": "22.15",
                    "sale_qty": 25
                    },
         "model": "SalesHistory",
         "pk": 1991
         },
        {"fields": {"book_id": 21,
                    "bookstore_id": 33,
                    "sale_date": "2011-06-29",
                    "price": "18.25",
                    "sale_qty": 29
                    },
         "model": "SalesHistory",
         "pk": 1992
         },
        {"fields": {"book_id": 1,
                    "bookstore_id": 12,
                    "sale_date": "2011-06-29",
                    "price": "13.44",
                    "sale_qty": 22
                    },
         "model": "SalesHistory",
         "pk": 1993
         },
        {"fields": {"book_id": 4,
                    "bookstore_id": 5,
                    "sale_date": "2011-06-29",
                    "price": "20.00",
                    "sale_qty": 2
                    },
         "model": "SalesHistory",
         "pk": 1994
         },
        {"fields": {"book_id": 19,
                    "bookstore_id": 9,
                    "sale_date": "2011-06-30",
                    "price": "8.07",
                    "sale_qty": 8
                    },
         "model": "SalesHistory",
         "pk": 1995
         },
        {"fields": {"book_id": 11,
                    "bookstore_id": 30,
                    "sale_date": "2011-06-30",
                    "price": "11.17",
                    "sale_qty": 3
                    },
         "model": "SalesHistory",
         "pk": 1996
         },
        {"fields": {"book_id": 8,
                    "bookstore_id": 31,
                    "sale_date": "2011-06-30",
                    "price": "14.37",
                    "sale_qty": 9
                    },
         "model": "SalesHistory",
         "pk": 1997
         },
        {"fields": {"book_id": 22,
                    "bookstore_id": 33,
                    "sale_date": "2011-06-30",
                    "price": "18.96",
                    "sale_qty": 10
                    },
         "model": "SalesHistory",
         "pk": 1998
         },
        {"fields": {"book_id": 14,
                    "bookstore_id": 12,
                    "sale_date": "2011-06-30",
                    "price": "15.29",
                    "sale_qty": 4
                    },
         "model": "SalesHistory",
         "pk": 1999
         }
    ]

    Book = apps.get_model("demoproject", "Book")
    BookRelated = None
    BookAuthors = None
    for relation in Book._meta.many_to_many:
        if relation.name == 'related':
            try:
                BookRelated = relation.remote_field.through
            except AttributeError:
                # available in Django 1.8
                BookRelated = relation.rel.through

        if relation.name == 'authors':
            try:
                BookAuthors = relation.remote_field.through
            except AttributeError:
                # available in Django 1.8
                BookAuthors = relation.rel.through

    # create objects which don't have FKs or ManyToMany fields
    for record in data:
        # Book has ManyToMany relation to itself
        if record['model'] in ['Book', 'BookStore', 'SalesHistory']:
            continue

        model_class = apps.get_model("demoproject", record['model'])
        obj = model_class(**record['fields'])
        obj.pk = record['pk']
        obj.save()

    # create Book objects
    for record in data:
        # skip everything which isn't a book
        if record['model'] != 'Book':
            continue

        # build a list of book authors using the intermediate
        # BookAuthors table
        for author_id in record['fields']['authors']:
            author_obj = BookAuthors()
            author_obj.book_id = record['pk']
            author_obj.author_id = author_id
            author_obj.save()
        del record['fields']['authors']

        # build a list of related books
        # fill data for the intermediate BookRelated table
        # due to circular dependencies in the data
        for related_id in record['fields']['related']:
            related_obj = BookRelated()
            related_obj.from_book_id = record['pk']
            related_obj.to_book_id = related_id
            related_obj.save()
        del record['fields']['related']

        model_class = apps.get_model("demoproject", record['model'])
        obj = model_class(**record['fields'])
        obj.pk = record['pk']
        obj.save()

    # now populate the obkects which hold FKs on Book
    for record in data:
        if record['model'] not in ['BookStore', 'SalesHistory']:
            continue

        model_class = apps.get_model("demoproject", record['model'])
        obj = model_class(**record['fields'])
        obj.pk = record['pk']
        obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('demoproject', '0002_chartdemo_initial_data')
    ]

    operations = [
        migrations.RunPython(initial_data),
    ]
