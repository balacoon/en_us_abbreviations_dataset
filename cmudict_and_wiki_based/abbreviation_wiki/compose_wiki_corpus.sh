
wget https://en.wikipedia.org/wiki/Athletics_abbreviations
wget https://en.wikipedia.org/wiki/List_of_business_and_finance_abbreviations
wget https://en.wikipedia.org/wiki/List_of_ecclesiastical_abbreviations
wget https://en.wikipedia.org/wiki/List_of_energy_abbreviations
wget https://en.wikipedia.org/wiki/List_of_glossing_abbreviations
wget https://en.wikipedia.org/wiki/List_of_legal_abbreviations
wget https://en.wikipedia.org/wiki/List_of_medical_abbreviations
wget https://en.wikipedia.org/wiki/List_of_abbreviations_for_medical_organisations_and_personnel
wget https://en.wikipedia.org/wiki/List_of_style_guide_abbreviations
wget https://en.wikipedia.org/wiki/Wikipedia:Wikipedia_abbreviations

> ./abbrev_wiki_corpus
python3 grep_abbreviations.py Athletics_abbreviations "<li><b>([^<]+)</b>" >> ./abbrev_wiki_corpus
python3 grep_abbreviations.py List_of_business_and_finance_abbreviations "<li><b>([^<]+)</b>" >> ./abbrev_wiki_corpus
python3 grep_abbreviations.py List_of_ecclesiastical_abbreviations "<li><b>([^<]+)</b>" >> ./abbrev_wiki_corpus
python3 grep_abbreviations.py List_of_energy_abbreviations "<li>([^—]+)—" >> ./abbrev_wiki_corpus
python3 grep_abbreviations.py List_of_glossing_abbreviations '<td><span class="smallcaps"><span style="font-variant: small-caps; text-transform: lowercase;">([^<]+)</span></span>' >> ./abbrev_wiki_corpus
python3 grep_abbreviations.py List_of_legal_abbreviations "<li>([^ ]+) —" >> ./abbrev_wiki_corpus
python3 grep_abbreviations.py List_of_medical_abbreviations "^<td>(.+)$" >> ./abbrev_wiki_corpus
python3 grep_abbreviations.py List_of_abbreviations_for_medical_organisations_and_personnel "<td>(.+)</td>" >> ./abbrev_wiki_corpus
python3 grep_abbreviations.py List_of_style_guide_abbreviations "<td>(.+)</td>" >> ./abbrev_wiki_corpus
python3 grep_abbreviations.py Wikipedia:Wikipedia_abbreviations "<li>(.+) \(" >> ./abbrev_wiki_corpus

cat ./abbrev_wiki_corpus | sort | uniq > tmp
mv tmp abbrev_wiki_corpus
