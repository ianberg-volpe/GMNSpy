# signal_phase Schema

```txt
spec/signal_phase.schema.json
```

For signalized nodes, establishes phases that may run concurrently, using ring-barrier notation. Each phase is associated with a ring and a barrier. In order to run concurrently, two phases must be in: the same barrier, and different rings.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                            |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [signal_phase.schema.json](../../out/signal_phase.schema.json "open original schema") |

## signal_phase Type

unknown ([signal_phase](signal_phase.md))

# signal_phase Properties

| Property                              | Type      | Required | Nullable       | Defined by                                                                                                               |
| :------------------------------------ | --------- | -------- | -------------- | :----------------------------------------------------------------------------------------------------------------------- |
| [signal_phase_id](#signal_phase_id)   | `any`     | Required | cannot be null | [signal_phase](signal_phase-properties-signal_phase_id.md "spec/signal_phase.schema.json#/properties/signal_phase_id")   |
| [timing_plan_id](#timing_plan_id)     | `any`     | Required | cannot be null | [signal_phase](signal_phase-properties-timing_plan_id.md "spec/signal_phase.schema.json#/properties/timing_plan_id")     |
| [signal_phase_num](#signal_phase_num) | `any`     | Required | cannot be null | [signal_phase](signal_phase-properties-signal_phase_num.md "spec/signal_phase.schema.json#/properties/signal_phase_num") |
| [ring](#ring)                         | `integer` | Required | cannot be null | [signal_phase](signal_phase-properties-ring.md "spec/signal_phase.schema.json#/properties/ring")                         |
| [barrier](#barrier)                   | `integer` | Required | cannot be null | [signal_phase](signal_phase-properties-barrier.md "spec/signal_phase.schema.json#/properties/barrier")                   |
| [position](#position)                 | `integer` | Required | cannot be null | [signal_phase](signal_phase-properties-position.md "spec/signal_phase.schema.json#/properties/position")                 |

## signal_phase_id

Primary key.


`signal_phase_id`

-   is required
-   Type: `any`
-   cannot be null
-   defined in: [signal_phase](signal_phase-properties-signal_phase_id.md "spec/signal_phase.schema.json#/properties/signal_phase_id")

### signal_phase_id Type

`any`

## timing_plan_id

Required. Foreign key (Signal_timing_plan table).


`timing_plan_id`

-   is required
-   Type: `any`
-   cannot be null
-   defined in: [signal_phase](signal_phase-properties-timing_plan_id.md "spec/signal_phase.schema.json#/properties/timing_plan_id")

### timing_plan_id Type

`any`

## signal_phase_num

Required. controller_id and signal_phase_num are unique


`signal_phase_num`

-   is required
-   Type: `any`
-   cannot be null
-   defined in: [signal_phase](signal_phase-properties-signal_phase_num.md "spec/signal_phase.schema.json#/properties/signal_phase_num")

### signal_phase_num Type

`any`

## ring

Required. Set of phases that conflict with each other. 


`ring`

-   is required
-   Type: `integer`
-   cannot be null
-   defined in: [signal_phase](signal_phase-properties-ring.md "spec/signal_phase.schema.json#/properties/ring")

### ring Type

`integer`

### ring Constraints

**maximum**: the value of this number must smaller than or equal to: `12`

**minimum**: the value of this number must greater than or equal to: `0`

## barrier

Required. Set of phases that can operate other.


`barrier`

-   is required
-   Type: `integer`
-   cannot be null
-   defined in: [signal_phase](signal_phase-properties-barrier.md "spec/signal_phase.schema.json#/properties/barrier")

### barrier Type

`integer`

### barrier Constraints

**maximum**: the value of this number must smaller than or equal to: `12`

**minimum**: the value of this number must greater than or equal to: `0`

## position

Required. Position.


`position`

-   is required
-   Type: `integer`
-   cannot be null
-   defined in: [signal_phase](signal_phase-properties-position.md "spec/signal_phase.schema.json#/properties/position")

### position Type

`integer`
