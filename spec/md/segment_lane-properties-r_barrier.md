# Untitled any in segment_lane Schema

```txt
spec/segment_lane.schema.json#/properties/r_barrier
```

Optional. Whether a barrier exists to prevent vehicles from changing lanes to the right (default is none)


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                              |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [segment_lane.schema.json\*](../../out/segment_lane.schema.json "open original schema") |

## r_barrier Type

`any`

## r_barrier Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value          | Explanation |
| :------------- | ----------- |
| `""`           |             |
| `"regulatory"` |             |
| `"physical"`   |             |
