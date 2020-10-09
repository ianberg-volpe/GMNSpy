# link Schema

```txt
undefined
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                            |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [link.schema.json](../../out/link.schema.json "open original schema") |

## link Type

unknown ([link](link.md))

# link Properties

| Property                          | Type      | Required | Nullable       | Defined by                                                                       |
| :-------------------------------- | --------- | -------- | -------------- | :------------------------------------------------------------------------------- |
| [link_id](#link_id)               | `any`     | Optional | cannot be null | [link](link-properties-link_id.md "undefined#/properties/link_id")               |
| [parent_link_id](#parent_link_id) | `any`     | Optional | cannot be null | [link](link-properties-parent_link_id.md "undefined#/properties/parent_link_id") |
| [name](#name)                     | `string`  | Optional | cannot be null | [link](link-properties-name.md "undefined#/properties/name")                     |
| [from_node_id](#from_node_id)     | `any`     | Optional | cannot be null | [link](link-properties-from_node_id.md "undefined#/properties/from_node_id")     |
| [to_node_id](#to_node_id)         | `any`     | Optional | cannot be null | [link](link-properties-to_node_id.md "undefined#/properties/to_node_id")         |
| [directed](#directed)             | `boolean` | Optional | cannot be null | [link](link-properties-directed.md "undefined#/properties/directed")             |
| [geometry_id](#geometry_id)       | `any`     | Optional | cannot be null | [link](link-properties-geometry_id.md "undefined#/properties/geometry_id")       |
| [geometry](#geometry)             | `any`     | Optional | cannot be null | [link](link-properties-geometry.md "undefined#/properties/geometry")             |
| [dir_flag](#dir_flag)             | `integer` | Optional | cannot be null | [link](link-properties-dir_flag.md "undefined#/properties/dir_flag")             |
| [length](#length)                 | `number`  | Optional | cannot be null | [link](link-properties-length.md "undefined#/properties/length")                 |
| [grade](#grade)                   | `number`  | Optional | cannot be null | [link](link-properties-grade.md "undefined#/properties/grade")                   |
| [facility_type](#facility_type)   | `string`  | Optional | cannot be null | [link](link-properties-facility_type.md "undefined#/properties/facility_type")   |
| [capacity](#capacity)             | `integer` | Optional | cannot be null | [link](link-properties-capacity.md "undefined#/properties/capacity")             |
| [free_speed](#free_speed)         | `integer` | Optional | cannot be null | [link](link-properties-free_speed.md "undefined#/properties/free_speed")         |
| [lanes](#lanes)                   | `integer` | Optional | cannot be null | [link](link-properties-lanes.md "undefined#/properties/lanes")                   |
| [bike_facility](#bike_facility)   | `string`  | Optional | cannot be null | [link](link-properties-bike_facility.md "undefined#/properties/bike_facility")   |
| [ped_facility](#ped_facility)     | `string`  | Optional | cannot be null | [link](link-properties-ped_facility.md "undefined#/properties/ped_facility")     |
| [parking](#parking)               | `string`  | Optional | cannot be null | [link](link-properties-parking.md "undefined#/properties/parking")               |
| [allowed_uses](#allowed_uses)     | `string`  | Optional | cannot be null | [link](link-properties-allowed_uses.md "undefined#/properties/allowed_uses")     |
| [toll](#toll)                     | `integer` | Optional | cannot be null | [link](link-properties-toll.md "undefined#/properties/toll")                     |
| [jurisdiction](#jurisdiction)     | `string`  | Optional | cannot be null | [link](link-properties-jurisdiction.md "undefined#/properties/jurisdiction")     |
| [row_width](#row_width)           | `number`  | Optional | cannot be null | [link](link-properties-row_width.md "undefined#/properties/row_width")           |

## link_id

Primary key â€“ could be SharedStreets Reference ID


`link_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [link](link-properties-link_id.md "undefined#/properties/link_id")

### link_id Type

`any`

## parent_link_id

Optional. The parent of this link. For example,for a sidewalk, this is the adjacent road.


`parent_link_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [link](link-properties-parent_link_id.md "undefined#/properties/parent_link_id")

### parent_link_id Type

`any`

## name

Optional. Street or Path Name


`name`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [link](link-properties-name.md "undefined#/properties/name")

### name Type

`string`

## from_node_id




`from_node_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [link](link-properties-from_node_id.md "undefined#/properties/from_node_id")

### from_node_id Type

`any`

## to_node_id




`to_node_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [link](link-properties-to_node_id.md "undefined#/properties/to_node_id")

### to_node_id Type

`any`

## directed

Required. Whether the link is directed (travel only occurs from the from_node to the to_node) or undirected.


`directed`

-   is optional
-   Type: `boolean`
-   cannot be null
-   defined in: [link](link-properties-directed.md "undefined#/properties/directed")

### directed Type

`boolean`

## geometry_id

Optional. Foreign key (Link_Geometry table).


`geometry_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [link](link-properties-geometry_id.md "undefined#/properties/geometry_id")

### geometry_id Type

`any`

## geometry

Optional. Link geometry, specific format could be WKT, GeoJSON, etc.


`geometry`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [link](link-properties-geometry.md "undefined#/properties/geometry")

### geometry Type

`any`

## dir_flag

Optional. 
1  shapepoints go from from_node to to_node;
\-1 shapepoints go in the reverse direction;
0  link is undirected or no geometry information is provided.


`dir_flag`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [link](link-properties-dir_flag.md "undefined#/properties/dir_flag")

### dir_flag Type

`integer`

### dir_flag Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation |
| :---- | ----------- |
| `-1`  |             |
| `0`   |             |
| `1`   |             |

## length

Optional. Length of the link in miles


`length`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [link](link-properties-length.md "undefined#/properties/length")

### length Type

`number`

### length Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## grade

% grade, negative is downhill


`grade`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [link](link-properties-grade.md "undefined#/properties/grade")

### grade Type

`number`

### grade Constraints

**maximum**: the value of this number must smaller than or equal to: `100`

**minimum**: the value of this number must greater than or equal to: `-100`

## facility_type

Facility type (e.g., freeway, arterial, etc.)


`facility_type`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [link](link-properties-facility_type.md "undefined#/properties/facility_type")

### facility_type Type

`string`

## capacity

Optional. Capacity (veh / hr / lane)


`capacity`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [link](link-properties-capacity.md "undefined#/properties/capacity")

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
-   defined in: [link](link-properties-free_speed.md "undefined#/properties/free_speed")

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
-   defined in: [link](link-properties-lanes.md "undefined#/properties/lanes")

### lanes Type

`integer`

### lanes Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## bike_facility

Optional. Type of bicycle accommodation: unknown, none, wcl, sharrow, bikelane, cycletrack, offstreet path


`bike_facility`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [link](link-properties-bike_facility.md "undefined#/properties/bike_facility")

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
-   defined in: [link](link-properties-ped_facility.md "undefined#/properties/ped_facility")

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
-   defined in: [link](link-properties-parking.md "undefined#/properties/parking")

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

Optional. Set of allowed uses: shoulder, parking, walk, all, bike, auto, hov2, hov3, truck, bus, etc. e.g. [auto,bike]


`allowed_uses`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [link](link-properties-allowed_uses.md "undefined#/properties/allowed_uses")

### allowed_uses Type

`string`

## toll

Optional.  Toll on the link, in cents.


`toll`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [link](link-properties-toll.md "undefined#/properties/toll")

### toll Type

`integer`

## jurisdiction

Optional.  Owner/operator of the link.


`jurisdiction`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [link](link-properties-jurisdiction.md "undefined#/properties/jurisdiction")

### jurisdiction Type

`string`

## row_width

Optional. Width (feet) of the entire right-of-way (both directions).


`row_width`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [link](link-properties-row_width.md "undefined#/properties/row_width")

### row_width Type

`number`

### row_width Constraints

**minimum**: the value of this number must greater than or equal to: `0`
