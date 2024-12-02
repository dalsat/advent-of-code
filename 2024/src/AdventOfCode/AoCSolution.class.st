"
Base abstract class for Advent of Code solutions.
"
Class {
	#name : 'AoCSolution',
	#superclass : 'Object',
	#instVars : [
		'data',
		'parsedData'
	],
	#category : 'AdventOfCode-Core',
	#package : 'AdventOfCode',
	#tag : 'Core'
}

{ #category : 'accessing' }
AoCSolution class >> day [

	^ self shouldBeImplemented
]

{ #category : 'accessing' }
AoCSolution class >> rawData [

	^ (InputRepository default day: self day) trimBoth
]

{ #category : 'accessing' }
AoCSolution class >> sample [

	^ self shouldBeImplemented
]

{ #category : 'instance creation' }
AoCSolution class >> withInput [

	^ self new
		  data: self rawData;
		  yourself
]

{ #category : 'instance creation' }
AoCSolution class >> withSample [

	^ self new
		  data: self sample;
		  yourself
]

{ #category : 'accessing' }
AoCSolution >> anyOne [

	^ self parsedData anyOne 
]

{ #category : 'accessing' }
AoCSolution >> data [

	^ data
]

{ #category : 'accessing' }
AoCSolution >> data: anObject [

	data := anObject
]

{ #category : 'parsing' }
AoCSolution >> parseInput: aString [

	^ aString
]

{ #category : 'accessing' }
AoCSolution >> parsedData [

	parsedData ifNil: [ parsedData := self parseInput: self data ].
	^ parsedData
]

{ #category : 'solution' }
AoCSolution >> part1 [

	^ self shouldBeImplemented
]

{ #category : 'solution' }
AoCSolution >> part2 [

	^ self shouldBeImplemented
]

{ #category : 'solution' }
AoCSolution >> solution [

	^ {
		  self part1.
		  self part2 }
]
