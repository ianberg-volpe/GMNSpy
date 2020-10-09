# Untitled integer in lane_tod Schema

```txt
undefined#/properties/lane_num
```

Required. Lane number identified as offset to the right from the centerline. i.e. -1, 1, 2 (use left-to-rightnumbering).


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                      |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | ------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [lane_tod.schema.json\*](../../out/lane_tod.schema.json "open original schema") |

## lane_num Type

`integer`

## lane_num Constraints

**maximum**: the value of this number must smaller than or equal to: `10`

**minimum**: the value of this number must greater than or equal to: `-10`
