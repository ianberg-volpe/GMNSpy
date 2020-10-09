# Untitled schema Schema

```txt
undefined
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                          |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [signal_timing_phase.schema.json](../../out/signal_timing_phase.schema.json "open original schema") |

## Untitled schema Type

unknown

# undefined Properties

| Property | Type      | Required | Nullable       | Defined by                                                                       |
| :------- | --------- | -------- | -------------- | :------------------------------------------------------------------------------- |
| [0](#0)  | `any`     | Optional | cannot be null | [Untitled schema](signal_timing_phase-properties-0.md "undefined#/properties/0") |
| [1](#1)  | `any`     | Optional | cannot be null | [Untitled schema](signal_timing_phase-properties-1.md "undefined#/properties/1") |
| [2](#2)  | `any`     | Optional | cannot be null | [Untitled schema](signal_timing_phase-properties-2.md "undefined#/properties/2") |
| [3](#3)  | `integer` | Optional | cannot be null | [Untitled schema](signal_timing_phase-properties-3.md "undefined#/properties/3") |
| [4](#4)  | `integer` | Optional | cannot be null | [Untitled schema](signal_timing_phase-properties-4.md "undefined#/properties/4") |
| [5](#5)  | `integer` | Optional | cannot be null | [Untitled schema](signal_timing_phase-properties-5.md "undefined#/properties/5") |
| [6](#6)  | `integer` | Optional | cannot be null | [Untitled schema](signal_timing_phase-properties-6.md "undefined#/properties/6") |
| [7](#7)  | `integer` | Optional | cannot be null | [Untitled schema](signal_timing_phase-properties-7.md "undefined#/properties/7") |
| [8](#8)  | `integer` | Optional | cannot be null | [Untitled schema](signal_timing_phase-properties-8.md "undefined#/properties/8") |
| [9](#9)  | `integer` | Optional | cannot be null | [Untitled schema](signal_timing_phase-properties-9.md "undefined#/properties/9") |

## 0

Primary key.


`0`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](signal_timing_phase-properties-0.md "undefined#/properties/0")

### 0 Type

`any`

## 1

Optional. Foreign key, the associated sigal phase.


`1`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](signal_timing_phase-properties-1.md "undefined#/properties/1")

### 1 Type

`any`

## 2




`2`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](signal_timing_phase-properties-2.md "undefined#/properties/2")

### 2 Type

`any`

## 3

Optional. Redundant with the record in the signal_phase table.


`3`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](signal_timing_phase-properties-3.md "undefined#/properties/3")

### 3 Type

`integer`

## 4

Required. The minimum green time in seconds for an actuated signal. Green time in seconds for a fixed time signal.


`4`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](signal_timing_phase-properties-4.md "undefined#/properties/4")

### 4 Type

`integer`

## 5

Optional.The maximum green time in seconds for an actuated signal; the default is minimum green plus one extension


`5`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](signal_timing_phase-properties-5.md "undefined#/properties/5")

### 5 Type

`integer`

## 6

Optional. The number of seconds the green time is extended each time vehicles are detected.


`6`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](signal_timing_phase-properties-6.md "undefined#/properties/6")

### 6 Type

`integer`

## 7

Required. Yellow interval plus all red interval


`7`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](signal_timing_phase-properties-7.md "undefined#/properties/7")

### 7 Type

`integer`

## 8

Required if have ped phase. If a pedestrian phase exists, the walk time in seconds


`8`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](signal_timing_phase-properties-8.md "undefined#/properties/8")

### 8 Type

`integer`

## 9

Required if have ped phase. If a pedestrian phase exists, the flashing don’t walk time.


`9`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](signal_timing_phase-properties-9.md "undefined#/properties/9")

### 9 Type

`integer`
