# Untitled any in signal_phase_mvmt Schema

```txt
spec/signal_phase_mvmt.schema.json#/properties/protection
```

Optional. Indicates whether the phase is protected, permitted, or right turn on red.


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                        |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | ------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [signal_phase_mvmt.schema.json\*](../../out/signal_phase_mvmt.schema.json "open original schema") |

## protection Type

`any`

## protection Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value         | Explanation |
| :------------ | ----------- |
| `"protected"` |             |
| `"permitted"` |             |
| `"rtor"`      |             |
