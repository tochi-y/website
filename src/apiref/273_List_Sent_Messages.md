---
id: 273_List_Sent_Messages
title: Retrieve List of SentMessage
sidebar_label: Retrieve List of SentMessage
---

## Overview

acquire SentMessage List

### Required Privileges

message or message-read

### Restrictions

* Always handles Content-Type in the request header as application/json
* Only accepts the request body in the JSON format
* Only application/json is supported for Content-Type in the request header and the JSON format for the response body
* Response body data is not ensured if atom or xml is specified in the $format query option, although it does not result in an error


## Request

### Request URL

```
{CellURL}__ctl/SentMessage
```

### Request Method

GET

### Request Query

The following query parameters are available

|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|

[$select  Query](406_Select_Query.md)

[$expand  Query](405_Expand_Query.md)

[$format  Query](404_Format_Query.md)

[$filter  Query](403_Filter_Query.md)

[$inlinecount  Query](407_Inlinecount_Query.md)

[$orderby  Query](400_Orderby_Query.md)

[$top  Query](401_Top_Query.md)

[$skip  Query](402_Skip_Query.md)

[Full-text Search (q) Query](408_Full_Text_Search_Query.md)

### Request Header

#### Common Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|Specifying this value in a request with the POST method indicates that the specified value is used as the method|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|The normal HTTP header value is overwritten. Specify multiple X-Override headers for the overwriting of multiple headers|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|When not specified, default value given with ${4 digits}_${22 digits} Base64url characters format representing an UUID for each request|

#### OData Common Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|

#### OData ListRequest Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Accept|Specifies the response body format|application/json|No|[application/json] by default|

### Request Body

None


## Response

### Response Code

200

### Response Header

None

### Response Body

#### Common

The response is a JSON object, the correspondence between the key (name) and type defined in the object (subobject) and the value are as follows

|Object|Name (Key)|Type|Value|
|:--|:--|:--|:--|
|Root|d|object|Object{1}|
|{1}|results|array|Array object {2}|
|{2}|__metadata|object|Object{3}|
|{3}|uri|string|URL to the resource that was created|
|{3}|etag|string|Etag value|
|{2}|__published|string|Creation date (UNIX time)|
|{2}|__updated|string|Update date (UNIX time)|
|{1}|__count|string|Get number of results in $inlinecount query|

#### OutMessage specific response body

|Object|Name (Key)|Type|Value|
|:--|:--|:--|:--|
|{3}|type|string|CellCtl.ReceivedMessage|
|{2}|__id|string|ReceivedMessage ID<br>Return a 32 character string such as "b5d008e9092f489c8d3c574a768afc33" with UUID|
|{2}|_Box.Name|string|BoxName for Relation|
|{2}|InReplyTo|string|ID message you are replying<br>Return a 32 character string such as "b5d008e9092f489c8d3c574a768afc33" with UUID|
|{2}|To|string|Destination cell URL|
|{2}|ToRelation|string|Relationship names to be sent|
|{2}|Type|string|Message type<br>message : message<br>relationship registration request(relation): req.relation.build<br>relationship deletion request(relation): req.relation.break<br>relationship registration request(role): req.role.grant<br>relationship deletion request(role): req.role.revoke|
|{2}|Title|string|Message Title|
|{2}|Body|string|Message Body|
|{2}|Priority|string|Priority<br>(high)1 - 5(low)|
|{2}|RequestObjects|array|Request details<br>Array object {4}|
|{4}|RequestType|string|Request type|
|{4}|Name|string|Refer to [SendMessage](271_Send_Message.md) for details|
|{4}|ClassUrl|string|Refer to [SendMessage](271_Send_Message.md) for details|
|{4}|TargetUrl|string|Refer to [SendMessage](271_Send_Message.md) for details|
|{4}|EventType|string|Refer to [SendMessage](271_Send_Message.md) for details|
|{4}|EventSubject|string|Refer to [SendMessage](271_Send_Message.md) for details|
|{4}|EventObject|string|Refer to [SendMessage](271_Send_Message.md) for details|
|{4}|EventInfo|string|Refer to [SendMessage](271_Send_Message.md) for details|
|{4}|Action|string|Refer to [SendMessage](271_Send_Message.md) for details|
|{2}|Result|array|Transmission result of each destination Cell<br>Array object {5}|
|{5}|To|string|Destination cell URL|
|{5}|Code|string|Response Code|
|{5}|Reason|string|Detailed message|

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

### Response Sample
```JSON
{
  "d": {
    "results": [
      {
        "__metadata": {
          "uri": "https://cell1.unit1.example/__ctl/SentMessage
('c87b42e10df846a9bee842225d1383fe')",
          "etag": "W/\"1-1486683974323\"",
          "type": "CellCtl.SentMessage"
        },
        "__id": "c87b42e10df846a9bee842225d1383fe",
        "_Box.Name": null,
        "InReplyTo": "xnKXmd4TTZCw-bfSEw4f0AxnKXmd4TTZ",
        "To": "https://cell2.unit1.example/",
        "ToRelation": null,
        "Type": "request",
        "Title": "Message Sample Title",
        "Body": "Message Sample Body",
        "Priority": 3,
        "RequestObjects": [
          {
            "RequestType": "relation.add",
            "Name": null,
            "ClassUrl": "https://app-cell1.unit1.example/__relation/__/relation1",
            "TargetUrl": "https://cell2.unit1.example/",
            "EventType": null,
            "EventSubject": null,
            "EventObject": null,
            "EventInfo": null,
            "Action": null
          }
        ],
        "Result": [
          {
            "To": "https://cell2.unit1.example/",
            "Code": "201",
            "Reason": "Created."
          }
        ],
        "__published": "/Date(1486683974323)/",
        "__updated": "/Date(1486683974323)/",
        "_Box": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/SentMessage
('c87b42e10df846a9bee842225d1383fe')/_Box"
          }
        }
      },
      {
        "__metadata": {
          "uri": "https://cell1.unit1.example/__ctl/SentMessage
('f87358607d0d46deae61eec6bb0ea490')",
          "etag": "W/\"1-1486685761907\"",
          "type": "CellCtl.SentMessage"
        },
        "__id": "f87358607d0d46deae61eec6bb0ea490",
        "_Box.Name": null,
        "InReplyTo": "xnKXmd4TTZCw-bfSEw4f0AxnKXmd4TTZ",
        "To": "https://cell3.unit1.example/",
        "ToRelation": null,
        "Type": "message",
        "Title": "Message Sample Title",
        "Body": "Message Sample Body",
        "Priority": 3,
        "Result": [
          {
            "To": "https://cell1.unit3.example/",
            "Code": "201",
            "Reason": "Created."
          }
        ],
        "__published": "/Date(1486685761907)/",
        "__updated": "/Date(1486685761907)/",
        "_Box": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/SentMessage
('f87358607d0d46deae61eec6bb0ea490')/_Box"
          }
        }
      }
    ]
  }
}
```


## cURL Command

```sh
curl "https://cell1.unit1.example/__ctl/SentMessage" -X GET -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json'
```

