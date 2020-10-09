# link Schema

```txt
spec/link.schema.json
```

A link is an edge in a network, defined by the nodes it travels from and to. It may have associated geometry information. Links have three types of attributes:

-   Those that define the physical location of the link (e.g., `shape` `information`, `length`, `width`)
-   Those that define the linkâ€™s directionality: `from_node`, `to_node`
-   Those that define properties in the direction of travel: capacity,free flow speed, number of lanes, permitted uses, grade, facility type


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                            |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [link.schema.json](../../out/link.schema.json "open original schema") |

## link Type

unknown ([link](link.md))

# link Properties

| Property                          | Type      | Required | Nullable       | Defined by                                                                                   |
| :-------------------------------- | --------- | -------- | -------------- | :------------------------------------------------------------------------------------------- |
| [link_id](#link_id)               | `any`     | Optional | cannot be null | [link](link-properties-link_id.md "spec/link.schema.json#/properties/link_id")               |
| [parent_link_id](#parent_link_id) | `any`     | Optional | cannot be null | [link](link-properties-parent_link_id.md "spec/link.schema.json#/properties/parent_link_id") |
| [name](#name)                     | `string`  | Optional | cannot be null | [link](link-properties-name.md "spec/link.schema.json#/properties/name")                     |
| [from_node_id](#from_node_id)     | `any`     | Optional | cannot be null | [link](link-properties-from_node_id.md "spec/link.schema.json#/properties/from_node_id")     |
| [to_node_id](#to_node_id)         | `any`     | Optional | cannot be null | [link](link-properties-to_node_id.md "spec/link.schema.json#/properties/to_node_id")         |
| [directed](#directed)             | `boolean` | Optional | cannot be null | [link](link-properties-directed.md "spec/link.schema.json#/properties/directed")             |
| [geometry_id](#geometry_id)       | `any`     | Optional | cannot be null | [link](link-properties-geometry_id.md "spec/link.schema.json#/properties/geometry_id")       |
| [geometry](#geometry)             | `any`     | Optional | cannot be null | [link](link-properties-geometry.md "spec/link.schema.json#/properties/geometry")             |
| [dir_flag](#dir_flag)             | `integer` | Optional | cannot be null | [link](link-properties-dir_flag.md "spec/link.schema.json#/properties/dir_flag")             |
| [length](#length)                 | `number`  | Optional | cannot be null | [link](link-properties-length.md "spec/link.schema.json#/properties/length")                 |
| [grade](#grade)                   | `number`  | Optional | cannot be null | [link](link-properties-grade.md "spec/link.schema.json#/properties/grade")                   |
| [facility_type](#facility_type)   | `string`  | Optional | cannot be null | [link](link-properties-facility_type.md "spec/link.schema.json#/properties/facility_type")   |
| [capacity](#capacity)             | `integer` | Optional | cannot be null | [link](link-properties-capacity.md "spec/link.schema.json#/properties/capacity")             |
| [free_speed](#free_speed)         | `integer` | Optional | cannot be null | [link](link-properties-free_speed.md "spec/link.schema.json#/properties/free_speed")         |
| [lanes](#lanes)                   | `integer` | Optional | cannot be null | [link](link-properties-lanes.md "spec/link.schema.json#/properties/lanes")                   |
| [bike_facility](#bike_facility)   | `string`  | Optional | cannot be null | [link](link-properties-bike_facility.md "spec/link.schema.json#/properties/bike_facility")   |
| [ped_facility](#ped_facility)     | `string`  | Optional | cannot be null | [link](link-properties-ped_facility.md "spec/link.schema.json#/properties/ped_facility")     |
| [parking](#parking)               | `string`  | Optional | cannot be null | [link](link-properties-parking.md "spec/link.schema.json#/properties/parking")               |
| [allowed_uses](#allowed_uses)     | `string`  | Optional | cannot be null | [link](link-properties-allowed_uses.md "spec/link.schema.json#/properties/allowed_uses")     |
| [toll](#toll)                     | `integer` | Optional | cannot be null | [link](link-properties-toll.md "spec/link.schema.json#/properties/toll")                     |
| [jurisdiction](#jurisdiction)     | `string`  | Optional | cannot be null | [link](link-properties-jurisdiction.md "spec/link.schema.json#/properties/jurisdiction")     |
| [row_width](#row_width)           | `number`  | Optional | cannot be null | [link](link-properties-row_width.md "spec/link.schema.json#/properties/row_width")           |

## link_id

Primary key â€“ could be SharedStreets Reference ID


`link_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [link](link-properties-link_id.md "spec/link.schema.json#/properties/link_id")

### link_id Type

`any`

## parent_link_id

Optional. The parent of this link. For example,for a sidewalk, this is the adjacent road.


`parent_link_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [link](link-properties-parent_link_id.md "spec/link.schema.json#/properties/parent_link_id")

### parent_link_id Type

`any`

## name

Optional. Street or Path Name


`name`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [link](link-properties-name.md "spec/link.schema.json#/properties/name")

### name Type

`string`

## from_node_id




`from_node_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [link](link-properties-from_node_id.md "spec/link.schema.json#/properties/from_node_id")

### from_node_id Type

`any`

## to_node_id




`to_node_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [link](link-properties-to_node_id.md "spec/link.schema.json#/properties/to_node_id")

### to_node_id Type

`any`

## directed

Required. Whether the link is directed (travel only occurs from the from_node to the to_node) or undirected.


`directed`

-   is optional
-   Type: `boolean`
-   cannot be null
-   defined in: [link](link-properties-directed.md "spec/link.schema.json#/properties/directed")

### directed Type

`boolean`

## geometry_id

Optional. Foreign key (Link_Geometry table).


`geometry_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [link](link-properties-geometry_id.md "spec/link.schema.json#/properties/geometry_id")

### geometry_id Type

`any`

## geometry

Optional. Link geometry, specific format could be WKT, GeoJSON, etc.


`geometry`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [link](link-properties-geometry.md "spec/link.schema.json#/properties/geometry")

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
-   defined in: [link](link-properties-dir_flag.md "spec/link.schema.json#/properties/dir_flag")

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
-   defined in: [link](link-properties-length.md "spec/link.schema.json#/properties/length")

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
-   defined in: [link](link-properties-grade.md "spec/link.schema.json#/properties/grade")

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
-   defined in: [link](link-properties-facility_type.md "spec/link.schema.json#/properties/facility_type")

### facility_type Type

`string`

## capacity

Optional. Capacity (veh / hr / lane)


`capacity`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [link](link-properties-capacity.md "spec/link.schema.json#/properties/capacity")

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
-   defined in: [link](link-properties-free_speed.md "spec/link.schema.json#/properties/free_speed")

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
-   defined in: [link](link-properties-lanes.md "spec/link.schema.json#/properties/lanes")

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
-   defined in: [link](link-properties-bike_facility.md "spec/link.schema.json#/properties/bike_facility")

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
-   defined in: [link](link-properties-ped_facility.md "spec/link.schema.json#/properties/ped_facility")

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
-   defined in: [link](link-properties-parking.md "spec/link.schema.json#/properties/parking")

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
-   defined in: [link](link-properties-allowed_uses.md "spec/link.schema.json#/properties/allowed_uses")

### allowed_uses Type

`string`

## toll

Optional.  Toll on the link, in cents.


`toll`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [link](link-properties-toll.md "spec/link.schema.json#/properties/toll")

### toll Type

`integer`

## jurisdiction

Optional.  Owner/operator of the link.


`jurisdiction`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [link](link-properties-jurisdiction.md "spec/link.schema.json#/properties/jurisdiction")

### jurisdiction Type

`string`

## row_width

Optional. Width (feet) of the entire right-of-way (both directions).


`row_width`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [link](link-properties-row_width.md "spec/link.schema.json#/properties/row_width")

### row_width Type

`number`

### row_width Constraints

**minimum**: the value of this number must greater than or equal to: `0`
