# Letters from Oakakhi

All letters live in `tools/letters.py`, in the `POSTS` list.

To add a letter, copy one entry and change `slug`, `date`, `tag`, `title`,
`dek` (one line summary), `description` (shown on Google), `hero` (an image
in `assets/img/`), `hero_alt`, `read` (minutes) and `body` (HTML). Then run:

    python3 tools/letters.py

This rebuilds `letters/`, the three newest letters shown on the home page,
`letters/feed.xml`, `sitemap.xml` and `robots.txt`.
