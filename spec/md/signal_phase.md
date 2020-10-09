# Untitled schema Schema

```txt
undefined
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                            |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [signal_phase.schema.json](../../out/signal_phase.schema.json "open original schema") |

## Untitled schema Type

unknown

# undefined Properties

| Property | Type      | Required | Nullable       | Defined by                                                                |
| :------- | --------- | -------- | -------------- | :------------------------------------------------------------------------ |
| [0](#0)  | `any`     | Optional | cannot be null | [Untitled schema](signal_phase-properties-0.md "undefined#/properties/0") |
| [1](#1)  | `any`     | Optional | cannot be null | [Untitled schema](signal_phase-properties-1.md "undefined#/properties/1") |
| [2](#2)  | `any`     | Optional | cannot be null | [Untitled schema](signal_phase-properties-2.md "undefined#/properties/2") |
| [3](#3)  | `integer` | Optional | cannot be null | [Untitled schema](signal_phase-properties-3.md "undefined#/properties/3") |
| [4](#4)  | `integer` | Optional | cannot be null | [Untitled schema](signal_phase-properties-4.md "undefined#/properties/4") |
| [5](#5)  | `integer` | Optional | cannot be null | [Untitled schema](signal_phase-properties-5.md "undefined#/properties/5") |

## 0

Primary key.


`0`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](signal_phase-properties-0.md "undefined#/properties/0")

### 0 Type

`any`

## 1

Required. Foreign key (Signal_timing_plan table).


`1`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](signal_phase-properties-1.md "undefined#/properties/1")

### 1 Type

`any`

## 2

Required. controller_id and signal_phase_num are unique


`2`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](signal_phase-properties-2.md "undefined#/properties/2")

### 2 Type

`any`

## 3

Required. Set of phases that conflict with each other. 


`3`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](signal_phase-properties-3.md "undefined#/properties/3")

### 3 Type

`integer`

## 4

Required. Set of phases that can operate other.


`4`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](signal_phase-properties-4.md "undefined#/properties/4")

### 4 Type

`integer`

## 5

Required. Position.


`5`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](signal_phase-properties-5.md "undefined#/properties/5")

### 5 Type

`integer`
