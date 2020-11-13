# signal_coordination Schema

```txt
spec/signal_coordination.schema.json
```

Establishes coordination for several signal controllers, associated with a timing_plan.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                          |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [signal_coordination.schema.json](../../out/signal_coordination.schema.json "open original schema") |

## signal_coordination Type

unknown ([signal_coordination](signal_coordination.md))

# signal_coordination Properties

| Property                            | Type      | Required | Nullable       | Defined by                                                                                                                                  |
| :---------------------------------- | --------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------------ |
| [coordination_id](#coordination_id) | `any`     | Required | cannot be null | [signal_coordination](signal_coordination-properties-coordination_id.md "spec/signal_coordination.schema.json#/properties/coordination_id") |
| [timing_plan_id](#timing_plan_id)   | `any`     | Required | cannot be null | [signal_coordination](signal_coordination-properties-timing_plan_id.md "spec/signal_coordination.schema.json#/properties/timing_plan_id")   |
| [controller_id](#controller_id)     | `any`     | Required | cannot be null | [signal_coordination](signal_coordination-properties-controller_id.md "spec/signal_coordination.schema.json#/properties/controller_id")     |
| [coord_contr_id](#coord_contr_id)   | `any`     | Optional | cannot be null | [signal_coordination](signal_coordination-properties-coord_contr_id.md "spec/signal_coordination.schema.json#/properties/coord_contr_id")   |
| [coord_phase](#coord_phase)         | `integer` | Optional | cannot be null | [signal_coordination](signal_coordination-properties-coord_phase.md "spec/signal_coordination.schema.json#/properties/coord_phase")         |
| [coord_ref_to](#coord_ref_to)       | `string`  | Optional | cannot be null | [signal_coordination](signal_coordination-properties-coord_ref_to.md "spec/signal_coordination.schema.json#/properties/coord_ref_to")       |
| [offset](#offset)                   | `integer` | Optional | cannot be null | [signal_coordination](signal_coordination-properties-offset.md "spec/signal_coordination.schema.json#/properties/offset")                   |

## coordination_id

Primary key.


`coordination_id`

-   is required
-   Type: `any`
-   cannot be null
-   defined in: [signal_coordination](signal_coordination-properties-coordination_id.md "spec/signal_coordination.schema.json#/properties/coordination_id")

### coordination_id Type

`any`

## timing_plan_id

Required. Foreign key (Signal_timing_plan table).


`timing_plan_id`

-   is required
-   Type: `any`
-   cannot be null
-   defined in: [signal_coordination](signal_coordination-properties-timing_plan_id.md "spec/signal_coordination.schema.json#/properties/timing_plan_id")

### timing_plan_id Type

`any`

## controller_id

Required. Foreign key (signal_controller table).


`controller_id`

-   is required
-   Type: `any`
-   cannot be null
-   defined in: [signal_coordination](signal_coordination-properties-controller_id.md "spec/signal_coordination.schema.json#/properties/controller_id")

### controller_id Type

`any`

## coord_contr_id

Optional. For coordinated signals, the master signal controller for coordination.


`coord_contr_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [signal_coordination](signal_coordination-properties-coord_contr_id.md "spec/signal_coordination.schema.json#/properties/coord_contr_id")

### coord_contr_id Type

`any`

## coord_phase

Optional. For coordinated signals, the phase at which coordination starts (time 0).


`coord_phase`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [signal_coordination](signal_coordination-properties-coord_phase.md "spec/signal_coordination.schema.json#/properties/coord_phase")

### coord_phase Type

`integer`

### coord_phase Constraints

**maximum**: the value of this number must smaller than or equal to: `32`

**minimum**: the value of this number must greater than or equal to: `0`

## coord_ref_to

Optional. For coordinated signals, the part of the phase where coordination starts: begin_of_green, begin_of_yellow, begin_of_red.


`coord_ref_to`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [signal_coordination](signal_coordination-properties-coord_ref_to.md "spec/signal_coordination.schema.json#/properties/coord_ref_to")

### coord_ref_to Type

`string`

### coord_ref_to Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value               | Explanation |
| :------------------ | ----------- |
| `"begin_of_green"`  |             |
| `"begin_of_yellow"` |             |
| `"begin_of_red"`    |             |

## offset

Optional. Offset in seconds.


`offset`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [signal_coordination](signal_coordination-properties-offset.md "spec/signal_coordination.schema.json#/properties/offset")

### offset Type

`integer`

### offset Constraints

**minimum**: the value of this number must greater than or equal to: `0`
