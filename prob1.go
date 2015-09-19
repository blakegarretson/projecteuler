package main

import "fmt"

func main() {
	a := 0
	for i := 1; i < 1000; i++ {
		if i%3 == 0 || i%5 == 0 {
			a += i
		}
	}
	fmt.Printf("%v\n", a)
}
