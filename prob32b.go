package main

import (
	"fmt"
	"strings"
)

func main() {
	products := map[int]bool{}
	sum := 0
	for _, limits := range [][]int{{12, 98, 123, 987}, {1, 9, 1234, 9876}} {
		l1l, l1u := limits[0], limits[1]
		l2l, l2u := limits[2], limits[3]
		for a := l1l; a <= l1u; a++ {
			for b := l2l; b <= l2u; b++ {
				c := a * b
				s := fmt.Sprintf("%d%d%d", a, b, c)
				if len(s) == 9 && strings.Count(s, "1") == 1 &&
					strings.Count(s, "2") == 1 &&
					strings.Count(s, "3") == 1 &&
					strings.Count(s, "4") == 1 &&
					strings.Count(s, "5") == 1 &&
					strings.Count(s, "6") == 1 &&
					strings.Count(s, "7") == 1 &&
					strings.Count(s, "8") == 1 &&
					strings.Count(s, "9") == 1 {
					if !products[c] {
						products[c] = true
						sum += c
					}
				}
			}
		}
	}
	fmt.Println(sum)
}
