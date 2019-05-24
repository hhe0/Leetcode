package main

import (
	"fmt"
)

func twoSum(nums []int, target int) []int {
	for i := 0; i < len(nums) - 1; i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[i] + nums[j] == target {
				return []int{i, j}
			}
		}
	}

	return nil
}

func main() {
	nums := []int{2, 7, 11, 15}
	target := 9

	var res []int
	res = twoSum(nums, target)
	fmt.Println(res)
}