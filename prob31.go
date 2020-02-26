package main

import (
	"fmt"
)

var coins = [8]int{1, 2, 5, 10, 20, 50, 100, 200}

func main() {
	// run through all the coin sizes for fun, only need 200 though
	for _, coin := range coins {
		fmt.Println(coin, solve(coin))
	}
}

func solve(target int) int {
	table := make([][]int, target+1)

	for i := 0; i <= target; i++ {
		table[i] = make([]int, len(coins))
		table[i][0] = 1
	}
	for i := 0; i <= target; i++ {
		for j := 1; j < len(coins); j++ {
			table[i][j] = table[i][j-1]
			if coins[j] <= i {
				table[i][j] += table[i-coins[j]][j]
			}
		}
	}
	return table[len(table)-1][len(table[0])-1]
}
