# signal_phase_mvmt Schema

```txt
undefined
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                      |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ----------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [signal_phase_mvmt.schema.json](../../out/signal_phase_mvmt.schema.json "open original schema") |

## signal_phase_mvmt Type

unknown ([signal_phase_mvmt](signal_phase_mvmt.md))

# signal_phase_mvmt Properties

| Property                                      | Type      | Required | Nullable       | Defined by                                                                                                             |
| :-------------------------------------------- | --------- | -------- | -------------- | :--------------------------------------------------------------------------------------------------------------------- |
| [signal_phase_mvmt_id](#signal_phase_mvmt_id) | `any`     | Optional | cannot be null | [signal_phase_mvmt](signal_phase_mvmt-properties-signal_phase_mvmt_id.md "undefined#/properties/signal_phase_mvmt_id") |
| [signal_phase_id](#signal_phase_id)           | `any`     | Optional | cannot be null | [signal_phase_mvmt](signal_phase_mvmt-properties-signal_phase_id.md "undefined#/properties/signal_phase_id")           |
| [controller_id](#controller_id)               | `any`     | Optional | cannot be null | [signal_phase_mvmt](signal_phase_mvmt-properties-controller_id.md "undefined#/properties/controller_id")               |
| [signal_phase_num](#signal_phase_num)         | `integer` | Optional | cannot be null | [signal_phase_mvmt](signal_phase_mvmt-properties-signal_phase_num.md "undefined#/properties/signal_phase_num")         |
| [mvmt_id](#mvmt_id)                           | `any`     | Optional | cannot be null | [signal_phase_mvmt](signal_phase_mvmt-properties-mvmt_id.md "undefined#/properties/mvmt_id")                           |
| [link_id](#link_id)                           | `any`     | Optional | cannot be null | [signal_phase_mvmt](signal_phase_mvmt-properties-link_id.md "undefined#/properties/link_id")                           |
| [protection](#protection)                     | `any`     | Optional | cannot be null | [signal_phase_mvmt](signal_phase_mvmt-properties-protection.md "undefined#/properties/protection")                     |

## signal_phase_mvmt_id

Primary key.


`signal_phase_mvmt_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [signal_phase_mvmt](signal_phase_mvmt-properties-signal_phase_mvmt_id.md "undefined#/properties/signal_phase_mvmt_id")

### signal_phase_mvmt_id Type

`any`

## signal_phase_id

Required. Foreign key to signal_phase table.


`signal_phase_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [signal_phase_mvmt](signal_phase_mvmt-properties-signal_phase_id.md "undefined#/properties/signal_phase_id")

### signal_phase_id Type

`any`

## controller_id

Redundant with field in the signal_phase table.


`controller_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [signal_phase_mvmt](signal_phase_mvmt-properties-controller_id.md "undefined#/properties/controller_id")

### controller_id Type

`any`

## signal_phase_num

Redundant with field in the signal_phase table. ; each phase has one or more Movements associated with it.


`signal_phase_num`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [signal_phase_mvmt](signal_phase_mvmt-properties-signal_phase_num.md "undefined#/properties/signal_phase_num")

### signal_phase_num Type

`integer`

### signal_phase_num Constraints

**maximum**: the value of this number must smaller than or equal to: `32`

**minimum**: the value of this number must greater than or equal to: `0`

## mvmt_id

Foreign key. Either Movement_ID (for phases used by vehicles), or Link_id (for phases used by pedestrians) is required.


`mvmt_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [signal_phase_mvmt](signal_phase_mvmt-properties-mvmt_id.md "undefined#/properties/mvmt_id")

### mvmt_id Type

`any`

## link_id

Foreign key. Either Movement_ID (for phases used by vehicles), or Link_id (for phases used by pedestrians) is required.


`link_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [signal_phase_mvmt](signal_phase_mvmt-properties-link_id.md "undefined#/properties/link_id")

### link_id Type

`any`

## protection

Optional. Indicates whether the phase is protected, permitted, or right turn on red.


`protection`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [signal_phase_mvmt](signal_phase_mvmt-properties-protection.md "undefined#/properties/protection")

### protection Type

`any`

### protection Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value         | Explanation |
| :------------ | ----------- |
| `"protected"` |             |
| `"permitted"` |             |
| `"rtor"`      |             |
