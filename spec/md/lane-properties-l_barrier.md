# Untitled any in lane Schema

```txt
undefined#/properties/l_barrier
```

Optional. Whether a barrier exists to prevent vehicles from changing lanes to the right (default is none).

-   '' (the default). Indicates that a vehicle can change lanes, provided that the vehicle-type is permitted in the destination lane
-   `regulatory`. There is a regulatory prohibition (e.g., a double-white solid line) against changing lanes, but no physical barrier
-   `physical`. A physical barrier (e.g., a curb, Jersey barrier) is in place.


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                              |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | ----------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [lane.schema.json\*](../../out/lane.schema.json "open original schema") |

## l_barrier Type

`any`

## l_barrier Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value          | Explanation |
| :------------- | ----------- |
| `""`           |             |
| `"regulatory"` |             |
| `"physical"`   |             |
