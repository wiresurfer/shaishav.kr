---
category:
- Engineering
coverImage: "https://www.epsglobal.com/getattachment/20c59b9b-abe3-4375-8210-366f6d8e9a7a/Containers,-Docker-and-Kubernetes-A-beginner-s-guide-Part-2.jpg?maxsidesize=780&width=780"
tags:
- 
- topic/platform-engineering
- topic/devops
title: Test Page
---

# Test Page

## Introduction

In today's rapidly evolving software development landscape, staying ahead of the curve is crucial for success. One emerging trend that has gained significant traction is the adoption of Internal Developer Portals (iDp).

In this introductory blog post, we will explore the concept of iDp, its growing popularity in 2023, and why it is essential for modern software development.

#### Image Embed

![Dark mode Background: Tailwind CSS](/Assets/media/Test%20Page/Test%20Page-image-20230825032830918.png)

#### Code Embed

``` python
import os
import json

print(json.load("a,txt"))
```

#### Mermaid Embed

``` mermaid
sequenceDiagram

    autonumber

    participant user as User

    participant HT as Handy Terminal

    participant WMS as WMS

    participant RCS as RCS

    %% link convertIntoEpicUIAction: Convert into Epic @ https://dev168935.service-now.com/nav_to.do?uri=sys_ui_action.do?sys_id=80e97a04ef301000a7450fa3f82256c0

    %% link scrumStatesUtilSI: Scrum States Util @ https://dev168935.service-now.com/nav_to.do?uri=sys_script_include.do?sys_id=30d6f144cb50330078e8dcbcf7076d6c

    user->> HT: UI menu, RECEIVE

    HT ->> WMS: receive_shipment {bin-id, inventory_list, temp_location_id}

    WMS->>user: Receviced Shipment

    user->>HT: UI menu, STOW

    HT ->> WMS: stow_bin- After Receive shipment. {bin-id, from: temp_location, to: location[oks_tile_id]}

    WMS ->> RCS: request_stow { tile_id, bin_id, manifest}
```

#### Excalidraw embed

![](/Assets/media/Test%20Page/Test%20Page%202023-08-25%2003.29.05.excalidraw)

/exca
\### Diagram as Code

[Diagram as Code - by Alex Xu - ByteByteGo Newsletter](https://blog.bytebytego.com/p/diagram-as-code)

![](/Assets/media/Test%20Page/Test%20Page%202023-08-25%2004.41.44.excalidraw.svg)
