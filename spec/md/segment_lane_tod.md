# segment_lane_tod Schema

```txt
undefined
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                    |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [segment_lane_tod.schema.json](../../out/segment_lane_tod.schema.json "open original schema") |

## segment_lane_tod Type

unknown ([segment_lane_tod](segment_lane_tod.md))

# segment_lane_tod Properties

| Property                                    | Type      | Required | Nullable       | Defined by                                                                                                         |
| :------------------------------------------ | --------- | -------- | -------------- | :----------------------------------------------------------------------------------------------------------------- |
| [segment_lane_tod_id](#segment_lane_tod_id) | `any`     | Optional | cannot be null | [segment_lane_tod](segment_lane_tod-properties-segment_lane_tod_id.md "undefined#/properties/segment_lane_tod_id") |
| [segment_lane_id](#segment_lane_id)         | `any`     | Optional | cannot be null | [segment_lane_tod](segment_lane_tod-properties-segment_lane_id.md "undefined#/properties/segment_lane_id")         |
| [timeday_id](#timeday_id)                   | `any`     | Optional | cannot be null | [segment_lane_tod](segment_lane_tod-properties-timeday_id.md "undefined#/properties/timeday_id")                   |
| [time_day](#time_day)                       | `any`     | Optional | cannot be null | [segment_lane_tod](segment_lane_tod-properties-time_day.md "undefined#/properties/time_day")                       |
| [lane_num](#lane_num)                       | `integer` | Optional | cannot be null | [segment_lane_tod](segment_lane_tod-properties-lane_num.md "undefined#/properties/lane_num")                       |
| [allowed_uses](#allowed_uses)               | `string`  | Optional | cannot be null | [segment_lane_tod](segment_lane_tod-properties-allowed_uses.md "undefined#/properties/allowed_uses")               |
| [r_barrier](#r_barrier)                     | `any`     | Optional | cannot be null | [segment_lane_tod](segment_lane_tod-properties-r_barrier.md "undefined#/properties/r_barrier")                     |
| [l_barrier](#l_barrier)                     | `any`     | Optional | cannot be null | [segment_lane_tod](segment_lane_tod-properties-l_barrier.md "undefined#/properties/l_barrier")                     |
| [width](#width)                             | `number`  | Optional | cannot be null | [segment_lane_tod](segment_lane_tod-properties-width.md "undefined#/properties/width")                             |

## segment_lane_tod_id

Primary key.


`segment_lane_tod_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [segment_lane_tod](segment_lane_tod-properties-segment_lane_tod_id.md "undefined#/properties/segment_lane_tod_id")

### segment_lane_tod_id Type

`any`

## segment_lane_id

Required. Foreign key, segment_lane table


`segment_lane_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [segment_lane_tod](segment_lane_tod-properties-segment_lane_id.md "undefined#/properties/segment_lane_id")

### segment_lane_id Type

`any`

## timeday_id

Conditionally required (either timeday_id or time_day). Foreign key to time_set_definitions.


`timeday_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [segment_lane_tod](segment_lane_tod-properties-timeday_id.md "undefined#/properties/timeday_id")

### timeday_id Type

`any`

## time_day

Conditionally required (either timeday_id or time_day). XXXXXXXX_HHMM_HHMM, where XXXXXXXX is a bitmap of days of the week, Sunday-Saturday, Holiday. The HHMM are the start and end times.


`time_day`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [segment_lane_tod](segment_lane_tod-properties-time_day.md "undefined#/properties/time_day")

### time_day Type

`any`

## lane_num

Required. Lane number identified as offset to the right from the centerline. i.e. -1, 1, 2 (use left-to-rightnumbering).


`lane_num`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [segment_lane_tod](segment_lane_tod-properties-lane_num.md "undefined#/properties/lane_num")

### lane_num Type

`integer`

### lane_num Constraints

**maximum**: the value of this number must smaller than or equal to: `10`

**minimum**: the value of this number must greater than or equal to: `-10`

## allowed_uses

Optional. Set of allowed uses; comma-separated. Foreign key to use_definition or use sets.


`allowed_uses`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [segment_lane_tod](segment_lane_tod-properties-allowed_uses.md "undefined#/properties/allowed_uses")

### allowed_uses Type

`string`

## r_barrier

Optional. Whether a barrier exists to prevent vehicles from changing lanes to the right (default is None).

-   '' (the default). Indicates that a vehicle can change lanes, provided that the vehicle-type is permitted in the destination lane
-   `Regulatory`. There is a regulatory prohibition (e.g., a double-white solid line) against changing lanes, but no physical barrier
-   `Physical`. A physical barrier (e.g., a curb, Jersey barrier) is in place.


`r_barrier`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [segment_lane_tod](segment_lane_tod-properties-r_barrier.md "undefined#/properties/r_barrier")

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

Optional. Whether a barrier exists to prevent vehicles from changing lanes to the right (default is None).

-   '' (the default). Indicates that a vehicle can change lanes, provided that the vehicle-type is permitted in the destination lane
-   `Regulatory`. There is a regulatory prohibition (e.g., a double-white solid line) against changing lanes, but no physical barrier
-   `Physical`. A physical barrier (e.g., a curb, Jersey barrier) is in place.


`l_barrier`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [segment_lane_tod](segment_lane_tod-properties-l_barrier.md "undefined#/properties/l_barrier")

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
-   defined in: [segment_lane_tod](segment_lane_tod-properties-width.md "undefined#/properties/width")

### width Type

`number`

### width Constraints

**minimum**: the value of this number must greater than or equal to: `0`
