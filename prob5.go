package main

import "fmt"

func main() {
	n := 1
	for {
		success := true
		for i := 1; i < 21; i++ {
			if n%i == 0 {
				continue
			} else {
				success = false
				break
			}
		}
		if success == true {
			break
		}
		n++
	}
	fmt.Println(n)
}
