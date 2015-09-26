package main

import "fmt"

func main() {
	total := 0

	for a, b := 1, 1; b < 4e6; a, b = b, a+b {
		if b%2 == 0 {
			total += b
		}
	}

	fmt.Println(total)

}
