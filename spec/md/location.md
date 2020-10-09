# Untitled schema Schema

```txt
undefined
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                    |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ----------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [location.schema.json](../../out/location.schema.json "open original schema") |

## Untitled schema Type

unknown

# undefined Properties

| Property | Type     | Required | Nullable       | Defined by                                                            |
| :------- | -------- | -------- | -------------- | :-------------------------------------------------------------------- |
| [0](#0)  | `any`    | Optional | cannot be null | [Untitled schema](location-properties-0.md "undefined#/properties/0") |
| [1](#1)  | `any`    | Optional | cannot be null | [Untitled schema](location-properties-1.md "undefined#/properties/1") |
| [2](#2)  | `any`    | Optional | cannot be null | [Untitled schema](location-properties-2.md "undefined#/properties/2") |
| [3](#3)  | `number` | Optional | cannot be null | [Untitled schema](location-properties-3.md "undefined#/properties/3") |
| [4](#4)  | `number` | Optional | cannot be null | [Untitled schema](location-properties-4.md "undefined#/properties/4") |
| [5](#5)  | `number` | Optional | cannot be null | [Untitled schema](location-properties-5.md "undefined#/properties/5") |
| [6](#6)  | `number` | Optional | cannot be null | [Untitled schema](location-properties-6.md "undefined#/properties/6") |
| [7](#7)  | `string` | Optional | cannot be null | [Untitled schema](location-properties-7.md "undefined#/properties/7") |
| [8](#8)  | `any`    | Optional | cannot be null | [Untitled schema](location-properties-8.md "undefined#/properties/8") |
| [9](#9)  | `string` | Optional | cannot be null | [Untitled schema](location-properties-9.md "undefined#/properties/9") |

## 0

Primary key. Location ID.


`0`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](location-properties-0.md "undefined#/properties/0")

### 0 Type

`any`

## 1

Required. Road Link ID. Foreign Key from Road_Link.


`1`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](location-properties-1.md "undefined#/properties/1")

### 1 Type

`any`

## 2

Required. The From node of the link. Foreign Key from Node.


`2`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](location-properties-2.md "undefined#/properties/2")

### 2 Type

`any`

## 3

Required. Linear Reference of the location, measured as distance along the link from the reference node.  If link_geometry exists, it is used. Otherwise, link geometry is assumed to be a crow-fly distance from A node to B node.


`3`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [Untitled schema](location-properties-3.md "undefined#/properties/3")

### 3 Type

`number`

## 4

Optional. Either provided, or derived from Link, Ref_Node and LR.


`4`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [Untitled schema](location-properties-4.md "undefined#/properties/4")

### 4 Type

`number`

## 5

Optional. Either provided, or derived from Link, Ref_Node and LR.


`5`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [Untitled schema](location-properties-5.md "undefined#/properties/5")

### 5 Type

`number`

## 6

Optional. Altitude.


`6`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [Untitled schema](location-properties-6.md "undefined#/properties/6")

### 6 Type

`number`

## 7

Optional. What it represents (driveway, bus stop, etc.) OpenStreetMap map feature names are recommended.


`7`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](location-properties-7.md "undefined#/properties/7")

### 7 Type

`string`

## 8

Optional. Foreign Key, Associated zone


`8`

-   is optional
-   Type: `any`
-   cannot be null
-   defined in: [Untitled schema](location-properties-8.md "undefined#/properties/8")

### 8 Type

`any`

## 9

Optional. Foreign Key to GTFS data. For bus stops and transit station entrances, provides a link to the General Transit Feed Specification.


`9`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Untitled schema](location-properties-9.md "undefined#/properties/9")

### 9 Type

`string`
