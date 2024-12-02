"
Solution for Day 2: Red-Nosed Reports
"
Class {
	#name : 'Day02',
	#superclass : 'AoCSolution',
	#category : 'AdventOfCode-Day02',
	#package : 'AdventOfCode',
	#tag : 'Day02'
}

{ #category : 'accessing' }
Day02 class >> day [

	^ 2
]

{ #category : 'accessing' }
Day02 class >> sample [

	^ '7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'
]

{ #category : 'solution' }
Day02 >> countSafeIn: aCollection [

	^ (aCollection select: [ :e | e isSafe ]) size
]

{ #category : 'parsing' }
Day02 >> parseInput: aString [

	^ aString lines collect: [ :eachLine | Day02Report fromString: eachLine ]
]

{ #category : 'solution' }
Day02 >> part1 [

	^ self countSafeIn: self parsedData
]

{ #category : 'solution' }
Day02 >> part2 [

	^ self countSafeIn: (self parsedData collect: #dampened)
]
