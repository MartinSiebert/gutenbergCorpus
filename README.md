# gutenbergCorpus
Original publication date metadata for 2912 Project Gutenberg book titles.

The Project Gutenberg (www.gutenberg.org) offers access to a steadily growing number of digitized books under the public domain. While the text files are freely and easily available, metadata ist not. For a research project on dynamic word embeddings trying analyze semantic change of words over time, we undertook the challenge to extract available metadata from gutenberg text files and string match author and title with all available Wikidata entries to retrieve the related original publication date (as Project Gutenberg only provides the ebook publication date).

We make the retrieved and cleansed data publicly available for future reasearch to be performed on this very data set.

Data is provided in in this repository as a tab seperated .csv file - gutenberg_corpus.csv. A short description of the available columns follows:

- bookNo - Project Gutenberg specific book number. Necessary for downloading the needed files from www.gutenberg.org.
- author - Author of the book. Retrieved from the ebook's header.
- year - original publication year of the books hard copy. Retrieved from Wikidata's SPARQL endpoint by stringmatching author and book title using Jaro Winkler with a threshold of 90 on the title and 70 on the author. 
- title - Title of the book. Retrieved from the ebook's header.
