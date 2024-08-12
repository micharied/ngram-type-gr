# Extraction and Transformation of german n-grams

This section contains the code used to extract german n-grams. The code is heavily based on the work of  
https://github.com/edmundlam/ngram-type-fr/ and contains only minor adjustments.

The source data `wordlist.csv` was obtained from https://www.ids-mannheim.de/digspra/kl/projekte/methoden/derewo/#c9778,
which is a frequency table of the most common german words built by:

Institut für Deutsche Sprache (2014): Korpusbasierte  
Wortformenliste DeReWo, DeReKo-2014-II-MainArchive-STT.100000,  
http://www.ids-mannheim.de/derewo,  
Institut für Deutsche Sprache, 
Programmbereich Korpuslinguistik, Mannheim, Deutschland 

---

and which is licensed under:

Creative Commons License
Attribution-NonCommercial 3.0 Unported (CC BY-NC 3.0)
(http://creativecommons.org/licenses/by-nc/3.0).

---

Use the scripts in the follwing order:
1. sortwordlist.py
2. extract.py
3. transform.py

Note that this code may not be optimal
at all, but it does the job.