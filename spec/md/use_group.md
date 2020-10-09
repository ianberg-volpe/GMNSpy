# use_group Schema

```txt
spec/use_group.schema.json
```

Defines groupings of uses, to reduce the size of the Allowed_Uses lists in the other tables.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                      |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [use_group.schema.json](../../out/use_group.schema.json "open original schema") |

## use_group Type

unknown ([use_group](use_group.md))

# use_group Properties

| Property                    | Type     | Required | Nullable       | Defined by                                                                                            |
| :-------------------------- | -------- | -------- | -------------- | :---------------------------------------------------------------------------------------------------- |
| [use_group](#use_group)     | `string` | Optional | cannot be null | [use_group](use_group-properties-use_group.md "spec/use_group.schema.json#/properties/use_group")     |
| [uses](#uses)               | `string` | Optional | cannot be null | [use_group](use_group-properties-uses.md "spec/use_group.schema.json#/properties/uses")               |
| [description](#description) | `string` | Optional | cannot be null | [use_group](use_group-properties-description.md "spec/use_group.schema.json#/properties/description") |

## use_group

Primary key.


`use_group`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [use_group](use_group-properties-use_group.md "spec/use_group.schema.json#/properties/use_group")

### use_group Type

`string`

## uses

Comma-separated list of uses.


`uses`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [use_group](use_group-properties-uses.md "spec/use_group.schema.json#/properties/uses")

### uses Type

`string`

## description

Optional.


`description`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [use_group](use_group-properties-description.md "spec/use_group.schema.json#/properties/description")

### description Type

`string`
