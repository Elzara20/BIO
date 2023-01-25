# Поиск фибриллярных белков

**Идея**: по ключевым словам найти фибриллярные белки в PDB ---```fib_protein = Query("fibrous | fibrillar").search()```, разделить на домены --- ```python3 wedjbservice-clients/iprscan5.py```  и найти возможные фибриллярные белки через регулярные выражения в названиях доменов --- ```find_word  =  re.findall('([Ff]ibr[a-z]+)|([Ff]iber)|([Cc]ollagen)|([Kk]eratin)|([Ee]lastin)', line[5])```.

**Реализация**: [colab](https://github.com/Elzara20/BIO/blob/main/forFibProt/%D0%9F%D0%BE%D0%B8%D1%81%D0%BA_%D1%84%D0%B8%D0%B1%D1%80%D0%B8%D0%BB%D0%BB%D1%8F%D1%80%D0%BD%D1%8B%D1%85_%D0%B1%D0%B5%D0%BB%D0%BA%D0%BE%D0%B2.ipynb) (проблема: более 11 часов делит белки - 3663шт. - на домены) + отдельные скрипты ([code.py](https://github.com/Elzara20/BIO/blob/main/forFibProt/code.py), [code.bash](https://github.com/Elzara20/BIO/blob/main/forFibProt/code.bash), [find_fib.py](https://github.com/Elzara20/BIO/blob/main/forFibProt/find_fib.py)) (!!! в скриптах не учтены создание папок и установка библиотек).

**Данные**: в папке [FIB_PROTEIN](https://github.com/Elzara20/BIO/tree/main/forFibProt/FIB_PROTEIN)

**Итог**: всего найденных белков 53, результат вывода в файле [out_fibrous_protein.txt](https://github.com/Elzara20/BIO/blob/main/forFibProt/out_fibrous_protein.txt)

**Литература**: 
1) [Using InterProScan like a pro (статья 2016)](https://medium.com/computer-says-no/using-interproscan-like-a-pro-ad18b8c3ccc0)
