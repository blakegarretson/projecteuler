package main

import (
	"fmt"
	"math"
)

func main() {
	sum_of_squares := 0
	sum := 0
	for x := 1; x < 101; x++ {
		sum_of_squares += x * x
		sum += x
	}
	square_of_sums := math.Pow(float64(sum), float64(2))
	fmt.Println(int(square_of_sums) - sum_of_squares)
}
