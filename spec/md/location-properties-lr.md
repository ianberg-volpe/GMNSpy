# Untitled number in location Schema

```txt
undefined#/properties/lr
```

Required. Linear Reference of the location, measured as distance along the link from the reference node.  If link_geometry exists, it is used. Otherwise, link geometry is assumed to be a crow-fly distance from A node to B node.


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                      |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | ------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [location.schema.json\*](../../out/location.schema.json "open original schema") |

## lr Type

`number`

## lr Constraints

**minimum**: the value of this number must greater than or equal to: `0`
