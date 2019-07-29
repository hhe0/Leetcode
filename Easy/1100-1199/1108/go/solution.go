package main

import "fmt"

func main() {
	fmt.Println(defangIPaddr("255.100.50.0"))
}

func defangIPaddr(address string) string {
	res := ""
	for _, s := range []rune(address) {
		if string(s) == "." {
			res += "[.]"
		} else {
			res += string(s)
		}
	}

	return res
}
