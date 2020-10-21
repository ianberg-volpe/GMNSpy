# link_tod Schema

```txt
spec/link_tod.schema.json
```

Handles day-of-week and time-of-day restrictions on links


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                    |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ----------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [link_tod.schema.json](../../out/link_tod.schema.json "open original schema") |

## link_tod Type

unknown ([link_tod](link_tod.md))

# link_tod Properties

| Property                        | Type      | Required | Nullable       | Defined by                                                                                             |
| :------------------------------ | --------- | -------- | -------------- | :----------------------------------------------------------------------------------------------------- |
| [link_tod_id](#link_tod_id)     | `any`     | Required | cannot be null | [link_tod](link_tod-properties-link_tod_id.md "spec/link_tod.schema.json#/properties/link_tod_id")     |
| [link_id](#link_id)             | `any`     | Required | cannot be null | [link_tod](link_tod-properties-link_id.md "spec/link_tod.schema.json#/properties/link_id")             |
| [timeday_id](#timeday_id)       | `any`     | Optional | cannot be null | [link_tod](link_tod-properties-timeday_id.md "spec/link_tod.schema.json#/properties/timeday_id")       |
| [time_day](#time_day)           | `any`     | Optional | cannot be null | [link_tod](link_tod-properties-time_day.md "spec/link_tod.schema.json#/properties/time_day")           |
| [capacity](#capacity)           | `integer` | Optional | cannot be null | [link_tod](link_tod-properties-capacity.md "spec/link_tod.schema.json#/properties/capacity")           |
| [free_speed](#free_speed)       | `integer` | Optional | cannot be null | [link_tod](link_tod-properties-free_speed.md "spec/link_tod.schema.json#/properties/free_speed")       |
| [lanes](#lanes)                 | `integer` | Optional | cannot be null | [link_tod](link_tod-properties-lanes.md "spec/link_tod.schema.json#/properties/lanes")                 |
| [bike_facility](#bike_facility) | `string`  | Optional | cannot be null | [link_tod](link_tod-properties-bike_facility.md "spec/link_tod.schema.json#/properties/bike_facility") |
| [ped_facility](#ped_facility)   | `string`  | Optional | cannot be null | [link_tod](link_tod-properties-ped_facility.md "spec/link_tod.schema.json#/properties/ped_facility")   |
| [parking](#parking)             | `string`  | Optional | cannot be null | [link_tod](link_tod-properties-parking.md "spec/link_tod.schema.json#/properties/parking")             |
| [allowed_uses](#allowed_uses)   | `Any`     | Optional | cannot be null | [link_tod](link_tod-properties-allowed_uses.md "spec/link_tod.schema.json#/properties/allowed_uses")   |
| [toll](#toll)                   | `integer` | Optional | cannot be null | [link_tod](link_tod-properties-toll.md "spec/link_tod.schema.json#/properties/toll")                   |

## link_tod_id

Primary key


`link_tod_id`

-   is required
-   Type: `any`
-   cannot be null
-   defined in: [link_tod](link_tod-properties-link_tod_id.md "spec/link_tod.schema.json#/properties/link_tod_id")

### link_tod_id Type

`any`

## link_id

Required. Foreign key, link table


`link_id`

-   is required
-   Type: `any`
-   cannot be null
-   defined in: [link_tod](link_tod-properties-link_id.md "spec/link_tod.schema.json#/properties/link_id")

### link_id Type

`any`

## timeday_id

Conditionally required (either timeday_id or time_day). Foreign key to time_set_definitions.


`timeday_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [link_tod](link_tod-properties-timeday_id.md "spec/link_tod.schema.json#/properties/timeday_id")

### timeday_id Type

`any`

## time_day

Conditionally required (either timeday_id or time_day). XXXXXXXX_HHMM_HHMM, where XXXXXXXX is a bitmap of days of the week, Sunday-Saturday, Holiday. The HHMM are the start and end times.


`time_day`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [link_tod](link_tod-properties-time_day.md "spec/link_tod.schema.json#/properties/time_day")

### time_day Type

`any`

## capacity

Optional. Capacity (veh / hr / lane)


`capacity`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [link_tod](link_tod-properties-capacity.md "spec/link_tod.schema.json#/properties/capacity")

### capacity Type

`integer`

### capacity Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## free_speed

Optional. Free flow speed mph


`free_speed`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [link_tod](link_tod-properties-free_speed.md "spec/link_tod.schema.json#/properties/free_speed")

### free_speed Type

`integer`

### free_speed Constraints

**maximum**: the value of this number must smaller than or equal to: `100`

**minimum**: the value of this number must greater than or equal to: `0`

## lanes

Optional. Number of permanent lanes (not including turn p
pockets) in the direction of travel open to motor vehicles.
It does not include bike lanes, shoulders or parking lanes.


`lanes`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [link_tod](link_tod-properties-lanes.md "spec/link_tod.schema.json#/properties/lanes")

### lanes Type

`integer`

### lanes Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## bike_facility

Optional. Type of bicycle accommodation: unknown, none, WCL, sharrow, bikelane, cycletrack, offstreet path


`bike_facility`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [link_tod](link_tod-properties-bike_facility.md "spec/link_tod.schema.json#/properties/bike_facility")

### bike_facility Type

`string`

### bike_facility Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value              | Explanation |
| :----------------- | ----------- |
| `"unknown"`        |             |
| `"none"`           |             |
| `"wcl"`            |             |
| `"sharrow"`        |             |
| `"bikelane"`       |             |
| `"cycletrack"`     |             |
| `"offstreet path"` |             |

## ped_facility

Optional. Type of pedestrian accommodation: unknown, none, shoulder, sidewalk, offstreet path


`ped_facility`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [link_tod](link_tod-properties-ped_facility.md "spec/link_tod.schema.json#/properties/ped_facility")

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
| `"offstreet path"` |             |

## parking

Optional. Type of parking: unknown, none, parallel, angle, other


`parking`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [link_tod](link_tod-properties-parking.md "spec/link_tod.schema.json#/properties/parking")

### parking Type

`string`

### parking Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value        | Explanation |
| :----------- | ----------- |
| `"unknown"`  |             |
| `"none"`     |             |
| `"parallel"` |             |
| `"angle"`    |             |
| `"other"`    |             |

## allowed_uses

Use_Set. Optional.


`allowed_uses`

-   is optional
-   Type: `Any`
-   cannot be null
-   defined in: [link_tod](link_tod-properties-allowed_uses.md "spec/link_tod.schema.json#/properties/allowed_uses")

### allowed_uses Type

`Any`

## toll

toll in cents.


`toll`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [link_tod](link_tod-properties-toll.md "spec/link_tod.schema.json#/properties/toll")

### toll Type

`integer`
