# FileDB Design Doc

**Summary**:  
Authors: [zyzhang2-zz](https://zyzhang2-zz.github.io)  
Status: Draft  
Created: 2019-01-26  
Last Updated: 2019-01-26  
Self Link: [https://github.com/zyzhang2-zz/filedb/blob/master/README.md](https://github.com/zyzhang2-zz/filedb/blob/master/README.md)

## Project Overview
### Goals
* Make data store cheap and easy for everyone!
* Enahance skills with Github apis and data operation

### Non-Goals
* Harm the benefit of any organization

### Background
* FileDB is NoSQL
* Database CURD -> Git(hub) CURD

## Usage
* Initialize a DAO
```python
from dao import DAO

dao = DAO(FILEDB_TOKEN, FILEDB_PATH)
```
Here ```FILEDB_TOKEN``` should be your Github api token; ```FILEDB_PATH``` should be the Github repository to store the your data ```your_user_name/your_repo_name```.

* Database operations
```python
dao.set(key, value)
dao.get(key)
```

## Detailed Design