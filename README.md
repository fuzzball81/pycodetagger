# pycodetagger
A python source code tagger that stores tag information in a sqlite database

## The Problem
Many source code taggers rely on large files or special database formats to store tag information. When dealing with large source code bases these files can become very large, several GB in size.

Many taggers do not easily support different programming languages, many are only setup for C or C++ code. Some taggers also confuse or are blind to parts of a language.

## The Goal
Create a source code tagger that is flexable and extensable to cover most programming languages. The tag database can be searched with basic SQL queries. The database size is keep minimal even for large project.
