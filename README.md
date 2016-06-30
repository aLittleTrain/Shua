# Shua - A multi-changing data and character output classes


----------
This is a **very simple** python library that provides a variety of output formats style.


----------
## Methods
```python
Shua.top(char='*', nums=15, rows=1, blank=(0, 0, 0, 0), blanks=(0, 0, 0, 0))
Shua.bottom(char='*', nums=15, rows=1, blank=(0, 0, 0, 0), blanks=(0, 0, 0, 0))
Shua.row(char=('|', 1), fields=(), blank=(0, 0), blanks=(0, 0), length=True)
```


----------
## Parameters
```python
> Shua.top()
        1. :param char: Output character(default=*,But you can also use any other arbitrary character.);
        2. :param nums: Number of characters in the output(default=15);
        3. :param rows: Number of rows in the output(default=1);
        4. :param blank: A definition of the empty tuple around for every row(
        default=(0,0,0,0),
        blank[0] is the row of top blank,
        blank[2] is the row of bottom blank,
        blank[3] is The number of characters on the left side of the blank,
        blank[1] is the number of characters on the right side of the blank
        )
        5. :param blanks: A definition of the empty tuple around for the output of all(
        default=(0,0,0,0),
        blank[0] is the rows of top blank,
        blank[2] is the rows of bottom blank,
        blank[3] is The number of characters on the left side of the blank,
        blank[1] is the number of characters on the right side of the blank
        )
        

```


----------
```python
> Shua.bottom()
        1. :param char: Output character(default=*,But you can also use any other arbitrary character.);
        2. :param nums: Number of characters in the output(default=15);
        3. :param rows: Number of rows in the output(default=1);
        4. :param blank: A definition of the empty tuple around for every row(
        default=(0,0,0,0),
        blank[0] is the row of top blank,
        blank[2] is the row of bottom blank,
        blank[3] is The number of characters on the left side of the blank,
        blank[1] is the number of characters on the right side of the blank
        )
        5. :param blanks: A definition of the empty tuple around for the output of all(
        default=(0,0,0,0),
        blank[0] is the rows of top blank,
        blank[2] is the rows of bottom blank,
        blank[3] is The number of characters on the left side of the blank,
        blank[1] is the number of characters on the right side of the blank
        )
```


----------


```python
> Shua.row()
        1. :param char: A definition of the character and number of output tuples(default=('|', 1),But you can also use any other arbitrary character.)
        2. :param fields: One can have multiple fields of tuples(default=())
        3. :param blank: The left and right margins within the line length(default=(0,0))
        4. :param blanks: The length of the outer row left and right margins(default=(0,0))
        5. :param length: Whether to output a single line of total length
```


----------

## Examples
```python
Shua.top()
> ***************

```


----------

```python
Shua.top(char='-', nums=20, rows=3)
> --------------------
  --------------------
  --------------------
```


----------
```python
Shua.top(char='-', nums=20, rows=3, blank=(2, 2, 2, 2))
> 

  --------------------  




  --------------------  




  --------------------  




```


----------
```python
Shua.top(char='-', nums=20, rows=3, blank=(2, 2, 2, 2))
> 
  --------------------  
  --------------------  
  --------------------  




```


----------
```python
Shua.bottom(char='/', nums=11)
> ///////////
```


----------
```python
Shua.bottom(char='/', nums=11, rows=2, blank=(0, 0, 1, 0))
> ///////////

  ///////////
```


----------
```python
Shua.bottom(char='/', nums=11, rows=2, blank=(0, 0, 1, 6), blanks=(0, 0, 0, 5))
>            ///////////

             ///////////



```


----------
```python
Shua.row(fields=('Shua',))
> |Shua|
 The length of string is 6
```


----------
```python
Shua.row(fields=('Shua', 'sHua'), blank=(3, 3))
> |   Shua   |   sHua   |
 The length of string is 23
```


----------
```python
Shua.row(fields=('Shua', 'sHua','shUa'), blank=(3, 3), blanks=(2, 2))
>   |   Shua   |   sHua   |     shUa   |
 The length of string is 38
```


----------
```python
Shua.row(fields=('Shua', 'sHua', 'shUa', 'shuA'), blank=(3, 3), blanks=(2, 2), length=False)
>   |   Shua   |   sHua   |     shUa   |     shuA   |
```


----------