# Untitled schema Schema

```txt
undefined
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                            |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [segment_lane.schema.json](../../out/segment_lane.schema.json "open original schema") |

## Untitled schema Type

unknown

# undefined Properties

| Property                            | Type      | Required | Nullable       | Defined by                                                                                            |
| :---------------------------------- | --------- | -------- | -------------- | :---------------------------------------------------------------------------------------------------- |
| [segment_lane_id](#segment_lane_id) | `any`     | Optional | cannot be null | [Untitled schema](segment_lane-properties-segment_lane_id.md "undefined#/properties/segment_lane_id") |
| [segment_id](#segment_id)           | `any`     | Optional | cannot be null | [Untitled schema](segment_lane-properties-segment_id.md "undefined#/properties/segment_id")           |
| [lane_num](#lane_num)               | `integer` | Optional | cannot be null | [Untitled schema](segment_lane-properties-lane_num.md "undefined#/properties/lane_num")               |
| [parent_lane_id](#parent_lane_id)   | `any`     | Optional | cannot be null | [Untitled schema](segment_lane-properties-parent_lane_id.md "undefined#/properties/parent_lane_id")   |
| [allowed_uses](#allowed_uses)       | `string`  | Optional | cannot be null | [Untitled schema](segment_lane-properties-allowed_uses.md "undefined#/properties/allowed_uses")       |
| [r_barrier](#r_barrier)             | `any`     | Optional | cannot be null | [Untitled schema](segment_lane-properties-r_barrier.md "undefined#/properties/r_barrier")             |
| [l_barrier](#l_barrier)             | `any`     | Optional | cannot be null | [Untitled schema](segment_lane-properties-l_barrier.md "undefined#/properties/l_barrier")             |
| [width](#width)                     | `number`  | Optional | cannot be null | [Untitled schema](segment_lane-properties-width.md "undefined#/properties/width")                     |

## segment_lane_id

Primary key.


`segment_lane_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](segment_lane-properties-segment_lane_id.md "undefined#/properties/segment_lane_id")

### segment_lane_id Type

`any`

## segment_id

Required. Foreign key to the associated segment.


`segment_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](segment_lane-properties-segment_id.md "undefined#/properties/segment_id")

### segment_id Type

`any`

## lane_num

Required. -1, 1, 2 (use left-to-right numbering). 0 signifies a lane that is dropped on the segment.


`lane_num`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](segment_lane-properties-lane_num.md "undefined#/properties/lane_num")

### lane_num Type

`integer`

### lane_num Constraints

**maximum**: the value of this number must smaller than or equal to: `10`

**minimum**: the value of this number must greater than or equal to: `-10`

## parent_lane_id

Optional. If a lane drops or changes characteristics on the segment, the lane_id for that lane.


`parent_lane_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](segment_lane-properties-parent_lane_id.md "undefined#/properties/parent_lane_id")

### parent_lane_id Type

`any`

## allowed_uses

Optional. Set of allowed uses; comma-separated. Foreign key for use group.


`allowed_uses`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](segment_lane-properties-allowed_uses.md "undefined#/properties/allowed_uses")

### allowed_uses Type

`string`

## r_barrier

Optional. Whether a barrier exists to prevent vehicles from changing lanes to the right (default is none)


`r_barrier`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](segment_lane-properties-r_barrier.md "undefined#/properties/r_barrier")

### r_barrier Type

`any`

### r_barrier Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value          | Explanation |
| :------------- | ----------- |
| `""`           |             |
| `"regulatory"` |             |
| `"physical"`   |             |

## l_barrier

Optional. Whether a barrier exists to prevent vehicles from changing lanes to the left (default is none)


`l_barrier`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](segment_lane-properties-l_barrier.md "undefined#/properties/l_barrier")

### l_barrier Type

`any`

### l_barrier Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value          | Explanation |
| :------------- | ----------- |
| `""`           |             |
| `"regulatory"` |             |
| `"physical"`   |             |

## width

Optional. Width of the lane (feet)


`width`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [Untitled schema](segment_lane-properties-width.md "undefined#/properties/width")

### width Type

`number`

### width Constraints

**minimum**: the value of this number must greater than or equal to: `0`
