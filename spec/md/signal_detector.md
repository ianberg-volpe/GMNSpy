# Untitled schema Schema

```txt
undefined
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                  |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [signal_detector.schema.json](../../out/signal_detector.schema.json "open original schema") |

## Untitled schema Type

unknown

# undefined Properties

| Property | Type      | Required | Nullable       | Defined by                                                                   |
| :------- | --------- | -------- | -------------- | :--------------------------------------------------------------------------- |
| [0](#0)  | `any`     | Optional | cannot be null | [Untitled schema](signal_detector-properties-0.md "undefined#/properties/0") |
| [1](#1)  | `any`     | Optional | cannot be null | [Untitled schema](signal_detector-properties-1.md "undefined#/properties/1") |
| [2](#2)  | `any`     | Optional | cannot be null | [Untitled schema](signal_detector-properties-2.md "undefined#/properties/2") |
| [3](#3)  | `integer` | Optional | cannot be null | [Untitled schema](signal_detector-properties-3.md "undefined#/properties/3") |
| [4](#4)  | `integer` | Optional | cannot be null | [Untitled schema](signal_detector-properties-4.md "undefined#/properties/4") |
| [5](#5)  | `any`     | Optional | cannot be null | [Untitled schema](signal_detector-properties-5.md "undefined#/properties/5") |
| [6](#6)  | `number`  | Optional | cannot be null | [Untitled schema](signal_detector-properties-6.md "undefined#/properties/6") |
| [7](#7)  | `number`  | Optional | cannot be null | [Untitled schema](signal_detector-properties-7.md "undefined#/properties/7") |
| [8](#8)  | `number`  | Optional | cannot be null | [Untitled schema](signal_detector-properties-8.md "undefined#/properties/8") |
| [9](#9)  | `string`  | Optional | cannot be null | [Untitled schema](signal_detector-properties-9.md "undefined#/properties/9") |

## 0

Primary key.


`0`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](signal_detector-properties-0.md "undefined#/properties/0")

### 0 Type

`any`

## 1

Required. Foreign key to signal_phase table.


`1`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](signal_detector-properties-1.md "undefined#/properties/1")

### 1 Type

`any`

## 2

Foreign key. The link covered by the detector.


`2`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](signal_detector-properties-2.md "undefined#/properties/2")

### 2 Type

`any`

## 3

Left-most lane covered by the detector.


`3`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](signal_detector-properties-3.md "undefined#/properties/3")

### 3 Type

`integer`

## 4

Right-most lane covered by the detector (blank if only one lane).


`4`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Untitled schema](signal_detector-properties-4.md "undefined#/properties/4")

### 4 Type

`integer`

## 5

The detector is on the approach to this node.


`5`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](signal_detector-properties-5.md "undefined#/properties/5")

### 5 Type

`any`

## 6

Required. Distance from from reference node to detector.


`6`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [Untitled schema](signal_detector-properties-6.md "undefined#/properties/6")

### 6 Type

`number`

## 7

Optional. Linear reference of front of detection zone.


`7`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [Untitled schema](signal_detector-properties-7.md "undefined#/properties/7")

### 7 Type

`number`

## 8

Optional. Linear reference of front of detection zone.


`8`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [Untitled schema](signal_detector-properties-8.md "undefined#/properties/8")

### 8 Type

`number`

## 9

Optional. Type of detector.


`9`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](signal_detector-properties-9.md "undefined#/properties/9")

### 9 Type

`string`
