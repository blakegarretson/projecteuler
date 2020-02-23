package main

import (
	"fmt"
)

var facts [10]uint64

func Factorial(n uint64) uint64 {
	if n > 0 {
		return n * Factorial(n-1)
	}
	return 1
}
func main() {
	var ans int

	for i := 0; i < 10; i++ {
		facts[i] = Factorial(uint64(i))
	}

	for n := 10; n < 999999; n++ {

		digits := []int{}
		for z := n; z != 0; {
			digits = append(digits, z%10)
			z = z / 10
		}
		//fmt.Println(digits)
		sum := 0
		for _, x := range digits {
			sum += int(facts[x])
		}
		//fmt.Println(digits, sum)
		if sum == n {
			fmt.Println(n)
			ans += n
		}

	}

	fmt.Println("sum", ans)
	fmt.Println(facts)
}
