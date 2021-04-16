# mark2code
mark2code is a utility to convert markdown in raw code, it converts all the:
```
CODE BLOCKS LIKE THIS
```
in raw code

## Usage
If you have a `CODE.md` file and you want to convert it on a `main.c` file you do:
```sh
python main.py CODE.md main.c
```
mark2code requires specific settings, in the top of your file you should put a
`codeset` code block with all of your settings, the `lang` is for the language,
for example if it's a C program all the codeblocks are in C language so you
write
```
```c
```
```
```
```codeset
{
    "lang": "c"
}
```
so mark2code will put in the raw file only the codeblocks of lang `lang`
