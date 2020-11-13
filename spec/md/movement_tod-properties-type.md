# Untitled string in movement_tod Schema

```txt
spec/movement_tod.schema.json#/properties/type
```

Optional. Describes the type of movement (left, right, thru, etc.).


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                              |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [movement_tod.schema.json\*](../../out/movement_tod.schema.json "open original schema") |

## type Type

`string`

## type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value     | Explanation |
| :-------- | ----------- |
| `"left"`  |             |
| `"right"` |             |
| `"uturn"` |             |
| `"thru"`  |             |
| `"merge"` |             |