"
Solution for Day 1: Historian Hysteria
"
Class {
	#name : 'Day01',
	#superclass : 'AoCSolution',
	#category : 'AdventOfCode',
	#package : 'AdventOfCode'
}

{ #category : 'accessing' }
Day01 class >> day [

	^ 1
]

{ #category : 'examples' }
Day01 class >> sample [

	^ '3   4
4   3
2   5
1   3
3   9
3   3'
]

{ #category : 'parsing' }
Day01 >> parseInput: aString [

	^ ((Character cr split: aString)
		   collect: [ :each | self parseLine: each ]
		   thenSelect: #notEmpty) flattened unzip
]

{ #category : 'parsing' }
Day01 >> parseLine: aString [

	^ ('\s+' asRegex split: aString) collect: #asNumber
]

{ #category : 'solution' }
Day01 >> part1 [

	| sortedCollections |
	sortedCollections := self parsedData collect: #sorted.
	^ (sortedCollections first
		   with: sortedCollections second
		   collect: [ :first :second | (first - second) abs ]) sum
]

{ #category : 'solution' }
Day01 >> part2 [

	| occurrences |
	occurrences := self parsedData second asBag.
	^ (self parsedData first collect: [ :each |
		   each * (occurrences occurrencesOf: each) ]) sum
]
