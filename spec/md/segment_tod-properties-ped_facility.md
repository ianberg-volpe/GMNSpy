# Untitled string in segment_tod Schema

```txt
spec/segment_tod.schema.json#/properties/ped_facility
```

Optional. Type of pedestrian accommodation: unknown,none,shoulder,sidewalk,offstreet_path.


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                            |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | ------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [segment_tod.schema.json\*](../../out/segment_tod.schema.json "open original schema") |

## ped_facility Type

`string`

## ped_facility Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value              | Explanation |
| :----------------- | ----------- |
| `"unknown"`        |             |
| `"none"`           |             |
| `"shoulder"`       |             |
| `"sidewalk"`       |             |
| `"offstreet_path"` |             |