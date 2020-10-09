# Untitled schema Schema

```txt
undefined
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                      |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ----------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [signal_phase_mvmt.schema.json](../../out/signal_phase_mvmt.schema.json "open original schema") |

## Untitled schema Type

unknown

# undefined Properties

| Property | Type      | Required | Nullable       | Defined by                                                                     |
| :------- | --------- | -------- | -------------- | :----------------------------------------------------------------------------- |
| [0](#0)  | `any`     | Optional | cannot be null | [Untitled schema](signal_phase_mvmt-properties-0.md "undefined#/properties/0") |
| [1](#1)  | `any`     | Optional | cannot be null | [Untitled schema](signal_phase_mvmt-properties-1.md "undefined#/properties/1") |
| [2](#2)  | `any`     | Optional | cannot be null | [Untitled schema](signal_phase_mvmt-properties-2.md "undefined#/properties/2") |
| [3](#3)  | `integer` | Optional | cannot be null | [Untitled schema](signal_phase_mvmt-properties-3.md "undefined#/properties/3") |
| [4](#4)  | `any`     | Optional | cannot be null | [Untitled schema](signal_phase_mvmt-properties-4.md "undefined#/properties/4") |
| [5](#5)  | `any`     | Optional | cannot be null | [Untitled schema](signal_phase_mvmt-properties-5.md "undefined#/properties/5") |
| [6](#6)  | `any`     | Optional | cannot be null | [Untitled schema](signal_phase_mvmt-properties-6.md "undefined#/properties/6") |

## 0

Primary key.


`0`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](signal_phase_mvmt-properties-0.md "undefined#/properties/0")

### 0 Type

`any`

## 1

Required. Foreign key to signal_phase table.


`1`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](signal_phase_mvmt-properties-1.md "undefined#/properties/1")

### 1 Type

`any`

## 2

Redundant with field in the signal_phase table.


`2`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](signal_phase_mvmt-properties-2.md "undefined#/properties/2")

### 2 Type

`any`

## 3

Redundant with field in the signal_phase table. ; each phase has one or more Movements associated with it.


`3`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](signal_phase_mvmt-properties-3.md "undefined#/properties/3")

### 3 Type

`integer`

## 4

Foreign key. Either Movement_ID (for phases used by vehicles), or Link_id (for phases used by pedestrians) is required.


`4`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](signal_phase_mvmt-properties-4.md "undefined#/properties/4")

### 4 Type

`any`

## 5

Foreign key. Either Movement_ID (for phases used by vehicles), or Link_id (for phases used by pedestrians) is required.


`5`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](signal_phase_mvmt-properties-5.md "undefined#/properties/5")

### 5 Type

`any`

## 6

Optional. Indicates whether the phase is protected, permitted, or right turn on red.


`6`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](signal_phase_mvmt-properties-6.md "undefined#/properties/6")

### 6 Type

`any`
