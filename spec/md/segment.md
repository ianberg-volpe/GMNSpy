# Untitled schema Schema

```txt
undefined
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [segment.schema.json](../../out/segment.schema.json "open original schema") |

## Untitled schema Type

unknown

# undefined Properties

| Property                        | Type      | Required | Nullable       | Defined by                                                                                   |
| :------------------------------ | --------- | -------- | -------------- | :------------------------------------------------------------------------------------------- |
| [segment_id](#segment_id)       | `any`     | Optional | cannot be null | [Untitled schema](segment-properties-segment_id.md "undefined#/properties/segment_id")       |
| [link_id](#link_id)             | `any`     | Optional | cannot be null | [Untitled schema](segment-properties-link_id.md "undefined#/properties/link_id")             |
| [ref_node_id](#ref_node_id)     | `any`     | Optional | cannot be null | [Untitled schema](segment-properties-ref_node_id.md "undefined#/properties/ref_node_id")     |
| [start_lr](#start_lr)           | `number`  | Optional | cannot be null | [Untitled schema](segment-properties-start_lr.md "undefined#/properties/start_lr")           |
| [end_lr](#end_lr)               | `number`  | Optional | cannot be null | [Untitled schema](segment-properties-end_lr.md "undefined#/properties/end_lr")               |
| [grade](#grade)                 | `number`  | Optional | cannot be null | [Untitled schema](segment-properties-grade.md "undefined#/properties/grade")                 |
| [capacity](#capacity)           | `integer` | Optional | cannot be null | [Untitled schema](segment-properties-capacity.md "undefined#/properties/capacity")           |
| [free_speed](#free_speed)       | `integer` | Optional | cannot be null | [Untitled schema](segment-properties-free_speed.md "undefined#/properties/free_speed")       |
| [lanes](#lanes)                 | `integer` | Optional | cannot be null | [Untitled schema](segment-properties-lanes.md "undefined#/properties/lanes")                 |
| [l_lanes_added](#l_lanes_added) | `integer` | Optional | cannot be null | [Untitled schema](segment-properties-l_lanes_added.md "undefined#/properties/l_lanes_added") |
| [r_lanes_added](#r_lanes_added) | `integer` | Optional | cannot be null | [Untitled schema](segment-properties-r_lanes_added.md "undefined#/properties/r_lanes_added") |
| [bike_facility](#bike_facility) | `string`  | Optional | cannot be null | [Untitled schema](segment-properties-bike_facility.md "undefined#/properties/bike_facility") |
| [ped_facility](#ped_facility)   | `string`  | Optional | cannot be null | [Untitled schema](segment-properties-ped_facility.md "undefined#/properties/ped_facility")   |
| [parking](#parking)             | `string`  | Optional | cannot be null | [Untitled schema](segment-properties-parking.md "undefined#/properties/parking")             |
| [allowed_uses](#allowed_uses)   | `string`  | Optional | cannot be null | [Untitled schema](segment-properties-allowed_uses.md "undefined#/properties/allowed_uses")   |
| [toll](#toll)                   | `integer` | Optional | cannot be null | [Untitled schema](segment-properties-toll.md "undefined#/properties/toll")                   |
| [jurisdiction](#jurisdiction)   | `string`  | Optional | cannot be null | [Untitled schema](segment-properties-jurisdiction.md "undefined#/properties/jurisdiction")   |
| [row_width](#row_width)         | `number`  | Optional | cannot be null | [Untitled schema](segment-properties-row_width.md "undefined#/properties/row_width")         |

## segment_id

Primary key.


`segment_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-segment_id.md "undefined#/properties/segment_id")

### segment_id Type

`any`

## link_id

Required. Foreign key to road_links. The link that the segment is located on.


`link_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-link_id.md "undefined#/properties/link_id")

### link_id Type

`any`

## ref_node_id

Required. Foreign key to node where distance is 0.


`ref_node_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-ref_node_id.md "undefined#/properties/ref_node_id")

### ref_node_id Type

`any`

## start_lr

Required. Distance from `ref_node_id`.


`start_lr`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-start_lr.md "undefined#/properties/start_lr")

### start_lr Type

`number`

### start_lr Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## end_lr

Required. Distance from `ref_node_id`.


`end_lr`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-end_lr.md "undefined#/properties/end_lr")

### end_lr Type

`number`

### end_lr Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## grade

% grade, negative is downhill


`grade`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-grade.md "undefined#/properties/grade")

### grade Type

`number`

### grade Constraints

**maximum**: the value of this number must smaller than or equal to: `100`

**minimum**: the value of this number must greater than or equal to: `-100`

## capacity

Optional. Capacity (veh/hr/ln)


`capacity`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-capacity.md "undefined#/properties/capacity")

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
-   defined in: [Untitled schema](segment-properties-free_speed.md "undefined#/properties/free_speed")

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
-   defined in: [Untitled schema](segment-properties-lanes.md "undefined#/properties/lanes")

### lanes Type

`integer`

## l_lanes_added

Optional. # of lanes added on the left of the road link (negative indicates a lane drop).


`l_lanes_added`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-l_lanes_added.md "undefined#/properties/l_lanes_added")

### l_lanes_added Type

`integer`

## r_lanes_added

Optional. # of lanes added on the right of the road link (negative indicates a lane drop).


`r_lanes_added`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-r_lanes_added.md "undefined#/properties/r_lanes_added")

### r_lanes_added Type

`integer`

## bike_facility

Optional. Type of bicycle accommodation: unknown, none,wcl, bikelane,cycletrack,wide_shoulder, offstreet_path.


`bike_facility`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-bike_facility.md "undefined#/properties/bike_facility")

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

Optional. Type of pedestrian accommodation:unknown,none,shoulder,sidewalk,offstreet_path.


`ped_facility`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-ped_facility.md "undefined#/properties/ped_facility")

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
-   defined in: [Untitled schema](segment-properties-parking.md "undefined#/properties/parking")

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

## allowed_uses

Optional. Set of allowed uses; comma-separated. Foreign key  to use_definition or use sets.


`allowed_uses`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-allowed_uses.md "undefined#/properties/allowed_uses")

### allowed_uses Type

`string`

## toll

Optional.  Toll on the link, in cents.


`toll`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-toll.md "undefined#/properties/toll")

### toll Type

`integer`

## jurisdiction

Optional. Optional.  Owner/operator of the link.


`jurisdiction`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-jurisdiction.md "undefined#/properties/jurisdiction")

### jurisdiction Type

`string`

## row_width

Optional. Width (feet) of the entire right-of-way (both directions).


`row_width`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [Untitled schema](segment-properties-row_width.md "undefined#/properties/row_width")

### row_width Type

`number`

### row_width Constraints

**minimum**: the value of this number must greater than or equal to: `0`
