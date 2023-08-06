# Alphac Registration Code

This is a Small Package For Generate Increment Registration Code.
The Format is : CustomTextYYYYMMIncrementCode 

### How To Use :

##### 1. Import Module Name
#
```Python
import alregcode
```
##### 2. Use Syntax
#
>regGenerate("Your Custom String", Start Number, CodeLength)
#
```Python
regGenerate("TEST", 0, 4)
```
##### For Get Increment Number, Just Write
#
```Python
regGenerate.inc
```

### Example :
 I Want Generate and Print Registration Code With Condition :
 1. I Want to Use "ALPHAC" Word to be First
 2. I Want The Increment Start From Number 00001
 
So i Write :

```Python
from alregcode import regGenerate

test = regGenerate("ALPHAC", 0, 5)
print(test)
```

#### Output : 
> ALPHAC20190100001
 


