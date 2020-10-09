# geometry Schema

```txt
undefined
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                    |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ----------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [geometry.schema.json](../../out/geometry.schema.json "open original schema") |

## geometry Type

unknown ([geometry](geometry.md))

# geometry Properties

| Property                    | Type  | Required | Nullable       | Defined by                                                                         |
| :-------------------------- | ----- | -------- | -------------- | :--------------------------------------------------------------------------------- |
| [geometry_id](#geometry_id) | `any` | Optional | cannot be null | [geometry](geometry-properties-geometry_id.md "undefined#/properties/geometry_id") |
| [geometry](#geometry)       | `any` | Optional | cannot be null | [geometry](geometry-properties-geometry.md "undefined#/properties/geometry")       |

## geometry_id

Primary key â€“ could be SharedStreets Geometry ID


`geometry_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [geometry](geometry-properties-geometry_id.md "undefined#/properties/geometry_id")

### geometry_id Type

`any`

## geometry

Optional. Link geometry, specific format could be WKT, GeoJSON, etc.


`geometry`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [geometry](geometry-properties-geometry.md "undefined#/properties/geometry")

### geometry Type

`any`
