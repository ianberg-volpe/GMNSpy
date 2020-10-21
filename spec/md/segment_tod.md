# segment_tod Schema

```txt
spec/segment_tod.schema.json
```

An optional file that handles day-of-week and time-of-day restrictions on segments. It is used for part-time changes in segment capacity and number of lanes.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                          |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [segment_tod.schema.json](../../out/segment_tod.schema.json "open original schema") |

## segment_tod Type

unknown ([segment_tod](segment_tod.md))

# segment_tod Properties

| Property                          | Type      | Required | Nullable       | Defined by                                                                                                        |
| :-------------------------------- | --------- | -------- | -------------- | :---------------------------------------------------------------------------------------------------------------- |
| [segment_tod_id](#segment_tod_id) | `any`     | Required | cannot be null | [segment_tod](segment_tod-properties-segment_tod_id.md "spec/segment_tod.schema.json#/properties/segment_tod_id") |
| [segment_id](#segment_id)         | `any`     | Required | cannot be null | [segment_tod](segment_tod-properties-segment_id.md "spec/segment_tod.schema.json#/properties/segment_id")         |
| [timeday_id](#timeday_id)         | `any`     | Optional | cannot be null | [segment_tod](segment_tod-properties-timeday_id.md "spec/segment_tod.schema.json#/properties/timeday_id")         |
| [time_day](#time_day)             | `any`     | Optional | cannot be null | [segment_tod](segment_tod-properties-time_day.md "spec/segment_tod.schema.json#/properties/time_day")             |
| [capacity](#capacity)             | `integer` | Optional | cannot be null | [segment_tod](segment_tod-properties-capacity.md "spec/segment_tod.schema.json#/properties/capacity")             |
| [free_speed](#free_speed)         | `integer` | Optional | cannot be null | [segment_tod](segment_tod-properties-free_speed.md "spec/segment_tod.schema.json#/properties/free_speed")         |
| [lanes](#lanes)                   | `integer` | Optional | cannot be null | [segment_tod](segment_tod-properties-lanes.md "spec/segment_tod.schema.json#/properties/lanes")                   |
| [l_lanes_added](#l_lanes_added)   | `integer` | Optional | cannot be null | [segment_tod](segment_tod-properties-l_lanes_added.md "spec/segment_tod.schema.json#/properties/l_lanes_added")   |
| [r_lanes_added](#r_lanes_added)   | `integer` | Optional | cannot be null | [segment_tod](segment_tod-properties-r_lanes_added.md "spec/segment_tod.schema.json#/properties/r_lanes_added")   |
| [bike_facility](#bike_facility)   | `string`  | Optional | cannot be null | [segment_tod](segment_tod-properties-bike_facility.md "spec/segment_tod.schema.json#/properties/bike_facility")   |
| [ped_facility](#ped_facility)     | `string`  | Optional | cannot be null | [segment_tod](segment_tod-properties-ped_facility.md "spec/segment_tod.schema.json#/properties/ped_facility")     |
| [parking](#parking)               | `string`  | Optional | cannot be null | [segment_tod](segment_tod-properties-parking.md "spec/segment_tod.schema.json#/properties/parking")               |
| [toll](#toll)                     | `integer` | Optional | cannot be null | [segment_tod](segment_tod-properties-toll.md "spec/segment_tod.schema.json#/properties/toll")                     |
| [allowed_uses](#allowed_uses)     | `string`  | Optional | cannot be null | [segment_tod](segment_tod-properties-allowed_uses.md "spec/segment_tod.schema.json#/properties/allowed_uses")     |

## segment_tod_id

Primary key.


`segment_tod_id`

-   is required
-   Type: `any`
-   cannot be null
-   defined in: [segment_tod](segment_tod-properties-segment_tod_id.md "spec/segment_tod.schema.json#/properties/segment_tod_id")

### segment_tod_id Type

`any`

## segment_id

Foreign key to segment table.


`segment_id`

-   is required
-   Type: `any`
-   cannot be null
-   defined in: [segment_tod](segment_tod-properties-segment_id.md "spec/segment_tod.schema.json#/properties/segment_id")

### segment_id Type

`any`

## timeday_id

Conditionally required (either timeday_id or time_day). Foreign key to time_set_definitions.


`timeday_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [segment_tod](segment_tod-properties-timeday_id.md "spec/segment_tod.schema.json#/properties/timeday_id")

### timeday_id Type

`any`

## time_day

Conditionally required (either timeday_id or time_day). XXXXXXXX_HHMM_HHMM, where XXXXXXXX is a bitmap of days of the week, Sunday-Saturday, Holiday. The HHMM are the start and end times.


`time_day`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [segment_tod](segment_tod-properties-time_day.md "spec/segment_tod.schema.json#/properties/time_day")

### time_day Type

`any`

## capacity

Optional. Capacity (veh/hr/ln)


`capacity`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [segment_tod](segment_tod-properties-capacity.md "spec/segment_tod.schema.json#/properties/capacity")

### capacity Type

`integer`

### capacity Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## free_speed

Optional. Free flow speed (mph)


`free_speed`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [segment_tod](segment_tod-properties-free_speed.md "spec/segment_tod.schema.json#/properties/free_speed")

### free_speed Type

`integer`

### free_speed Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## lanes

Optional. Number of lanes in the direction of travel (must be consistent with link lanes + lanes added).


`lanes`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [segment_tod](segment_tod-properties-lanes.md "spec/segment_tod.schema.json#/properties/lanes")

### lanes Type

`integer`

## l_lanes_added

Optional. # of lanes added on the left of the road link (negative indicates a lane drop).


`l_lanes_added`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [segment_tod](segment_tod-properties-l_lanes_added.md "spec/segment_tod.schema.json#/properties/l_lanes_added")

### l_lanes_added Type

`integer`

## r_lanes_added

Optional. # of lanes added on the right of the road link (negative indicates a lane drop).


`r_lanes_added`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [segment_tod](segment_tod-properties-r_lanes_added.md "spec/segment_tod.schema.json#/properties/r_lanes_added")

### r_lanes_added Type

`integer`

## bike_facility

Optional. Type of bicycle accommodation: unknown, none,wcl, bikelane,cycletrack,wide_shoulder, offstreet_path.


`bike_facility`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [segment_tod](segment_tod-properties-bike_facility.md "spec/segment_tod.schema.json#/properties/bike_facility")

### bike_facility Type

`string`

### bike_facility Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value              | Explanation |
| :----------------- | ----------- |
| `"unknown"`        |             |
| `"none"`           |             |
| `"wcl"`            |             |
| `"bikelane"`       |             |
| `"cycletrack"`     |             |
| `"wide_shoulder"`  |             |
| `"offstreet_path"` |             |

## ped_facility

Optional. Type of pedestrian accommodation: unknown,none,shoulder,sidewalk,offstreet_path.


`ped_facility`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [segment_tod](segment_tod-properties-ped_facility.md "spec/segment_tod.schema.json#/properties/ped_facility")

### ped_facility Type

`string`

### ped_facility Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value              | Explanation |
| :----------------- | ----------- |
| `"unknown"`        |             |
| `"none"`           |             |
| `"shoulder"`       |             |
| `"sidewalk"`       |             |
| `"offstreet_path"` |             |

## parking

Optional. Type of parking: unknown,none,shoulder,sidewalk,offstreet_path.


`parking`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [segment_tod](segment_tod-properties-parking.md "spec/segment_tod.schema.json#/properties/parking")

### parking Type

`string`

### parking Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value              | Explanation |
| :----------------- | ----------- |
| `"unknown"`        |             |
| `"none"`           |             |
| `"shoulder"`       |             |
| `"sidewalk"`       |             |
| `"offstreet_path"` |             |

## toll

Optional. Toll in cents


`toll`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [segment_tod](segment_tod-properties-toll.md "spec/segment_tod.schema.json#/properties/toll")

### toll Type

`integer`

## allowed_uses

Optional. Set of allowed uses; comma-separated. Foreign key to use_definition or use sets.


`allowed_uses`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [segment_tod](segment_tod-properties-allowed_uses.md "spec/segment_tod.schema.json#/properties/allowed_uses")

### allowed_uses Type

`string`
