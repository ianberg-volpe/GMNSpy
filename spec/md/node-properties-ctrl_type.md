# Untitled string in node Schema

```txt
spec/node.schema.json#/properties/ctrl_type
```

Optional. Intersection control type - one of ControlType_Set.


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                              |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | ----------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [node.schema.json\*](../../out/node.schema.json "open original schema") |

## ctrl_type Type

`string`

## ctrl_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value      | Explanation |
| :--------- | ----------- |
| `"none"`   |             |
| `"yield"`  |             |
| `"stop"`   |             |
| `"4_stop"` |             |
| `"signal"` |             |
