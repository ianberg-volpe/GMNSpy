# Untitled string in signal_timing_plan Schema

```txt
spec/signal_timing_plan.schema.json#/properties/coord_ref_to
```

Optional. For coordinated signals, the part of the phase where coordination starts: begin_of_green, begin_of_yellow, begin_of_red.


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                          |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [signal_timing_plan.schema.json\*](../../out/signal_timing_plan.schema.json "open original schema") |

## coord_ref_to Type

`string`

## coord_ref_to Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value               | Explanation |
| :------------------ | ----------- |
| `"begin_of_green"`  |             |
| `"begin_of_yellow"` |             |
| `"begin_of_red"`    |             |
