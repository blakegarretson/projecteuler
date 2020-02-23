package main

import (
	"fmt"
	//"sort"
	"strconv"
	"strings"
)

func main() {
	products := map[int]bool{}
	sum := 0
	//for i := 391867254; i < 391867255; i++ {
	for i := 123456789; i < 987654322; i++ {
		if i%10000000 == 0 {
			fmt.Println("Working on", i)
		}
		s := strconv.Itoa(i)
		if strings.Contains(s, "0") {
			continue
		}
		//b := []byte(s)
		//sort.Slice(b, func(i int, j int) bool { return b[i] < b[j] })
		//ss := string(b)

		//if ss == "123456789" {
		if strings.Count(s, "1") == 1 &&
			strings.Count(s, "2") == 1 &&
			strings.Count(s, "3") == 1 &&
			strings.Count(s, "4") == 1 &&
			strings.Count(s, "5") == 1 &&
			strings.Count(s, "6") == 1 &&
			strings.Count(s, "7") == 1 &&
			strings.Count(s, "8") == 1 &&
			strings.Count(s, "9") == 1 {

			//fmt.Println("Pandigit", i)
			// check 1 digit x 4 digits = 4 digits
			// check 2 digit x 3 digits = 4 digits
			for _, dgt := range [][]int{
				{1, 4},
				{2, 3},
			} {
				a, b := dgt[0], dgt[1]
				x, _ := strconv.Atoi(s[:a])
				y, _ := strconv.Atoi(s[a : b+a])
				z, _ := strconv.Atoi(s[b+a:])
				//fmt.Println(x, y, z, x*y)
				if x*y == z {
					if !products[z] {
						products[z] = true
						sum += z
						fmt.Println("Adding", x, y, z)
					}
				}
			}
		}
	}
	fmt.Println(products)
	fmt.Println(sum)
}
