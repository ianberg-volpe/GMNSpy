# Untitled schema Schema

```txt
undefined
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ----------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [use_definition.schema.json](../../out/use_definition.schema.json "open original schema") |

## Untitled schema Type

unknown

# undefined Properties

| Property                                    | Type     | Required | Nullable       | Defined by                                                                                                      |
| :------------------------------------------ | -------- | -------- | -------------- | :-------------------------------------------------------------------------------------------------------------- |
| [use](#use)                                 | `string` | Optional | cannot be null | [Untitled schema](use_definition-properties-use.md "undefined#/properties/use")                                 |
| [persons_per_vehicle](#persons_per_vehicle) | `number` | Optional | cannot be null | [Untitled schema](use_definition-properties-persons_per_vehicle.md "undefined#/properties/persons_per_vehicle") |
| [pce](#pce)                                 | `number` | Optional | cannot be null | [Untitled schema](use_definition-properties-pce.md "undefined#/properties/pce")                                 |
| [special_conditions](#special_conditions)   | `string` | Optional | cannot be null | [Untitled schema](use_definition-properties-special_conditions.md "undefined#/properties/special_conditions")   |
| [description](#description)                 | `string` | Optional | cannot be null | [Untitled schema](use_definition-properties-description.md "undefined#/properties/description")                 |

## use

Primary key


`use`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](use_definition-properties-use.md "undefined#/properties/use")

### use Type

`string`

## persons_per_vehicle

Required.


`persons_per_vehicle`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [Untitled schema](use_definition-properties-persons_per_vehicle.md "undefined#/properties/persons_per_vehicle")

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
-   defined in: [Untitled schema](use_definition-properties-pce.md "undefined#/properties/pce")

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
-   defined in: [Untitled schema](use_definition-properties-special_conditions.md "undefined#/properties/special_conditions")

### special_conditions Type

`string`

## description

Optional 


`description`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](use_definition-properties-description.md "undefined#/properties/description")

### description Type

`string`
