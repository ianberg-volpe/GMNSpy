# signal_timing_phase Schema

```txt
undefined
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                          |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [signal_timing_phase.schema.json](../../out/signal_timing_phase.schema.json "open original schema") |

## signal_timing_phase Type

unknown ([signal_timing_phase](signal_timing_phase.md))

# signal_timing_phase Properties

| Property                              | Type      | Required | Nullable       | Defined by                                                                                                         |
| :------------------------------------ | --------- | -------- | -------------- | :----------------------------------------------------------------------------------------------------------------- |
| [timing_phase_id](#timing_phase_id)   | `any`     | Optional | cannot be null | [signal_timing_phase](signal_timing_phase-properties-timing_phase_id.md "undefined#/properties/timing_phase_id")   |
| [signal_phase_id](#signal_phase_id)   | `any`     | Optional | cannot be null | [signal_timing_phase](signal_timing_phase-properties-signal_phase_id.md "undefined#/properties/signal_phase_id")   |
| [timing_plan_id](#timing_plan_id)     | `any`     | Optional | cannot be null | [signal_timing_phase](signal_timing_phase-properties-timing_plan_id.md "undefined#/properties/timing_plan_id")     |
| [signal_phase_num](#signal_phase_num) | `integer` | Optional | cannot be null | [signal_timing_phase](signal_timing_phase-properties-signal_phase_num.md "undefined#/properties/signal_phase_num") |
| [min_green](#min_green)               | `integer` | Optional | cannot be null | [signal_timing_phase](signal_timing_phase-properties-min_green.md "undefined#/properties/min_green")               |
| [max_green](#max_green)               | `integer` | Optional | cannot be null | [signal_timing_phase](signal_timing_phase-properties-max_green.md "undefined#/properties/max_green")               |
| [extension](#extension)               | `integer` | Optional | cannot be null | [signal_timing_phase](signal_timing_phase-properties-extension.md "undefined#/properties/extension")               |
| [clearance](#clearance)               | `integer` | Optional | cannot be null | [signal_timing_phase](signal_timing_phase-properties-clearance.md "undefined#/properties/clearance")               |
| [walk_time](#walk_time)               | `integer` | Optional | cannot be null | [signal_timing_phase](signal_timing_phase-properties-walk_time.md "undefined#/properties/walk_time")               |
| [ped_clearance](#ped_clearance)       | `integer` | Optional | cannot be null | [signal_timing_phase](signal_timing_phase-properties-ped_clearance.md "undefined#/properties/ped_clearance")       |

## timing_phase_id

Primary key.


`timing_phase_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [signal_timing_phase](signal_timing_phase-properties-timing_phase_id.md "undefined#/properties/timing_phase_id")

### timing_phase_id Type

`any`

## signal_phase_id

Optional. Foreign key, the associated sigal phase.


`signal_phase_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [signal_timing_phase](signal_timing_phase-properties-signal_phase_id.md "undefined#/properties/signal_phase_id")

### signal_phase_id Type

`any`

## timing_plan_id




`timing_plan_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [signal_timing_phase](signal_timing_phase-properties-timing_plan_id.md "undefined#/properties/timing_plan_id")

### timing_plan_id Type

`any`

## signal_phase_num

Optional. Redundant with the record in the signal_phase table.


`signal_phase_num`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [signal_timing_phase](signal_timing_phase-properties-signal_phase_num.md "undefined#/properties/signal_phase_num")

### signal_phase_num Type

`integer`

### signal_phase_num Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## min_green

Required. The minimum green time in seconds for an actuated signal. Green time in seconds for a fixed time signal.


`min_green`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [signal_timing_phase](signal_timing_phase-properties-min_green.md "undefined#/properties/min_green")

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
-   defined in: [signal_timing_phase](signal_timing_phase-properties-max_green.md "undefined#/properties/max_green")

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
-   defined in: [signal_timing_phase](signal_timing_phase-properties-extension.md "undefined#/properties/extension")

### extension Type

`integer`

### extension Constraints

**maximum**: the value of this number must smaller than or equal to: `120`

**minimum**: the value of this number must greater than or equal to: `0`

## clearance

Required. Yellow interval plus all red interval


`clearance`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [signal_timing_phase](signal_timing_phase-properties-clearance.md "undefined#/properties/clearance")

### clearance Type

`integer`

### clearance Constraints

**maximum**: the value of this number must smaller than or equal to: `120`

**minimum**: the value of this number must greater than or equal to: `0`

## walk_time

Required if have ped phase. If a pedestrian phase exists, the walk time in seconds


`walk_time`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [signal_timing_phase](signal_timing_phase-properties-walk_time.md "undefined#/properties/walk_time")

### walk_time Type

`integer`

### walk_time Constraints

**maximum**: the value of this number must smaller than or equal to: `120`

**minimum**: the value of this number must greater than or equal to: `0`

## ped_clearance

Required if have ped phase. If a pedestrian phase exists, the flashing donâ€™t walk time.


`ped_clearance`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [signal_timing_phase](signal_timing_phase-properties-ped_clearance.md "undefined#/properties/ped_clearance")

### ped_clearance Type

`integer`

### ped_clearance Constraints

**maximum**: the value of this number must smaller than or equal to: `120`

**minimum**: the value of this number must greater than or equal to: `0`
