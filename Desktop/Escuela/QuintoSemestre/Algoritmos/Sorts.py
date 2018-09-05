#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 11:42:54 2018

@author: memoherrera


Sort algorithms

Insertion Sort
Selection Sort
Bubble Sort
Shell Sort
"""

import time

def insertionSort(array):
   for index in range(1,len(array)):
     currentvalue = array[index]
     position = index

     while position>0 and array[position-1]>currentvalue:
         array[position]=array[position-1]
         position = position-1

     array[position]=currentvalue


def selectionSort(array):
   for i in range(len(array)-1):
	minIndex = i
	for j in range(i+1, len(array)):
		if array[j] < array[minIndex]:
			minIndex = j
	if minIndex != i :
		array[i], array[minIndex] = array[minIndex], array[i]

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

 #     print("After increments of size",sublistcount,
 #                                  "The list is",alist)
      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue



array10 = [54,26,93,17,77,31,44,55,20,10]
array20 = [65,39,65,55,110,135,24,83,108,171,
           163,58,167,73,22,114,30,95,162,109]
array30 = [119,121	,49,83,146,130,101,130,37,94,
           114,148,39,105,85,122,18,34,118,16,
           87,157,71,4,43,83,77,56,9,38]
array40 = [61,5,-87,89,86,58,-1,-82,-78,-61
           ,80,-73,-72,21,-95,-7,-25,-7,-74,-72,
           -95,-13,-23,-34,61,36,70,24,13,-65,
           51,-28,96,-45,-54,-78,6,-97,9,-69]
array50 = [61,5,-87,89,86,58,-1,-82,-78,-61
           ,80,-73,-72,21,-95,-7,-25,-7,-74,0,
           -95,-13,-23,-34,61,36,70,24,13,-65,
           51,-28,96,-45,-54,-78,6,-97,9,-69,
           65,39,65,55,110,135,24,83,108,171,]

array = [array10,array20,array30,array40,array50]

tiempoIns = []
tiempoSel = []
tiempoBub = []
tiempoShe = []

for i in (array):
    start = time.process_time()
    insertionSort(i)
    end = time.process_time()
    total = end - start
    tiempoIns.append(total)
    
for i in (array):
    start = time.process_time()
    selectionSort(i)
    end = time.process_time()
    total = end - start
    tiempoSel.append(total)
    
for i in (array):
    start = time.process_time()
    bubbleSort(i)
    end = time.process_time()
    total = end - start
    tiempoBub.append(total)
    
for i in (array):
    start = time.process_time()
    shellSort(i)
    end = time.process_time()
    total = end - start
    tiempoShe.append(total)
    
print(tiempoSel)
print(tiempoIns)
print(tiempoBub)
print(tiempoShe)
