# Shua - A multi-changing data and character output classes.


----------
This is a **very simple** python library that provides a variety of output formats style.


----------
## Methods
```python
Shua.top(char='*', nums=15, rows=1, padding=(0, 0, 0, 0), margin=(0, 0, 0, 0))
Shua.bottom(char='*', nums=15, rows=1, padding=(0, 0, 0, 0), margin=(0, 0, 0, 0))
Shua.row(char=('|', 1), fields=(), padding=(0, 0), margin=(0, 0), length=True)
```


----------
## Parameters
```python
> Shua.top()
        :param char: Output character(default=*,But you can also use any other arbitrary character.);

        :param nums: Number of characters in the output(default=15);

        :param rows: Number of rows in the output(default=1);

        :param padding: A definition of the empty tuple around for every row(
        default=(0,0,0,0),
        padding[0] is the row of top blank,
        padding[2] is the row of bottom blank,
        padding[3] is The number of characters on the left side of the blank,
        padding[1] is the number of characters on the right side of the blank
        )

        :param margin: A definition of the empty tuple around for the output of all(
        default=(0,0,0,0),
        margin[0] is the rows of top blank,
        margin[2] is the rows of bottom blank,
        margin[3] is The number of characters on the left side of the blank,
        margin[1] is the number of characters on the right side of the blank
        )


```


----------
```python
> Shua.bottom()

        :param char: Output character(default=*,But you can also use any other arbitrary character.);

        :param nums: Number of characters in the output(default=15);

        :param rows: Number of rows in the output(default=1);

        :param padding: A definition of the empty tuple around for every row(
        default=(0,0,0,0),
        padding[0] is the row of top blank,
        padding[2] is the row of bottom blank,
        padding[3] is The number of characters on the left side of the blank,
        padding[1] is the number of characters on the right side of the blank
        )

        :param margin: A definition of the empty tuple around for the output of all(
        default=(0,0,0,0),
        margin[0] is the rows of top blank,
        margin[2] is the rows of bottom blank,
        margin[3] is The number of characters on the left side of the blank,
        margin[1] is the number of characters on the right side of the blank
        )

```


----------


```python
> Shua.row()
        :param char: A definition of the character and number of output tuples(default=('|', 1),But you can also use any other arbitrary character.)
        :param fields: One can have multiple fields of tuples(default=())
        :param padding: The left and right margins within the line length(default=(0,0))
        :param margin: The length of the outer row left and right margins(default=(0,0))
        :param length: Whether to output a single line of total length
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
Shua.top(char='-', nums=20, rows=3, padding=(2, 2, 2, 2))
>

  --------------------




  --------------------




  --------------------




```


----------
```python
Shua.top(char='-', nums=20, rows=3, padding=(2, 2, 2, 2))
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
Shua.bottom(char='/', nums=11, rows=2, padding=(0, 0, 1, 0))
> ///////////

  ///////////
```


----------
```python
Shua.bottom(char='/', nums=11, rows=2, padding=(0, 0, 1, 6), margin=(0, 0, 0, 5))
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
Shua.row(fields=('Shua', 'sHua'), padding=(3, 3))
> |   Shua   |   sHua   |
 The length of string is 23
```


----------
```python
Shua.row(fields=('Shua', 'sHua','shUa'), padding=(3, 3), margin=(2, 2))
>   |   Shua   |   sHua   |     shUa   |
 The length of string is 38
```


----------
```python
Shua.row(fields=('Shua', 'sHua', 'shUa', 'shuA'), padding=(3, 3), margin=(2, 2), length=False)
>   |   Shua   |   sHua   |     shUa   |     shuA   |
```


----------
## Changelog
### 0.1
 1. Overwrite `blank` to `padding`
 2. Overwrite `blanks` to `margin`
    `