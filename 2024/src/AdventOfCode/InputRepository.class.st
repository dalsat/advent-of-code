"
Support class to load input data from disk.
"
Class {
	#name : 'InputRepository',
	#superclass : 'Object',
	#instVars : [
		'path'
	],
	#classInstVars : [
		'defaultInstance'
	],
	#category : 'AdventOfCode',
	#package : 'AdventOfCode'
}

{ #category : 'accessing' }
InputRepository class >> default [

	defaultInstance ifNil: [ defaultInstance := self withPath: self defaultPath ].
	^ defaultInstance 
]

{ #category : 'accessing' }
InputRepository class >> defaultPath [

	^ './data/' asPath
]

{ #category : 'accessing' }
InputRepository class >> setDefaultWithPath: aPath [

	defaultInstance := self withPath: aPath
]

{ #category : 'accessing' }
InputRepository class >> withPath: aPath [

	^ self new
		  path: aPath;
		  yourself
]

{ #category : 'accessing' }
InputRepository >> day: aNumber [

	^ (self path asFileReference / (self fileNameForDay: aNumber))
		  contents
]

{ #category : 'accessing' }
InputRepository >> fileNameForDay: aNumber [
	"in house zero padding"

	^ 'day' , ('0' , aNumber asString last: 2), '.txt'
]

{ #category : 'accessing' }
InputRepository >> path [

	^ path
]

{ #category : 'accessing' }
InputRepository >> path: aStringOrPath [

	path := aStringOrPath asPath
]
