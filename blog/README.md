# Technical blog

The portfolio remains a static GitHub Pages site. The blog lives at `/blog/` and Stingray's journal at `/blog/stingray/`.

To add an activity, append an object to the `logs` array in `blog/content.json` with a unique date-prefixed slug, date, title, category, status, summary, and sections (heading/text pairs). Optional photos should be placed in `blog/assets/` with descriptive alt text and captions. Do not include unverified causes, measurements, or private information.

Run `python3 blog/build.py` from the repository root, then commit the content and generated HTML in a pull request. Technical articles use the separate `articles` array. No additional dependencies, backend, or build service are required.
