"""Code snippets vol-56
   277-Search PubMed with BioPython

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg
   Blog: stevepython.wordpress.com

Requirements:
pip3 install biopython

Origin:
https://gist.github.com/ehazlett/1104507
"""
from Bio import Entrez


def search(query):
    """Leave as is for guest access."""
    Entrez.email = 'your.email@example.com'
    handle = Entrez.esearch(db='pubmed',
                            sort='relevance',
                            retmax='5',
                            retmode='xml',
                            term=query)
    results = Entrez.read(handle)
    return results


def fetch_details(id_list):
    ids = ','.join(id_list)
    Entrez.email = 'your.email@example.com'
    handle = Entrez.efetch(db='pubmed',
                           retmode='xml',
                           id=ids)
    results = Entrez.read(handle)
    return results


if __name__ == '__main__':
    results = search('ADHD')  # <Enter search query here instead of ADHD

    id_list = results['IdList']
    papers = fetch_details(id_list)

    for i, paper in enumerate(papers['PubmedArticle']):
        print("\n{}) {}".format(i+1, paper['MedlineCitation']
                                ['Article']['ArticleTitle']))
