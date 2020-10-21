# node Schema

```txt
spec/node.schema.json
```

A list of vertices that locate points on a map. Typically, they will represent intersections, but may also represent other points, such as a transition between divided and undivided highway. Nodes are the endpoints of a link (as opposed to the other type of vertex, location, which is used to represent points along a link)


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                            |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [node.schema.json](../../out/node.schema.json "open original schema") |

## node Type

unknown ([node](node.md))

# node Properties

| Property                          | Type     | Required | Nullable       | Defined by                                                                                   |
| :-------------------------------- | -------- | -------- | -------------- | :------------------------------------------------------------------------------------------- |
| [node_id](#node_id)               | `any`    | Required | cannot be null | [node](node-properties-node_id.md "spec/node.schema.json#/properties/node_id")               |
| [name](#name)                     | `string` | Optional | cannot be null | [node](node-properties-name.md "spec/node.schema.json#/properties/name")                     |
| [x_coord](#x_coord)               | `number` | Required | cannot be null | [node](node-properties-x_coord.md "spec/node.schema.json#/properties/x_coord")               |
| [y_coord](#y_coord)               | `number` | Required | cannot be null | [node](node-properties-y_coord.md "spec/node.schema.json#/properties/y_coord")               |
| [z_coord](#z_coord)               | `number` | Required | cannot be null | [node](node-properties-z_coord.md "spec/node.schema.json#/properties/z_coord")               |
| [node_type](#node_type)           | `string` | Optional | cannot be null | [node](node-properties-node_type.md "spec/node.schema.json#/properties/node_type")           |
| [ctrl_type](#ctrl_type)           | `string` | Optional | cannot be null | [node](node-properties-ctrl_type.md "spec/node.schema.json#/properties/ctrl_type")           |
| [zone_id](#zone_id)               | `any`    | Optional | cannot be null | [node](node-properties-zone_id.md "spec/node.schema.json#/properties/zone_id")               |
| [parent_node_id](#parent_node_id) | `any`    | Optional | cannot be null | [node](node-properties-parent_node_id.md "spec/node.schema.json#/properties/parent_node_id") |

## node_id

Primary key


`node_id`

-   is required
-   Type: `any`
-   cannot be null
-   defined in: [node](node-properties-node_id.md "spec/node.schema.json#/properties/node_id")

### node_id Type

`any`

## name




`name`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [node](node-properties-name.md "spec/node.schema.json#/properties/name")

### name Type

`string`

## x_coord

Coordinate system specified in config file (longitude, UTM-easting etc.)


`x_coord`

-   is required
-   Type: `number`
-   cannot be null
-   defined in: [node](node-properties-x_coord.md "spec/node.schema.json#/properties/x_coord")

### x_coord Type

`number`

## y_coord

Coordinate system specified in config file (latitude, UTM-northing etc.)


`y_coord`

-   is required
-   Type: `number`
-   cannot be null
-   defined in: [node](node-properties-y_coord.md "spec/node.schema.json#/properties/y_coord")

### y_coord Type

`number`

## z_coord

Optional. Altitude.


`z_coord`

-   is required
-   Type: `number`
-   cannot be null
-   defined in: [node](node-properties-z_coord.md "spec/node.schema.json#/properties/z_coord")

### z_coord Type

`number`

## node_type

Optional. What it represents (intersection, transit station, park & ride).


`node_type`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [node](node-properties-node_type.md "spec/node.schema.json#/properties/node_type")

### node_type Type

`string`

## ctrl_type

Optional. Intersection control type - one of ControlType_Set.


`ctrl_type`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [node](node-properties-ctrl_type.md "spec/node.schema.json#/properties/ctrl_type")

### ctrl_type Type

`string`

### ctrl_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value      | Explanation |
| :--------- | ----------- |
| `"none"`   |             |
| `"yield"`  |             |
| `"stop"`   |             |
| `"4_stop"` |             |
| `"signal"` |             |

## zone_id

Optional. Could be a Transportation Analysis Zone (TAZ) or city, or census tract, or census block.


`zone_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [node](node-properties-zone_id.md "spec/node.schema.json#/properties/zone_id")

### zone_id Type

`any`

## parent_node_id

Optional. Associated node. For example, if this node is a sidewalk, a parent_nodek_id could represent the intersection  it is associated with.


`parent_node_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [node](node-properties-parent_node_id.md "spec/node.schema.json#/properties/parent_node_id")

### parent_node_id Type

`any`
