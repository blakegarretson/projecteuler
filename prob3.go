package main

import (
	"fmt"
	"math"
)

func main() {

	var n, x, limit int64
	n = 600851475143
	//n = 13195
	x = 2
	limit = int64(math.Sqrt(float64(n)))

	factors := make([]int64, 0)

	for x < limit {
		if n%x == 0 {
			factors = append(factors, x)
		}
		x += 1
	}
    
	var prime bool
	primefactors := make([]int64, 0)
	for _, x := range factors {
		prime = true
		for _, y := range factors {
			if x == y {
				continue
			}
			if x%y == 0 {
				prime = false
				break
			}
		}
		if prime {
			primefactors = append(primefactors, x)
		}
	}
    fmt.Println(factors)
	fmt.Println(primefactors)
	fmt.Println(primefactors[len(primefactors)-1])
}
