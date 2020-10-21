# movement_tod Schema

```txt
spec/movement_tod.schema.json
```

Handles day-of-week and time-of-day restrictions on movements.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                            |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [movement_tod.schema.json](../../out/movement_tod.schema.json "open original schema") |

## movement_tod Type

unknown ([movement_tod](movement_tod.md))

# movement_tod Properties

| Property                        | Type      | Required | Nullable       | Defined by                                                                                                         |
| :------------------------------ | --------- | -------- | -------------- | :----------------------------------------------------------------------------------------------------------------- |
| [mvmt_tod_id](#mvmt_tod_id)     | `any`     | Required | cannot be null | [movement_tod](movement_tod-properties-mvmt_tod_id.md "spec/movement_tod.schema.json#/properties/mvmt_tod_id")     |
| [mvmt_id](#mvmt_id)             | `any`     | Required | cannot be null | [movement_tod](movement_tod-properties-mvmt_id.md "spec/movement_tod.schema.json#/properties/mvmt_id")             |
| [time_day](#time_day)           | `string`  | Optional | cannot be null | [movement_tod](movement_tod-properties-time_day.md "spec/movement_tod.schema.json#/properties/time_day")           |
| [timeday_id](#timeday_id)       | `string`  | Optional | cannot be null | [movement_tod](movement_tod-properties-timeday_id.md "spec/movement_tod.schema.json#/properties/timeday_id")       |
| [ib_link_id](#ib_link_id)       | `any`     | Required | cannot be null | [movement_tod](movement_tod-properties-ib_link_id.md "spec/movement_tod.schema.json#/properties/ib_link_id")       |
| [start_ib_lane](#start_ib_lane) | `integer` | Optional | cannot be null | [movement_tod](movement_tod-properties-start_ib_lane.md "spec/movement_tod.schema.json#/properties/start_ib_lane") |
| [end_ib_lane](#end_ib_lane)     | `integer` | Optional | cannot be null | [movement_tod](movement_tod-properties-end_ib_lane.md "spec/movement_tod.schema.json#/properties/end_ib_lane")     |
| [ob_link_id](#ob_link_id)       | `any`     | Required | cannot be null | [movement_tod](movement_tod-properties-ob_link_id.md "spec/movement_tod.schema.json#/properties/ob_link_id")       |
| [start_ob_lane](#start_ob_lane) | `integer` | Optional | cannot be null | [movement_tod](movement_tod-properties-start_ob_lane.md "spec/movement_tod.schema.json#/properties/start_ob_lane") |
| [end_ob_lane](#end_ob_lane)     | `integer` | Optional | cannot be null | [movement_tod](movement_tod-properties-end_ob_lane.md "spec/movement_tod.schema.json#/properties/end_ob_lane")     |
| [type](#type)                   | `string`  | Required | cannot be null | [movement_tod](movement_tod-properties-type.md "spec/movement_tod.schema.json#/properties/type")                   |
| [penalty](#penalty)             | `any`     | Optional | cannot be null | [movement_tod](movement_tod-properties-penalty.md "spec/movement_tod.schema.json#/properties/penalty")             |
| [capacity](#capacity)           | `any`     | Optional | cannot be null | [movement_tod](movement_tod-properties-capacity.md "spec/movement_tod.schema.json#/properties/capacity")           |
| [ctrl_type](#ctrl_type)         | `any`     | Optional | cannot be null | [movement_tod](movement_tod-properties-ctrl_type.md "spec/movement_tod.schema.json#/properties/ctrl_type")         |

## mvmt_tod_id

Primary key.


`mvmt_tod_id`

-   is required
-   Type: `any`
-   cannot be null
-   defined in: [movement_tod](movement_tod-properties-mvmt_tod_id.md "spec/movement_tod.schema.json#/properties/mvmt_tod_id")

### mvmt_tod_id Type

`any`

## mvmt_id

The referenced movement.


`mvmt_id`

-   is required
-   Type: `any`
-   cannot be null
-   defined in: [movement_tod](movement_tod-properties-mvmt_id.md "spec/movement_tod.schema.json#/properties/mvmt_id")

### mvmt_id Type

`any`

## time_day

Time of day in XXXXXXXX_HHMM_HHMM format, where XXXXXXXX is a bitmap of days of the week, Sunday-Saturday, Holiday. The HHMM are the start and end times.


`time_day`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [movement_tod](movement_tod-properties-time_day.md "spec/movement_tod.schema.json#/properties/time_day")

### time_day Type

`string`

## timeday_id

Time of day set. Used if times-of-day are defined on the time_set_definitions table


`timeday_id`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [movement_tod](movement_tod-properties-timeday_id.md "spec/movement_tod.schema.json#/properties/timeday_id")

### timeday_id Type

`string`

## ib_link_id

Inbound link id.


`ib_link_id`

-   is required
-   Type: `any`
-   cannot be null
-   defined in: [movement_tod](movement_tod-properties-ib_link_id.md "spec/movement_tod.schema.json#/properties/ib_link_id")

### ib_link_id Type

`any`

## start_ib_lane

Innermost lane number the movement applies to at the inbound end.


`start_ib_lane`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [movement_tod](movement_tod-properties-start_ib_lane.md "spec/movement_tod.schema.json#/properties/start_ib_lane")

### start_ib_lane Type

`integer`

## end_ib_lane

Outermost lane number the movement applies to at the inbound end. Blank indicates a movement with a single inbound lane.


`end_ib_lane`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [movement_tod](movement_tod-properties-end_ib_lane.md "spec/movement_tod.schema.json#/properties/end_ib_lane")

### end_ib_lane Type

`integer`

## ob_link_id

Outbound link id.


`ob_link_id`

-   is required
-   Type: `any`
-   cannot be null
-   defined in: [movement_tod](movement_tod-properties-ob_link_id.md "spec/movement_tod.schema.json#/properties/ob_link_id")

### ob_link_id Type

`any`

## start_ob_lane

Innermost lane number the movement applies to at the outbound end.


`start_ob_lane`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [movement_tod](movement_tod-properties-start_ob_lane.md "spec/movement_tod.schema.json#/properties/start_ob_lane")

### start_ob_lane Type

`integer`

## end_ob_lane

Outermost lane number the movement applies to at the outbound end. Blank indicates a movement with a single outbound lane.


`end_ob_lane`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [movement_tod](movement_tod-properties-end_ob_lane.md "spec/movement_tod.schema.json#/properties/end_ob_lane")

### end_ob_lane Type

`integer`

## type

Optional. Describes the type of movement (left, right, thru, etc.).


`type`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [movement_tod](movement_tod-properties-type.md "spec/movement_tod.schema.json#/properties/type")

### type Type

`string`

### type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value     | Explanation |
| :-------- | ----------- |
| `"left"`  |             |
| `"right"` |             |
| `"uturn"` |             |
| `"thru"`  |             |
| `"merge"` |             |

## penalty

Turn penalty (seconds)


`penalty`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [movement_tod](movement_tod-properties-penalty.md "spec/movement_tod.schema.json#/properties/penalty")

### penalty Type

`any`

## capacity

Capacity in vehicles per hour.


`capacity`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [movement_tod](movement_tod-properties-capacity.md "spec/movement_tod.schema.json#/properties/capacity")

### capacity Type

`any`

## ctrl_type

Optional. .


`ctrl_type`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [movement_tod](movement_tod-properties-ctrl_type.md "spec/movement_tod.schema.json#/properties/ctrl_type")

### ctrl_type Type

`any`

### ctrl_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value      | Explanation |
| :--------- | ----------- |
| `"none"`   |             |
| `"yield"`  |             |
| `"stop"`   |             |
| `"4_stop"` |             |
| `"signal"` |             |
