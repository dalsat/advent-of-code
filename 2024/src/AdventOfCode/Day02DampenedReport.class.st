"
Model for a Red-Nosed Report with one level of dampening.
"
Class {
	#name : 'Day02DampenedReport',
	#superclass : 'Day02Report',
	#category : 'AdventOfCode-Day02',
	#package : 'AdventOfCode',
	#tag : 'Day02'
}

{ #category : 'testing' }
Day02DampenedReport >> isSafe [

	^ super isSafe | (self withoutOneDetect: [ :e | e isSafe ])
]

{ #category : 'enumerating' }
Day02DampenedReport >> withoutOneDetect: aBlock [

	1 to: values size do: [ :index |
		| report |
		report := Day02Report withValues: (values copyWithoutIndex: index).
		(aBlock value: report) ifTrue: [ ^ true ] ].
	^ false
]
