# Untitled any in undefined Schema

```txt
undefined#/properties/6
```

Optional. Whether a barrier exists to prevent vehicles from changing lanes to the right (default is None).

-   '' (the default). Indicates that a vehicle can change lanes, provided that the vehicle-type is permitted in the destination lane
-   `Regulatory`. There is a regulatory prohibition (e.g., a double-white solid line) against changing lanes, but no physical barrier
-   `Physical`. A physical barrier (e.g., a curb, Jersey barrier) is in place.


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                      |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | ------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [lane_tod.schema.json\*](../../out/lane_tod.schema.json "open original schema") |

## 6 Type

`any`
