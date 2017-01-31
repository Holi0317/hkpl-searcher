# Hong Kong public library searcher
A small script designed to search public library books in bulk

I built this because of 好書龍虎榜. It is hard to search for books 60 books at once. Therefore this is written in order to finish that.

# Usage
1. Install Python and pipenv
2. Install dependencies by running `pipenv install`
2. Run main.py
3. Use result printed on screen. Go to library and borrow it.
4. Finish that (God damn) homework

By default, it will only search for books available in Tiu King Leng library. This is hardcoded.

You can amend that by changing the variable, `LIBRARY_LOCATION`, to the code of your library location.

# Book list
The book list included is the 28th of 好書龍虎榜, reading report done in 2016-2017 academic year.

To update the list, enter ISBN of the books into `books` file.
