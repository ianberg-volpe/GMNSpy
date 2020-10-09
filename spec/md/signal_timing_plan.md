# Untitled schema Schema

```txt
undefined
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                        |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [signal_timing_plan.schema.json](../../out/signal_timing_plan.schema.json "open original schema") |

## Untitled schema Type

unknown

# undefined Properties

| Property                          | Type      | Required | Nullable       | Defined by                                                                                                |
| :-------------------------------- | --------- | -------- | -------------- | :-------------------------------------------------------------------------------------------------------- |
| [timing_plan_id](#timing_plan_id) | `any`     | Optional | cannot be null | [Untitled schema](signal_timing_plan-properties-timing_plan_id.md "undefined#/properties/timing_plan_id") |
| [controller_id](#controller_id)   | `any`     | Optional | cannot be null | [Untitled schema](signal_timing_plan-properties-controller_id.md "undefined#/properties/controller_id")   |
| [timeday_id](#timeday_id)         | `any`     | Optional | cannot be null | [Untitled schema](signal_timing_plan-properties-timeday_id.md "undefined#/properties/timeday_id")         |
| [time_day](#time_day)             | `any`     | Optional | cannot be null | [Untitled schema](signal_timing_plan-properties-time_day.md "undefined#/properties/time_day")             |
| [cycle_length](#cycle_length)     | `integer` | Optional | cannot be null | [Untitled schema](signal_timing_plan-properties-cycle_length.md "undefined#/properties/cycle_length")     |
| [coord_contr_id](#coord_contr_id) | `any`     | Optional | cannot be null | [Untitled schema](signal_timing_plan-properties-coord_contr_id.md "undefined#/properties/coord_contr_id") |
| [coord_phase](#coord_phase)       | `integer` | Optional | cannot be null | [Untitled schema](signal_timing_plan-properties-coord_phase.md "undefined#/properties/coord_phase")       |
| [coord_ref_to](#coord_ref_to)     | `string`  | Optional | cannot be null | [Untitled schema](signal_timing_plan-properties-coord_ref_to.md "undefined#/properties/coord_ref_to")     |
| [offset](#offset)                 | `integer` | Optional | cannot be null | [Untitled schema](signal_timing_plan-properties-offset.md "undefined#/properties/offset")                 |

## timing_plan_id

Primary key.


`timing_plan_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](signal_timing_plan-properties-timing_plan_id.md "undefined#/properties/timing_plan_id")

### timing_plan_id Type

`any`

## controller_id

Required. Foreign key (signal_controller table).


`controller_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](signal_timing_plan-properties-controller_id.md "undefined#/properties/controller_id")

### controller_id Type

`any`

## timeday_id

Conditionally required (either timeday_id or time_day). Foreign key to time_set_definitions.


`timeday_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](signal_timing_plan-properties-timeday_id.md "undefined#/properties/timeday_id")

### timeday_id Type

`any`

## time_day

Conditionally required (either timeday_id or time_day). XXXXXXXX_HHMM_HHMM, where XXXXXXXX is a bitmap of days of the week, Sunday-Saturday, Holiday. The HHMM are the start and end times.


`time_day`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](signal_timing_plan-properties-time_day.md "undefined#/properties/time_day")

### time_day Type

`any`

## cycle_length

Required. Cycle length in seconds.


`cycle_length`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](signal_timing_plan-properties-cycle_length.md "undefined#/properties/cycle_length")

### cycle_length Type

`integer`

### cycle_length Constraints

**maximum**: the value of this number must smaller than or equal to: `600`

**minimum**: the value of this number must greater than or equal to: `0`

## coord_contr_id

Optional. For coordinated signals, the `master` signal controller for coordination.


`coord_contr_id`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](signal_timing_plan-properties-coord_contr_id.md "undefined#/properties/coord_contr_id")

### coord_contr_id Type

`any`

## coord_phase

Optional. For coordinated signals, the phase at which coordination starts (time 0).


`coord_phase`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](signal_timing_plan-properties-coord_phase.md "undefined#/properties/coord_phase")

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
-   defined in: [Untitled schema](signal_timing_plan-properties-coord_ref_to.md "undefined#/properties/coord_ref_to")

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
-   defined in: [Untitled schema](signal_timing_plan-properties-offset.md "undefined#/properties/offset")

### offset Type

`integer`

### offset Constraints

**minimum**: the value of this number must greater than or equal to: `0`
