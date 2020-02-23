package main

import (
	"fmt"
	"os"
	"sort"
)

func main() {
	nums := []int{}
	for i := 1; i < 997; i++ {
		nums = append(nums, i)
	}
	for _, x := range nums {
		for _, y := range nums {
			for _, z := range nums {
				if x+y+z == 1000 {
					l := []int{x, y, z}
					sort.Ints(l)
					a, b, c := l[0], l[1], l[2]
					if a*a+b*b == c*c {
						fmt.Println(a, b, c)
						fmt.Println(a * b * c)
						os.Exit(0)
					}
				}
			}
		}
	}
}
