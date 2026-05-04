# Chris Lovell's Personal Website

Source code for [christopherlovell.co.uk](https://christopherlovell.co.uk).

## Publication Updates

To update the publication list from the NASA ADS API:

1. Activate the Python virtual environment:
   ```bash
   source ~/venvs/synth/bin/activate
   ```
2. Ensure your NASA ADS API key is exported:
   ```bash
   export ADS_DEV_KEY=your_api_key_here
   ```
3. Run the update script:
   ```bash
   ./bin/update_publications
   ```

This script will:
* Update `publications.tex` with the latest entries from ADS.
* Regenerate `_includes/publications_generated.html` for display on the website.

## Local Development

The site is built using Jekyll. To run the site locally:

1. Install dependencies:
   ```bash
   bundle install
   pip install -r requirements.txt
   ```
2. Serve the site:
   ```bash
   bundle exec jekyll serve
   ```
