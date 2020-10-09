# use_definition Schema

```txt
spec/use_definition.schema.json
```

The Use_Definition file defines the characteristics of each vehicle type or non-travel purpose (e.g., a shoulder or parking lane). A two-way left turn lane (TWLTL) is also a use.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ----------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [use_definition.schema.json](../../out/use_definition.schema.json "open original schema") |

## use_definition Type

unknown ([use_definition](use_definition.md))

# use_definition Properties

| Property                                    | Type     | Required | Nullable       | Defined by                                                                                                                           |
| :------------------------------------------ | -------- | -------- | -------------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| [use](#use)                                 | `string` | Optional | cannot be null | [use_definition](use_definition-properties-use.md "spec/use_definition.schema.json#/properties/use")                                 |
| [persons_per_vehicle](#persons_per_vehicle) | `number` | Optional | cannot be null | [use_definition](use_definition-properties-persons_per_vehicle.md "spec/use_definition.schema.json#/properties/persons_per_vehicle") |
| [pce](#pce)                                 | `number` | Optional | cannot be null | [use_definition](use_definition-properties-pce.md "spec/use_definition.schema.json#/properties/pce")                                 |
| [special_conditions](#special_conditions)   | `string` | Optional | cannot be null | [use_definition](use_definition-properties-special_conditions.md "spec/use_definition.schema.json#/properties/special_conditions")   |
| [description](#description)                 | `string` | Optional | cannot be null | [use_definition](use_definition-properties-description.md "spec/use_definition.schema.json#/properties/description")                 |

## use

Primary key


`use`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [use_definition](use_definition-properties-use.md "spec/use_definition.schema.json#/properties/use")

### use Type

`string`

## persons_per_vehicle

Required.


`persons_per_vehicle`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [use_definition](use_definition-properties-persons_per_vehicle.md "spec/use_definition.schema.json#/properties/persons_per_vehicle")

### persons_per_vehicle Type

`number`

### persons_per_vehicle Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## pce

Required. Passenger car equivelent.


`pce`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [use_definition](use_definition-properties-pce.md "spec/use_definition.schema.json#/properties/pce")

### pce Type

`number`

### pce Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## special_conditions

Optional.


`special_conditions`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [use_definition](use_definition-properties-special_conditions.md "spec/use_definition.schema.json#/properties/special_conditions")

### special_conditions Type

`string`

## description

Optional 


`description`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [use_definition](use_definition-properties-description.md "spec/use_definition.schema.json#/properties/description")

### description Type

`string`
