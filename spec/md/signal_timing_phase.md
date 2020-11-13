# signal_timing_phase Schema

```txt
spec/signal_timing_phase.schema.json
```

For signalized nodes, provides signal timing and establishes phases that may run concurrently.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                          |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [signal_timing_phase.schema.json](../../out/signal_timing_phase.schema.json "open original schema") |

## signal_timing_phase Type

unknown ([signal_timing_phase](signal_timing_phase.md))

# signal_timing_phase Properties

| Property                              | Type      | Required | Nullable       | Defined by                                                                                                                                    |
| :------------------------------------ | --------- | -------- | -------------- | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| [timing_phase_id](#timing_phase_id)   | `any`     | Required | cannot be null | [signal_timing_phase](signal_timing_phase-properties-timing_phase_id.md "spec/signal_timing_phase.schema.json#/properties/timing_phase_id")   |
| [timing_plan_id](#timing_plan_id)     | `any`     | Optional | cannot be null | [signal_timing_phase](signal_timing_phase-properties-timing_plan_id.md "spec/signal_timing_phase.schema.json#/properties/timing_plan_id")     |
| [signal_phase_num](#signal_phase_num) | `integer` | Required | cannot be null | [signal_timing_phase](signal_timing_phase-properties-signal_phase_num.md "spec/signal_timing_phase.schema.json#/properties/signal_phase_num") |
| [min_green](#min_green)               | `integer` | Optional | cannot be null | [signal_timing_phase](signal_timing_phase-properties-min_green.md "spec/signal_timing_phase.schema.json#/properties/min_green")               |
| [max_green](#max_green)               | `integer` | Optional | cannot be null | [signal_timing_phase](signal_timing_phase-properties-max_green.md "spec/signal_timing_phase.schema.json#/properties/max_green")               |
| [extension](#extension)               | `integer` | Optional | cannot be null | [signal_timing_phase](signal_timing_phase-properties-extension.md "spec/signal_timing_phase.schema.json#/properties/extension")               |
| [clearance](#clearance)               | `integer` | Optional | cannot be null | [signal_timing_phase](signal_timing_phase-properties-clearance.md "spec/signal_timing_phase.schema.json#/properties/clearance")               |
| [walk_time](#walk_time)               | `integer` | Optional | cannot be null | [signal_timing_phase](signal_timing_phase-properties-walk_time.md "spec/signal_timing_phase.schema.json#/properties/walk_time")               |
| [ped_clearance](#ped_clearance)       | `integer` | Optional | cannot be null | [signal_timing_phase](signal_timing_phase-properties-ped_clearance.md "spec/signal_timing_phase.schema.json#/properties/ped_clearance")       |
| [ring](#ring)                         | `integer` | Required | cannot be null | [signal_timing_phase](signal_timing_phase-properties-ring.md "spec/signal_timing_phase.schema.json#/properties/ring")                         |
| [barrier](#barrier)                   | `integer` | Required | cannot be null | [signal_timing_phase](signal_timing_phase-properties-barrier.md "spec/signal_timing_phase.schema.json#/properties/barrier")                   |
| [position](#position)                 | `integer` | Required | cannot be null | [signal_timing_phase](signal_timing_phase-properties-position.md "spec/signal_timing_phase.schema.json#/properties/position")                 |

## timing_phase_id

Primary key.


`timing_phase_id`

-   is required
-   Type: `any`
-   cannot be null
-   defined in: [signal_timing_phase](signal_timing_phase-properties-timing_phase_id.md "spec/signal_timing_phase.schema.json#/properties/timing_phase_id")

### timing_phase_id Type

`any`

## timing_plan_id

Foreign key; connects to a timing_plan associated with a controller.


`timing_plan_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [signal_timing_phase](signal_timing_phase-properties-timing_plan_id.md "spec/signal_timing_phase.schema.json#/properties/timing_plan_id")

### timing_plan_id Type

`any`

## signal_phase_num

Signal phase number.


`signal_phase_num`

-   is required
-   Type: `integer`
-   cannot be null
-   defined in: [signal_timing_phase](signal_timing_phase-properties-signal_phase_num.md "spec/signal_timing_phase.schema.json#/properties/signal_phase_num")

### signal_phase_num Type

`integer`

### signal_phase_num Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## min_green

The minimum green time in seconds for an actuated signal. Green time in seconds for a fixed time signal.


`min_green`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [signal_timing_phase](signal_timing_phase-properties-min_green.md "spec/signal_timing_phase.schema.json#/properties/min_green")

### min_green Type

`integer`

### min_green Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## max_green

Optional.The maximum green time in seconds for an actuated signal; the default is minimum green plus one extension


`max_green`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [signal_timing_phase](signal_timing_phase-properties-max_green.md "spec/signal_timing_phase.schema.json#/properties/max_green")

### max_green Type

`integer`

### max_green Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## extension

Optional. The number of seconds the green time is extended each time vehicles are detected.


`extension`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [signal_timing_phase](signal_timing_phase-properties-extension.md "spec/signal_timing_phase.schema.json#/properties/extension")

### extension Type

`integer`

### extension Constraints

**maximum**: the value of this number must smaller than or equal to: `120`

**minimum**: the value of this number must greater than or equal to: `0`

## clearance

Yellow interval plus all red interval


`clearance`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [signal_timing_phase](signal_timing_phase-properties-clearance.md "spec/signal_timing_phase.schema.json#/properties/clearance")

### clearance Type

`integer`

### clearance Constraints

**maximum**: the value of this number must smaller than or equal to: `120`

**minimum**: the value of this number must greater than or equal to: `0`

## walk_time

If a pedestrian phase exists, the walk time in seconds


`walk_time`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [signal_timing_phase](signal_timing_phase-properties-walk_time.md "spec/signal_timing_phase.schema.json#/properties/walk_time")

### walk_time Type

`integer`

### walk_time Constraints

**maximum**: the value of this number must smaller than or equal to: `120`

**minimum**: the value of this number must greater than or equal to: `0`

## ped_clearance

If a pedestrian phase exists, the flashing donâ€™t walk time.


`ped_clearance`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [signal_timing_phase](signal_timing_phase-properties-ped_clearance.md "spec/signal_timing_phase.schema.json#/properties/ped_clearance")

### ped_clearance Type

`integer`

### ped_clearance Constraints

**maximum**: the value of this number must smaller than or equal to: `120`

**minimum**: the value of this number must greater than or equal to: `0`

## ring

Required. Set of phases that conflict with each other. 


`ring`

-   is required
-   Type: `integer`
-   cannot be null
-   defined in: [signal_timing_phase](signal_timing_phase-properties-ring.md "spec/signal_timing_phase.schema.json#/properties/ring")

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
-   defined in: [signal_timing_phase](signal_timing_phase-properties-barrier.md "spec/signal_timing_phase.schema.json#/properties/barrier")

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
-   defined in: [signal_timing_phase](signal_timing_phase-properties-position.md "spec/signal_timing_phase.schema.json#/properties/position")

### position Type

`integer`
