# encoding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# Authentication for user filing issue (must have read/write access to repository to add issue to)
USERNAME = 'olozhika'

# The repository to add this issue to
REPO_OWNER = 'B1GeasY'
REPO_NAME = 'ArXivDaily'

# Set new submission url of subject
NEW_SUB_URL = 'https://arxiv.org/list/astro-ph/new'

# Keywords to search
KEYWORD_EX_LIST = ["planet","FRB","GRB","standard candle"]
# Keywords to exclude
KEYWORD_LIST = ["galaxy", "galaxies", " AGN ","star formation"]
# Note that the 'Keywords' above are actually searched in the abstract instead of the real keyword section. 
