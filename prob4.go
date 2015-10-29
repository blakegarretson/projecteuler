package main

import (
	"fmt"
	"sort"
)

func Reverse(s string) string {
	r := []rune(s)
	for i, j := 0, len(r)-1; i < len(r)/2; i, j = i+1, j-1 {
		r[i], r[j] = r[j], r[i]
	}
	return string(r)
}

func main() {
	palindromes := []int{}
	var num int
	for x := 100; x < 1000; x++ {
		for y := 100; y < 1000; y++ {
			num = x * y
			if fmt.Sprintf("%d", num) == Reverse(fmt.Sprintf("%d", num)) {
				palindromes = append(palindromes, num)
			}

		}
	}
	sort.Ints(palindromes)
	fmt.Println(palindromes[len(palindromes)-1])
}
