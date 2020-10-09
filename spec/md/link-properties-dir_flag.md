# Untitled integer in link Schema

```txt
undefined#/properties/dir_flag
```

Optional. 
1  shapepoints go from from_node to to_node;
\-1 shapepoints go in the reverse direction;
0  link is undirected or no geometry information is provided.


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                              |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | ----------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [link.schema.json\*](../../out/link.schema.json "open original schema") |

## dir_flag Type

`integer`

## dir_flag Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation |
| :---- | ----------- |
| `-1`  |             |
| `0`   |             |
| `1`   |             |
