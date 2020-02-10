package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

func main() {
	combos := []int64{}
	const numdigits = 5
	const minnum = 2
	var maxnum, _ = strconv.ParseInt(strings.Repeat("9", numdigits+1), 10, 64)
	var num = int64(minnum)

	//var numstr string
	var fourthed float64
	for ; num <= maxnum; num += 1 {
		//numstr = strconv.Itoa(num)
		fourthed = 0
		for _, a := range strconv.FormatInt(num, 10) {
			i, _ := strconv.Atoi(string(a))
			fourthed += math.Pow(float64(i), numdigits)
		}
		if int64(fourthed) == num {
			combos = append(combos, num)
			fmt.Println(num)
		}
	}

	var sum int64
	for _, i := range combos {
		sum += i
	}

	fmt.Println("Sum of combos:", sum)
}
