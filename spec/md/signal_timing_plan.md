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

| Property | Type      | Required | Nullable       | Defined by                                                                      |
| :------- | --------- | -------- | -------------- | :------------------------------------------------------------------------------ |
| [0](#0)  | `any`     | Optional | cannot be null | [Untitled schema](signal_timing_plan-properties-0.md "undefined#/properties/0") |
| [1](#1)  | `any`     | Optional | cannot be null | [Untitled schema](signal_timing_plan-properties-1.md "undefined#/properties/1") |
| [2](#2)  | `any`     | Optional | cannot be null | [Untitled schema](signal_timing_plan-properties-2.md "undefined#/properties/2") |
| [3](#3)  | `any`     | Optional | cannot be null | [Untitled schema](signal_timing_plan-properties-3.md "undefined#/properties/3") |
| [4](#4)  | `integer` | Optional | cannot be null | [Untitled schema](signal_timing_plan-properties-4.md "undefined#/properties/4") |
| [5](#5)  | `any`     | Optional | cannot be null | [Untitled schema](signal_timing_plan-properties-5.md "undefined#/properties/5") |
| [6](#6)  | `integer` | Optional | cannot be null | [Untitled schema](signal_timing_plan-properties-6.md "undefined#/properties/6") |
| [7](#7)  | `string`  | Optional | cannot be null | [Untitled schema](signal_timing_plan-properties-7.md "undefined#/properties/7") |
| [8](#8)  | `integer` | Optional | cannot be null | [Untitled schema](signal_timing_plan-properties-8.md "undefined#/properties/8") |

## 0

Primary key.


`0`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](signal_timing_plan-properties-0.md "undefined#/properties/0")

### 0 Type

`any`

## 1

Required. Foreign key (signal_controller table).


`1`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](signal_timing_plan-properties-1.md "undefined#/properties/1")

### 1 Type

`any`

## 2

Conditionally required (either timeday_id or time_day). Foreign key to time_set_definitions.


`2`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](signal_timing_plan-properties-2.md "undefined#/properties/2")

### 2 Type

`any`

## 3

Conditionally required (either timeday_id or time_day). XXXXXXXX_HHMM_HHMM, where XXXXXXXX is a bitmap of days of the week, Sunday-Saturday, Holiday. The HHMM are the start and end times.


`3`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](signal_timing_plan-properties-3.md "undefined#/properties/3")

### 3 Type

`any`

## 4

Required. Cycle length in seconds.


`4`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](signal_timing_plan-properties-4.md "undefined#/properties/4")

### 4 Type

`integer`

## 5

Optional. For coordinated signals, the “master” signal controller for coordination.


`5`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](signal_timing_plan-properties-5.md "undefined#/properties/5")

### 5 Type

`any`

## 6

Optional. For coordinated signals, the phase at which coordination starts (time 0).


`6`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](signal_timing_plan-properties-6.md "undefined#/properties/6")

### 6 Type

`integer`

## 7

Optional. For coordinated signals, the part of the phase where coordination starts: begin_of_green, begin_of_yellow, begin_of_red.


`7`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](signal_timing_plan-properties-7.md "undefined#/properties/7")

### 7 Type

`string`

## 8

Optional. Offset in seconds.


`8`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](signal_timing_plan-properties-8.md "undefined#/properties/8")

### 8 Type

`integer`
