# Untitled schema Schema

```txt
undefined
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                            |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [lane.schema.json](../../out/lane.schema.json "open original schema") |

## Untitled schema Type

unknown

# undefined Properties

| Property                      | Type      | Required | Nullable       | Defined by                                                                              |
| :---------------------------- | --------- | -------- | -------------- | :-------------------------------------------------------------------------------------- |
| [lane_id](#lane_id)           | `any`     | Optional | cannot be null | [Untitled schema](lane-properties-lane_id.md "undefined#/properties/lane_id")           |
| [link_id](#link_id)           | `any`     | Optional | cannot be null | [Untitled schema](lane-properties-link_id.md "undefined#/properties/link_id")           |
| [lane_num](#lane_num)         | `integer` | Optional | cannot be null | [Untitled schema](lane-properties-lane_num.md "undefined#/properties/lane_num")         |
| [allowed_uses](#allowed_uses) | `string`  | Optional | cannot be null | [Untitled schema](lane-properties-allowed_uses.md "undefined#/properties/allowed_uses") |
| [r_barrier](#r_barrier)       | `any`     | Optional | cannot be null | [Untitled schema](lane-properties-r_barrier.md "undefined#/properties/r_barrier")       |
| [l_barrier](#l_barrier)       | `any`     | Optional | cannot be null | [Untitled schema](lane-properties-l_barrier.md "undefined#/properties/l_barrier")       |
| [width](#width)               | `number`  | Optional | cannot be null | [Untitled schema](lane-properties-width.md "undefined#/properties/width")               |

## lane_id

Primary key


`lane_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](lane-properties-lane_id.md "undefined#/properties/lane_id")

### lane_id Type

`any`

## link_id

Required. Foreign key to link table.


`link_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](lane-properties-link_id.md "undefined#/properties/link_id")

### link_id Type

`any`

## lane_num

Required. e.g., -1, 1, 2 (use left-to-right numbering).


`lane_num`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](lane-properties-lane_num.md "undefined#/properties/lane_num")

### lane_num Type

`integer`

## allowed_uses

Required. Set of allowed uses from Use_set: shoulder, parking, walk, all, bike, auto, hov2, hov3, truck, bus, etc.


`allowed_uses`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](lane-properties-allowed_uses.md "undefined#/properties/allowed_uses")

### allowed_uses Type

`string`

## r_barrier

Optional. Whether a barrier exists to prevent vehicles from changing lanes to the right (default is none).

-   '' (the default). Indicates that a vehicle can change lanes, provided that the vehicle-type is permitted in the destination lane
-   `regulatory`. There is a regulatory prohibition (e.g., a double-white solid line) against changing lanes, but no physical barrier
-   `physical`. A physical barrier (e.g., a curb, Jersey barrier) is in place.


`r_barrier`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](lane-properties-r_barrier.md "undefined#/properties/r_barrier")

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

Optional. Whether a barrier exists to prevent vehicles from changing lanes to the right (default is none).

-   '' (the default). Indicates that a vehicle can change lanes, provided that the vehicle-type is permitted in the destination lane
-   `regulatory`. There is a regulatory prohibition (e.g., a double-white solid line) against changing lanes, but no physical barrier
-   `physical`. A physical barrier (e.g., a curb, Jersey barrier) is in place.


`l_barrier`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](lane-properties-l_barrier.md "undefined#/properties/l_barrier")

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

Optional. Width of the lane, feet.


`width`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [Untitled schema](lane-properties-width.md "undefined#/properties/width")

### width Type

`number`

### width Constraints

**minimum**: the value of this number must greater than or equal to: `0`
