Sort

Sort by multiple keys

python sort by multiple keys

```
ret.sort(key=lambda x:(x[2],x[1],x[0]))
```

set the second key as reverse order

```
ret.sort(key=lambda x:(x[2],-x[1],x[0]))
```

