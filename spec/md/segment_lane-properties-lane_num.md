# Untitled integer in undefined Schema

```txt
undefined#/properties/lane_num
```

Required. -1, 1, 2 (use left-to-right numbering). 0 signifies a lane that is dropped on the segment.


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                              |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [segment_lane.schema.json\*](../../out/segment_lane.schema.json "open original schema") |

## lane_num Type

`integer`

## lane_num Constraints

**maximum**: the value of this number must smaller than or equal to: `10`

**minimum**: the value of this number must greater than or equal to: `-10`
