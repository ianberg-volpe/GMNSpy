# Untitled schema Schema

```txt
undefined
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                            |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [movement_tod.schema.json](../../out/movement_tod.schema.json "open original schema") |

## Untitled schema Type

unknown

# undefined Properties

| Property  | Type      | Required | Nullable       | Defined by                                                                  |
| :-------- | --------- | -------- | -------------- | :-------------------------------------------------------------------------- |
| [0](#0)   | `any`     | Optional | cannot be null | [Untitled schema](movement_tod-properties-0.md "undefined#/properties/0")   |
| [1](#1)   | `any`     | Optional | cannot be null | [Untitled schema](movement_tod-properties-1.md "undefined#/properties/1")   |
| [2](#2)   | `string`  | Optional | cannot be null | [Untitled schema](movement_tod-properties-2.md "undefined#/properties/2")   |
| [3](#3)   | `string`  | Optional | cannot be null | [Untitled schema](movement_tod-properties-3.md "undefined#/properties/3")   |
| [4](#4)   | `any`     | Optional | cannot be null | [Untitled schema](movement_tod-properties-4.md "undefined#/properties/4")   |
| [5](#5)   | `integer` | Optional | cannot be null | [Untitled schema](movement_tod-properties-5.md "undefined#/properties/5")   |
| [6](#6)   | `integer` | Optional | cannot be null | [Untitled schema](movement_tod-properties-6.md "undefined#/properties/6")   |
| [7](#7)   | `any`     | Optional | cannot be null | [Untitled schema](movement_tod-properties-7.md "undefined#/properties/7")   |
| [8](#8)   | `integer` | Optional | cannot be null | [Untitled schema](movement_tod-properties-8.md "undefined#/properties/8")   |
| [9](#9)   | `integer` | Optional | cannot be null | [Untitled schema](movement_tod-properties-9.md "undefined#/properties/9")   |
| [10](#10) | `string`  | Optional | cannot be null | [Untitled schema](movement_tod-properties-10.md "undefined#/properties/10") |
| [11](#11) | `any`     | Optional | cannot be null | [Untitled schema](movement_tod-properties-11.md "undefined#/properties/11") |
| [12](#12) | `any`     | Optional | cannot be null | [Untitled schema](movement_tod-properties-12.md "undefined#/properties/12") |
| [13](#13) | `any`     | Optional | cannot be null | [Untitled schema](movement_tod-properties-13.md "undefined#/properties/13") |

## 0

Primary key.


`0`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](movement_tod-properties-0.md "undefined#/properties/0")

### 0 Type

`any`

## 1

The referenced movement.


`1`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](movement_tod-properties-1.md "undefined#/properties/1")

### 1 Type

`any`

## 2

Time of day in XXXXXXXX_HHMM_HHMM format, where XXXXXXXX is a bitmap of days of the week, Sunday-Saturday, Holiday. The HHMM are the start and end times.


`2`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](movement_tod-properties-2.md "undefined#/properties/2")

### 2 Type

`string`

## 3

Time of day set. Used if times-of-day are defined on the time_set_definitions table


`3`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](movement_tod-properties-3.md "undefined#/properties/3")

### 3 Type

`string`

## 4

Inbound link id.


`4`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](movement_tod-properties-4.md "undefined#/properties/4")

### 4 Type

`any`

## 5

Innermost lane number the movement applies to at the inbound end.


`5`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](movement_tod-properties-5.md "undefined#/properties/5")

### 5 Type

`integer`

## 6

Outermost lane number the movement applies to at the inbound end. Blank indicates a movement with a single inbound lane.


`6`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](movement_tod-properties-6.md "undefined#/properties/6")

### 6 Type

`integer`

## 7

Outbound link id.


`7`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](movement_tod-properties-7.md "undefined#/properties/7")

### 7 Type

`any`

## 8

Innermost lane number the movement applies to at the outbound end.


`8`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](movement_tod-properties-8.md "undefined#/properties/8")

### 8 Type

`integer`

## 9

Outermost lane number the movement applies to at the outbound end. Blank indicates a movement with a single outbound lane.


`9`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](movement_tod-properties-9.md "undefined#/properties/9")

### 9 Type

`integer`

## 10

Optional. Describes the type of movement (left, right, thru, etc.).


`10`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](movement_tod-properties-10.md "undefined#/properties/10")

### 10 Type

`string`

## 11

Turn penalty (seconds)


`11`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](movement_tod-properties-11.md "undefined#/properties/11")

### 11 Type

`any`

## 12

Capacity in vehicles per hour.


`12`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](movement_tod-properties-12.md "undefined#/properties/12")

### 12 Type

`any`

## 13

Optional. .


`13`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](movement_tod-properties-13.md "undefined#/properties/13")

### 13 Type

`any`
