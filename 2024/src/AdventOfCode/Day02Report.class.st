"
Model for a Red-Nosed Report.
"
Class {
	#name : 'Day02Report',
	#superclass : 'Object',
	#instVars : [
		'values'
	],
	#category : 'AdventOfCode-Day02',
	#package : 'AdventOfCode',
	#tag : 'Day02'
}

{ #category : 'instance creation' }
Day02Report class >> fromString: aString [

	^ self new
		  valueString: aString;
		  yourself
]

{ #category : 'instance creation' }
Day02Report class >> withValues: aCollection [

	^ self new
		  values: aCollection;
		  yourself
]

{ #category : 'converting' }
Day02Report >> dampened [

	^ Day02DampenedReport withValues: values copy
]

{ #category : 'testing' }
Day02Report >> isGradual [
	"Check that the difference among adjacent values is at least 1 and at most 3"

	^ (values overlappingPairsCollect: [ :a :b | (a - b) abs between: 1 and: 3 ]) allSatisfy: #yourself 
]

{ #category : 'testing' }
Day02Report >> isMonotonic [

	^ values isSorted or: [ values reversed isSorted ]
]

{ #category : 'testing' }
Day02Report >> isSafe [

	^ self isMonotonic & self isGradual
]

{ #category : 'printing' }
Day02Report >> printOn: aStream [
	"Generate a string representation of the receiver based on its instance variables."

	super printOn: aStream.
	aStream
		nextPutAll: ' values: ';
		print: values
]

{ #category : 'initialization' }
Day02Report >> valueString: aString [

	values := (Character space split: aString) collect: #asNumber
]

{ #category : 'accessing' }
Day02Report >> values [

	^ values
]

{ #category : 'accessing' }
Day02Report >> values: anObject [

	values := anObject
]
