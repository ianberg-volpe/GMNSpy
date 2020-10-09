# movement Schema

```txt
spec/movement.schema.json
```

Describes how inbound and outbound links connect at an intersection.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                    |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ----------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [movement.schema.json](../../out/movement.schema.json "open original schema") |

## movement Type

unknown ([movement](movement.md))

# movement Properties

| Property                        | Type      | Required | Nullable       | Defined by                                                                                             |
| :------------------------------ | --------- | -------- | -------------- | :----------------------------------------------------------------------------------------------------- |
| [mvmt_id](#mvmt_id)             | `any`     | Optional | cannot be null | [movement](movement-properties-mvmt_id.md "spec/movement.schema.json#/properties/mvmt_id")             |
| [node_id](#node_id)             | `any`     | Optional | cannot be null | [movement](movement-properties-node_id.md "spec/movement.schema.json#/properties/node_id")             |
| [name](#name)                   | `any`     | Optional | cannot be null | [movement](movement-properties-name.md "spec/movement.schema.json#/properties/name")                   |
| [ib_link_id](#ib_link_id)       | `any`     | Optional | cannot be null | [movement](movement-properties-ib_link_id.md "spec/movement.schema.json#/properties/ib_link_id")       |
| [start_ib_lane](#start_ib_lane) | `integer` | Optional | cannot be null | [movement](movement-properties-start_ib_lane.md "spec/movement.schema.json#/properties/start_ib_lane") |
| [end_ib_lane](#end_ib_lane)     | `integer` | Optional | cannot be null | [movement](movement-properties-end_ib_lane.md "spec/movement.schema.json#/properties/end_ib_lane")     |
| [ob_link_id](#ob_link_id)       | `any`     | Optional | cannot be null | [movement](movement-properties-ob_link_id.md "spec/movement.schema.json#/properties/ob_link_id")       |
| [start_ob_lane](#start_ob_lane) | `integer` | Optional | cannot be null | [movement](movement-properties-start_ob_lane.md "spec/movement.schema.json#/properties/start_ob_lane") |
| [end_ob_lane](#end_ob_lane)     | `integer` | Optional | cannot be null | [movement](movement-properties-end_ob_lane.md "spec/movement.schema.json#/properties/end_ob_lane")     |
| [type](#type)                   | `string`  | Optional | cannot be null | [movement](movement-properties-type.md "spec/movement.schema.json#/properties/type")                   |
| [penalty](#penalty)             | `any`     | Optional | cannot be null | [movement](movement-properties-penalty.md "spec/movement.schema.json#/properties/penalty")             |
| [capacity](#capacity)           | `any`     | Optional | cannot be null | [movement](movement-properties-capacity.md "spec/movement.schema.json#/properties/capacity")           |
| [ctrl_type](#ctrl_type)         | `any`     | Optional | cannot be null | [movement](movement-properties-ctrl_type.md "spec/movement.schema.json#/properties/ctrl_type")         |

## mvmt_id

Primary key.


`mvmt_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [movement](movement-properties-mvmt_id.md "spec/movement.schema.json#/properties/mvmt_id")

### mvmt_id Type

`any`

## node_id

The node representing the junction.


`node_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [movement](movement-properties-node_id.md "spec/movement.schema.json#/properties/node_id")

### node_id Type

`any`

## name

Optional.


`name`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [movement](movement-properties-name.md "spec/movement.schema.json#/properties/name")

### name Type

`any`

## ib_link_id

Inbound link id.


`ib_link_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [movement](movement-properties-ib_link_id.md "spec/movement.schema.json#/properties/ib_link_id")

### ib_link_id Type

`any`

## start_ib_lane

Innermost lane number the movement applies to at the inbound end.


`start_ib_lane`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [movement](movement-properties-start_ib_lane.md "spec/movement.schema.json#/properties/start_ib_lane")

### start_ib_lane Type

`integer`

## end_ib_lane

Outermost lane number the movement applies to at the inbound end. Blank indicates a movement with a single inbound lane.


`end_ib_lane`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [movement](movement-properties-end_ib_lane.md "spec/movement.schema.json#/properties/end_ib_lane")

### end_ib_lane Type

`integer`

## ob_link_id

Outbound link id.


`ob_link_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [movement](movement-properties-ob_link_id.md "spec/movement.schema.json#/properties/ob_link_id")

### ob_link_id Type

`any`

## start_ob_lane

Innermost lane number the movement applies to at the outbound end.


`start_ob_lane`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [movement](movement-properties-start_ob_lane.md "spec/movement.schema.json#/properties/start_ob_lane")

### start_ob_lane Type

`integer`

## end_ob_lane

Outermost lane number the movement applies to at the outbound end. Blank indicates a movement with a single outbound lane.


`end_ob_lane`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [movement](movement-properties-end_ob_lane.md "spec/movement.schema.json#/properties/end_ob_lane")

### end_ob_lane Type

`integer`

## type

Optional. Describes the type of movement (left, right, thru, etc.).


`type`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [movement](movement-properties-type.md "spec/movement.schema.json#/properties/type")

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
-   defined in: [movement](movement-properties-penalty.md "spec/movement.schema.json#/properties/penalty")

### penalty Type

`any`

## capacity

Capacity in vehicles per hour.


`capacity`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [movement](movement-properties-capacity.md "spec/movement.schema.json#/properties/capacity")

### capacity Type

`any`

## ctrl_type

Optional. .


`ctrl_type`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [movement](movement-properties-ctrl_type.md "spec/movement.schema.json#/properties/ctrl_type")

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
