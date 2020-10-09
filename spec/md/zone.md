# zone Schema

```txt
undefined
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                            |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [zone.schema.json](../../out/zone.schema.json "open original schema") |

## zone Type

unknown ([zone](zone.md))

# zone Properties

| Property                  | Type     | Required | Nullable       | Defined by                                                               |
| :------------------------ | -------- | -------- | -------------- | :----------------------------------------------------------------------- |
| [zone_id](#zone_id)       | `any`    | Optional | cannot be null | [zone](zone-properties-zone_id.md "undefined#/properties/zone_id")       |
| [name](#name)             | `any`    | Optional | cannot be null | [zone](zone-properties-name.md "undefined#/properties/name")             |
| [boundary](#boundary)     | `any`    | Optional | cannot be null | [zone](zone-properties-boundary.md "undefined#/properties/boundary")     |
| [super_zone](#super_zone) | `string` | Optional | cannot be null | [zone](zone-properties-super_zone.md "undefined#/properties/super_zone") |

## zone_id

Primary key.


`zone_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [zone](zone-properties-zone_id.md "undefined#/properties/zone_id")

### zone_id Type

`any`

## name

Optional.


`name`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [zone](zone-properties-name.md "undefined#/properties/name")

### name Type

`any`

## boundary

Optional. The polygon geometry of the zone in WKT or Polygon.


`boundary`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [zone](zone-properties-boundary.md "undefined#/properties/boundary")

### boundary Type

`any`

## super_zone

Optional. If there is a hierarchy of zones (e.g., parcels and TAZs), indicates the zone of next higher level.


`super_zone`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [zone](zone-properties-super_zone.md "undefined#/properties/super_zone")

### super_zone Type

`string`
