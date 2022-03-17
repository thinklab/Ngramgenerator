# Name generator
Generate some new names lookalike text from tokenized(*.tok file)

https://en.wikipedia.org/wiki/N-gram

## Example
Source (names from Wikipedia ):

https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%9F%D1%80%D0%B0%D0%B2%D0%BE%D1%81%D0%BB%D0%B0%D0%B2%D0%BD%D1%8B%D0%B5_%D0%B8%D0%BC%D0%B5%D0%BD%D0%B0
https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B5_%D0%BC%D1%83%D0%B6%D1%81%D0%BA%D0%B8%D0%B5_%D0%B8%D0%BC%D0%B5%D0%BD%D0%B0

```text
Авдей
Авксентий
Агапит
Агафон
Акакий
Александр
Алексей
Альберт
Альвиан
Анатолий
Андрей
Аникита
Антон
Антонин
Анфим
Аристарх
Аркадий
```

## Tokenize text:
```shell script
    letter_tokenizer.py < rus.txt > rus.tok
```
### Result:

Original text is divided by words and letters: 

```text
а л ь в и а н
а н а т о л и й
а н д р е й
а н и к и т а
а н т о н
а н т о н и н
а н ф и м
а р и с т а р х
а р к а д и й
а р с е н и й
а р т ё м
а р т е м и й
а р т у р
а р х и п п
а ф а н а с и й
б о г д а н
б о р и с
в а в и л а
в а д и м
в а л е н т и н
в а л е р и й
в а л е р ь я н
в а р л а м
в а р с о н о ф и й
в а р ф о л о м е й
в а с и л и й
в е н е д и к т
```


## Generate new words:

```shell script
    markovModel.py < rus.tok > out.txt
```

### Result:
New names will be fictional and similar to the original names.

```text
вельян
расилипп
иулица
ар
лав
лукий
кадий
веленидордей
куприй
влай
гермар
виадленикакапиам
```
