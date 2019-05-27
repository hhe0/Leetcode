package main

import (
	"fmt"
)

func main() {
	test := singleNumber([]int{4, 1, 2, 1, 2})
	fmt.Println(test)
}

func singleNumber(nums []int) int {
	numberMap := make(map[int]int)
	for _, num := range nums {
		numberMap[num]++
	}

	for num, count := range numberMap {
		if count == 1 {
			return num
		}
	}

	return -1
}
