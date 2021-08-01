"""Scrape A Table

   stevepython.wordpress.com
   code-snippet-vol_42-snip_206


pip3 install pandas

source:
https://stackoverflow.com/questions/59669139/is-there-a-way-to-search-for-a-specific-div-in-an-html-comment-using-python-an
"""

import pandas as pd

# Original source example, baseball.
#df = pd.read_html("https://www.baseball-reference.com/teams/OAK/2019.shtml")[0]

# Premier league table.
df = pd.read_html("https://www.skysports.com/premier-league-table")[0]

# Movie Box Office.
#df = pd.read_html("https://www.imdb.com/chart/boxoffice?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=d120b30e-f0de-4d19-a67b-80c0ca1f8c6e&pf_rd_r=XRW55SFQ53NR5F7XTRCD&pf_rd_s=right-6&pf_rd_t=15061&pf_rd_i=homepage&ref_=hm_cht_hd")[0]


df.to_csv("out.csv", index=False)
