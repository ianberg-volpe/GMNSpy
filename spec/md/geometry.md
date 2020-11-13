# geometry Schema

```txt
spec/geometry.schema.json
```

The geometry is an optional file that contains geometry information (shapepoints) for a line object. It is similar to Geometries in the SharedStreets reference system. The specification also allows for geometry information to be stored directly on the link table.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                    |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ----------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [geometry.schema.json](../../out/geometry.schema.json "open original schema") |

## geometry Type

unknown ([geometry](geometry.md))

# geometry Properties

| Property                    | Type  | Required | Nullable       | Defined by                                                                                         |
| :-------------------------- | ----- | -------- | -------------- | :------------------------------------------------------------------------------------------------- |
| [geometry_id](#geometry_id) | `any` | Required | cannot be null | [geometry](geometry-properties-geometry_id.md "spec/geometry.schema.json#/properties/geometry_id") |
| [geometry](#geometry)       | `any` | Optional | cannot be null | [geometry](geometry-properties-geometry.md "spec/geometry.schema.json#/properties/geometry")       |

## geometry_id

Primary key â€“ could be SharedStreets Geometry ID


`geometry_id`

-   is required
-   Type: `any`
-   cannot be null
-   defined in: [geometry](geometry-properties-geometry_id.md "spec/geometry.schema.json#/properties/geometry_id")

### geometry_id Type

`any`

## geometry

Optional. Link geometry, specific format could be WKT, GeoJSON, etc.


`geometry`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [geometry](geometry-properties-geometry.md "spec/geometry.schema.json#/properties/geometry")

### geometry Type

`any`