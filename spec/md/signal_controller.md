# signal_controller Schema

```txt
spec/signal_controller.schema.json
```

The signal controller is associated with an intersection or a cluster of intersections.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                      |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ----------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [signal_controller.schema.json](../../out/signal_controller.schema.json "open original schema") |

## signal_controller Type

unknown ([signal_controller](signal_controller.md))

# signal_controller Properties

| Property                        | Type  | Required | Nullable       | Defined by                                                                                                                        |
| :------------------------------ | ----- | -------- | -------------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| [controller_id](#controller_id) | `any` | Required | cannot be null | [signal_controller](signal_controller-properties-controller_id.md "spec/signal_controller.schema.json#/properties/controller_id") |

## controller_id

Primary key.


`controller_id`

-   is required
-   Type: `any`
-   cannot be null
-   defined in: [signal_controller](signal_controller-properties-controller_id.md "spec/signal_controller.schema.json#/properties/controller_id")

### controller_id Type

`any`