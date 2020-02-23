package main

import "fmt"
import "math"

func main() {
	primenum := 1
	n := 1
	for primenum <= 10001 {
		n += 1
		isprime := true
		for x := 2; x < int(math.Sqrt(float64(n)))+1; x++ {
			if n%x == 0 {
				isprime = false
				break
			}
		}
		if isprime {
			primenum += 1
		}

	}
	fmt.Println(n)
}
