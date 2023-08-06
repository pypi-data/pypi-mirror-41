(* 
	This file contains the list of APIs used in the test suite.
	It should be used to deploy them on a given account to avoid
	false negative testing results.
 *)

If[Not@$CloudConnected,
	Return[$Failed]
]

co = CloudObject["api/private/requesterid"];
CloudDeploy[
	APIFunction[
		{}, 
		$RequesterWolframID &
	], 
	co
]

co = CloudObject["api/private/stringreverse"];
CloudDeploy[
	APIFunction[
		{"str" -> "String"}, 
		StringReverse[#str] &
	], 
	co
]

co = CloudObject["api/private/range/formated/json"];
CloudDeploy[APIFunction[
  {"max" -> "Integer", "min" -> "Integer" -> 1, 
   "step" -> "Integer" -> 1},
  Range[#min, #max, #step] &,
  "JSON"],
 co
]

co = CloudObject["api/public/jsonrange"];
CloudDeploy[
	APIFunction[
		{"i"->"Integer"},
		Range[#i]&,
		"JSON"
	],
	Permissions->"Public"
]

co = CloudObject["api/private/range/wlerror"];
CloudDeploy[APIFunction[
  {"i"},
  Range[#i] &,
  "JSON"],
 co
 ];

co = CloudObject["api/private/dimensions"];
CloudDeploy[APIFunction[
  {"data" -> "RawJSON"},
  Dimensions[#data] &,
  "JSON"],
 co
 ];

CloudDeploy[
	APIFunction[{"image" -> "Image"}, ImageDimensions[#image] &, "JSON"], 
 	CloudObject["api/private/imagedimensions"]
];

api = APIFunction[{"str" -> "String", "image" -> "Image", 
   "int" -> "Integer"},
  {#str, ImageDimensions[#image], #int} &,
  "JSON"
];
CloudDeploy[api, CloudObject["api/private/str_image_int"]];