# location Schema

```txt
spec/location.schema.json
```

A location is a vertex that is associated with a specific location along a link. Locations may be used to represent places where activities occur (e.g., driveways and bus stops). Its attributes are nearly the same as those for a node, except that the location includes an associated link and node, with location specified as distance along the link from the node.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                    |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ----------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [location.schema.json](../../out/location.schema.json "open original schema") |

## location Type

unknown ([location](location.md))

# location Properties

| Property                      | Type     | Required | Nullable       | Defined by                                                                                           |
| :---------------------------- | -------- | -------- | -------------- | :--------------------------------------------------------------------------------------------------- |
| [loc_id](#loc_id)             | `any`    | Optional | cannot be null | [location](location-properties-loc_id.md "spec/location.schema.json#/properties/loc_id")             |
| [link_id](#link_id)           | `any`    | Optional | cannot be null | [location](location-properties-link_id.md "spec/location.schema.json#/properties/link_id")           |
| [ref_node_id](#ref_node_id)   | `any`    | Optional | cannot be null | [location](location-properties-ref_node_id.md "spec/location.schema.json#/properties/ref_node_id")   |
| [lr](#lr)                     | `number` | Optional | cannot be null | [location](location-properties-lr.md "spec/location.schema.json#/properties/lr")                     |
| [x_coord](#x_coord)           | `number` | Optional | cannot be null | [location](location-properties-x_coord.md "spec/location.schema.json#/properties/x_coord")           |
| [y_coord](#y_coord)           | `number` | Optional | cannot be null | [location](location-properties-y_coord.md "spec/location.schema.json#/properties/y_coord")           |
| [z_coord](#z_coord)           | `number` | Optional | cannot be null | [location](location-properties-z_coord.md "spec/location.schema.json#/properties/z_coord")           |
| [loc_type](#loc_type)         | `string` | Optional | cannot be null | [location](location-properties-loc_type.md "spec/location.schema.json#/properties/loc_type")         |
| [zone_id](#zone_id)           | `any`    | Optional | cannot be null | [location](location-properties-zone_id.md "spec/location.schema.json#/properties/zone_id")           |
| [gtfs_stop_id](#gtfs_stop_id) | `string` | Optional | cannot be null | [location](location-properties-gtfs_stop_id.md "spec/location.schema.json#/properties/gtfs_stop_id") |

## loc_id

Primary key. Location ID.


`loc_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [location](location-properties-loc_id.md "spec/location.schema.json#/properties/loc_id")

### loc_id Type

`any`

## link_id

Required. Road Link ID. Foreign Key from Road_Link.


`link_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [location](location-properties-link_id.md "spec/location.schema.json#/properties/link_id")

### link_id Type

`any`

## ref_node_id

Required. The From node of the link. Foreign Key from Node.


`ref_node_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [location](location-properties-ref_node_id.md "spec/location.schema.json#/properties/ref_node_id")

### ref_node_id Type

`any`

## lr

Required. Linear Reference of the location, measured as distance along the link from the reference node.  If link_geometry exists, it is used. Otherwise, link geometry is assumed to be a crow-fly distance from A node to B node.


`lr`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [location](location-properties-lr.md "spec/location.schema.json#/properties/lr")

### lr Type

`number`

### lr Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## x_coord

Optional. Either provided, or derived from Link, Ref_Node and LR.


`x_coord`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [location](location-properties-x_coord.md "spec/location.schema.json#/properties/x_coord")

### x_coord Type

`number`

## y_coord

Optional. Either provided, or derived from Link, Ref_Node and LR.


`y_coord`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [location](location-properties-y_coord.md "spec/location.schema.json#/properties/y_coord")

### y_coord Type

`number`

## z_coord

Optional. Altitude.


`z_coord`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [location](location-properties-z_coord.md "spec/location.schema.json#/properties/z_coord")

### z_coord Type

`number`

## loc_type

Optional. What it represents (driveway, bus stop, etc.) OpenStreetMap map feature names are recommended.


`loc_type`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [location](location-properties-loc_type.md "spec/location.schema.json#/properties/loc_type")

### loc_type Type

`string`

## zone_id

Optional. Foreign Key, Associated zone


`zone_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [location](location-properties-zone_id.md "spec/location.schema.json#/properties/zone_id")

### zone_id Type

`any`

## gtfs_stop_id

Optional. Foreign Key to GTFS data. For bus stops and transit station entrances, provides a link to the General Transit Feed Specification.


`gtfs_stop_id`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [location](location-properties-gtfs_stop_id.md "spec/location.schema.json#/properties/gtfs_stop_id")

### gtfs_stop_id Type

`string`
